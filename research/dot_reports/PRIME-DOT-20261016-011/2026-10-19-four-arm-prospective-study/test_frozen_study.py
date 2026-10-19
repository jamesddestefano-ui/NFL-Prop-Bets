"""Deterministic tests of small invented examples. Standard library only."""
import unittest
from fractions import Fraction as F
import frozen_study as s

class ExactArithmeticTests(unittest.TestCase):
    def test_market_brier_exact(self):
        self.assertEqual(s.brier([F(1,10), F(1,2)], [0,1]), F(13,100))


import copy
import json
import math
from pathlib import Path

FIXTURE = Path(__file__).with_name('fixture.json')
def fixture():
    return json.loads(FIXTURE.read_text())

class StudyContractTests(unittest.TestCase):
    def test_four_arms_same_common_cohort(self):
        out = s.compare_four_arms(fixture())
        self.assertEqual(out['cohort_ids'], ['toy-1', 'toy-2'])
        self.assertEqual(list(out['brier']), ['M', 'G', 'C', 'S'])
        self.assertEqual(out['brier'], {'M':F(13,100), 'G':F(1,4), 'C':F(1,25), 'S':F(89,800)})
        self.assertEqual(out['delta_vs_M'], {'G':F(3,25), 'C':F(-9,100), 'S':F(-3,160)})
    def test_missing_and_abstain_distinct(self):
        self.assertEqual(s.validate_fixture(fixture())['excluded'], {'toy-3':['C:MISSING'], 'toy-4':['C:ABSTAIN']})
    def test_common_cohort_cannot_change_afterward(self):
        f = fixture(); f['protocol']['common_cohort_ids'] = ['toy-1']
        with self.assertRaisesRegex(ValueError, 'common cohort'): s.validate_fixture(f)
    def test_input_hash_mismatch_rejected(self):
        f = fixture(); f['rows'][0]['forecasts']['C']['input_hash'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'input hash'): s.validate_fixture(f)
    def test_changed_input_packet_rejected(self):
        f = fixture(); f['rows'][0]['input_packet']['invented_note'] = 'changed'
        with self.assertRaisesRegex(ValueError, 'input hash'): s.validate_fixture(f)
    def test_incomplete_contract_rejected(self):
        f = fixture(); del f['rows'][0]['contract']['book_rule']
        with self.assertRaisesRegex(ValueError, 'contract fields'): s.validate_fixture(f)
    def test_forecast_contract_mismatch_rejected(self):
        f = fixture(); f['rows'][0]['forecasts']['G']['contract']['threshold'] = '11/2'
        with self.assertRaisesRegex(ValueError, 'forecast contract'): s.validate_fixture(f)
    def test_settlement_contract_mismatch_rejected(self):
        f = fixture(); f['rows'][0]['settlement']['contract']['period'] = 'first_half'
        with self.assertRaisesRegex(ValueError, 'settlement contract'): s.validate_fixture(f)
    def test_probability_target_mismatch_rejected(self):
        f = fixture(); f['rows'][0]['contract']['probability_target'] = 'unconditional_win'
        with self.assertRaisesRegex(ValueError, 'probability target'): s.validate_fixture(f)
    def test_forecast_must_precede_lock(self):
        f = fixture(); f['rows'][0]['forecasts']['C']['generated_at'] = '2026-01-01T10:00:01Z'
        with self.assertRaisesRegex(ValueError, 'input <= forecast <= lock'): s.validate_fixture(f)
    def test_input_must_precede_forecast(self):
        f = fixture(); f['rows'][0]['forecasts']['C']['generated_at'] = '2026-01-01T08:00:00Z'
        with self.assertRaisesRegex(ValueError, 'input <= forecast <= lock'): s.validate_fixture(f)
    def test_lock_must_precede_event(self):
        f = fixture(); f['rows'][0]['event_start'] = '2026-01-01T10:00:00Z'
        with self.assertRaisesRegex(ValueError, 'lock < event'): s.validate_fixture(f)
    def test_protocol_must_precede_prediction_lock(self):
        f = fixture(); f['protocol']['locked_at'] = '2026-01-01T10:00:01Z'
        with self.assertRaisesRegex(ValueError, 'protocol <= cohort <= prediction lock'): s.validate_fixture(f)
    def test_settlement_must_follow_event_start(self):
        f = fixture(); f['rows'][0]['settlement']['observed_at'] = '2026-01-01T09:59:00Z'
        with self.assertRaisesRegex(ValueError, 'settlement after event'): s.validate_fixture(f)
    def test_chatgpt_anchor_is_fixed(self):
        f = fixture(); f['protocol']['anchor'] = 'C'
        with self.assertRaisesRegex(ValueError, 'prospective G anchor'): s.validate_fixture(f)
    def test_claude_shrinkage_needs_prespecification(self):
        with self.assertRaisesRegex(ValueError, 'not prespecified'): s.claude_secondary(fixture())
        f = fixture(); f['protocol']['claude_secondary_prespecified'] = True
        self.assertEqual(s.claude_secondary(f), F(157,1600))
    def test_protocol_must_precede_evidence_capture(self):
        f = fixture(); f['protocol']['locked_at'] = '2026-01-01T09:01:00Z'
        with self.assertRaisesRegex(ValueError, 'protocol <= input'): s.validate_fixture(f)
    def test_cohort_freeze_must_follow_included_replies(self):
        f = fixture(); f['protocol']['common_cohort_locked_at'] = '2026-01-01T09:29:00Z'
        with self.assertRaisesRegex(ValueError, 'forecast <= cohort'): s.validate_fixture(f)
    def test_model_packet_cannot_contain_market_probability(self):
        f = fixture(); packet = f['rows'][0]['input_packet']; packet['market_probability'] = '1/10'
        for arm in ('G', 'C'): f['rows'][0]['forecasts'][arm]['input_hash'] = s.input_hash(packet)
        with self.assertRaisesRegex(ValueError, 'price-blind evidence packet'): s.validate_fixture(f)
    def test_market_probability_matches_separate_frozen_snapshot(self):
        f = fixture(); f['rows'][0]['forecasts']['M']['p'] = '1/2'
        with self.assertRaisesRegex(ValueError, 'M must equal'): s.validate_fixture(f)
    def test_model_prompt_hash_mismatch_rejected(self):
        f = fixture(); f['rows'][0]['forecasts']['G']['prompt_hash'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'prompt hash'): s.validate_fixture(f)
    def test_abstain_cannot_carry_probability(self):
        f = fixture(); f['rows'][3]['forecasts']['C']['p'] = '1/2'
        with self.assertRaisesRegex(ValueError, 'ABSTAIN has no probability'): s.validate_fixture(f)

class MathematicalLessonsTests(unittest.TestCase):
    def setUp(self):
        self.m, self.g, self.y = [F(1,10),F(1,2)], [F(7,10),F(9,10)], [0,1]
    def test_exact_brier_expansion(self):
        for w in [F(0),F(1,4),F(1)]:
            parts = s.brier_expansion(self.m,self.g,self.y,w)
            self.assertEqual(parts['cross'], F(-7,100))
            self.assertEqual(parts['movement'], F(13,50))
            self.assertEqual(parts['difference'], s.brier(s.blend(self.m,self.g,w),self.y)-s.brier(self.m,self.y))
    def test_raw_worse_but_fixed_blend_better(self):
        self.assertGreater(s.brier(self.g,self.y),s.brier(self.m,self.y))
        self.assertEqual(s.blend(self.m,self.g,F(1,4)),[F(1,4),F(3,5)])
        self.assertLess(s.brier(s.blend(self.m,self.g,F(1,4)),self.y),s.brier(self.m,self.y))
    def test_oracle_is_separate_from_selected_weight(self):
        self.assertEqual(s.oracle_weight(self.m,self.g,self.y),F(7,26))
        self.assertEqual(fixture()['protocol']['shrinkage_weight'],'1/4')
        self.assertIsNone(s.oracle_weight(self.m,self.m,self.y))
    def test_invalid_probabilities_and_empty_scores_rejected(self):
        for p in [F(-1,10), F(11,10)]:
            with self.assertRaises(ValueError): s.brier([p],[1])
        with self.assertRaises(ValueError): s.brier([],[])
        with self.assertRaises(ValueError): s.brier([F(1,2)],[])
    def test_endpoint_log_loss_is_infinite(self):
        self.assertEqual(s.log_loss(F(0),1),math.inf)
        self.assertEqual(s.log_loss(F(1),0),math.inf)
        self.assertEqual(s.log_loss(F(1),1),0.0)
        self.assertEqual(s.log_loss(F(0),0),0.0)
        self.assertAlmostEqual(s.log_loss(F(1,2),1),math.log(2))
    def test_near_one_log_loss_stays_positive(self):
        actual = F(2**100-1,2**100)
        self.assertEqual(s.log_loss(actual,1), -math.log1p(-2**-100))
        self.assertGreater(s.log_loss(actual,1),0.0)
    def test_infinity_minus_infinity_is_undefined(self):
        with self.assertRaisesRegex(ValueError,'undefined'): s.log_loss_difference(math.inf,math.inf)
        self.assertEqual(s.log_loss_difference(math.inf,1.0),math.inf)
        self.assertEqual(s.log_loss_difference(1.0,math.inf),-math.inf)
    def test_conditional_probability_does_not_identify_push_mass(self):
        v0, v1 = s.full_wlp(F(3,5),F(0)), s.full_wlp(F(3,5),F(1,2))
        self.assertEqual(v0,(F(3,5),F(2,5),F(0)))
        self.assertEqual(v1,(F(3,10),F(1,5),F(1,2)))
        for w,l,p in [v0,v1]: self.assertEqual(w/(w+l),F(3,5))
        self.assertEqual(s.roi(v0,F(2)),F(1,5))
        self.assertEqual(s.roi(v1,F(2)),F(1,10))
    def test_opposite_side_duplication_changes_weighting(self):
        ss = s.blend(self.m,self.g,F(1,4))
        d = [(p-y)**2-(m-y)**2 for p,m,y in zip(ss,self.m,self.y)]
        opposite = ((1-ss[0])-(1-self.y[0]))**2-((1-self.m[0])-(1-self.y[0]))**2
        self.assertEqual(opposite,d[0])
        self.assertEqual(sum(d,F(0))/2,F(-3,160))
        self.assertEqual((d[0]+opposite+d[1])/3,F(1,200))
        self.assertEqual(s.equal_game_mean([('a',d[0]),('a',opposite),('b',d[1])]),F(-3,160))
    def test_whole_game_resampling_keeps_cluster_unit(self):
        samples = s.cluster_resample_means([F(21,400),F(-9,100)])
        self.assertEqual(samples,[F(21,400),F(-3,160),F(-3,160),F(-9,100)])

if __name__ == '__main__':
    unittest.main(verbosity=2)
