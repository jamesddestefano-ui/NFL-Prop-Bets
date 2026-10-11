"""Deterministic binomial-oracle checks for an invented fixed-model example.
Requires the already installed numpy/scipy. Does not test an NFL model.
"""
import json
import numpy as np
from scipy.stats import binom

n, hits, p0, d = 10_000, 5_280, 0.528, 21 / 11
z = 1.959963984540054
phat = hits / n

def wilson(p, n):
    denom = 1 + z*z/n
    center = (p + z*z/(2*n)) / denom
    half = z*np.sqrt(p*(1-p)/n + z*z/(4*n*n)) / denom
    return center-half, center+half

lo, hi = wilson(phat, n)
k = np.arange(n+1)
x = k/n
mass = binom.pmf(k, n, p0)
mean = np.sum(mass*x)
variance = np.sum(mass*(x-p0)**2)
ev_variance = np.sum(mass*((d*x-1)-(d*p0-1))**2)
all_lo, all_hi = wilson(x, n)
coverage = mass[(all_lo <= p0) & (p0 <= all_hi)].sum()
expected_variance = p0*(1-p0)/n
assert abs(mass.sum()-1) < 1e-12
assert abs(mean-p0) < 1e-12
assert abs(variance/expected_variance-1) < 1e-10
assert abs(ev_variance/(d*d*expected_variance)-1) < 1e-10
# Fixed-p binomial oracle: all possible count outcomes, not random replicates.
# This interval has approximate 95% coverage; this checks this particular p,n.
assert 0.948 <= coverage <= 0.952
assert lo < 1/d < hi
se = np.sqrt(phat*(1-phat)/n)
result = {
    'assumptions': 'iid Bernoulli draws; fixed model; fixed N; fixed price; binary settlement',
    'n': n, 'hits': hits, 'phat': phat, 'decimal_price': d,
    'break_even_p': 1/d, 'plugin_mcse_p': se,
    'wilson_approx_95_p': [lo, hi], 'ev_per_accounting_unit': d*phat-1,
    'mcse_ev': d*se, 'wilson_approx_95_ev': [d*lo-1, d*hi-1],
    'oracle_p0': p0, 'oracle_mean_phat': mean,
    'oracle_variance_phat': variance,
    'formula_variance_phat': expected_variance,
    'oracle_wilson_coverage': coverage,
    'projected_mcse_at_1000000_same_p': se/10,
    'validation': 'PASS: exact binomial summation within stated numerical tolerances'
}
print(json.dumps(result, indent=2))
