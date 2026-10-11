#!/usr/bin/env python3
"""Exact-arithmetic research fixtures for combined PRIME-style pricing gates.

Run: python combined_gate_checks.py
No actual NFL data. Exact 4pp/5% here are nominal research thresholds, not a
replacement for the framework's approximate starting gates or non-price gates.
Push conditioning is a proposed clarification requiring policy review.
"""
from fractions import Fraction as F
from pathlib import Path
import json

from verify_examples import numeric, american


def validate_scenario(win, push):
    assert 0 <= win <= 1 and 0 <= push <= 1 and win+push <= 1


def q_no_push(win, push):
    validate_scenario(win, push)
    if push == 1:
        raise ValueError("Conditional win probability is undefined if every outcome pushes")
    return win/(1-push)


def ev(win, push, d):
    validate_scenario(win, push)
    assert d > 1
    return win*d+push-1


def bounds(central, scenarios, edge=F(1, 25), roi=F(1, 20)):
    win, push = central
    q = q_no_push(win, push)
    if win <= 0 or q <= edge or any(w <= 0 for w, _ in scenarios):
        raise ValueError("No finite price can pass all specified positive-EV gates")
    return {"edge_bound_inclusive": 1/(q-edge),
            "central_ROI_bound_inclusive": (1+roi-push)/win,
            "adverse_bound_strict": max((1-v)/w for w, v in scenarios)}


def gate_result(central, scenarios, d, edge=F(1, 25), roi=F(1, 20)):
    p, v = central
    q = q_no_push(p, v)
    evs = [ev(w, u, d) for w, u in scenarios]
    result = {"decimal_odds": d, "American_equivalent": american(d),
              "central_conditional_probability": q,
              "central_probability_edge": q-1/d,
              "central_ROI": ev(p, v, d), "scenario_ROIs": evs,
              "worst_scenario_ROI": min(evs),
              "edge_pass": q-1/d >= edge,
              "central_ROI_pass": ev(p, v, d) >= roi,
              "adverse_positive_EV_pass": min(evs) > 0}
    result["all_numeric_gates_pass"] = (result["edge_pass"] and
        result["central_ROI_pass"] and result["adverse_positive_EV_pass"])
    b = bounds(central, scenarios, edge, roi)
    analytic = (d >= b["edge_bound_inclusive"] and
                d >= b["central_ROI_bound_inclusive"] and
                d > b["adverse_bound_strict"])
    assert analytic == result["all_numeric_gates_pass"]
    return result


def main():
    e, r = F(1, 25), F(1, 20)
    central = (F(11, 20), F(0))
    narrow = [(F(53, 100), F(0)), (F(57, 100), F(0))]
    wide = [(F(49, 100), F(0)), (F(61, 100), F(0))]
    narrow_b = bounds(central, narrow)
    wide_b = bounds(central, wide)
    assert narrow_b == {"edge_bound_inclusive": F(100, 51),
                        "central_ROI_bound_inclusive": F(21, 11),
                        "adverse_bound_strict": F(100, 53)}
    assert wide_b["adverse_bound_strict"] == F(100, 49)
    narrow_boundary = gate_result(central, narrow, F(100, 51))
    assert narrow_boundary["all_numeric_gates_pass"]
    assert narrow_boundary["central_ROI"] == F(4, 51)
    assert narrow_boundary["worst_scenario_ROI"] == F(2, 51)
    wide_boundary = gate_result(central, wide, F(100, 49))
    assert not wide_boundary["all_numeric_gates_pass"]
    assert wide_boundary["worst_scenario_ROI"] == 0
    assert gate_result(central, wide, F(41, 20))["all_numeric_gates_pass"] # +105

    push_central = (F(27, 50), F(1, 10))
    push_scenarios = [(F(1, 2), F(1, 10)), (F(51, 100), F(1, 20))]
    push_b = bounds(push_central, push_scenarios)
    assert push_b == {"edge_bound_inclusive": F(25, 14),
                      "central_ROI_bound_inclusive": F(95, 54),
                      "adverse_bound_strict": F(95, 51)}
    at_minus_110 = gate_result(push_central, push_scenarios, F(21, 11))
    assert at_minus_110["scenario_ROIs"] == [F(3, 55), F(13, 550)]
    at_185 = gate_result(push_central, push_scenarios, F(37, 20))
    assert at_185["edge_pass"] and at_185["central_ROI_pass"]
    assert at_185["scenario_ROIs"] == [F(1, 40), -F(13, 2000)]
    assert not at_185["all_numeric_gates_pass"]
    assert gate_result(push_central, push_scenarios, 1+F(100, 115))["all_numeric_gates_pass"]
    assert not gate_result(push_central, push_scenarios, 1+F(100, 116))["all_numeric_gates_pass"]

    # Check algebra against direct gates across a finite exact-rational grid.
    n_checks = 0
    for numerator in range(2, 10):
        q = F(numerator, 10)
        for push in (F(0), F(1, 10), F(1, 5)):
            win = (1-push)*q
            for d in (F(6, 5), F(3, 2), F(37, 20), F(21, 11), F(2), F(5, 2), F(4)):
                adverse = [(max(F(1, 100), win-F(1, 20)), push)]
                gate_result((win, push), adverse, d)
                n_checks += 1

    # General edge-versus-ROI crossover, conditional scale with nonpush mass lambda.
    crossover_no_push = e*(1+r)/r
    crossover_push_10 = e*(F(9, 10)+r)/r
    assert crossover_no_push == F(21, 25) # .84
    assert crossover_push_10 == F(19, 25) # .76

    result = {
      "label": "SYNTHETIC RESEARCH FIXTURES; NO POLICY ADOPTION OR HISTORICAL VALIDATION",
      "thresholds": {"probability_edge": e, "central_ROI": r,
                     "adverse_gate": "strictly greater than zero"},
      "no_push_central_55_pct": {
         "narrow_bounds": narrow_b,
         "narrow_at_minus_110": gate_result(central, narrow, F(21, 11)),
         "narrow_at_edge_boundary": narrow_boundary,
         "narrow_at_minus_104": gate_result(central, narrow, 1+F(100, 104)),
         "narrow_at_minus_105": gate_result(central, narrow, 1+F(100, 105)),
         "wide_bounds": wide_b, "wide_at_adverse_boundary": wide_boundary,
         "wide_at_plus_105": gate_result(central, wide, F(41, 20))},
      "push_central_win54_push10": {
         "scenario_win_push_pairs": push_scenarios, "bounds": push_b,
         "at_minus_110": at_minus_110, "at_decimal_1_85": at_185,
         "at_minus_115": gate_result(push_central, push_scenarios, 1+F(100, 115)),
         "at_minus_116": gate_result(push_central, push_scenarios, 1+F(100, 116))},
      "edge_vs_ROI_gate_crossover_conditional_p": {
         "no_push": crossover_no_push, "10_pct_push": crossover_push_10},
      "grid_analytic_vs_direct_assertions_passed": n_checks,
    }
    path = Path(__file__).with_name("combined_gate_results.json")
    path.write_text(json.dumps(numeric(result), indent=2)+"\n")
    print(f"All combined-gate fixtures passed, including {n_checks} grid comparisons.")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
