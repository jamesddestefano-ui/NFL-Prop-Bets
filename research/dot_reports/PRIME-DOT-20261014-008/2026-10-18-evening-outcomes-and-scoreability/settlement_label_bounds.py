#!/usr/bin/env python3
"""Synthetic education only: no real event, bookmaker, policy, quote, or API.
Run: python3 settlement_label_bounds.py
All calculation uses exact fractions. Decimal strings are accepted; floats are
rejected so accidental binary-floating-point inputs cannot change exact tests.
"""
from fractions import Fraction as F
from collections.abc import Mapping
import json
import unittest
import sys

STATES = ("W", "L", "V")

def exact(value):
    if isinstance(value, bool) or not isinstance(value, (F, int, str)):
        raise ValueError("Use a finite Fraction, integer, or numeric string")
    try:
        return F(value)
    except (ValueError, ZeroDivisionError, OverflowError) as exc:
        raise ValueError("Value must be finite and rational") from exc

def validate(p):
    if not isinstance(p, Mapping) or set(p) != set(STATES):
        raise ValueError("Forecast must contain exactly W, L, V")
    p = {k: exact(p[k]) for k in STATES}
    if any(v < 0 for v in p.values()):
        raise ValueError("Probabilities must be nonnegative")
    if sum(p.values(), F(0)) != 1:
        raise ValueError("Probabilities must sum exactly to one")
    return p

def validate_state(state):
    if not isinstance(state, str) or state not in STATES:
        raise ValueError("Settlement unresolved or invalid; do not map to L")
    return state

def brier(p, state):
    p, state = validate(p), validate_state(state)
    return sum(((p[k] - int(k == state)) ** 2 for k in STATES), F(0))

def paired_bounds(a, b, possible):
    a, b = validate(a), validate(b)
    possible = tuple(possible)
    if not possible or len(set(possible)) != len(possible):
        raise ValueError("Possible states must be nonempty and distinct")
    differences = {validate_state(s): brier(a, s) - brier(b, s) for s in possible}
    return differences, (min(differences.values()), max(differences.values()))

def conditional_win(p):
    p = validate(p)
    action = p["W"] + p["L"]
    if action == 0:
        raise ValueError("Conditional-on-action forecast undefined")
    return p["W"] / action

def unit_stake_ev(p, decimal_odds):
    p, d = validate(p), exact(decimal_odds)
    if d < 1:
        raise ValueError("Illustrative decimal odds must be at least one")
    return (d - 1) * p["W"] - p["L"]

A = validate(dict(W="0.5", L="0.2", V="0.3"))
B = validate(dict(W="0.5", L="0.4", V="0.1"))

class SyntheticTests(unittest.TestCase):
    def test_all_scores_and_independent_identity(self):
        expected = {"W": (F(19,50), F(21,50)),
                    "L": (F(49,50), F(31,50)),
                    "V": (F(39,50), F(61,50))}
        for s, pair in expected.items():
            self.assertEqual((brier(A,s), brier(B,s)), pair)
            for p in (A,B):
                self.assertEqual(brier(p,s), 1 + sum(x*x for x in p.values()) - 2*p[s])
    def test_paired_bounds_and_ranking_reversal(self):
        diffs, bounds = paired_bounds(A,B,("L","V"))
        self.assertEqual(diffs, {"L":F(9,25),"V":F(-11,25)})
        self.assertEqual(bounds, (F(-11,25),F(9,25)))
        self.assertGreater(diffs["L"],0)
        self.assertLess(diffs["V"],0)
        self.assertEqual(F(11,20)*diffs["L"] + F(9,20)*diffs["V"],0)
    def test_unknown_never_becomes_loss(self):
        for s in (None,"unknown","pending","", "VOID",0,float("nan")):
            with self.subTest(state=repr(s)), self.assertRaises(ValueError):
                brier(A,s)
    def test_forecast_schema(self):
        for p in ({"W":1,"L":0},{"W":1,"L":0,"V":0,"X":0},[1,0,0]):
            with self.assertRaises(ValueError): validate(p)
    def test_negative_and_not_normalized(self):
        for p in ({"W":"1.1","L":"-0.1","V":0},
                  {"W":"0.5","L":"0.2","V":"0.2"}):
            with self.assertRaises(ValueError): validate(p)
    def test_finite_and_exact_input(self):
        for bad in (float("nan"),float("inf"),float("-inf"),"NaN","Infinity","1/0",0.5,True):
            with self.subTest(bad=repr(bad)), self.assertRaises(ValueError):
                validate({"W":bad,"L":0,"V":0})
    def test_candidate_states(self):
        for states in ((),("L","L"),("L","unknown")):
            with self.assertRaises(ValueError): paired_bounds(A,B,states)
    def test_conditional_forecast(self):
        self.assertEqual(conditional_win(A),F(5,7))
        self.assertEqual(conditional_win(B),F(5,9))
        with self.assertRaises(ValueError): conditional_win({"W":0,"L":0,"V":1})
    def test_ev_identity(self):
        for p in (A,B):
            for d in (F(1),F(3,2),F(2),F(7,2)):
                direct = sum((p[s]*{"W":d-1,"L":F(-1),"V":F(0)}[s] for s in STATES),F(0))
                self.assertEqual(unit_stake_ev(p,d),direct)
                self.assertEqual(direct,(p["W"]+p["L"])*(d*conditional_win(p)-1))
        self.assertEqual(unit_stake_ev(A,2),F(3,10))
        self.assertEqual(unit_stake_ev(B,2),F(1,10))
    def test_brier_extremes(self):
        p = {"W":1,"L":0,"V":0}
        self.assertEqual(brier(p,"W"),0)
        self.assertEqual(brier(p,"L"),2)

if __name__ == "__main__":
    result = unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(SyntheticTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    differences, bounds = paired_bounds(A,B,("L","V"))
    report = {
        "scope":"fictional W/L/V full-refund scheme; no real policy or quote",
        "normalization":"sum over three categories, no half scaling; lower is better",
        "scores":{s:{"A":str(brier(A,s)),"B":str(brier(B,s)),"A_minus_B":str(brier(A,s)-brier(B,s))} for s in STATES},
        "unresolved_L_or_V":{"possible_differences":{s:str(v) for s,v in differences.items()},"sharp_interval":[str(x) for x in bounds]},
        "conditional_win_given_action":{"A":str(conditional_win(A)),"B":str(conditional_win(B))},
        "illustrative_EV_at_d_2":{"A":str(unit_stake_ev(A,2)),"B":str(unit_stake_ev(B,2))},
        "tests_run":result.testsRun,"tests_passed":result.wasSuccessful()
    }
    print(json.dumps(report,indent=2))
