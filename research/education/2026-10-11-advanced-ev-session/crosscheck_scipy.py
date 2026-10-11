#!/usr/bin/env python3
"""Independent numerical cross-checks of the educational fixtures.

Requires SciPy. It reads new_lesson_results.json and writes a separate result.
No real NFL data, network access, production code or betting action is involved.
The main verify_new_lessons.py script requires only the Python standard library.
"""

import argparse
import json
import math
from pathlib import Path
import platform

import scipy
from scipy.integrate import quad
from scipy.stats import binom, nbinom, gamma


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=Path(__file__).with_name('new_lesson_results.json'))
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('crosscheck_scipy.json'))
    args = parser.parse_args()
    raw = json.loads(args.input.read_text())
    ex = raw['examples']
    checks = []
    def close(name, got, expected, tol=1e-11):
        error = abs(got-expected)
        if error > tol:
            raise AssertionError((name, got, expected, error, tol))
        checks.append({'name': name, 'calculated': got, 'reference': expected,
                       'absolute_error': error, 'tolerance': tol})

    role = ex['1_role_news_update']
    high, low = float(binom.sf(4,8,.65)), float(binom.sf(4,6,.65))
    close('8-target tail from scipy binomial survival', high, role['high_role_over_probability']['decimal'])
    close('6-target tail from scipy binomial survival', low, role['ordinary_role_over_probability']['decimal'])
    p = high*2/3+low/3
    close('mixture using scipy tails',p,role['cases'][1]['event_probability']['decimal'])
    close('binary payoff from win/loss expectation',p*(10/11)-(1-p),role['cases'][1]['roi_at_minus110']['decimal'])

    gp = ex['4_predictive_checks_and_holdout']['gamma_poisson']
    t = float(nbinom.sf(499,501,101/201))
    close('replicated total upper tail from scipy negative binomial',t,gp['mean_statistic_posterior_predictive_tail'])
    # Independent integration of exp(-lambda) against Gamma(shape=501,rate=101).
    # The upper endpoint 10 is far beyond the posterior mass for this fixture.
    integrand = lambda x: math.exp(-x+500*math.log(x)-101*x+501*math.log(101)-math.lgamma(501))
    z, quad_error = quad(integrand,0,10,epsabs=1e-13,epsrel=1e-11)
    close('single replicated zero probability by direct quadrature',z,gp['predictive_zero_probability'])
    omitted_tail_bound = math.exp(-10)*float(gamma.sf(10,a=501,scale=1/101))
    if omitted_tail_bound >= 1e-13:
        raise AssertionError('Quadrature tail bound exceeds tolerance')
    log_bound = math.lgamma(101)-2*math.lgamma(51)+501*(math.log(101)-math.log(151))
    close('shared-lambda union bound on log scale',log_bound,math.log(gp['P_replicated_zero_count_ge_50_upper_bound']))

    # Explicit 50-row population, independent of the original joint-cell builder.
    rows=[]
    for a,b,wins,losses in [(1,1,16,1),(1,0,4,4),(0,1,4,4),(0,0,1,16)]:
        rows.extend([(a,b,1)]*wins+[(a,b,0)]*losses)
    for signal in [0,1]:
        for column in [0,1]:
            selected=[r for r in rows if r[column]==signal]
            close(f'component {column} calibration for signal {signal}',sum(r[2] for r in selected)/len(selected),.8 if signal else .2)
    individual=sum(((.8 if a else .2)-y)**2 for a,b,y in rows)/50
    ensemble=sum((((.8 if a else .2)+(.8 if b else .2))/2-y)**2 for a,b,y in rows)/50
    fused_p={(1,1):16/17,(1,0):.5,(0,1):.5,(0,0):1/17}
    fused=sum((fused_p[a,b]-y)**2 for a,b,y in rows)/50
    e5=ex['5_calibrated_source_ensemble']
    close('single-source Brier from explicit rows',individual,e5['single_source_population_Brier']['decimal'])
    close('averaged Brier from explicit rows',ensemble,e5['averaged_forecast_population_Brier']['decimal'])
    close('fused Brier from explicit rows',fused,e5['correctly_fused_population_Brier']['decimal'])

    result={'scope':'Synthetic consistency cross-checks only; no empirical NFL validation.',
            'status':'PASS','check_count':len(checks),'python_version':platform.python_version(),
            'scipy_version':scipy.__version__,'quadrature_absolute_error_estimate':quad_error,
            'quadrature_omitted_tail_upper_bound':omitted_tail_bound,
            'checks':checks}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(checks)} independent cross-checks; results: {args.output}')


if __name__=='__main__':
    main()
