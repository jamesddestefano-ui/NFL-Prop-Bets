#!/usr/bin/env python3
"""Independently cross-check exact toy PMFs/tails against installed SciPy.

Run: python crosscheck_scipy.py
Requires an existing SciPy installation; performs no installation or network I/O.
Writes crosscheck_scipy.json alongside this file. No NFL observations are used.
"""
import json
from fractions import Fraction as F
from math import isclose
from pathlib import Path

import scipy
from scipy.stats import binom, betabinom

from verify_examples import binomial, beta_binomial


def main():
    tolerance = 1e-12
    pairs = [
        ("binomial_n8", binomial(8, F(13, 20)), binom(8, .65)),
        ("beta_binomial_n8", beta_binomial(8, F(13, 2), F(7, 2)),
         betabinom(8, 6.5, 3.5)),
    ]
    summary = []
    for name, pmf, distribution in pairs:
        errors = [abs(float(probability)-float(distribution.pmf(r)))
                  for r, probability in pmf.items()]
        assert max(errors) <= tolerance
        for threshold in range(10):
            exact_tail = float(sum(probability for r, probability in pmf.items()
                                   if r >= threshold))
            assert isclose(exact_tail, float(distribution.sf(threshold-1)),
                           rel_tol=0, abs_tol=tolerance)
        summary.append({
            "distribution": name,
            "maximum_pmf_absolute_error": max(errors),
            "all_threshold_tails_0_to_9_match": True,
        })
    output = {"scipy_version": scipy.__version__, "comparisons": summary,
              "tolerance": tolerance}
    path = Path(__file__).with_name("crosscheck_scipy.json")
    path.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
