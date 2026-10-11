#!/usr/bin/env python3
"""Synthetic PRIME prop-pricing demonstrations; no historical or live NFL data.

Run: python verify_examples.py
Writes results.json beside this script. Python standard library only; no network.
All discrete marginal calculations use exact Fraction arithmetic. Correlation
examples use double precision for one square root and test full 2x2 PMFs.
"""
from fractions import Fraction as F
from math import comb, isclose, sqrt
from pathlib import Path
import json


def numeric(value):
    if isinstance(value, F):
        return {"decimal": float(value), "exact": str(value)}
    if isinstance(value, dict):
        return {str(k): numeric(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [numeric(v) for v in value]
    return value


def binomial(n, p):
    return {r: F(comb(n, r)) * p**r * (1-p)**(n-r) for r in range(n+1)}


def rising(x, k):
    product = F(1)
    for i in range(k):
        product *= x+i
    return product


def beta_binomial(n, a, b):
    return {r: F(comb(n, r))*rising(a, r)*rising(b, n-r)/rising(a+b, n)
            for r in range(n+1)}


def check_pmf(pmf):
    assert sum(pmf.values()) == 1
    assert min(pmf.values()) >= 0


def mean(pmf):
    return sum(x*p for x, p in pmf.items())


def variance(pmf):
    mu = mean(pmf)
    return sum((x-mu)**2*p for x, p in pmf.items())


def lower_median(pmf):
    cumulative = F(0)
    for x, p in sorted(pmf.items()):
        cumulative += p
        if cumulative >= F(1, 2):
            return x
    raise AssertionError("Not a probability mass function")


def tail(pmf, threshold):
    return sum(p for x, p in pmf.items() if x >= threshold)


def roi(p, decimal_odds):
    return p*decimal_odds-1


def american(decimal_odds):
    assert decimal_odds > 1
    if decimal_odds >= 2:
        return 100*(decimal_odds-1)
    return -100/(decimal_odds-1)


def pmf_summary(pmf):
    check_pmf(pmf)
    return {"pmf": pmf, "mean": mean(pmf), "variance": variance(pmf),
            "lower_median": lower_median(pmf)}


def calibration_score(forecasts, outcomes):
    assert len(forecasts) == len(outcomes)
    n = len(outcomes)
    base = F(sum(outcomes), n)
    bins = {}
    for p, y in zip(forecasts, outcomes):
        bins.setdefault(p, []).append(y)
    reliability = F(0)
    resolution = F(0)
    details = []
    for p, values in sorted(bins.items()):
        observed = F(sum(values), len(values))
        weight = F(len(values), n)
        reliability += weight*(p-observed)**2
        resolution += weight*(observed-base)**2
        details.append({"forecast": p, "count": len(values),
                        "wins": sum(values), "observed": observed})
    uncertainty = base*(1-base)
    brier = sum((p-y)**2 for p, y in zip(forecasts, outcomes))/n
    assert brier == reliability-resolution+uncertainty
    return {"n": n, "brier": brier, "reliability": reliability,
            "resolution": resolution, "uncertainty": uncertainty,
            "bins": details}


def build():
    d = F(21, 11)  # American -110
    output = {"label": "SYNTHETIC DEMONSTRATION; NOT NFL HISTORICAL EVIDENCE",
              "odds_convention": "Decimal odds include returned stake; ROI per unit risked.",
              "common_decimal_odds": d,
              "common_break_even": 1/d}

    # 1. Same mean and unique median; different tail and opposite ROI signs.
    a = {20: F(2, 5), 60: F(1, 5), 100: F(2, 5)}
    b = {40: F(49, 100), 60: F(1, 50), 80: F(49, 100)}
    example_1 = {}
    for name, pmf in (("A", a), ("B", b)):
        item = pmf_summary(pmf)
        item.update({"P_yards_over_49_5": tail(pmf, 50),
                     "ROI_minus_110": roi(tail(pmf, 50), d)})
        example_1[name] = item
    assert mean(a) == mean(b) == 60
    assert lower_median(a) == lower_median(b) == 60
    assert roi(tail(a, 50), d) > 0 > roi(tail(b, 50), d)
    output["example_1_mean_median_do_not_price_tail"] = example_1

    # 2. Same expected targets/catch chance, different count distributions.
    q = F(13, 20)
    fixed = binomial(8, q)
    low, high = binomial(4, q), binomial(12, q)
    random_targets = {r: (low.get(r, F(0))+high.get(r, F(0)))/2
                      for r in range(13)}
    beta = beta_binomial(8, F(13, 2), F(7, 2))
    example_2 = {}
    for name, pmf in (("fixed_8_targets", fixed),
                      ("targets_4_or_12_equal_weights", random_targets),
                      ("fixed_8_targets_beta_6_5_3_5", beta)):
        item = pmf_summary(pmf)
        item.update({"P_receptions_ge_5": tail(pmf, 5),
                     "P_receptions_ge_6": tail(pmf, 6),
                     "P_receptions_ge_8": tail(pmf, 8),
                     "ROI_over_4_5_minus_110": roi(tail(pmf, 5), d)})
        example_2[name] = item
    assert mean(fixed) == mean(random_targets) == mean(beta) == F(26, 5)
    assert variance(fixed) == 8*q*(1-q) == F(91, 50)
    assert variance(random_targets) == 8*q*(1-q)+q*q*16 == F(429, 50)
    assert variance(beta) == 8*q*(1-q)*(1+F(7, 11)) == F(819, 275)
    assert roi(tail(fixed, 5), d) > 0 > roi(tail(random_targets, 5), d)
    # More spread need not increase each upper-tail probability.
    assert tail(beta, 5) < tail(fixed, 5)
    assert tail(beta, 8) > tail(fixed, 8)
    output["example_2_fixed_random_targets_and_beta_binomial"] = example_2

    # 3. Latent parameter uncertainty versus single-bet outcome uncertainty.
    example_3 = {}
    for name, values in (("narrow", (F(53, 100), F(57, 100))),
                         ("wide", (F(49, 100), F(61, 100)))):
        mu = sum(values)/2
        parameter_variance = sum((p-mu)**2 for p in values)/2
        conditional_outcome_variance = sum(p*(1-p) for p in values)/2
        predictive_variance = conditional_outcome_variance+parameter_variance
        assert mu == F(11, 20)
        assert predictive_variance == mu*(1-mu) == F(99, 400)
        lower = min(values)
        fair_d = 1/lower
        hurdle_d = F(105, 100)/lower
        example_3[name] = {
            "equally_weighted_parameter_scenarios": values,
            "mean_probability": mu,
            "parameter_variance": parameter_variance,
            "E_conditional_outcome_variance": conditional_outcome_variance,
            "predictive_single_Bernoulli_variance": predictive_variance,
            "mean_ROI_minus_110": roi(mu, d),
            "worst_scenario_ROI_minus_110": roi(lower, d),
            "worst_scenario_probability": lower,
            "zero_ROI_min_decimal_odds": fair_d,
            "zero_ROI_equivalent_american": american(fair_d),
            "five_pct_ROI_min_decimal_odds": hurdle_d,
            "five_pct_ROI_equivalent_american": american(hurdle_d),
        }
        assert roi(lower, fair_d) == 0
        assert roi(lower, hurdle_d) == F(1, 20)
    output["example_3_uncertainty_and_price_gates"] = example_3

    # 4. Rho is correlation of EVENT INDICATORS, not underlying yard totals.
    pa, pb = .60, .55
    s = sqrt(pa*(1-pa)*pb*(1-pb))
    example_4 = {"P_QB_over_249_5": pa, "P_WR_over_69_5": pb,
                 "frechet_joint_bounds": [max(0, pa+pb-1), min(pa, pb)],
                 "decimal_price": 3., "price_american": 200,
                 "break_even": 1/3, "scenarios": []}
    for rho in (-.20, 0., .20):
        joint = pa*pb+rho*s
        cells = {"both_win": joint, "QB_only": pa-joint,
                 "WR_only": pb-joint, "neither": 1-pa-pb+joint}
        assert min(cells.values()) >= 0
        assert isclose(sum(cells.values()), 1)
        assert isclose(cells["both_win"]+cells["QB_only"], pa)
        assert isclose(cells["both_win"]+cells["WR_only"], pb)
        assert isclose((joint-pa*pb)/s, rho, abs_tol=1e-12)
        example_4["scenarios"].append({
            "indicator_correlation": rho, "joint_probability": joint,
            "ROI_plus_200": 3*joint-1, "pmf_2x2": cells,
            "fair_decimal": 1/joint,
            "fair_american": american(1/joint)})
    # A fully specified two-script mixture also creates positive dependence.
    # The legs are independent CONDITIONAL ON script, not unconditionally.
    script_joint = (F(4, 5)*F(3, 4)+F(2, 5)*F(7, 20))/2
    assert script_joint == F(37, 100)
    assert (F(4, 5)+F(2, 5))/2 == F(3, 5)
    assert (F(3, 4)+F(7, 20))/2 == F(11, 20)
    example_4["equal_weight_script_mixture"] = {
        "high_script_marginals": [F(4, 5), F(3, 4)],
        "low_script_marginals": [F(2, 5), F(7, 20)],
        "joint_under_conditional_independence": script_joint,
        "ROI_plus_150": roi(script_joint, F(5, 2)),
        "ROI_plus_200": roi(script_joint, F(3)),
    }
    output["example_4_joint_probability_sensitivity"] = example_4

    # Calibration diagnostic: exact invented outcomes, not observed NFL results.
    outcomes = [1]*20+[0]*80+[1]*80+[0]*20
    scores = {
        "A_always_50_pct": calibration_score([F(1, 2)]*200, outcomes),
        "B_30_then_70_pct": calibration_score([F(3, 10)]*100+[F(7, 10)]*100, outcomes),
        "C_20_then_80_pct": calibration_score([F(1, 5)]*100+[F(4, 5)]*100, outcomes),
    }
    assert scores["A_always_50_pct"]["brier"] == F(1, 4)
    assert scores["B_30_then_70_pct"]["brier"] == F(17, 100)
    assert scores["C_20_then_80_pct"]["brier"] == F(4, 25)
    assert scores["B_30_then_70_pct"]["reliability"] > scores["A_always_50_pct"]["reliability"]
    output["validation_calibration_is_not_brier_alone"] = scores

    # Push probability belongs to the settlement contract, not the loss bucket.
    pw, pl, pp = F(1, 2), F(2, 5), F(1, 10)
    assert pw+pl+pp == 1
    correct_ev = pw*(d-1)-pl
    conditional_p = pw/(1-pp)
    assert correct_ev == pw*d+pp-1 == F(3, 55)
    assert correct_ev == (1-pp)*roi(conditional_p, d)
    assert pw*d-1 == -F(1, 22)
    # Multiplicative de-vig toy example: Over -120 / Under +100, same line.
    raw_over, raw_under = F(6, 11), F(1, 2)
    market_conditional_over = raw_over/(raw_over+raw_under)
    output["validation_push_contract"] = {
        "p_win": pw, "p_loss": pl, "p_push": pp,
        "decimal_odds": d, "correct_ROI": correct_ev,
        "incorrect_push_as_loss_ROI": pw*d-1,
        "conditional_on_no_push_win_probability": conditional_p,
        "fair_decimal_odds_with_push": (1-pp)/pw,
        "fair_inverse_odds_conditional_probability": pw/(1-pp),
        "toy_market_normalized_over_minus120_under_plus100": market_conditional_over,
        "market_unconditional_over_if_push_is_10_pct": (1-pp)*market_conditional_over,
    }
    output["verification"] = "All exact arithmetic and consistency assertions passed."
    return output


if __name__ == "__main__":
    result = numeric(build())
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(result["verification"])
    print(f"Wrote {path}")
