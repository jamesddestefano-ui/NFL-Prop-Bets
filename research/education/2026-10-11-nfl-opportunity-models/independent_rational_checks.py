"""Independent rational audit of invented opportunity-count fixtures.

Imports no code from the reviewed implementation. All finite probabilities and
moments use Fraction; conversion to float occurs only to compare saved outputs.
"""
from fractions import Fraction as F
from math import comb, isclose
from pathlib import Path
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=Path, default=Path(__file__).with_name('example_results.json'))
parser.add_argument('--output', type=Path, default=Path(__file__).with_name('rational_audit_results.json'))
args = parser.parse_args()
saved = json.loads(args.input.read_text())
checks = []

def mass(n, p):
    return [F(comb(n, k)) * p**k * (1-p)**(n-k) for k in range(n+1)]

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def matches(x, y):
    return isclose(float(x), y, rel_tol=0, abs_tol=1e-12)

def encode(x):
    return {'exact_fraction': str(x), 'decimal_approximation': float(x)}

receiver_results = []
short_mass = mass(18, F(6, 25))
for n, key in [(6, 'receiver_baseline'), (18, 'receiver_expanded_deep_routes')]:
    deep_mass = mass(n, F(1, 25))
    pairs = [(i, j, a*b) for i, a in enumerate(short_mass) for j, b in enumerate(deep_mass)]
    check(key+' exact normalization', sum(v for i, j, v in pairs) == 1)
    rec_tail = sum(v for i, j, v in pairs if i+j >= 5)
    yard_tail = sum(v for i, j, v in pairs if 8*i+30*j >= 50)
    check(key+' reception tail', matches(rec_tail, saved[key]['p_over_4_5_receptions']))
    check(key+' yardage tail', matches(yard_tail, saved[key]['p_over_49_5_yards']))
    rec_mean = sum((i+j)*v for i, j, v in pairs)
    yard_mean = sum((8*i+30*j)*v for i, j, v in pairs)
    rec_variance = sum((i+j-rec_mean)**2*v for i, j, v in pairs)
    yard_variance = sum((8*i+30*j-yard_mean)**2*v for i, j, v in pairs)
    check(key+' exact reception mean', rec_mean == 18*F(6,25)+n*F(1,25))
    check(key+' yardage mean', matches(yard_mean, saved[key]['yards']['mean']))
    check(key+' reception variance', matches(rec_variance, saved[key]['receptions']['variance']))
    check(key+' yardage variance', matches(yard_variance, saved[key]['yards']['variance']))
    receiver_results.append({'case':key, 'reception_tail':encode(rec_tail), 'yardage_tail':encode(yard_tail),
                             'reception_mean':encode(rec_mean), 'yardage_mean':encode(yard_mean),
                             'reception_variance':encode(rec_variance), 'yardage_variance':encode(yard_variance)})

high, low = F(21,50), F(3,20)
mean_probability = (high+low)/2
within = F(60,2)*(high*(1-high)+low*(1-low))
between = F(60**2,4)*(high-low)**2
check('carry variance by total-variance decomposition', within+between == F(76743,1000))
check('single-binomial carry variance', 60*mean_probability*(1-mean_probability) == F(24453,2000))
carry_results = []
for key, dist in [('carry_mixture', [(a+b)/2 for a,b in zip(mass(60,high),mass(60,low))]),
                  ('carry_same_mean_binomial', mass(60,mean_probability))]:
    check(key+' exact normalization', sum(dist) == 1)
    tail = sum(dist[20:])
    check(key+' tail', matches(tail, saved[key]['p_over_19_5']))
    carry_results.append({'case':key,'tail':encode(tail)})

covariance = (F(3,5)*F(7,10)+F(3,10)*F(1,2))/2-F(9,20)*F(3,5)
check('product-of-means mean error', 60*covariance == F(9,10))
result = {'status':'PASS','named_check_count':len(checks),'checks':checks,
          'receiver_results':receiver_results,'carry_results':carry_results,
          'carry_within_script_variance':encode(within),'carry_between_script_variance':encode(between),
          'run_probability_carry_share_covariance':encode(covariance),'product_of_means_error':encode(60*covariance),
          'scope':'Invented fixtures only. Exact finite rational probabilities and moments; no NFL data, source-performance verification or model validation.'}
args.output.write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: {len(checks)} independent rational checks; {args.output}')
