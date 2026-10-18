"""Deterministic educational proper-score/abstention fixture. No external I/O.

This is deliberately separate from production code and observed sports data.
The fixed contract is constructed before the synthetic outcomes are attached.
"""
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

BASIS = 'binary_affirmative_no_push'


def probability(value):
    if isinstance(value, bool) or not isinstance(value, (int, float, Fraction)):
        raise TypeError('A probability must be a number; null and ABSTAIN are not probabilities')
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('A probability must be finite')
    p = value if isinstance(value, Fraction) else Fraction(str(value))
    if not 0 <= p <= 1:
        raise ValueError('A probability must lie in [0,1]')
    return p


def binary_outcome(value):
    if type(value) is not int or value not in (0, 1):
        raise ValueError('A scored outcome must be observed binary 0 or 1; no nulls or pushes')
    return value


def brier(p, y):
    return (probability(p) - binary_outcome(y)) ** 2


def log_loss(p, y):
    p, y = probability(p), binary_outcome(y)
    chance = p if y else 1-p
    return math.inf if chance == 0 else -math.log(float(chance))


def _epsilon(value):
    eps = probability(value)
    if not 0 < eps < Fraction(1, 2):
        raise ValueError('Declare 0 < epsilon < 1/2 before observing outcomes')
    return eps


def predeclared_clip(p, epsilon):
    """A different forecast, only valid if this transformation was fixed ex ante."""
    p, eps = probability(p), _epsilon(epsilon)
    return max(eps, min(1-eps, p))


def observation_ids(ids):
    """Synthetic mask depends only on stable numeric IDs, never on outcomes."""
    return [event_id for event_id in ids if int(event_id.rsplit('_', 1)[1]) % 10 != 0]


def build_fixture():
    rows = []
    # Fix eligibility, probabilities, abstention, weights, and observation mask
    # before attaching any synthetic outcome.
    for stratum, count in [('easy', 10), ('hard', 40)]:
        for index in range(1, count+1):
            rows.append({
                'event_id': f'{stratum}_{index:03d}',
                'event_side': 'affirmative', 'stratum': stratum,
                'probability_basis': BASIS,
                'market_p': .9 if stratum == 'easy' else .5,
                'model_status': 'PREDICT' if stratum == 'easy' else 'ABSTAIN',
                'model_p': .7 if stratum == 'easy' else None,
            })
    observed = set(observation_ids([r['event_id'] for r in rows]))
    for row in rows:
        row['masked_demo_observed'] = row['event_id'] in observed
    # These are invented labels, not sampled or externally collected outcomes.
    for row in rows:
        index = int(row['event_id'].rsplit('_', 1)[1])
        row['outcome'] = int(index <= (9 if row['stratum'] == 'easy' else 20))
    return rows


def policy_forecasts(rows):
    if not rows:
        raise ValueError('The frozen cohort must be nonempty')
    ids, covered, market, model, fallback, mixture, mixed_fallback, outcomes = [], [], {}, {}, {}, {}, {}, {}
    for row in rows:
        event_id = row['event_id']
        if event_id in market:
            raise ValueError('Duplicate underlying event, including complementary-side duplicate')
        if row['event_side'] != 'affirmative' or row['probability_basis'] != BASIS:
            raise ValueError('All forecasts and labels must share the canonical binary affirmative no-push basis')
        status = row['model_status']
        if status == 'MISSING':
            raise ValueError('Unplanned operational missingness is not chosen abstention; contract needs explicit handling')
        if status not in ('PREDICT', 'ABSTAIN'):
            raise ValueError('Unknown prediction status')
        p = probability(row['market_p'])
        ids.append(event_id)
        market[event_id] = p
        outcomes[event_id] = binary_outcome(row['outcome'])
        if status == 'PREDICT':
            m = probability(row['model_p'])
            covered.append(event_id)
            model[event_id] = fallback[event_id] = m
            mixture[event_id] = mixed_fallback[event_id] = Fraction(1,4)*m+Fraction(3,4)*p
        else:
            if row['model_p'] is not None:
                raise ValueError('ABSTAIN has no model probability; do not replace null with zero')
            fallback[event_id] = mixed_fallback[event_id] = p
    return {'cohort_ids': ids, 'covered_ids': covered, 'market': market, 'model': model,
            'fallback': fallback, 'mixture': mixture, 'mixture_fallback': mixed_fallback,
            'outcomes': outcomes}


def paired_scores(left, right, outcomes, cohort_ids, score='brier'):
    ids = list(cohort_ids)
    if not ids or len(set(ids)) != len(ids):
        raise ValueError('One explicit nonempty, duplicate-free paired cohort is required')
    if any(i not in left or i not in right or i not in outcomes or outcomes[i] is None for i in ids):
        raise ValueError('Both forecasts and observed outcomes must exist for every fixed paired cohort ID')
    if score not in ('brier','log_loss'):
        raise ValueError('Unknown proper score')
    fn = brier if score == 'brier' else log_loss
    left_losses = [fn(left[i],outcomes[i]) for i in ids]
    right_losses = [fn(right[i],outcomes[i]) for i in ids]
    if score == 'brier':
        a,b = sum(left_losses,Fraction(0))/len(ids),sum(right_losses,Fraction(0))/len(ids)
    else:
        a,b = math.fsum(left_losses)/len(ids), math.fsum(right_losses)/len(ids)
        if math.isinf(a) and math.isinf(b):
            raise ValueError('Paired log-loss difference is undefined: both aggregate losses are infinite; no retroactive clipping')
    return {'n':len(ids),'left':a,'right':b,'left_minus_right':a-b}


def _missing_inputs(predictions,outcomes):
    predictions,outcomes = list(predictions),list(outcomes)
    if not predictions or len(predictions) != len(outcomes):
        raise ValueError('Use the full fixed target cohort, with one known forecast per outcome slot')
    ps = [probability(p) for p in predictions]
    ys = [None if y is None else binary_outcome(y) for y in outcomes]
    return ps,ys


def missing_brier_bounds(predictions,outcomes):
    ps,ys = _missing_inputs(predictions,outcomes)
    lows,highs = [],[]
    for p,y in zip(ps,ys):
        possibilities = [brier(p,0),brier(p,1)] if y is None else [brier(p,y)]
        lows.append(min(possibilities)); highs.append(max(possibilities))
    return sum(lows,Fraction(0))/len(ps),sum(highs,Fraction(0))/len(ps)


def missing_paired_brier_bounds(left,right,outcomes):
    ps,ys = _missing_inputs(left,outcomes)
    qs,ys2 = _missing_inputs(right,ys)
    lows,highs = [],[]
    for p,q,y in zip(ps,qs,ys2):
        possibilities = [brier(p,z)-brier(q,z) for z in ([0,1] if y is None else [y])]
        lows.append(min(possibilities));highs.append(max(possibilities))
    return sum(lows,Fraction(0))/len(ps),sum(highs,Fraction(0))/len(ps)


def missing_log_loss_bounds(predictions,outcomes,*,epsilon):
    """Finite uniform-envelope contract. Validate, never silently clip forecasts."""
    ps,ys = _missing_inputs(predictions,outcomes)
    eps = _epsilon(epsilon)
    if any(not eps <= p <= 1-eps for p in ps):
        raise ValueError('Forecast violates declared epsilon envelope; retroactive clipping is forbidden')
    lows,highs = [],[]
    for p,y in zip(ps,ys):
        possibilities = [log_loss(p,0),log_loss(p,1)] if y is None else [log_loss(p,y)]
        lows.append(min(possibilities));highs.append(max(possibilities))
    return math.fsum(lows)/len(ps),math.fsum(highs)/len(ps)


def _exact(value):
    return {'exact':str(value),'decimal':float(value)}


def routing_counterexample():
    """Optional 30 invented rows: equal source coverage, unequal routing value."""
    specs = [('easy',9,.9,.85,None),('common',7,.65,.68,.66),('hard',5,.65,None,.5)]
    ids,ys,market,a,b,pa,pb,common = [],{},{},{},{},{},{},[]
    route_ids = {'both':[],'a_only':[],'b_only':[],'neither':[]}
    for kind,positives,m,ap,bp in specs:
        for index in range(1,11):
            event_id = f'{kind}_{index:03d}'
            ids.append(event_id)
            market[event_id] = probability(m)
            if ap is not None:
                a[event_id] = probability(ap)
            if bp is not None:
                b[event_id] = probability(bp)
            pa[event_id] = a.get(event_id,market[event_id])
            pb[event_id] = b.get(event_id,market[event_id])
            route = 'both' if ap is not None and bp is not None else 'a_only' if ap is not None else 'b_only' if bp is not None else 'neither'
            route_ids[route].append(event_id)
            if route == 'both':
                common.append(event_id)
    # Frozen forecasts/routing exist before the deterministic labels are attached.
    for kind,positives,m,ap,bp in specs:
        for index in range(1,11):
            ys[f'{kind}_{index:03d}'] = int(index <= positives)
    output = {'cohort_n':len(ids),'a_covered_n':len(a),'b_covered_n':len(b),
              'common_n':len(common),'evidence_type':'invented_deterministic_educational_fixture',
              'specification':[{'stratum':kind,'n':10,'positive_labels':positives,
                                'market_p':m,'a_p_or_abstain_null':ap,'b_p_or_abstain_null':bp}
                               for kind,positives,m,ap,bp in specs]}
    for score in ['brier','log_loss']:
        own_a = paired_scores(a,a,ys,list(a),score)['left']
        own_b = paired_scores(b,b,ys,list(b),score)['left']
        both = paired_scores(a,b,ys,common,score)
        policies = paired_scores(pa,pb,ys,ids,score)
        vals = {'a_own_covered':own_a,'b_own_covered':own_b,
                'a_common':both['left'],'b_common':both['right'],
                'market_all':paired_scores(market,market,ys,ids,score)['left'],
                'a_policy_all':policies['left'],'b_policy_all':policies['right'],
                'a_policy_minus_b_policy':policies['left_minus_right']}
        output['brier' if score=='brier' else 'log_loss_nats'] = {k:_exact(v) for k,v in vals.items()} if score=='brier' else vals
    output['brier_difference_total_by_route_exact'] = {
        route:str(sum((brier(pa[i],ys[i])-brier(pb[i],ys[i]) for i in group),Fraction(0)))
        for route,group in route_ids.items()}
    return output


def calculate_results():
    rows = build_fixture()
    f = policy_forecasts(rows)
    all_ids,covered,ys = f['cohort_ids'],f['covered_ids'],f['outcomes']
    reports = {}
    for score in ['brier','log_loss']:
        covered_pair = paired_scores(f['model'],f['market'],ys,covered,score)
        fallback_pair = paired_scores(f['fallback'],f['market'],ys,all_ids,score)
        mix_pair = paired_scores(f['mixture_fallback'],f['market'],ys,all_ids,score)
        mix_covered = paired_scores(f['mixture'],f['market'],ys,covered,score)
        vals = {'model_covered':covered_pair['left'],'market_covered':covered_pair['right'],
                'market_all':fallback_pair['right'],'fallback_all':fallback_pair['left'],
                'mixture_covered':mix_covered['left'],'mixture_fallback_all':mix_pair['left'],
                'fallback_minus_market_all':fallback_pair['left_minus_right'],
                'mixture_fallback_minus_market_all':mix_pair['left_minus_right'],
                'model_minus_market_covered':covered_pair['left_minus_right']}
        reports['brier' if score=='brier' else 'log_loss_nats'] = {k:_exact(v) for k,v in vals.items()} if score=='brier' else vals
    hidden_ys = [r['outcome'] if r['masked_demo_observed'] else None for r in rows]
    market_ps = [f['market'][i] for i in all_ids]
    fallback_ps = [f['fallback'][i] for i in all_ids]
    observed = [r['event_id'] for r in rows if r['masked_demo_observed']]
    observed_pair = paired_scores(f['fallback'],f['market'],ys,observed)
    reports.update({
        'evidence_type':'invented_deterministic_educational_fixture',
        'empirical_validation':False,'statistical_significance_estimated':False,
        'cohort_n':50,'covered_n':10,'coverage':.2,
        'score_orientation':'Lower is better; all deltas are policy minus market',
        'probability_basis':BASIS,'weighting':'One equal-weight observation per underlying binary event',
        'mixture_weight_model':.25,'mixture_weight_market':.75,
        'epsilon_envelope_for_masked_log_bounds':.01,
        'epsilon_changes_primary_forecasts':False,
        'masked_demo':{
            'mask_rule':'Before labels: event ID suffix not divisible by 10 is observed',
            'target_n':50,'observed_n':45,'missing_n':5,
            'observed_only_market_brier':_exact(observed_pair['right']),
            'observed_only_fallback_brier':_exact(observed_pair['left']),
            'market_brier_bounds_exact':[str(x) for x in missing_brier_bounds(market_ps,hidden_ys)],
            'fallback_brier_bounds_exact':[str(x) for x in missing_brier_bounds(fallback_ps,hidden_ys)],
            'paired_delta_bounds_exact':[str(x) for x in missing_paired_brier_bounds(fallback_ps,market_ps,hidden_ys)],
            'market_log_loss_bounds_nats':missing_log_loss_bounds(market_ps,hidden_ys,epsilon=.01),
            'fallback_log_loss_bounds_nats':missing_log_loss_bounds(fallback_ps,hidden_ys,epsilon=.01),
        },
    })
    reports['optional_equal_coverage_routing'] = routing_counterexample()
    return reports


def canonical_bytes(value):
    return (json.dumps(value,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode('utf-8')


def main():
    destination = Path(__file__).resolve().parent
    fixture,results = build_fixture(),calculate_results()
    (destination/'fixture.json').write_bytes(canonical_bytes(fixture))
    (destination/'results.json').write_bytes(canonical_bytes(results))
    print(json.dumps({'fixture_sha256':hashlib.sha256(canonical_bytes(fixture)).hexdigest(),
                      'results_sha256':hashlib.sha256(canonical_bytes(results)).hexdigest(),
                      'cohort_n':len(fixture),'empirical_validation':False},sort_keys=True))


if __name__ == '__main__':
    main()
