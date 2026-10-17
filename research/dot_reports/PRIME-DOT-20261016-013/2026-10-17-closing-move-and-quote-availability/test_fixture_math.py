"""Independent exact-value and negative-control oracles for synthetic fixtures."""
from copy import deepcopy
from fractions import Fraction as F
import unittest
import fixture_math as fm


class MechanicalTests(unittest.TestCase):
    def test_eight_equally_weighted_sign_combinations(self):
        result = fm.mechanical_fixture()
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result['rows']), 8)
        triples = {(r['u'], r['e'], r['v']) for r in result['rows']}
        self.assertEqual(len(triples), 8)
        self.assertEqual({r['weight'] for r in result['rows']}, {F(1, 8)})

    def test_covariance_and_correlation_exact_oracle(self):
        r = fm.mechanical_fixture()
        self.assertIsInstance(r, dict)
        self.assertEqual(r['covariance_move_model'], F(1, 2500))
        self.assertEqual(r['variance_model_deviation'], F(1, 2000))
        self.assertEqual(r['variance_close_move'], F(1, 2000))
        self.assertEqual(r['correlation'], F(4, 5))
        self.assertEqual(r['covariance_model_close_level'], 0)
        # Stronger than zero covariance: all four level pairs occur twice.
        self.assertEqual(sorted(r['level_pair_counts'].values()), [2, 2, 2, 2])

    def test_constant_beats_model_on_close_forecast_loss(self):
        r = fm.mechanical_fixture()
        self.assertIsInstance(r, dict)
        self.assertEqual(r['loss_model'], F(1, 5000))
        self.assertEqual(r['loss_no_change'], F(1, 2000))
        self.assertEqual(r['loss_constant'], F(1, 10000))
        self.assertLess(r['loss_constant'], r['loss_model'])
        self.assertLess(r['loss_model'], r['loss_no_change'])

    def test_paired_loss_identity_pointwise(self):
        # Nonidentical values catch direction and sign mistakes.
        for c, a, b in [(F(3, 5), F(11, 20), F(1, 2)),
                        (F(2, 5), F(3, 5), F(1, 2)),
                        (F(1, 2), F(1, 2), F(1, 2))]:
            expected = (c - b) ** 2 - (c - a) ** 2
            self.assertEqual(fm.paired_loss_improvement(c, a, b), expected)


class MissingnessAndSurvivalTests(unittest.TestCase):
    def test_all_attempt_bounds_and_complete_case_differ(self):
        r = fm.checkpoint_summary(['active'] * 6 + ['inactive'] * 2 + ['unknown'] * 2)
        self.assertIsInstance(r, dict)
        self.assertEqual(r, {'attempts': 10, 'active': 6, 'inactive': 2, 'unknown': 2,
                             'lower': F(3, 5), 'upper': F(4, 5),
                             'complete_case': F(3, 4)})

    def test_all_unknown_does_not_create_complete_case_estimate(self):
        r = fm.checkpoint_summary(['unknown'] * 3)
        self.assertIsInstance(r, dict)
        self.assertEqual((r['lower'], r['upper'], r['complete_case']), (0, 1, None))

    def test_zero_attempts_not_zero_availability(self):
        self.assertEqual(fm.checkpoint_summary([]), {'attempts': 0, 'active': 0,
            'inactive': 0, 'unknown': 0, 'lower': None, 'upper': None, 'complete_case': None})

    def test_invalid_observation_not_silently_dropped(self):
        with self.assertRaises(ValueError):
            fm.checkpoint_summary(['active', 'timeout'])

    def test_resurrection_cannot_repair_observed_interruption(self):
        self.assertEqual(fm.uninterrupted_status(['active', 'inactive', 'active']), 'refuted')

    def test_active_endpoints_do_not_prove_continuity(self):
        self.assertEqual(fm.uninterrupted_status(['active', 'active']), 'not_identified')
        self.assertEqual(fm.uninterrupted_status(['active', 'unknown', 'active']), 'not_identified')


class ClusterTests(unittest.TestCase):
    def test_identical_duplicate_rows_do_not_add_independent_games(self):
        rows = [(g, F(d, 100)) for g, d in [('g1', 1), ('g2', -1), ('g3', 2), ('g4', -2)]
                for _ in range(10)]
        r = fm.cluster_summary(rows)
        self.assertIsInstance(r, dict)
        self.assertEqual(r['rows'], 40)
        self.assertEqual(r['games'], 4)
        self.assertEqual(r['row_mean'], 0)
        self.assertEqual(r['game_equal_weight_mean'], 0)
        self.assertEqual(r['naive_row_mean_variance'], F(1, 156000))
        self.assertEqual(r['game_mean_variance'], F(1, 12000))
        self.assertEqual(r['game_mean_variance'] / r['naive_row_mean_variance'], 13)

    def test_single_game_has_no_between_game_variance_estimate(self):
        r = fm.cluster_summary([('only', F(1, 100))] * 5)
        self.assertIsInstance(r, dict)
        self.assertIsNone(r['game_mean_variance'])


class GuardTests(unittest.TestCase):
    def test_valid_case_has_no_rejections(self):
        self.assertEqual(fm.guard_case(fm.valid_guard_case()), [])

    def test_forecast_must_be_recorded_strictly_before_decision(self):
        c = fm.valid_guard_case()
        self.assertIn('decision_at', c)
        c['forecast_recorded_at'] = c['decision_at']
        self.assertIn('forecast_not_locked_before_decision', fm.guard_case(c))

    def test_initial_request_cannot_finish_at_kickoff(self):
        c = fm.valid_guard_case()
        self.assertIn('kickoff_at', c)
        c['initial_completed_at'] = c['kickoff_at']
        self.assertIn('initial_completion_not_before_kickoff', fm.guard_case(c))

    def test_close_request_cannot_finish_at_kickoff(self):
        c = fm.valid_guard_case()
        self.assertIn('kickoff_at', c)
        c['close_completed_at'] = c['kickoff_at']
        self.assertIn('close_completion_not_before_kickoff', fm.guard_case(c))

    def test_contract_mismatches_never_match(self):
        original = fm.valid_guard_case()
        self.assertIn('close', original)
        # Each mismatch separately proves the guard is active.
        for field in ['event', 'participant', 'market', 'period', 'threshold', 'book', 'region', 'settlement']:
            c = deepcopy(original)
            c['close'][field] = F(501, 2) if field == 'threshold' else 'DIFFERENT'
            with self.subTest(field=field):
                self.assertIn('close_' + field + '_mismatch', fm.guard_case(c))

    def test_missing_threshold_stays_unmatched(self):
        c = fm.valid_guard_case()
        self.assertIn('close', c)
        c['close']['threshold'] = None
        self.assertIn('close_threshold_missing', fm.guard_case(c))

    def test_opposite_quotes_require_full_contract_and_opposite_side(self):
        original = fm.valid_guard_case()
        self.assertIn('initial_opposite', original)
        for name in ['initial_opposite', 'close_opposite']:
            for field in ['threshold', 'book', 'region', 'settlement', 'side']:
                c = deepcopy(original)
                c[name][field] = F(501, 2) if field == 'threshold' else ('over' if field == 'side' else 'DIFFERENT')
                with self.subTest(quote=name, field=field):
                    self.assertIn(name + '_' + field + '_mismatch', fm.guard_case(c))

    def test_exact_close_lag_not_rounded_or_assumed(self):
        c = fm.valid_guard_case()
        self.assertIn('recorded_close_lag_seconds', c)
        c['recorded_close_lag_seconds'] = 59
        self.assertIn('close_lag_mismatch', fm.guard_case(c))

    def test_wrong_prespecified_close_lag_is_not_interpolated(self):
        c = fm.valid_guard_case()
        self.assertIn('required_close_lag_seconds', c)
        c['required_close_lag_seconds'] = 30
        self.assertIn('close_lag_outside_fixture_target', fm.guard_case(c))

    def test_decision_cannot_precede_initial_response(self):
        c = fm.valid_guard_case()
        self.assertIn('initial_started_at', c)
        c['decision_at'] = c['initial_started_at']
        self.assertIn('initial_response_after_decision', fm.guard_case(c))

    def guard_without_exception(self, case):
        try:
            return fm.guard_case(case)
        except Exception as exc:
            self.fail(f'Malformed inputs must be rejected, not raise {type(exc).__name__}: {exc}')

    def test_all_unknown_identity_fields_cannot_match_each_other(self):
        original = fm.valid_guard_case()
        for field in ['event', 'participant', 'market', 'period', 'book', 'region', 'settlement']:
            for value in [None, '', '   ']:
                c = deepcopy(original)
                for quote in ['initial', 'close', 'initial_opposite', 'close_opposite']:
                    c[quote][field] = value
                with self.subTest(field=field, value=value):
                    self.assertNotEqual(self.guard_without_exception(c), [])

    def test_all_unknown_or_unrecognized_sides_cannot_match(self):
        for value in [None, '', 'push', 'OVER']:
            c = fm.valid_guard_case()
            for quote in ['initial', 'close', 'initial_opposite', 'close_opposite']:
                c[quote]['side'] = value
            with self.subTest(value=value):
                self.assertNotEqual(self.guard_without_exception(c), [])

    def test_all_invalid_thresholds_cannot_match(self):
        for value in [None, '', True, float('nan'), float('inf')]:
            c = fm.valid_guard_case()
            for quote in ['initial', 'close', 'initial_opposite', 'close_opposite']:
                c[quote]['threshold'] = value
            with self.subTest(value=repr(value)):
                self.assertNotEqual(self.guard_without_exception(c), [])

    def test_missing_contract_field_is_a_rejection_not_a_crash(self):
        c = fm.valid_guard_case()
        del c['close']['book']
        self.assertIsInstance(self.guard_without_exception(c), list)
        self.assertNotEqual(self.guard_without_exception(c), [])

    def test_missing_or_wrong_type_quote_is_a_rejection(self):
        for value in [None, 'not a quote', []]:
            c = fm.valid_guard_case()
            c['close'] = value
            with self.subTest(value=value):
                self.assertNotEqual(self.guard_without_exception(c), [])

    def test_missing_naive_or_nondatetime_time_is_rejected(self):
        original = fm.valid_guard_case()
        times = ['forecast_recorded_at', 'decision_at', 'initial_started_at',
                 'initial_completed_at', 'close_started_at', 'close_completed_at', 'kickoff_at']
        for field in times:
            for value in [None, '2026-01-01T12:00:00Z', original[field].replace(tzinfo=None)]:
                c = deepcopy(original)
                c[field] = value
                with self.subTest(field=field, value=str(value)):
                    self.assertNotEqual(self.guard_without_exception(c), [])

    def test_missing_time_key_is_a_rejection_not_a_crash(self):
        c = fm.valid_guard_case()
        del c['kickoff_at']
        self.assertNotEqual(self.guard_without_exception(c), [])

    def test_missing_or_invalid_lags_are_rejected(self):
        for field in ['recorded_close_lag_seconds', 'required_close_lag_seconds']:
            for value in [None, True, '60', float('nan'), float('inf'), -1]:
                c = fm.valid_guard_case()
                c[field] = value
                with self.subTest(field=field, value=repr(value)):
                    self.assertNotEqual(self.guard_without_exception(c), [])

    def test_inverted_request_timing_is_rejected(self):
        c = fm.valid_guard_case()
        self.assertIn('close_started_at', c)
        c['close_started_at'] = c['kickoff_at']
        self.assertIn('close_request_timing_inverted', fm.guard_case(c))


if __name__ == '__main__':
    unittest.main(verbosity=2)
