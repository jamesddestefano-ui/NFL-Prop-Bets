"""Public EDUCATIONAL toy; invented inputs, exact fractions, no external services.

This checks the internal consistency of supplied records. It cannot establish that
records really existed before an event or detect a forged historical timestamp.
It intentionally supports one canonical half-line contract per game, not a
production scorer. M=market, G=ChatGPT, C=Claude, S=3/4 M + 1/4 G.
"""
from collections import defaultdict
from datetime import datetime
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import math

ARMS = ('M', 'G', 'C')
CONTRACT_FIELDS = {'event_id', 'subject_id', 'market', 'threshold', 'orientation',
                   'period', 'book_rule', 'probability_target'}

def probability(value):
    if isinstance(value, (bool, float)):
        raise ValueError('Use exact integer, fraction, or fraction-string probabilities')
    q = F(value)
    if not 0 <= q <= 1:
        raise ValueError('Probability outside [0,1]')
    return q

def mean(values):
    values = list(values)
    if not values:
        raise ValueError('Empty mean')
    return sum(values, F(0)) / len(values)

def checked_pairs(probabilities, outcomes):
    ps, ys = list(probabilities), list(outcomes)
    if not ps or len(ps) != len(ys):
        raise ValueError('Nonempty equal-length inputs required')
    if any(y not in (0, 1) for y in ys):
        raise ValueError('Binary outcomes required')
    return [probability(p) for p in ps], ys

def brier(probabilities, outcomes):
    ps, ys = checked_pairs(probabilities, outcomes)
    return mean((p-y)**2 for p, y in zip(ps, ys))

def blend(market, anchor, weight):
    w = probability(weight)
    if not market or len(market) != len(anchor):
        raise ValueError('Nonempty equal-length inputs required')
    return [(1-w)*probability(m)+w*probability(a) for m, a in zip(market, anchor)]

def brier_expansion(market, anchor, outcomes, weight):
    m, y = checked_pairs(market, outcomes)
    a, _ = checked_pairs(anchor, outcomes)
    w = probability(weight)
    cross = mean((aa-mm)*(mm-yy) for mm, aa, yy in zip(m, a, y))
    movement = mean((aa-mm)**2 for mm, aa in zip(m, a))
    return {'cross': cross, 'movement': movement,
            'difference': 2*w*cross + w*w*movement}

def oracle_weight(market, anchor, outcomes):
    """Ex-post constrained oracle diagnostic; NEVER used to choose study S."""
    parts = brier_expansion(market, anchor, outcomes, F(0))
    if parts['movement'] == 0:
        return None  # All weights produce identical forecasts.
    return min(F(1), max(F(0), -parts['cross']/parts['movement']))

def log_loss(p, y):
    """Natural logarithm; no silently imposed endpoint clipping."""
    p = probability(p)
    if y not in (0, 1):
        raise ValueError('Binary outcome required')
    actual = p if y == 1 else 1-p
    if actual == 0:
        return math.inf
    if actual == 1:
        return 0.0
    if actual > F(1, 2):
        return -math.log1p(-float(1-actual))  # Avoid cancellation near certainty.
    # Difference of integer logs avoids converting a tiny fraction to zero.
    return math.log(actual.denominator)-math.log(actual.numerator)

def log_loss_difference(arm_loss, market_loss):
    if math.isinf(arm_loss) and math.isinf(market_loss):
        raise ValueError('infinity minus infinity is undefined')
    return arm_loss-market_loss

def full_wlp(conditional_win, push_mass):
    q, p = probability(conditional_win), probability(push_mass)
    if p == 1:
        raise ValueError('Conditional win undefined when all outcomes push')
    return ((1-p)*q, (1-p)*(1-q), p)

def roi(wlp, decimal_odds):
    """Expected net return per original unit stake; push has zero return."""
    w, l, p = map(probability, wlp)
    d = F(decimal_odds)
    if w+l+p != 1 or d <= 1:
        raise ValueError('Valid W/L/P distribution and decimal odds >1 required')
    return w*(d-1)-l

def equal_game_mean(game_deltas):
    groups = defaultdict(list)
    for game, delta in game_deltas:
        groups[game].append(F(delta))
    return mean(mean(ds) for ds in groups.values())

def cluster_resample_means(game_means):
    """Enumerate tiny ordered whole-game bootstrap samples, not a valid CI claim."""
    if not 1 <= len(game_means) <= 5:
        raise ValueError('This instructional enumeration supports 1 to 5 games')
    return [mean(draw) for draw in product(game_means, repeat=len(game_means))]

def input_hash(packet):
    encoded = json.dumps(packet, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(encoded).hexdigest()

def timestamp(raw):
    t = datetime.fromisoformat(raw.replace('Z', '+00:00'))
    if t.tzinfo is None:
        raise ValueError('Timezone-aware timestamp required')
    return t

def validate_fixture(fixture):
    """Check a SMALL stated protocol and common complete-case cohort.

    A real frozen record requires externally auditable storage/provenance. A
    regenerated hash or edited timestamp cannot establish historical existence.
    Missing/ABSTAIN are pre-event exclusions, never numeric probabilities.
    """
    if fixture['fixture_kind'] != 'invented_educational':
        raise ValueError('Only the invented educational fixture is supported')
    protocol = fixture['protocol']
    lock = timestamp(protocol['prediction_lock'])
    protocol_lock = timestamp(protocol['locked_at'])
    cohort_lock = timestamp(protocol['common_cohort_locked_at'])
    if not protocol_lock <= cohort_lock <= lock:
        raise ValueError('Require protocol <= cohort <= prediction lock')
    if protocol['anchor'] != 'G' or F(protocol['shrinkage_weight']) != F(1, 4):
        raise ValueError('Require prospective G anchor and fixed 1/4 weight')
    if protocol['primary_weighting'] != 'equal_game_then_unique_canonical_over_contract':
        raise ValueError('Wrong predeclared weighting')
    rows = fixture['rows']
    ids = [row['id'] for row in rows]
    if len(set(ids)) != len(ids) or ids != protocol['declared_universe']:
        raise ValueError('Rows must match unique declared universe')
    expected_prompt_hash = input_hash(fixture['shared_model_prompt'])
    eligible, excluded, seen_games = [], {}, set()
    for row in rows:
        contract = row['contract']
        if not CONTRACT_FIELDS.issubset(contract) or any(not contract[k] for k in CONTRACT_FIELDS):
            raise ValueError('Missing required contract fields')
        if contract['probability_target'] != 'win_given_win_or_loss':
            raise ValueError('Wrong probability target for this binary fixture')
        if contract['orientation'] != 'OVER' or F(contract['threshold']).denominator != 2:
            raise ValueError('Only canonical OVER half-lines supported')
        if contract['event_id'] in seen_games:
            raise ValueError('Toy supports only one canonical contract per game')
        seen_games.add(contract['event_id'])
        event_start = timestamp(row['event_start'])
        if not lock < event_start:
            raise ValueError('Require prediction lock < event start')
        settlement = row['settlement']
        if settlement['contract'] != contract:
            raise ValueError('Wrong settlement contract identity')
        if not event_start < timestamp(settlement['observed_at']):
            raise ValueError('Require settlement after event start')
        if settlement['outcome'] not in (0, 1):
            raise ValueError('This half-line toy supports binary decisive settlements only')
        packet = row['input_packet']
        if packet['event_id'] != contract['event_id']:
            raise ValueError('Input event mismatch')
        if set(packet) != {'event_id', 'captured_at', 'invented_note'}:
            raise ValueError('Only the declared price-blind evidence packet is allowed')
        captured = timestamp(packet['captured_at'])
        market = row['market_snapshot']
        market_captured = timestamp(market['captured_at'])
        if market['contract'] != contract:
            raise ValueError('Wrong market snapshot contract identity')
        if not protocol_lock <= captured or not protocol_lock <= market_captured:
            raise ValueError('Require protocol <= input and market snapshot capture')
        expected_hash = input_hash(packet)
        market_hash = input_hash(market)
        reasons = []
        for arm in ARMS:
            record = row['forecasts'].get(arm)
            if record is None:
                reasons.append(arm + ':MISSING')
                continue
            if arm == 'M':
                if record['market_snapshot_hash'] != market_hash:
                    raise ValueError('Frozen market snapshot hash required')
            else:
                if record['input_hash'] != expected_hash:
                    raise ValueError('Identical input hash required')
                if record['prompt_hash'] != expected_prompt_hash:
                    raise ValueError('Identical model prompt hash required')
            if record['contract'] != contract:
                raise ValueError('Wrong forecast contract identity')
            arm_capture = market_captured if arm == 'M' else captured
            produced = timestamp(record['generated_at'])
            if not arm_capture <= produced <= lock:
                raise ValueError('Require input <= forecast <= lock')
            if not produced <= cohort_lock:
                raise ValueError('Require forecast <= cohort lock')
            if record['status'] == 'ABSTAIN':
                if 'p' in record:
                    raise ValueError('ABSTAIN has no probability')
                reasons.append(arm + ':ABSTAIN')
            elif record['status'] == 'PREDICT':
                probability(record['p'])
                if arm == 'M' and F(record['p']) != F(market['market_probability']):
                    raise ValueError('M must equal the separate frozen market snapshot probability')
            else:
                raise ValueError('Unknown forecast status')
        if reasons:
            excluded[row['id']] = reasons
        else:
            eligible.append(row['id'])
    if not eligible or eligible != protocol['common_cohort_ids']:
        raise ValueError('Predeclared common cohort does not match pre-event complete cases')
    return {'cohort_ids': eligible, 'excluded': excluded}

def cohort_arrays(fixture):
    validation = validate_fixture(fixture)
    rows = {row['id']: row for row in fixture['rows']}
    cohort = [rows[row_id] for row_id in validation['cohort_ids']]
    ps = {arm: [F(row['forecasts'][arm]['p']) for row in cohort] for arm in ARMS}
    ys = [row['settlement']['outcome'] for row in cohort]
    return validation, ps, ys

def compare_four_arms(fixture):
    validation, ps, ys = cohort_arrays(fixture)
    ps['S'] = blend(ps['M'], ps['G'], F(1, 4))
    scores = {arm: brier(values, ys) for arm, values in ps.items()}
    return {**validation, 'brier': scores,
            'delta_vs_M': {arm: scores[arm]-scores['M'] for arm in ('G', 'C', 'S')}}

def claude_secondary(fixture):
    """Separate optional secondary, never substituted for prospectively fixed S."""
    _, ps, ys = cohort_arrays(fixture)
    if fixture['protocol']['claude_secondary_prespecified'] is not True:
        raise ValueError('Claude-shrunk secondary not prespecified')
    return brier(blend(ps['M'], ps['C'], F(1, 4)), ys)
