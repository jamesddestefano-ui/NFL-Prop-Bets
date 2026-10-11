"""Finite-sum, floating-point invented NFL opportunity examples. No fitted NFL parameters or market odds."""
from math import comb, isclose
import json
from pathlib import Path

def binom(n,p):
    return [comb(n,k)*p**k*(1-p)**(n-k) for k in range(n+1)]

def conv(a,b):
    out=[0.]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def stats(pmf):
    mean=sum(k*p for k,p in enumerate(pmf))
    return {'mean':mean,'variance':sum((k-mean)**2*p for k,p in enumerate(pmf))}

def receiver(short,deep):
    # Each short route: target=.30, catch conditional target=.80, yards if caught=8.
    # Each deep route: target=.10, catch conditional target=.40, yards if caught=30.
    s,d=binom(short,.30*.80),binom(deep,.10*.40)
    rec=conv(s,d)
    yards=[0.]*(8*short+30*deep+1)
    for i,x in enumerate(s):
        for j,y in enumerate(d): yards[8*i+30*j]+=x*y
    return {'routes':short+deep,'route_participation':(short+deep)/40,
            'expected_targets':short*.30+deep*.10,
            'expected_targets_per_route':(short*.30+deep*.10)/(short+deep),
            'receptions':stats(rec),'p_over_4_5_receptions':sum(rec[5:]),
            'yards':stats(yards),'p_over_49_5_yards':sum(yards[50:])}

base,expanded=receiver(18,6),receiver(18,18)
a,b=binom(60,.6*.7),binom(60,.3*.5)
mix=[.5*x+.5*y for x,y in zip(a,b)]
flat=binom(60,.285)
res={'label':'All inputs invented; arithmetic only, not empirical NFL probabilities',
     'receiver_baseline':base,'receiver_expanded_deep_routes':expanded,
     'carry_mixture':{**stats(mix),'p_over_19_5':sum(mix[20:])},
     'carry_same_mean_binomial':{**stats(flat),'p_over_19_5':sum(flat[20:])},
     'carry_product_of_mean_rates':60*((.6+.3)/2)*((.7+.5)/2)}
checks=0
for pmf in [a,b,mix,flat]:
    assert isclose(sum(pmf),1,abs_tol=1e-12); checks+=1
assert isclose(base['receptions']['mean'],4.56); checks+=1
assert isclose(expanded['receptions']['mean'],5.04); checks+=1
assert isclose(base['yards']['mean'],41.76); checks+=1
assert isclose(expanded['yards']['mean'],56.16); checks+=1
assert isclose(res['carry_mixture']['mean'],17.1); checks+=1
assert isclose(res['carry_same_mean_binomial']['mean'],17.1); checks+=1
assert isclose(res['carry_mixture']['variance'],76.743); checks+=1
assert isclose(res['carry_same_mean_binomial']['variance'],12.2265); checks+=1
assert isclose(res['carry_product_of_mean_rates'],16.2); checks+=1
res['passed_checks']=checks
p=Path(__file__).with_name('example_results.json')
p.write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
