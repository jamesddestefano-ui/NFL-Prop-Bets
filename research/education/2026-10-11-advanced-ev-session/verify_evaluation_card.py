"""Exact synthetic active-WR price card. No wagering or empirical validation."""
from fractions import Fraction as F
import json
from math import comb, floor
from pathlib import Path

p_catch=F(13,20)
tail=lambda n:sum((F(comb(n,k))*p_catch**k*(1-p_catch)**(n-k) for k in range(5,n+1)),F())
high,ordinary=tail(8),tail(6)
central=F(2,3)*high+F(1,3)*ordinary
adverse=(high+ordinary)/2
d=F(21,11)
implied=1/d
no_vig=implied/(implied+implied)
checks=[]
def test(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)
def encode(x):
    if isinstance(x,F):return {'exact':str(x),'decimal':float(x)}
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,list):return [encode(v) for v in x]
    return x
test('matching same-time complementary -110 prices imply no-vig .50',no_vig==F(1,2))
test('raw implied probability is 11/21',implied==F(11,21))
cases=[]
for name,p in [('raw_central',central),('assumption_only_adverse',adverse)]:
    be_decimal=1/p
    be_american=-100*p/(1-p)
    first_pass=-floor(-be_american)
    first_fail=first_pass-1
    whole=[]
    for a in [first_pass,first_fail]:
        quoted_d=1+F(100,abs(a))
        whole.append({'american':a,'decimal':quoted_d,'roi':p*quoted_d-1})
    test(name+' exact break-even gives zero EV',p*be_decimal-1==0)
    test(name+' American boundary matches decimal',1+F(100)/abs(be_american)==be_decimal)
    test(name+' better whole-number price strictly positive',whole[0]['roi']>0)
    test(name+' next worse whole-number price negative',whole[1]['roi']<0)
    cases.append({'name':name,'p':p,'minus_offered_break_even':p-implied,'minus_no_vig_reference':p-no_vig,'roi_at_minus110':p*d-1,'zero_EV_decimal':be_decimal,'zero_EV_American':be_american,'whole_integer_price_checks':whole})
test('central positive but adverse negative at offered price',central*d-1>0>adverse*d-1)
result={'scope':'All inputs invented. Active WR Over 4.5 receptions, matching same-time hypothetical Over -110 and Under -110. No push or void in this card. Adverse probability is an assumption-only role stress, not a calibrated lower bound.','offered_decimal':d,'offered_raw_implied_probability':implied,'same_book_complementary_raw_implied_probability':implied,'two_way_overround':2*implied-1,'proportional_no_vig_probability':no_vig,'cases':cases,'boundary_rule':'Equality is zero EV. Positive EV requires decimal odds strictly above the zero-EV decimal boundary, equivalently a strictly better American price.','operational_status':'No operational play-to price or line. Role, calibration, reference-quality and other applicable gates remain unresolved. These boundaries enforce positive EV only.','test_count':len(checks),'checks':checks,'status':'PASS'}
out=Path(__file__).with_name('evaluation_card_verified.json')
out.write_text(json.dumps(encode(result),indent=2)+'\n')
print(f'PASS: {len(checks)} price-card checks; {out}')
