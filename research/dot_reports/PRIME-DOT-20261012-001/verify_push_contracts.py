"""Research fixtures only. No live prices, NFL probability estimates or production imports."""
from fractions import Fraction as F
import json, math
from pathlib import Path
checks=[]
def check(name, condition):
    assert condition, name
    checks.append(name)
def roi(w,t,l,d):
    assert w+t+l==1 and min(w,t,l)>=0
    return w*(d-1)-l
def kelly(w,t,l,d):
    if w+l==0: return None
    return max(F(0),min(F(1),(w*(d-1)-l)/((d-1)*(w+l))))
def settle(x,line,side='over',inclusive=False,eligible=True):
    if not eligible:return 'VOID'
    if inclusive:return 'WIN' if x>=line else 'LOSS'
    if x==line:return 'PUSH'
    return 'WIN' if ((x>line)==(side=='over')) else 'LOSS'
d=F(21,11);w,t,l=F(46,100),F(16,100),F(38,100);q=w/(w+l)
e=roi(w,t,l,d)
check('mass sums one',w+t+l==1)
check('EV equivalent forms',e==w*d+t-1==(1-t)*(q*d-1))
check('unconditional binary error exactly push mass',e-(w*d-1)==t)
check('conditional ROI requires action-frequency factor',q*d-1==e/(1-t))
check('fair price zeros EV',roi(w,t,l,(1-t)/w)==0)
check('conditional edge matches unconditional equivalent',q-F(1,d)==(w-(1-t)/d)/(1-t))
f=kelly(w,t,l,d)
check('Kelly reference exact',f==F(1,20))
check('Kelly first derivative zero',w*(d-1)/(1+f*(d-1))-l/(1-f)==0)
g=lambda z:float(w)*math.log1p(float(z*(d-1)))+float(l)*math.log1p(-float(z))
check('Kelly locally maximizes expected log',g(f)>g(f-F(1,10000)) and g(f)>g(f+F(1,10000)))
check('Kelly unchanged conditional no-push',f==kelly(q,F(0),1-q,d))
check('all push has no identified Kelly fraction',kelly(F(0),F(1),F(0),d) is None)
check('negative EV clipped to no bet',kelly(F(2,5),F(0),F(3,5),d)==0)
check('no-push reduction',roi(F(3,5),F(0),F(2,5),d)==F(3,5)*d-1)
check('receptions 5 on over5 pushes',settle(5,5)=='PUSH')
check('receptions 5 on over4.5 wins',settle(5,F(9,2))=='WIN')
check('receptions 5 on over5.5 loses',settle(5,F(11,2))=='LOSS')
check('inclusive5+ differs from over5',settle(5,5,inclusive=True)=='WIN')
check('half-unit sack support can push',settle(F(3,2),F(3,2))=='PUSH')
check('void distinct from threshold push',settle(5,5,eligible=False)=='VOID')
check('under reverses win loss, not push',settle(4,5,'under')=='WIN' and settle(5,5,'under')=='PUSH')
lo=roi(w+t,F(0),l,d);hi=roi(w,F(0),l+t,d)
check('lower half line vs integer difference',lo-e==t*(d-1))
check('integer vs higher half difference',e-hi==t)
check('two half lines difference',lo-hi==t*d)
# Identical conditional fair q, different push masses -> different ROI magnitudes.
w2,l2,t2=q*F(1,2),(1-q)*F(1,2),F(1,2)
check('same fair odds cannot identify push mass',(1-t2)/w2==(1-t)/w)
check('same q does not identify per-staked ROI',roi(w2,t2,l2,d)!=e)
# Brier targets and scaling.
p=[w,l,t];obs=[0,0,1];brier=sum((a-b)**2 for a,b in zip(p,obs))
check('multiclass push score',brier==F(1327,1250))
check('binary two-class sum is double conventional',sum((a-b)**2 for a,b in zip([q,1-q],[1,0]))==2*(q-1)**2)
# Synthetic early-win over yardage / final under can both win.
path=[40,51,49];threshold=F(101,2)
check('early over and final under not complements',max(path)>threshold and path[-1]<threshold)
# Coherent scenario pairs: minimum unconditional win is not worst ROI.
sa=(F(1,2),F(1,10),F(2,5));sb=(F(51,100),F(5,100),F(44,100));ds=F(185,100)
check('conservative scenario reversal',sa[0]<sb[0] and roi(*sa,ds)>roi(*sb,ds))
result={'classification':'synthetic arithmetic checks; no empirical NFL validation','passed':len(checks),'checks':checks,'receptions_fixture':{'decimal_odds':float(d),'p_win':float(w),'p_push':float(t),'p_loss':float(l),'q_win_nonpush':float(q),'roi':float(e),'incorrect_binary_roi':float(w*d-1),'conditional_roi':float(q*d-1),'fair_decimal':float((1-t)/w),'fair_american':float(-100/((1-t)/w-1)),'full_kelly_reference':float(f),'over4_5_roi':float(lo),'over5_5_roi':float(hi),'multiclass_brier_for_push':float(brier)}}
Path(__file__).with_name('test-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
