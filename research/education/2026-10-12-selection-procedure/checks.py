"""Synthetic arithmetic only. No NFL observations, fitted model, quotes or wagers."""
import math,json
from pathlib import Path
checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
p=[math.comb(100,k)*0.5**100 for k in range(101)]
check('binomial_mass',abs(sum(p)-1)<1e-12)
one=sum(p[60:]); family=1-(1-one)**100
expected_max=sum(1-sum(p[:k])**100 for k in range(1,101))
check('one_tail',abs(one-0.02844396682049)<1e-12)
check('family',abs(family-0.94418058245582)<1e-12)
check('max_in_range',60<expected_max<65)
check('one_search_mean',abs(sum(1-sum(p[:k]) for k in range(1,101))-50)<1e-10)
d=21/11; central=.57;conservative=.54
check('true_null_roi',abs(.5*d-1+1/22)<1e-12)
check('60win_roi',abs(.6*d-1-.1454545454545455)<1e-12)
check('symmetrical_devig',abs((1/d)/(2/d)-.5)<1e-12)
check('central_ev',abs(central*d-1-.08818181818181814)<1e-12)
check('conservative_ev',abs(conservative*d-1-.03090909090909)<1e-12)
check('sensitivity_fails',.52*d-1<0)
D=max(1.05/central,1/(central-.04),1/conservative)
maxjuice=100/(D-1)
def gates(a):
 odds=1+100/a
 return central-1/odds>=.04 and central*odds-1>=.05 and conservative*odds-1>0
check('max_juice',abs(maxjuice-112.76595744680849)<1e-9)
check('minus112_passes_numeric',gates(112))
check('minus113_fails_numeric',not gates(113))
check('next_threshold_fails',.49*d-1<0)
check('duplicate_variance_factor',math.isclose((.25/20)/(.25/100),5))
# Chronological fixtures: a label can enter training only after it is settled/available.
rows=[{'game':'A','kickoff':10,'label_available':14},{'game':'B','kickoff':11,'label_available':15},{'game':'C','kickoff':20,'label_available':24}]
train=[r for r in rows if r['label_available']<20]
check('eligible_labels_only',len(train)==2 and all(r['label_available']<20 for r in train))
check('no_same_game_split',set(r['game'] for r in train).isdisjoint({'C'}))
result={'status':'passed','checks':checks,'count':len(checks),'one_trial_tail':one,'independent_100_trial_tail':family,'expected_max_wins':expected_max,'selected_apparent_roi':expected_max/100*d-1,'true_future_roi':.5*d-1,'central_ev':central*d-1,'conservative_ev':conservative*d-1,'max_negative_juice_magnitude':maxjuice,'limitations':'Deterministic synthetic identities and tiny illustrative eligibility fixtures only; not empirical NFL or production validation.'}
Path(__file__).with_name('check-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
