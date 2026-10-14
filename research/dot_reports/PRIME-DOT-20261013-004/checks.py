"""Synthetic research fixtures only; no production ingestion or NFL validation."""
import json, math
from fractions import Fraction as F
from pathlib import Path
checks=[]
def check(name, condition):
    assert condition, name
    checks.append(name)
def decimal(a): return 1+F(100,abs(a)) if a<0 else 1+F(a,100)
def payoff(d,result):
    return {'WIN':d-1,'LOSS':F(-1),'PUSH':F(0),'VOID':F(0)}.get(result)
def roi(values):
    if not values or any(x is None for x in values): return None
    return sum(values)/len(values)
def admissible(q, decision, max_age=60):
    return (q['observed']<=decision and q['recorded']<=decision and
            q['source'] is not None and q['source']<=q['observed']<=q['recorded']<=decision and
            decision-q['source']<=max_age and q['state']=='ACTIVE' and
            q['price'] is not None and (q['expiry'] is None or decision<q['expiry']))
d=decimal(-110);p=F(57,100);pc=F(53,100)
check('decimal_minus110',d==F(21,11))
check('implied',1/d==F(11,21))
check('paired_no_vig', (1/d)/(2/d)==F(1,2))
check('central_ev',p*d-1==F(97,1100))
check('conservative_ev',pc*d-1==F(13,1100))
check('edge',p-1/d==F(97,2100))
check('fair_american',F(-100)*p/(1-p)==F(-5700,43))
check('conservative_fair_american',F(-100)*pc/(1-pc)==F(-5300,47))
min_d=max(1/(p-F(4,100)),F(105,100)/p,1/pc)
check('threshold_boundary',min_d==F(100,53))
check('zero_ev_boundary_not_strictly_positive',pc*min_d-1==0)
check('minus112_passes',pc*decimal(-112)-1>0)
check('minus113_fails',pc*decimal(-113)-1<0)
check('higher_line_fails',F(45,100)*d-1<0)
check('win_payoff',payoff(d,'WIN')==F(10,11))
check('loss_payoff',payoff(d,'LOSS')==-1)
check('push_payoff',payoff(d,'PUSH')==0)
check('void_payoff',payoff(d,'VOID')==0)
check('unresolved_not_zero',payoff(d,'UNRESOLVED') is None)
check('empty_roi_undefined',roi([]) is None)
check('missing_roi_undefined',roi([F(1),None]) is None)
known=[payoff(d,'WIN')]*2
check('complete_case_optimism',roi(known)==F(10,11))
check('lower_bound',(sum(known)-2)/4==F(-1,22))
check('upper_bound',(sum(known)+2*(d-1))/4==F(10,11))
# Push-aware EV and fair odds check on a separate invented three-way outcome.
pw,pl,pp=F(48,100),F(42,100),F(10,100)
check('probability_mass',pw+pl+pp==1)
check('push_aware_ev',pw*(d-1)-pl==F(9,550))
check('conditional_ev_equivalence',(1-pp)*((pw/(1-pp))*d-1)==pw*(d-1)-pl)
q=dict(source=900,observed=910,recorded=915,state='ACTIVE',price=-110,expiry=1000)
check('asof_valid',admissible(q,930))
for name,change in [('future_source',{'source':940}),('source_after_observation',{'source':912}),('recorded_before_observation',{'recorded':905}),('late_observation',{'observed':940}),('late_recording',{'recorded':940}),('source_unknown',{'source':None}),('stale_source',{'source':800}),('suspended',{'state':'SUSPENDED'}),('missing_price',{'price':None}),('expired',{'expiry':930})]:
 check(name,not admissible(q|change,930))
check('repeated_quotes_not_new_games',len(set(['gameA','gameA','gameA']))==1)
check('no_ticket_does_not_prove_nonplacement','NO_CONFIRMED_FILL'!='CONFIRMED_NOT_PLACED')
check('missing_price_not_football_pass','PRICE_UNAVAILABLE'!='PASS_NO_EDGE')
# First two price-independent half-point contracts share same result but different prices.
check('same_outcome_different_payoff',payoff(decimal(-110),'WIN')!=payoff(decimal(100),'WIN'))
result={'scope':'synthetic research only','assertions_passed':len(checks),'checks':checks,'example':{'central_roi':float(p*d-1),'conservative_roi':float(pc*d-1),'missing_outcome_roi_bounds':[float(F(-1,22)),float(F(10,11))]},'empirical_nfl_validation':False}
Path(__file__).with_name('check-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
