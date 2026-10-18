"""Behavioral tests for a synthetic, non-production scoring lesson."""
import copy
from fractions import Fraction as F
import hashlib
import json
import math
import pathlib
import unittest
import score_fixture as s


class ScoreFixtureTests(unittest.TestCase):
    def api(self, name):
        fn = getattr(s, name, None)
        self.assertTrue(callable(fn), f"Missing required behavior: {name}")
        return fn

    def test_brier_exact_binary_scores(self):
        brier = self.api('brier')
        self.assertEqual(brier(.7, 1), F(9, 100))
        self.assertEqual(brier(.7, 0), F(49, 100))
        self.assertEqual(brier(0, 0), 0)
        self.assertEqual(brier(1, 0), 1)

    def test_invalid_probability_is_not_silently_coerced(self):
        brier = self.api('brier')
        for value in [None, 'ABSTAIN', float('nan'), float('inf'), -0.1, 1.1, True]:
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                brier(value, 1)

    def test_unobserved_outcome_is_not_a_loss(self):
        brier = self.api('brier')
        for value in [None, 'PUSH', .5, True]:
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                brier(.5, value)

    def test_log_loss_uses_natural_log(self):
        loss = self.api('log_loss')
        self.assertAlmostEqual(loss(.7, 1), -math.log(.7), places=14)
        self.assertAlmostEqual(loss(.7, 0), -math.log(.3), places=14)

    def test_unclipped_log_loss_has_infinite_endpoint_loss(self):
        loss = self.api('log_loss')
        self.assertEqual(loss(0, 0), 0)
        self.assertEqual(loss(1, 1), 0)
        self.assertEqual(loss(0, 1), math.inf)
        self.assertEqual(loss(1, 0), math.inf)

    def test_explicit_clipping_changes_the_forecast(self):
        clip = self.api('predeclared_clip')
        self.assertEqual(clip(.001, .01), F(1, 100))
        self.assertEqual(clip(.999, .01), F(99, 100))
        self.assertEqual(clip(.7, .01), F(7, 10))

    def test_invalid_epsilon_is_rejected(self):
        clip = self.api('predeclared_clip')
        for eps in [None, 0, -.1, .5, 1, float('nan')]:
            with self.subTest(eps=eps), self.assertRaises((TypeError, ValueError)):
                clip(.7, eps)

    def test_fixture_binary_basis_and_counts(self):
        rows = self.api('build_fixture')()
        self.assertEqual(len(rows), 50)
        self.assertEqual(sum(r['stratum'] == 'easy' for r in rows), 10)
        self.assertEqual(sum(r['outcome'] for r in rows[:10]), 9)
        self.assertEqual(sum(r['outcome'] for r in rows[10:]), 20)
        self.assertEqual({r['probability_basis'] for r in rows}, {'binary_affirmative_no_push'})

    def test_fixture_coverage_is_one_fifth(self):
        rows = self.api('build_fixture')()
        forecast = self.api('policy_forecasts')(rows)
        self.assertEqual(len(forecast['covered_ids']), 10)
        self.assertEqual(len(forecast['cohort_ids']), 50)
        self.assertEqual(set(forecast['model']), set(forecast['covered_ids']))

    def test_abstention_remains_null_and_fallback_is_market(self):
        rows = self.api('build_fixture')()
        f = self.api('policy_forecasts')(rows)
        for r in rows[10:]:
            self.assertEqual(r['model_status'], 'ABSTAIN')
            self.assertIsNone(r['model_p'])
            self.assertNotIn(r['event_id'], f['model'])
            self.assertEqual(f['fallback'][r['event_id']], F(1, 2))

    def test_probability_basis_mismatch_is_rejected(self):
        rows = self.api('build_fixture')()
        rows[0]['probability_basis'] = 'raw_implied_price_probability'
        with self.assertRaises(ValueError):
            self.api('policy_forecasts')(rows)

    def test_complementary_side_duplicate_is_rejected(self):
        rows = self.api('build_fixture')()
        duplicate = copy.deepcopy(rows[0])
        duplicate['event_side'] = 'negative'
        rows.append(duplicate)
        with self.assertRaises(ValueError):
            self.api('policy_forecasts')(rows)

    def test_noncanonical_side_is_rejected(self):
        rows = self.api('build_fixture')()
        rows[0]['event_side'] = 'negative'
        with self.assertRaises(ValueError):
            self.api('policy_forecasts')(rows)

    def test_operational_missingness_is_not_abstention(self):
        rows = self.api('build_fixture')()
        rows[0]['model_status'] = 'MISSING'
        rows[0]['model_p'] = None
        with self.assertRaisesRegex(ValueError, 'operational missingness'):
            self.api('policy_forecasts')(rows)

    def test_predict_null_and_abstain_number_are_invalid(self):
        for index, value in [(0, None), (10, 0)]:
            rows = self.api('build_fixture')()
            rows[index]['model_p'] = value
            with self.assertRaises((ValueError, TypeError)):
                self.api('policy_forecasts')(rows)

    def test_exact_common_cohort_brier_quantities(self):
        result = self.api('calculate_results')()
        scores = result['brier']
        expected = {'market_all': F(109,500), 'model_covered': F(13,100),
                    'market_covered': F(9,100), 'fallback_all': F(113,500),
                    'mixture_covered': F(37,400), 'mixture_fallback_all': F(437,2000),
                    'fallback_minus_market_all': F(1,125),
                    'mixture_fallback_minus_market_all': F(1,2000)}
        for key, value in expected.items():
            self.assertEqual(F(scores[key]['exact']), value, key)

    def test_log_loss_quantities_are_direct_finite_sums(self):
        result = self.api('calculate_results')()
        logs = result['log_loss_nats']
        market_easy = -.9*math.log(.9)-.1*math.log(.1)
        model_easy = -.9*math.log(.7)-.1*math.log(.3)
        mix_easy = -.9*math.log(.85)-.1*math.log(.15)
        expected = {'market_covered':market_easy,'model_covered':model_easy,
                    'mixture_covered':mix_easy, 'market_all':.2*market_easy+.8*math.log(2),
                    'fallback_all':.2*model_easy+.8*math.log(2),
                    'mixture_fallback_all':.2*mix_easy+.8*math.log(2)}
        for key, value in expected.items():
            self.assertAlmostEqual(logs[key], value, places=14)

    def test_pair_requires_one_explicit_common_cohort(self):
        pair = self.api('paired_scores')
        with self.assertRaises(ValueError):
            pair({'a':.5}, {'a':.5,'b':.5}, {'a':1,'b':0}, ['a','b'])
        with self.assertRaises(ValueError):
            pair({'a':.5}, {'a':.5}, {'a':None}, ['a'])
        with self.assertRaises(ValueError):
            pair({'a':.5}, {'a':.5}, {'a':1}, ['a','a'])
        with self.assertRaises(ValueError):
            pair({}, {}, {}, [])

    def test_paired_log_loss_rejects_undefined_infinity_minus_infinity(self):
        pair = self.api('paired_scores')
        with self.assertRaisesRegex(ValueError, 'undefined'):
            pair({'a':0},{'a':0},{'a':1},['a'],'log_loss')
        with self.assertRaisesRegex(ValueError, 'undefined'):
            pair({'a':0,'b':.5},{'a':.5,'b':1},{'a':1,'b':0},['a','b'],'log_loss')

    def test_paired_log_loss_preserves_defined_one_sided_infinity(self):
        pair = self.api('paired_scores')
        left = pair({'a':0},{'a':.5},{'a':1},['a'],'log_loss')
        self.assertEqual(left['left_minus_right'],math.inf)
        right = pair({'a':.5},{'a':0},{'a':1},['a'],'log_loss')
        self.assertEqual(right['left_minus_right'],-math.inf)

    def test_pair_reports_same_denominator_and_oriented_delta(self):
        result = self.api('paired_scores')({'a':.7,'b':.7}, {'a':.9,'b':.9}, {'a':1,'b':0}, ['a','b'])
        self.assertEqual(result['n'], 2)
        self.assertEqual(result['left'], F(29,100))
        self.assertEqual(result['right'], F(41,100))
        self.assertEqual(result['left_minus_right'], F(-3,25))

    def test_missing_brier_identification_bounds_are_sharp(self):
        bounds = self.api('missing_brier_bounds')([.9,.5], [None,1])
        self.assertEqual(bounds, (F(13,100), F(53,100)))
        self.assertEqual(self.api('missing_brier_bounds')([.9], [None]), (F(1,100), F(81,100)))

    def test_missing_brier_bounds_contain_every_completion(self):
        bounds_fn = self.api('missing_brier_bounds')
        brier = self.api('brier')
        low, high = bounds_fn([.9,.2,.5],[None,None,1])
        completions = [sum([brier(.9,y0),brier(.2,y1),brier(.5,1)])/3 for y0 in [0,1] for y1 in [0,1]]
        self.assertEqual(low, min(completions))
        self.assertEqual(high, max(completions))

    def test_missing_bound_validates_denominator_and_forecasts(self):
        bound = self.api('missing_brier_bounds')
        for ps, ys in [([],[]),([.5],[]),([None],[None]),([.5],['PUSH'])]:
            with self.subTest(ps=ps,ys=ys), self.assertRaises((ValueError,TypeError)):
                bound(ps,ys)

    def test_paired_missing_bounds_share_each_unknown_outcome(self):
        bounds_fn = self.api('missing_paired_brier_bounds')
        self.assertEqual(bounds_fn([.7],[.9],[None]), (F(-8,25),F(2,25)))
        self.assertEqual(bounds_fn([.5],[.5],[None]), (F(0),F(0)))

    def test_log_loss_bounds_require_declared_epsilon_and_never_clip(self):
        bounds = self.api('missing_log_loss_bounds')
        with self.assertRaises((ValueError,TypeError)):
            bounds([.9],[None],epsilon=None)
        with self.assertRaises(ValueError):
            bounds([.999],[None],epsilon=.01)
        low,high = bounds([.9],[None],epsilon=.01)
        self.assertAlmostEqual(low,-math.log(.9),places=14)
        self.assertAlmostEqual(high,-math.log(.1),places=14)

    def test_complement_scores_are_identical_not_independent_samples(self):
        brier = self.api('brier')
        loss = self.api('log_loss')
        for p in [F(1,10),F(1,2),F(9,10)]:
            for y in [0,1]:
                self.assertEqual(brier(p,y),brier(1-p,1-y))
                self.assertAlmostEqual(loss(p,y),loss(1-p,1-y),places=14)

    def test_observation_mask_is_fixed_by_id_not_outcome(self):
        mask = self.api('observation_ids')
        ids = ['easy_001','easy_010','hard_001','hard_040']
        self.assertEqual(mask(ids), ['easy_001','hard_001'])

    def test_masked_demo_keeps_full_50_case_denominator(self):
        r = self.api('calculate_results')()['masked_demo']
        self.assertEqual(r['observed_n'],45)
        self.assertEqual(r['target_n'],50)
        self.assertEqual(r['missing_n'],5)
        self.assertEqual([F(v) for v in r['market_brier_bounds_exact']], [F(101,500),F(109,500)])
        self.assertEqual([F(v) for v in r['fallback_brier_bounds_exact']], [F(109,500),F(113,500)])
        self.assertEqual([F(v) for v in r['paired_delta_bounds_exact']], [F(1,125),F(2,125)])

    def test_report_has_no_empirical_performance_or_significance_claim(self):
        result = self.api('calculate_results')()
        self.assertEqual(result['evidence_type'],'invented_deterministic_educational_fixture')
        self.assertFalse(result['empirical_validation'])
        self.assertFalse(result['statistical_significance_estimated'])
        self.assertNotIn('p_value',result)

    def test_equal_coverage_optional_routing_counterexample(self):
        r = self.api('routing_counterexample')()
        self.assertEqual(r['cohort_n'], 30)
        self.assertEqual(r['a_covered_n'], 20)
        self.assertEqual(r['b_covered_n'], 20)
        expected = {'a_own_covered':F(3029,20000), 'b_own_covered':F(577,2500),
                    'a_common':F(263,1250), 'b_common':F(529,2500),
                    'market_all':F(23,120), 'a_policy_all':F(959,5000),
                    'b_policy_all':F(1379,7500), 'a_policy_minus_b_policy':F(119,15000)}
        for key,value in expected.items():
            self.assertEqual(F(r['brier'][key]['exact']),value,key)
        self.assertLess(r['brier']['a_own_covered']['decimal'],r['brier']['b_own_covered']['decimal'])
        self.assertLess(r['brier']['a_common']['decimal'],r['brier']['b_common']['decimal'])
        self.assertGreater(r['brier']['a_policy_all']['decimal'],r['brier']['b_policy_all']['decimal'])

    def test_optional_routing_decomposition_uses_disjoint_case_sets(self):
        r = self.api('routing_counterexample')()
        terms = r['brier_difference_total_by_route_exact']
        self.assertEqual(F(terms['both']),F(-3,250))
        self.assertEqual(F(terms['a_only']),F(1,40))
        self.assertEqual(F(terms['b_only']),F(9,40))
        self.assertEqual(F(terms['neither']),0)
        self.assertEqual(sum(F(v) for v in terms.values())/30,F(119,15000))

    def test_optional_routing_log_loss_ordering_is_independently_checked(self):
        r = self.api('routing_counterexample')()['log_loss_nats']
        ce = lambda q,p: -q*math.log(p)-(1-q)*math.log(1-p)
        self.assertAlmostEqual(r['a_own_covered'],(ce(.9,.85)+ce(.7,.68))/2,places=14)
        self.assertAlmostEqual(r['b_own_covered'],(ce(.7,.66)+ce(.5,.5))/2,places=14)
        self.assertAlmostEqual(r['a_policy_all'],(ce(.9,.85)+ce(.7,.68)+ce(.5,.65))/3,places=14)
        self.assertAlmostEqual(r['b_policy_all'],(ce(.9,.9)+ce(.7,.66)+ce(.5,.5))/3,places=14)
        self.assertLess(r['a_common'],r['b_common'])
        self.assertGreater(r['a_policy_all'],r['b_policy_all'])

    def test_outputs_are_deterministic(self):
        calculate = self.api('calculate_results')
        canonical = lambda x: json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
        self.assertEqual(hashlib.sha256(canonical(calculate())).hexdigest(),hashlib.sha256(canonical(calculate())).hexdigest())


if __name__ == '__main__':
    unittest.main(verbosity=2)
