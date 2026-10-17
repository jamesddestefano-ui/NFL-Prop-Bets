#!/usr/bin/env python3
"""Recheck test suite, exact saved artifact, determinism, and SHA-256 manifest.

Run from any directory: python -B /path/to/math/verify.py
No network, nonstandard packages, private inputs, or writes are needed.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def run_fresh(*args):
    return subprocess.run([sys.executable, '-B', *args], cwd=ROOT,
                          text=True, capture_output=True, check=True)


def main():
    tests = run_fresh('-m', 'unittest', 'discover', '-v')
    # unittest logs to stderr. Keep the complete test evidence visible.
    print(tests.stdout + tests.stderr, end='')
    first = run_fresh('fixture_math.py').stdout
    second = run_fresh('fixture_math.py').stdout
    if first != second:
        raise AssertionError('Fresh-process generated outputs differ.')
    if first != (ROOT / 'results.json').read_text():
        raise AssertionError('Saved results.json is stale or altered.')
    data = json.loads(first)
    m = data['mechanical']
    # Independent integer-rational oracles, not recomputed by implementation helpers.
    expected = {'covariance_move_model': '1/2500', 'variance_model_deviation': '1/2000',
                'variance_close_move': '1/2000', 'correlation': '4/5',
                'loss_model': '1/5000', 'loss_no_change': '1/2000',
                'loss_constant': '1/10000', 'paired_improvement_no_change': '3/10000',
                'paired_improvement_constant': '-1/10000'}
    for key, value in expected.items():
        if m[key]['exact'] != value:
            raise AssertionError(f'Wrong exact result: {key}')
    if len(m['rows']) != 8 or any(row['weight']['exact'] != '1/8' for row in m['rows']):
        raise AssertionError('Wrong finite population or weights.')
    av = data['checkpoint_availability']
    if [av[k]['exact'] for k in ('lower', 'upper', 'complete_case')] != ['3/5', '4/5', '3/4']:
        raise AssertionError('Wrong checkpoint missingness bounds.')
    if data['guards']['outcomes']['valid'] != {'matched': True, 'reasons': []}:
        raise AssertionError('Valid guard fixture failed.')
    if any(v['matched'] for k, v in data['guards']['outcomes'].items() if k != 'valid'):
        raise AssertionError('An invalid guard fixture matched.')
    for line in (ROOT / 'SHA256SUMS').read_text().splitlines():
        expected_hash, name = line.split('  ', 1)
        if Path(name).name != name:
            raise AssertionError('Manifest path must be a local filename.')
        actual_hash = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            raise AssertionError(f'Manifest mismatch: {name}')
    print('PASS: two fresh-process outputs are byte-identical and match results.json.')
    print('PASS: independent exact-value artifact oracles, guard outcomes, and SHA-256 manifest.')
    print('All inputs are synthetic. No network or live quote was used.')


if __name__ == '__main__':
    main()
