"""Deterministic invented fixtures, not empirical NFL/source evidence."""
import json, math
r={}
p=.55; pc=.52; d=1+100/110; d2=2.0
r['shop_ev_minus110']=p*d-1; r['shop_ev_even']=p*d2-1
assert math.isclose(r['shop_ev_minus110'],.05)
assert math.isclose(r['shop_ev_even'],.10)
r['conservative_minus110']=pc*d-1; assert r['conservative_minus110']<0
r['conservative_even']=pc*d2-1; assert math.isclose(r['conservative_even'],.04)
r['raw_close_minus130']=130/230
r['paired_no_vig_close']=r['raw_close_minus130']/(r['raw_close_minus130']+100/210)
r['close_referenced_roi']=r['paired_no_vig_close']*d-1
assert r['raw_close_minus130']>r['paired_no_vig_close']
# same contract, early tip 12:00; unchanged quote 11:59, changed 12:03
r['lead_interval_minutes']=[-1,3]; assert r['lead_interval_minutes'][0]<0 # not proved before move
# capture and verification denominators, not zero-fill inaccessible sources
r['verification_rate']=8/20;r['matched_clv_coverage']=5/20;r['positive_clv_rate_matched']=4/5
assert r['positive_clv_rate_matched'] != 4/20
r['raw_posts']=10;r['upstream_clusters']=1; assert r['raw_posts']!=r['upstream_clusters']
# settled win/loss conditional probability does not use unconditional p when pushes removed
r['conditional_win']=.5/(1-.1); assert r['conditional_win']!=.5
print(json.dumps({'fixture_type':'invented educational inputs','assertions_passed':9,'results':r},indent=2))
