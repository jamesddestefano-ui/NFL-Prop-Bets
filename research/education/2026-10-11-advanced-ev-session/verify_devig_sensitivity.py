"""Optional synthetic de-vig sensitivity check, not a sixth core lesson.
No quote is observed; transforms of assumed prices are not true probabilities.
"""
from fractions import Fraction as F
import json
from pathlib import Path

q_over,q_under=F(5,19),F(4,5)  # Invented +280 / -400, exact same contract/time.
Q=q_over+q_under
offered_decimal=F(21,5)  # Invented different executable venue at +320.
proportional=q_over/Q
additive=(1+q_over-q_under)/2
z=(q_over*q_over/Q-additive*additive)/(additive*(1-additive))
checks=[]
def test(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)
test('overround exact',Q==F(101,95))
test('proportional probability exact',proportional==F(25,101))
test('additive probability exact',additive==F(22,95))
test('Shin parameter feasible for this example',0<=z<1)
for q,p in [(q_over,additive),(q_under,1-additive)]:
    test('binary Shin normalized identity for '+str(q),q*q/Q==(1-z)*p*p+z*p)
# Unique k>1 since q_over^k+q_under^k strictly decreases to zero.
lo,hi=1.,3.
for _ in range(100):
    mid=(lo+hi)/2
    if float(q_over)**mid+float(q_under)**mid>1:lo=mid
    else:hi=mid
power=(lo+hi)/2
power_p=float(q_over)**power
test('power probabilities normalize',abs(power_p+float(q_under)**power-1)<1e-14)
test('devig choice reverses modeled EV sign',proportional*offered_decimal-1>0>additive*offered_decimal-1 and power_p*float(offered_decimal)-1<0)
test('favorable proportional case below illustrative 4pp edge hurdle',proportional-1/offered_decimal<F(4,100))
test('favorable proportional case below illustrative 5percent ROI hurdle',proportional*offered_decimal-1<F(5,100))
def numeric(x):return {'exact':str(x),'decimal':float(x)} if isinstance(x,F) else x
methods=[]
for name,p in [('proportional',proportional),('additive_equals_binary_Shin',additive),('power',power_p)]:
    methods.append({'method':name,'p':numeric(p),'roi':numeric(p*offered_decimal-1),'minus_offered_break_even':numeric(p-1/offered_decimal)})
result={'status':'PASS','test_count':len(checks),'checks':checks,'scope':'Invented active-receiver Over 99.5 yards, identical settlement and notional time, no actual quote/fill. This illustrates existing sensitivity requirements; it does not identify true probability or validate a reference book. Nominal hurdles are arithmetic fixtures, not rule changes.','reference_Over_American':280,'reference_Under_American':-400,'raw_implied_Over':numeric(q_over),'raw_implied_Under':numeric(q_under),'raw_implied_sum':numeric(Q),'offered_American':320,'offered_decimal':numeric(offered_decimal),'offered_break_even':numeric(1/offered_decimal),'binary_Shin_parameter':numeric(z),'power_exponent':power,'methods':methods,'Shin_derivation':'Assume q_i²/Q=(1-z)p_i²+z*p_i and p1+p2=1. Subtraction gives q1-q2=p1-p2, hence p1=(1+q1-q2)/2, exactly the additive transform for two outcomes.'}
path=Path(__file__).with_name('devig_sensitivity_verified.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: {len(checks)} optional de-vig checks; {path}')
