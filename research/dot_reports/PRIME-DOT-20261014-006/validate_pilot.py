"""Research-only synthetic contract/quote admission checks; no collector or wager code."""
from datetime import datetime
from math import isfinite

def time(s):
    if not isinstance(s,str): raise ValueError('timestamp missing')
    t=datetime.fromisoformat(s.replace('Z','+00:00'))
    if t.tzinfo is None: raise ValueError('timezone missing')
    return t

def admitted(q, decision_at, ttl_seconds=120):
    try:
        if q.get('evidence_kind') not in ('DIRECT_PUBLIC','FRESH_NAMED_BOARD'): return False
        for k in ('game','player','stat','side','period','book','jurisdiction','rules_hash','source_url','capture_hash'):
            if not q.get(k): return False
        if q['side'] not in ('OVER','UNDER'): return False
        if q.get('status')!='ACTIVE' or q.get('fill_status')!='NO_CONFIRMED_FILL': return False
        if not isinstance(q.get('threshold'),(int,float)) or isinstance(q['threshold'],bool) or not isfinite(q['threshold']): return False
        if q['threshold'] % 1 != .5: return False
        d=q.get('decimal_odds')
        if isinstance(d,bool) or not isinstance(d,(int,float)) or not isfinite(d) or d<=1: return False
        source,observed,recorded,decision,kickoff=map(time,[q.get('source_updated_at'),q.get('observed_at'),q.get('recorded_at'),decision_at,q.get('kickoff_at')])
        return source<=observed<=recorded<=decision<kickoff and 0<ttl_seconds and (decision-source).total_seconds()<=ttl_seconds
    except (ValueError,TypeError,KeyError): return False

def complementary(a,b,decision):
    keys=('game','player','stat','period','book','jurisdiction','rules_hash','threshold','source_updated_at','observed_at','capture_hash')
    return admitted(a,decision) and admitted(b,decision) and {a['side'],b['side']}=={'OVER','UNDER'} and all(a[k]==b[k] for k in keys) and a.get('complementary_standard_rules') is True and b.get('complementary_standard_rules') is True

def prior_close(rows, decision, kickoff):
    # Caller supplies the exact same contract and predeclared reference book panel.
    valid=[q for q in rows if admitted(q,q['recorded_at']) and time(q['recorded_at'])<time(kickoff) and time(q['observed_at'])>=time(decision)]
    return max(valid,key=lambda q:time(q['observed_at'])) if valid else None

def ev(pw,pl,d):
    if not all(isfinite(v) for v in (pw,pl,d)) or min(pw,pl)<0 or pw+pl>1 or d<=1: raise ValueError('invalid probabilities/price')
    return pw*(d-1)-pl

if __name__=='__main__':
    from copy import deepcopy
    import json
    q=dict(game='SYNTHETIC_NFL_GAME',player='SYNTHETIC_PLAYER',stat='RECEPTIONS',side='OVER',period='FULL_GAME_OT_INCLUDED',book='SYNTHETIC_BOOK',jurisdiction='SYNTHETIC_JURISDICTION',rules_hash='synthetic_standard_rules',source_url='https://example.org/synthetic-only',capture_hash='synthetic_capture',status='ACTIVE',fill_status='NO_CONFIRMED_FILL',threshold=4.5,decimal_odds=2.,source_updated_at='2026-10-18T13:59:00Z',observed_at='2026-10-18T13:59:30Z',recorded_at='2026-10-18T13:59:40Z',kickoff_at='2026-10-18T17:00:00Z',evidence_kind='DIRECT_PUBLIC',complementary_standard_rules=True)
    decision='2026-10-18T14:00:00Z'; n=0
    def check(x):
        global n
        assert x
        n+=1
    check(admitted(q,decision))
    for key,value in [('source_updated_at',None),('source_updated_at','2026-10-18T14:01:00Z'),('source_updated_at','2026-10-18T13:57:59Z'),('observed_at','2026-10-18T14:01:00Z'),('recorded_at','2026-10-18T14:01:00Z'),('kickoff_at','2026-10-18T13:30:00Z'),('kickoff_at',decision),('jurisdiction',None),('rules_hash',None),('status','SUSPENDED'),('status','UNKNOWN'),('decimal_odds',float('nan')),('decimal_odds',1),('threshold',float('inf')),('threshold',4),('threshold',4.25),('evidence_kind','DOCUMENTATION_EXAMPLE'),('evidence_kind','SEARCH_SNIPPET'),('fill_status','CONFIRMED_FILL')]:
        z=deepcopy(q);z[key]=value;check(not admitted(z,decision))
    u=deepcopy(q);u['side']='UNDER';check(complementary(q,u,decision))
    for key,value in [('threshold',5.5),('book','OTHER'),('rules_hash','EARLY_WIN_RULE'),('source_updated_at','2026-10-18T13:59:01Z'),('capture_hash','OTHER'),('side','OVER'),('complementary_standard_rules',False)]:
        z=deepcopy(u);z[key]=value;check(not complementary(q,z,decision))
    check(abs(ev(.55,.45,2)-.10)<1e-12)
    check(abs(ev(.50,.50,2))<1e-12)
    check(abs(ev(.50,.40,2)-.10)<1e-12)
    check(prior_close([q],decision,q['kickoff_at']) is None)
    z=deepcopy(q);z.update(source_updated_at='2026-10-18T16:58:00Z',observed_at='2026-10-18T16:58:30Z',recorded_at='2026-10-18T16:58:40Z');check(prior_close([z],decision,q['kickoff_at'])==z)
    # Same quote with a later actual kickoff argument cannot override its own pregame identity.
    z['recorded_at']='2026-10-18T17:00:00Z';check(prior_close([z],decision,q['kickoff_at']) is None)
    check(abs(ev(.54,.46,2)-.08)<1e-12)
    check(abs((1/.54)-1.8518518518518516)<1e-12)
    check(abs((.5*.5+.5*.6)-.55)<1e-12)
    check(abs(((.5*.5+.5*.6)-.5)-((1-.5)*(.6-.5)))<1e-12)
    print(json.dumps({'synthetic_assertions_passed':n,'empirical_quotes':0,'scope':'Research fixture checks only; not full schema or collector validation'},indent=2))
