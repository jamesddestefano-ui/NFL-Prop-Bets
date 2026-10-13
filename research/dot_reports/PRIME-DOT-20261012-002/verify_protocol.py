"""Synthetic deterministic research tests, not a betting engine or backtest."""
import math,json
checks=[]
def check(name, condition):
 assert condition,name
 checks.append(name)
def devig(q, method):
 if len(q)!=2 or any(not 0<x<1 for x in q):raise ValueError('invalid binary prices')
 s=sum(q)
 if s<1-1e-12: raise ValueError('underround flagged outside primary panel')
 if method=='proportional':return [x/s for x in q]
 if method=='additive':return [x-(s-1)/2 for x in q]
 lo,hi=0.,1.
 while sum(x**hi for x in q)>1:
  hi*=2
 for _ in range(200):
  k=(lo+hi)/2
  if sum(x**k for x in q)>1:lo=k
  else:hi=k
 return [x**((lo+hi)/2) for x in q]
for q in [[.5,.5],[.55,.55],[.75,.30],[.99,.02],[.999,.999]]:
 for m in ['proportional','additive','power']:
  p=devig(q,m)
  check(f'{q}:{m}:normalization',abs(sum(p)-1)<1e-12)
  check(f'{q}:{m}:range',all(0<=x<=1 for x in p))
  check(f'{q}:{m}:label_symmetry',abs(p[0]-devig(q[::-1],m)[1])<1e-12)
check('equal_odds_all_half',all(abs(devig([.55,.55],m)[0]-.5)<1e-12 for m in ['proportional','additive','power']))
q=[111/211,120/220]
check('archived_Kincaid_correction',abs(devig(q,'proportional')[0]*100-49.09529553679132)<1e-6)
q=[.75,.30];d=1.4;raw=.79;w=.5;delta=.02
values={}
for m in ['proportional','additive','power']:
 market=devig(q,m)[0];central=w*raw+(1-w)*market;conservative=central-delta
 values[m]={'market':market,'central':central,'conservative':conservative,'edge':central-1/d,'expected_roi':central*d-1,'conservative_ev':conservative*d-1}
 values[m]['numeric_gate']=values[m]['edge']>=.04 and values[m]['expected_roi']>=.05 and values[m]['conservative_ev']>0
check('method_can_flip_numeric_gate',not values['proportional']['numeric_gate'] and values['power']['numeric_gate'])
check('independent_probability_EV_invariant',all(abs((raw*d-1)-.106)<1e-12 for _ in values))
# Contract/source gates fail closed. Synthetic UTC epoch-seconds.
def eligible(a,b,t):
 keys=['game','player','stat','line','period','book','rules_version','settlement_basis']
 return all(a.get(k) is not None and a.get(k)==b.get(k) for k in keys) and a.get('side')=='OVER' and b.get('side')=='UNDER' and all(x.get('quote_time') is not None and 0<=t-x['quote_time']<=60 and x.get('status')=='OPEN' for x in [a,b]) and abs(a['quote_time']-b['quote_time'])<=30
base=dict(game='G',player='P',stat='RECEPTIONS',line=4.5,period='FULL_OT',book='B',rules_version='v1',settlement_basis='ACTION',quote_time=100,status='OPEN')
a={**base,'side':'OVER'};b={**base,'side':'UNDER'}
check('matched_pair_eligible',eligible(a,b,120))
for field,value in [('line',5.5),('book','C'),('rules_version','v2'),('period','REGULATION'),('settlement_basis','OTHER'),('quote_time',None),('quote_time',0),('quote_time',125),('status','SUSPENDED')]:
 check('reject_'+field+'_'+str(value),not eligible(a,{**b,field:value},120))
check('one_sided_rejected',not eligible(a,{},120))
def post_news_pair(a,b,news_time):
 return a['quote_time']>=news_time and b['quote_time']>=news_time
check('news_between_quotes_needs_new_capture',not post_news_pair(a,{**b,'quote_time':115},110))
check('both_quotes_after_news',post_news_pair({**a,'quote_time':111},{**b,'quote_time':115},110))
print(json.dumps({'tests_passed':len(checks),'test_names':checks,'hypothetical_example':values,'Kincaid_proportional_over_pct':devig([111/211,120/220],'proportional')[0]*100,'scope':'synthetic arithmetic and contract-gate fixtures; not production or empirical NFL validation'},indent=2))
