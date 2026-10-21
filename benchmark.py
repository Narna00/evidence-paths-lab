"""Synthetic pilot: paired graphs, explicit perfect-validation oracle, raw JSONL."""
import argparse
import copy
from datetime import datetime,timezone,timedelta
import hashlib
import json
from pathlib import Path
import random
import statistics
import sys
import time as clock
from evidence_paths import infer,recommend,path,current,validate

NOW=datetime(2026,10,21,tzinfo=timezone.utc)
METHODS=('optimistic','two_origins','bounds_random','bounds_path_first','bounds_gain')


def observation(value,source='scanner',origin='export-1',verified=False,stale=False):
    return {'source_id':source,'origin_id':origin,'value':value,'verified':verified,
            'observed_at':(NOW-timedelta(days=20 if stale else 1)).isoformat(),'ttl_days':7}


def generate(seed,family,n=12):
    rng=random.Random(seed)
    nodes=[f'n{i}' for i in range(n)]
    pairs={(i,i+1) for i in range(n-1)}
    if family=='layered':
        pairs|={(i,j) for i in range(n) for j in range(i+2,min(n,i+5)) if rng.random()<.35}
    elif family=='cyclic':
        pairs|={(i,j) for i in range(n) for j in range(n) if i!=j and rng.random()<.09}
    elif family=='bottleneck':
        middle=n//2
        pairs={(i,j) for i in range(n) for j in range(i+1,n) if (i<middle)==(j<middle) and rng.random()<.25}
        pairs|={(i,i+1) for i in range(n-1)}
    elif family=='heldout_random':
        pairs={(i,j) for i in range(n) for j in range(n) if i!=j and rng.random()<.12}
    else:raise ValueError('Unknown family')
    edges=[];truth={}
    for index,(i,j) in enumerate(sorted(pairs)):
        edge_id=f'e{index:03d}'
        value=rng.random()<.68
        truth[edge_id]=value
        obs=[]
        if rng.random()<.65:
            claim=value if rng.random()>.18 else not value
            base=observation(claim,origin=f'origin-{index}',stale=rng.random()<.2)
            obs.append(base)
            if rng.random()<.35:
                # Correlated re-exports share the same lineage and are not
                # independent confirmations. Some carry different source labels.
                obs.extend([{**base,'source_id':f'reexport-{k}'} for k in range(3)])
            if rng.random()<.15:obs.append(observation(not claim,source='scanner-2',origin=f'independent-{index}'))
        if rng.random()<.10:obs.append(observation(value,source='lab-validator',origin=f'validation-{index}',verified=True))
        edges.append({'id':edge_id,'source':nodes[i],'target':nodes[j],'observations':obs})
    data={'schema':'evidence-paths/v1','nodes':nodes,'start':nodes[0],'goal':nodes[-1],'edges':edges}
    return data,truth


def reported_decision(data,method):
    edges=[]
    for edge in data['edges']:
        obs=[x for x in edge['observations'] if current(x,NOW)]
        positive={x['origin_id'] for x in obs if x['value']}
        if positive and (method=='optimistic' or len(positive)>=2):edges.append(edge)
    return 'reachable' if path(data['nodes'],edges,data['start'],data['goal']) is not None else 'unreachable_in_model'


def run_case(data,truth,method,budget,seed):
    working=copy.deepcopy(data);rng=random.Random(seed+991)
    used=0;trace=[];trusted={'lab-validator'}
    started=clock.perf_counter()
    if method in ('optimistic','two_origins'):
        decision=reported_decision(working,method)
    else:
        while True:
            report=infer(working,NOW,trusted)
            if report['decision']!='unknown' or used>=budget:break
            unknown=[edge for edge in working['edges'] if report['edge_states'][edge['id']]['state']=='unknown']
            if not unknown:break
            if method=='bounds_random':chosen=rng.choice(sorted(unknown,key=lambda x:x['id']))['id']
            elif method=='bounds_path_first':chosen=next(edge_id for edge_id in report['possible_path'] if report['edge_states'][edge_id]['state']=='unknown')
            elif method=='bounds_gain':chosen=recommend(working,NOW,trusted)['edge_id']
            else:raise ValueError('Unknown method')
            selected=next(edge for edge in working['edges'] if edge['id']==chosen)
            selected['observations'].append(observation(truth[chosen],source='lab-validator',origin=f'oracle-{used}',verified=True))
            trace.append({'edge_id':chosen,'answer':truth[chosen]});used+=1
        decision=infer(working,NOW,trusted)['decision']
    elapsed=clock.perf_counter()-started
    actual=path(data['nodes'],[edge for edge in data['edges'] if truth[edge['id']]],data['start'],data['goal']) is not None
    false_safe=decision=='unreachable_in_model' and actual
    false_alarm=decision=='reachable' and not actual
    abstain=decision=='unknown'
    return {'method':method,'budget':budget,'validations_used':used,'truth_reachable':actual,'decision':decision,
            'false_safe':int(false_safe),'false_alarm':int(false_alarm),'abstain':int(abstain),'covered':int(not abstain),
            'loss':10*int(false_safe)+3*int(false_alarm)+int(abstain),'seconds':elapsed,'validation_trace':trace}


def bootstrap_mean(values,rng,resamples=1000):
    if not values:return None
    estimates=sorted(statistics.mean(rng.choices(values,k=len(values))) for _ in range(resamples))
    return {'mean':statistics.mean(values),'ci95_percentile':[estimates[int(.025*(resamples-1))],estimates[int(.975*(resamples-1))]],'n':len(values)}


def summarize(rows):
    groups={}
    for row in rows:groups.setdefault((row['family'],row['budget'],row['method']),[]).append(row)
    summaries=[]
    for (family,budget,method),items in sorted(groups.items()):
        summaries.append({'family':family,'budget':budget,'method':method,'n':len(items),**{metric:statistics.mean(item[metric] for item in items) for metric in ('false_safe','false_alarm','abstain','covered','loss','validations_used','seconds')}})
    paired=[]
    for family in sorted({row['family'] for row in rows}):
        for budget in sorted({row['budget'] for row in rows}):
            selected=[row for row in rows if row['family']==family and row['budget']==budget]
            by_key={(row['seed'],row['method']):row for row in selected}
            seeds=sorted({row['seed'] for row in selected})
            for baseline in ('bounds_random','bounds_path_first'):
                differences=[by_key[(seed,'bounds_gain')]['loss']-by_key[(seed,baseline)]['loss'] for seed in seeds]
                paired.append({'family':family,'budget':budget,'contrast':f'bounds_gain minus {baseline} loss',**bootstrap_mean(differences,random.Random(20261021))})
    return {'schema':'evidence-paths-summary/v1','groups':summaries,'paired_loss_contrasts':paired,
            'limits':['Synthetic pilot only; no efficacy claim about real assessments.','Intervals are pointwise paired bootstrap over seeds, not corrected for multiple comparisons.','Perfect edge validation and a complete candidate universe are simulation assumptions.','Loss weights 10/3/1 are declared modeling choices, not estimated organizational costs.']}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seeds',type=int,default=30)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args(argv)
    if not 2<=args.seeds<=1000:parser.error('Use 2 through 1000 seeds')
    try:
        args.output.mkdir(parents=True,exist_ok=False)
        rows=[];datasets=[]
        for family in ('layered','cyclic','bottleneck','heldout_random'):
            for seed in range(args.seeds):
                data,truth=generate(seed,family);validate(data)
                graph_hash=hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()
                datasets.append({'family':family,'seed':seed,'graph_sha256':graph_hash,'graph':data,'truth':truth})
                for budget in (0,2,5,10):
                    for method in METHODS:
                        rows.append({'family':family,'seed':seed,'graph_sha256':graph_hash,**run_case(data,truth,method,budget,seed)})
        for name,records in [('raw.jsonl',rows),('datasets.jsonl',datasets)]:
            with (args.output/name).open('x',encoding='utf-8') as stream:
                for record in records:stream.write(json.dumps(record,sort_keys=True)+'\n')
        (args.output/'summary.json').write_text(json.dumps(summarize(rows),indent=2)+'\n',encoding='utf-8')
        manifest={path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(args.output.iterdir()) if path.is_file()}
        (args.output/'manifest.json').write_text(json.dumps({'schema':'experiment-manifest/v1','as_of':NOW.isoformat(),'seeds_per_family':args.seeds,'files':manifest},indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'rows':len(rows),'graphs':len(datasets),'output':str(args.output)}))
        return 0
    except (OSError,ValueError,KeyError,TypeError) as error:
        print(f'error: {error}',file=sys.stderr);return 2


if __name__=='__main__':sys.exit(main())
