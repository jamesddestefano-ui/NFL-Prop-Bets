"""Task013 synthetic educational fixtures. No current quotes or private data.

All finite-population moments and losses use exact Fraction arithmetic.
This is a counterexample and a narrow validation demonstration, not a live pipeline.
"""
from collections import Counter, defaultdict
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import product
import json
import math


def mean(values):
    return sum(values, F(0)) / len(values)


def covariance(xs, ys):
    mx, my = mean(xs), mean(ys)
    return mean([(x - mx) * (y - my) for x, y in zip(xs, ys)])


def paired_loss_improvement(target, model, baseline):
    """Positive means the model beats the named baseline on squared close loss."""
    return (model - baseline) * (2 * target - model - baseline)


def mechanical_fixture():
    rows = []
    for su, se, sv in product((-1, 1), repeat=3):
        u, e, v = F(su, 50), F(se, 100), F(sv, 100)
        m0, a, mc = F(1, 2) + u, F(1, 2) + e, F(1, 2) + v
        d, y = a - m0, mc - m0
        rows.append({'u': u, 'e': e, 'v': v, 'm0': m0, 'a': a, 'mc': mc,
                     'weight': F(1, 8), 'model_deviation': d, 'close_move': y,
                     'loss_model': (mc - a) ** 2, 'loss_no_change': y ** 2,
                     'loss_constant': (mc - F(1, 2)) ** 2,
                     'paired_improvement_no_change': paired_loss_improvement(mc, a, m0),
                     'paired_improvement_constant': paired_loss_improvement(mc, a, F(1, 2))})
    ds = [r['model_deviation'] for r in rows]
    ys = [r['close_move'] for r in rows]
    cov = covariance(ds, ys)
    vd, vy = covariance(ds, ds), covariance(ys, ys)
    # This fixture has equal variances; avoid an unnecessary inexact square root.
    assert vd == vy and vd > 0
    return {'rows': rows, 'covariance_move_model': cov,
            'variance_model_deviation': vd, 'variance_close_move': vy,
            'correlation': cov / vd,
            'covariance_model_close_level': covariance([r['a'] for r in rows], [r['mc'] for r in rows]),
            'level_pair_counts': dict(sorted(Counter((str(r['a']), str(r['mc'])) for r in rows).items())),
            **{key: mean([r[key] for r in rows]) for key in
               ('loss_model', 'loss_no_change', 'loss_constant',
                'paired_improvement_no_change', 'paired_improvement_constant')}}


def checkpoint_summary(states):
    if any(state not in ('active', 'inactive', 'unknown') for state in states):
        raise ValueError('Use active/inactive/unknown; timeouts must be explicitly coded unknown.')
    n = len(states)
    counts = Counter(states)
    a, i, u = (counts[key] for key in ('active', 'inactive', 'unknown'))
    return {'attempts': n, 'active': a, 'inactive': i, 'unknown': u,
            'lower': F(a, n) if n else None,
            'upper': F(a + u, n) if n else None,
            'complete_case': F(a, a + i) if a + i else None}


def uninterrupted_status(states):
    checkpoint_summary(states)  # Reject unrecognized observation states.
    return 'refuted' if 'inactive' in states else 'not_identified'


def sample_mean_variance(values):
    """s^2/n, valid only when the listed sampling units satisfy independence."""
    n = len(values)
    if n < 2:
        return None
    avg = mean(values)
    return sum(((x - avg) ** 2 for x in values), F(0)) / (n * (n - 1))


def cluster_summary(rows):
    by_game = defaultdict(list)
    for game, value in rows:
        by_game[game].append(value)
    row_values = [value for _, value in rows]
    game_means = [mean(values) for _, values in sorted(by_game.items())]
    return {'rows': len(rows), 'games': len(by_game),
            'row_mean': mean(row_values) if row_values else None,
            'game_equal_weight_mean': mean(game_means) if game_means else None,
            'naive_row_mean_variance': sample_mean_variance(row_values),
            'game_mean_variance': sample_mean_variance(game_means)}


def valid_guard_case():
    """Every name, contract, value, and timestamp here is invented."""
    contract = {'event': 'SYNTHETIC_GAME_1', 'participant': 'SYNTHETIC_PLAYER_1',
                'market': 'passing_yards', 'period': 'full_game', 'threshold': F(499, 2),
                'book': 'SYNTHETIC_BOOK_A', 'region': 'SYNTHETIC_REGION_A',
                'settlement': 'include_overtime_void_if_dnp', 'side': 'over'}
    opposite = dict(contract, side='under')
    def utc(hour, minute, second):
        return datetime(2026, 1, 1, hour, minute, second, tzinfo=timezone.utc)
    return {'initial': deepcopy(contract), 'initial_opposite': deepcopy(opposite),
            'close': deepcopy(contract), 'close_opposite': deepcopy(opposite),
            'forecast_recorded_at': utc(12, 0, 0), 'decision_at': utc(12, 0, 10),
            'initial_started_at': utc(12, 0, 3), 'initial_completed_at': utc(12, 0, 5),
            'close_started_at': utc(12, 58, 58), 'close_completed_at': utc(12, 59, 0),
            'kickoff_at': utc(13, 0, 0), 'recorded_close_lag_seconds': 60,
            'required_close_lag_seconds': 60}


def guard_case(case):
    """Narrow strict fixture matcher; no interpolation or repair is attempted."""
    if not isinstance(case, dict):
        return ['case_missing_or_invalid']
    reasons = []
    identity_fields = ('event', 'participant', 'market', 'period', 'book', 'region', 'settlement')
    # Equal missing values are not evidence of an exact known contract.
    for name in ('initial', 'close', 'initial_opposite', 'close_opposite'):
        quote = case.get(name)
        if not isinstance(quote, dict):
            reasons.append(name + '_contract_missing_or_invalid')
            continue
        for field in identity_fields:
            value = quote.get(field)
            if not isinstance(value, str) or not value.strip():
                reasons.append(name + '_' + field + '_missing_or_invalid')
        threshold = quote.get('threshold')
        if threshold is None:
            reasons.append(name + '_threshold_missing')
        elif (isinstance(threshold, bool) or not isinstance(threshold, (int, float, F))
              or isinstance(threshold, float) and not math.isfinite(threshold)):
            reasons.append(name + '_threshold_invalid')
        if quote.get('side') not in ('over', 'under'):
            reasons.append(name + '_side_invalid')
    time_fields = ('forecast_recorded_at', 'decision_at', 'initial_started_at',
                   'initial_completed_at', 'close_started_at', 'close_completed_at', 'kickoff_at')
    for field in time_fields:
        value = case.get(field)
        if not isinstance(value, datetime) or value.tzinfo is None or value.utcoffset() is None:
            reasons.append(field + '_missing_or_not_timezone_aware')
    for field in ('recorded_close_lag_seconds', 'required_close_lag_seconds'):
        value = case.get(field)
        if (isinstance(value, bool) or not isinstance(value, (int, float, F))
                or isinstance(value, float) and not math.isfinite(value) or value < 0):
            reasons.append(field + '_missing_or_invalid')
    if reasons:
        return reasons
    if not case['forecast_recorded_at'] < case['decision_at']:
        reasons.append('forecast_not_locked_before_decision')
    for phase in ('initial', 'close'):
        if not case[phase + '_started_at'] <= case[phase + '_completed_at']:
            reasons.append(phase + '_request_timing_inverted')
        if not case[phase + '_completed_at'] < case['kickoff_at']:
            reasons.append(phase + '_completion_not_before_kickoff')
    if case['initial_completed_at'] > case['decision_at']:
        reasons.append('initial_response_after_decision')
    if not case['decision_at'] < case['close_started_at']:
        reasons.append('close_not_later_than_decision')
    fields = ('event', 'participant', 'market', 'period', 'threshold', 'book', 'region', 'settlement')
    for name in ('close', 'initial_opposite', 'close_opposite'):
        quote = case[name]
        for field in fields:
            if quote[field] != case['initial'][field]:
                reasons.append(name + '_' + field + '_mismatch')
        expected_side = case['initial']['side'] if name == 'close' else {'over': 'under', 'under': 'over'}.get(case['initial']['side'])
        if quote['side'] != expected_side:
            reasons.append(name + '_side_mismatch')
    lag = case['kickoff_at'] - case['close_completed_at']
    actual_lag_seconds = F(lag.days * 86400 + lag.seconds) + F(lag.microseconds, 1000000)
    if case['recorded_close_lag_seconds'] != actual_lag_seconds:
        reasons.append('close_lag_mismatch')
    if actual_lag_seconds != case['required_close_lag_seconds']:
        reasons.append('close_lag_outside_fixture_target')
    return reasons


def guard_examples():
    cases = {'valid': valid_guard_case()}
    for label, target, field, value in [
        ('missing_threshold', 'close', 'threshold', None),
        ('wrong_threshold', 'close', 'threshold', F(501, 2)),
        ('wrong_book', 'close', 'book', 'SYNTHETIC_BOOK_B'),
        ('wrong_region', 'close', 'region', 'SYNTHETIC_REGION_B'),
        ('wrong_settlement', 'close', 'settlement', 'regulation_only'),
        ('same_side_instead_of_opposite', 'initial_opposite', 'side', 'over')]:
        c = valid_guard_case()
        c[target][field] = value
        cases[label] = c
    for label, field, value in [
        ('forecast_at_decision', 'forecast_recorded_at', cases['valid']['decision_at']),
        ('request_at_kickoff', 'close_completed_at', cases['valid']['kickoff_at']),
        ('incorrect_recorded_lag', 'recorded_close_lag_seconds', 59),
        ('different_required_lag', 'required_close_lag_seconds', 30)]:
        c = valid_guard_case()
        c[field] = value
        cases[label] = c
    for label, field in [('all_books_unknown', 'book'), ('all_sides_unknown', 'side')]:
        c = valid_guard_case()
        for name in ('initial', 'close', 'initial_opposite', 'close_opposite'):
            c[name][field] = None
        cases[label] = c
    c = valid_guard_case()
    c['kickoff_at'] = c['kickoff_at'].replace(tzinfo=None)
    cases['timezone_naive_kickoff'] = c
    return {'valid_input': cases['valid'],
            'outcomes': {name: {'matched': not guard_case(c), 'reasons': guard_case(c)}
                         for name, c in cases.items()}}


def results():
    rows = [(g, F(d, 100)) for g, d in [('g1', 1), ('g2', -1), ('g3', 2), ('g4', -2)] for _ in range(10)]
    cluster = cluster_summary(rows)
    cluster['naive_row_standard_error'] = math.sqrt(cluster['naive_row_mean_variance'])
    cluster['game_level_standard_error'] = math.sqrt(cluster['game_mean_variance'])
    return {'task': 'PRIME task013 synthetic educational fixtures',
            'current_quote': False, 'private_data': False, 'betting_recommendation': False,
            'mechanical': mechanical_fixture(),
            'checkpoint_availability': checkpoint_summary(['active'] * 6 + ['inactive'] * 2 + ['unknown'] * 2),
            'continuity': {'active_inactive_active': uninterrupted_status(['active', 'inactive', 'active']),
                           'active_active': uninterrupted_status(['active', 'active'])},
            'duplicate_rows': cluster, 'guards': guard_examples(),
            'controls_v2_context_only': {'standard_american_odds_min': -150,
                'standard_american_odds_max': 150, 'central_edge_min_probability_points': 4,
                'conservative_ev_min': 0, 'separate_five_percent_roi_gate': False}}


def jsonable(value):
    if isinstance(value, F):
        return {'exact': str(value), 'decimal': float(value)}
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, dict):
        return {('|'.join(k) if isinstance(k, tuple) else k): jsonable(v) for k, v in value.items()}
    if isinstance(value, list):
        return [jsonable(v) for v in value]
    return value


if __name__ == '__main__':
    print(json.dumps(jsonable(results()), sort_keys=True, indent=2))
