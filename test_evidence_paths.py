import copy
from datetime import timedelta
import itertools
import unittest
from evidence_paths import infer,recommend,path,validate
from benchmark import NOW,observation,generate,run_case


def graph():
    return {'schema':'evidence-paths/v1','nodes':['a','b','c'],'start':'a','goal':'c','edges':[
        {'id':'ab','source':'a','target':'b','observations':[]},
        {'id':'bc','source':'b','target':'c','observations':[]},
        {'id':'ac','source':'a','target':'c','observations':[]}]}


def validation(value,**kwargs):return observation(value,source='lab-validator',verified=True,**kwargs)


class BoundsTests(unittest.TestCase):
    def infer(self,data):return infer(data,NOW,{'lab-validator'})

    def test_missing_is_unknown_not_safe(self):
        self.assertEqual(self.infer(graph())['decision'],'unknown')

    def test_confirmed_path_and_cut(self):
        data=graph();data['edges'][2]['observations']=[validation(True)]
        self.assertEqual(self.infer(data)['confirmed_path'],['ac'])
        data['edges'][2]['observations']=[validation(False)]
        data['edges'][0]['observations']=[validation(False)]
        self.assertEqual(self.infer(data)['decision'],'unreachable_in_model')

    def test_expired_and_future_not_trusted(self):
        data=graph();data['edges'][2]['observations']=[validation(True,stale=True)]
        self.assertEqual(self.infer(data)['decision'],'unknown')
        data['edges'][2]['observations']=[{**validation(True),'observed_at':(NOW+timedelta(days=1)).isoformat()}]
        self.assertEqual(self.infer(data)['decision'],'unknown')

    def test_untrusted_verified_label_not_sufficient(self):
        data=graph();data['edges'][2]['observations']=[observation(True,source='attacker',verified=True)]
        self.assertEqual(self.infer(data)['decision'],'unknown')

    def test_contradictory_validators_abstain(self):
        data=graph();data['edges'][2]['observations']=[validation(True),validation(False)]
        result=self.infer(data)
        self.assertEqual(result['edge_states']['ac']['reason'],'conflicting_validators')
        self.assertEqual(result['decision'],'unknown')

    def test_duplicate_reports_do_not_create_confirmation(self):
        data=graph();data['edges'][2]['observations']=[observation(True)]*100
        self.assertEqual(self.infer(data)['decision'],'unknown')
        self.assertEqual(self.infer(data)['edge_states']['ac']['current_origins'],['export-1'])

    def test_cycle_and_zero_length_path(self):
        data=graph();data['edges'].append({'id':'ba','source':'b','target':'a','observations':[validation(True)]})
        self.assertEqual(self.infer(data)['decision'],'unknown')
        data['goal']='a'
        self.assertEqual(self.infer(data)['confirmed_path'],[])

    def test_exhaustive_bounds_soundness_all_small_worlds(self):
        # For every combination of known true / known false / unknown on three
        # edges, enumerate every ground truth consistent with known values.
        for states in itertools.product(('true','false','unknown'),repeat=3):
            data=graph()
            for edge,state in zip(data['edges'],states):
                edge['observations']=[] if state=='unknown' else [validation(state=='true')]
            result=self.infer(data)
            unknown=[i for i,state in enumerate(states) if state=='unknown']
            for bits in itertools.product((False,True),repeat=len(unknown)):
                world=[state=='true' for state in states]
                for index,bit in zip(unknown,bits):world[index]=bit
                truth=path(data['nodes'],[edge for edge,value in zip(data['edges'],world) if value],'a','c') is not None
                self.assertFalse(result['lower_reachable'] and not truth)
                self.assertFalse(truth and not result['upper_reachable'])

    def test_recommendation_is_unknown_edge(self):
        data=graph();next_step=recommend(data,NOW,{'lab-validator'})
        self.assertIn(next_step['edge_id'],{'ab','bc','ac'})
        data['edges'][2]['observations']=[validation(True)]
        self.assertIsNone(recommend(data,NOW,{'lab-validator'}))

    def test_duplicate_edge_and_invalid_ttl_fail(self):
        data=graph();data['edges'].append(copy.deepcopy(data['edges'][0]))
        with self.assertRaises(ValueError):validate(data)
        data=graph();data['edges'][0]['observations']=[dict(validation(True),ttl_days=-1)]
        with self.assertRaises(ValueError):validate(data)

    def test_generator_determinism_and_budget(self):
        first,truth=generate(7,'cyclic')
        self.assertEqual((first,truth),generate(7,'cyclic'))
        for method in ('bounds_random','bounds_path_first','bounds_gain'):
            result=run_case(first,truth,method,2,7)
            self.assertLessEqual(result['validations_used'],2)
            self.assertEqual(result['false_safe']+result['false_alarm'],0)

    def test_all_generated_worlds_obey_bounds(self):
        for family in ('layered','cyclic','bottleneck','heldout_random'):
            for seed in range(10):
                data,truth=generate(seed,family)
                result=self.infer(data)
                actual=path(data['nodes'],[edge for edge in data['edges'] if truth[edge['id']]],data['start'],data['goal']) is not None
                self.assertFalse(result['lower_reachable'] and not actual)
                self.assertFalse(actual and not result['upper_reachable'])


if __name__=='__main__':unittest.main()
