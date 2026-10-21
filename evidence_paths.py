"""Evidence-bounded directed reachability; no scanning or exploit execution."""
from collections import deque
from datetime import datetime,timezone,timedelta
import argparse
import copy
import json
from pathlib import Path
import sys


def time(value):
    parsed=datetime.fromisoformat(value.replace('Z','+00:00'))
    if parsed.tzinfo is None:raise ValueError('Timezone required')
    return parsed.astimezone(timezone.utc)


def validate(data):
    if data.get('schema')!='evidence-paths/v1':raise ValueError('Unsupported graph schema')
    nodes=data['nodes']
    if not nodes or any(not isinstance(x,str) or not x for x in nodes) or len(nodes)!=len(set(nodes)):
        raise ValueError('Unique nonempty node IDs required')
    if data['start'] not in nodes or data['goal'] not in nodes:raise ValueError('Unknown start/goal')
    ids=set()
    for edge in data['edges']:
        if not edge['id'] or edge['id'] in ids:raise ValueError('Duplicate/empty edge ID')
        ids.add(edge['id'])
        if edge['source'] not in nodes or edge['target'] not in nodes:raise ValueError('Unknown endpoint')
        for obs in edge['observations']:
            if type(obs['value']) is not bool or type(obs['verified']) is not bool:raise ValueError('Boolean observation fields required')
            if not obs['source_id'] or not obs['origin_id']:raise ValueError('Source and origin lineage required')
            time(obs['observed_at'])
            if type(obs['ttl_days']) is not int or obs['ttl_days']<0:raise ValueError('Invalid TTL')


def current(obs,now):
    observed=time(obs['observed_at'])
    return observed<=now<observed+timedelta(days=obs['ttl_days'])


def classify(edge,now,trusted):
    live=[obs for obs in edge['observations'] if current(obs,now)]
    verified=[obs for obs in live if obs['verified'] and obs['source_id'] in trusted]
    values={obs['value'] for obs in verified}
    state='true' if values=={True} else 'false' if values=={False} else 'unknown'
    reason='conflicting_validators' if len(values)>1 else 'validated' if values else 'no_current_trusted_validation'
    return {'state':state,'reason':reason,'current_origins':sorted({obs['origin_id'] for obs in live}),
            'discarded_observations':len(edge['observations'])-len(live)}


def path(nodes,edges,start,goal):
    graph={node:[] for node in nodes}
    for edge in sorted(edges,key=lambda x:x['id']):graph[edge['source']].append((edge['target'],edge['id']))
    queue=deque([start]);previous={start:None}
    while queue:
        node=queue.popleft()
        if node==goal:
            result=[]
            while previous[node] is not None:
                parent,edge_id=previous[node];result.append(edge_id);node=parent
            return list(reversed(result))
        for target,edge_id in graph[node]:
            if target not in previous:previous[target]=(node,edge_id);queue.append(target)
    return None


def infer(data,now,trusted):
    validate(data)
    states={edge['id']:classify(edge,now,trusted) for edge in data['edges']}
    lower=[edge for edge in data['edges'] if states[edge['id']]['state']=='true']
    upper=[edge for edge in data['edges'] if states[edge['id']]['state']!='false']
    lower_path=path(data['nodes'],lower,data['start'],data['goal'])
    upper_path=path(data['nodes'],upper,data['start'],data['goal'])
    decision='reachable' if lower_path is not None else 'unreachable_in_model' if upper_path is None else 'unknown'
    return {'decision':decision,'lower_reachable':lower_path is not None,'upper_reachable':upper_path is not None,
            'confirmed_path':lower_path,'possible_path':upper_path,'edge_states':states,
            'as_of':now.isoformat(),'scope':'Finite declared candidate graph; no claim about omitted transitions or real exploitation.'}


def closure(nodes,edges,start):
    reached={start};queue=deque([start]);adj={node:[] for node in nodes}
    for edge in edges:adj[edge['source']].append(edge['target'])
    while queue:
        for target in adj[queue.popleft()]:
            if target not in reached:reached.add(target);queue.append(target)
    return reached


def corridor(data,report):
    upper=[edge for edge in data['edges'] if report['edge_states'][edge['id']]['state']!='false']
    forward=closure(data['nodes'],upper,data['start'])
    reverse=[{'source':edge['target'],'target':edge['source']} for edge in upper]
    backward=closure(data['nodes'],reverse,data['goal'])
    return {edge['id'] for edge in upper if edge['source'] in forward and edge['target'] in backward}


def recommend(data,now,trusted):
    """Equal-branch minimax-style heuristic; scores are not probabilities."""
    report=infer(data,now,trusted)
    if report['decision']!='unknown':return None
    relevant=corridor(data,report)
    candidates=[edge for edge in data['edges'] if edge['id'] in relevant and report['edge_states'][edge['id']]['state']=='unknown']
    ranked=[]
    for candidate in candidates:
        resolution=0;reduction=0
        for value in (False,True):
            altered=copy.deepcopy(data)
            edge=next(edge for edge in altered['edges'] if edge['id']==candidate['id'])
            # Hypothetical replacement of *all* validation for this edge. A real
            # contradictory validator needs adjudication, not automatic override.
            edge['observations']=[{'source_id':'hypothesis','origin_id':'hypothesis','observed_at':now.isoformat(),'ttl_days':1,'value':value,'verified':True}]
            changed=infer(altered,now,{'hypothesis'}|set(trusted))
            resolution+=int(changed['decision']!='unknown')
            reduction+=len(relevant)-len(corridor(altered,changed))
        ranked.append((resolution,reduction,candidate['id']))
    if not ranked:return None
    best=sorted(ranked,key=lambda item:(-item[0],-item[1],item[2]))[0]
    return {'edge_id':best[2],'resolving_branches':best[0],'corridor_reduction_sum':best[1],
            'meaning':'Hypothetical perfect edge validation; no exploitability probability or expected-time guarantee.'}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('graph',type=Path)
    parser.add_argument('--trust-policy',type=Path,required=True)
    parser.add_argument('--as-of',required=True,type=time)
    parser.add_argument('--recommend',action='store_true')
    args=parser.parse_args(argv)
    try:
        data=json.loads(args.graph.read_text(encoding='utf-8'))
        policy=json.loads(args.trust_policy.read_text(encoding='utf-8'))
        if policy.get('schema')!='evidence-trust/v1' or not isinstance(policy['trusted_validators'],list):raise ValueError('Invalid trust policy')
        trusted=set(policy['trusted_validators'])
        report=infer(data,args.as_of,trusted)
        if args.recommend:report['next_validation']=recommend(data,args.as_of,trusted)
        print(json.dumps(report,indent=2))
        return 0 if report['decision']!='unknown' else 1
    except (OSError,ValueError,KeyError,TypeError,AttributeError) as error:
        print(f'error: {error}',file=sys.stderr);return 2


if __name__=='__main__':sys.exit(main())
