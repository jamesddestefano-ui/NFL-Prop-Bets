"""Run all named tests and emit reproducible public educational results JSON."""
from fractions import Fraction as F
import json
from pathlib import Path
import sys
import unittest
import frozen_study as s
import test_frozen_study


def cases(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from cases(item)
        else:
            yield item


def main():
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_frozen_study)
    names = [test.id() for test in cases(suite)]
    result = unittest.TestResult()
    suite.run(result)
    fixture = json.loads(Path(__file__).with_name('fixture.json').read_text())
    m, g, y = [F(1,10),F(1,2)], [F(7,10),F(9,10)], [0,1]
    output = {
        'notice': 'PUBLIC EDUCATIONAL SYNTHETIC EXAMPLES ONLY; no real performance, current odds, or confidence-interval validity claim.',
        'status': 'PASS' if result.wasSuccessful() else 'FAIL',
        'tests_run': result.testsRun,
        'named_tests': names,
        'failures': [(test.id(), detail) for test,detail in result.failures],
        'errors': [(test.id(), detail) for test,detail in result.errors],
        'four_arm_comparison': s.compare_four_arms(fixture),
        'fixed_weight_brier_expansion': s.brier_expansion(m,g,y,F(1,4)),
        'oracle_weight_not_selected': s.oracle_weight(m,g,y),
        'fixed_weight_selected': F(1,4),
        'conditional_probability': {
            'q': F(3,5), 'decimal_odds': F(2),
            'no_push_wlp': s.full_wlp(F(3,5),F(0)),
            'half_push_wlp': s.full_wlp(F(3,5),F(1,2)),
            'no_push_roi': s.roi(s.full_wlp(F(3,5),F(0)),F(2)),
            'half_push_roi': s.roi(s.full_wlp(F(3,5),F(1,2)),F(2)),
        },
        'weighting_example': {
            'equal_game_delta': F(-3,160),
            'opposite_side_duplicated_naive_row_delta': F(1,200),
            'whole_game_resample_means': s.cluster_resample_means([F(21,400),F(-9,100)]),
            'ci_claim': 'None: two games only illustrate resampling mechanics.',
        },
        'endpoint_log_loss': {
            'zero_probability_for_observed_outcome': 'positive infinity',
            'infinity_minus_infinity': 'undefined; comparison raises ValueError',
        },
    }
    print(json.dumps(output, indent=2, default=lambda value: str(value), allow_nan=False))
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(main())
