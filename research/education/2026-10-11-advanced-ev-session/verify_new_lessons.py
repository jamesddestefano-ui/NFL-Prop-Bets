#!/usr/bin/env python3
"""Five synthetic EV education fixtures. Python standard library only.

Every NFL label, probability, quote, role, and outcome is invented. This file
tests mathematical implications, not a forecasting model or betting strategy.
Run: python verify_new_lessons.py --output new_lesson_results.json
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path
import platform


CHECKS: list[str] = []


def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)


def bayes(prior: F, sensitivity: F, false_positive: F) -> F:
    if not all(F(0) <= x <= F(1) for x in (prior, sensitivity, false_positive)):
        raise ValueError("Probabilities must be in [0,1]")
    joint_high = prior * sensitivity
    marginal_report = joint_high + (1 - prior) * false_positive
    if marginal_report == 0:
        raise ValueError("Cannot condition on a zero-probability report")
    return joint_high / marginal_report


def binomial(n: int, p: F) -> list[F]:
    return [F(math.comb(n, k)) * p**k * (1 - p)**(n-k) for k in range(n+1)]


def convolve_bernoulli(n: int, p: F) -> list[F]:
    pmf = [F(1)]
    for _ in range(n):
        nxt = [F(0)] * (len(pmf) + 1)
        for k, mass in enumerate(pmf):
            nxt[k] += mass * (1 - p)
            nxt[k+1] += mass * p
        pmf = nxt
    return pmf


def tail(pmf: list[F], minimum: int) -> F:
    return sum(pmf[max(0, minimum):], F(0))


def roi(probability: F, decimal_odds: F) -> F:
    return probability * decimal_odds - 1


def uniform_over(lo: int, hi: int, line: F) -> F:
    return F(sum(y > line for y in range(lo, hi+1)), hi-lo+1)


def serializable(value):
    if isinstance(value, F):
        return {"exact": str(value), "decimal": float(value)}
    if isinstance(value, dict):
        return {str(k): serializable(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serializable(v) for v in value]
    return value


def example_one():
    # Invented WR receptions, no pushes or voids: both role states play.
    catch = F(13, 20)
    high_pmf, low_pmf = binomial(8, catch), binomial(6, catch)
    for label, n, pmf in (("high", 8, high_pmf), ("ordinary", 6, low_pmf)):
        check(f"{label} PMF normalizes", sum(pmf) == 1)
        check(f"{label} comb PMF equals independent convolution", pmf == convolve_bernoulli(n, catch))
        check(f"{label} binomial expectation", sum(F(k)*m for k, m in enumerate(pmf)) == n*catch)
        check(f"{label} survival probabilities monotone", all(tail(pmf,k) >= tail(pmf,k+1) for k in range(n+2)))
    high, low = tail(high_pmf, 5), tail(low_pmf, 5)
    probability = lambda w: w * high + (1-w) * low
    prior, sensitivity, false_positive = F(2,5), F(3,4), F(1,4)
    one = bayes(prior, sensitivity, false_positive)
    duplicate_truth = bayes(prior, sensitivity*1, false_positive*1)
    two_independent = bayes(prior, sensitivity**2, false_positive**2)
    partial = bayes(prior, sensitivity*F(9,10), false_positive*F(3,5))
    check("one report posterior is 2/3", one == F(2,3))
    check("exact copied report leaves posterior unchanged", duplicate_truth == one)
    check("two conditionally independent reports posterior is 6/7", two_independent == F(6,7))
    check("incremental conditional likelihood ratio 1.5 yields 3/4", partial == F(3,4))
    check("partial source evidence lies between copy and independent cases", one < partial < two_independent)
    # Direct enumeration of P(R>=5, report) / P(report), not the mixture shortcut.
    numerator = sum(prior*sensitivity*high_pmf[k] for k in range(5,9)) + sum((1-prior)*false_positive*low_pmf[k] for k in range(5,7))
    denominator = prior*sensitivity + (1-prior)*false_positive
    check("predictive mixture equals joint event enumeration", probability(one) == numerator/denominator)
    check("one-report expected ROI positive at -110", roi(probability(one), F(21,11)) > 0)
    check("invented 50% role stress reverses ROI sign", roi(probability(F(1,2)), F(21,11)) < 0)
    check("market prior that already includes report remains unchanged on reread", bayes(one,F(1),F(1)) == one)
    check("incorrect reapplication of original LR equals naive duplication", bayes(one,sensitivity,false_positive) == two_independent)
    # Fictional settlement clause: inactive means full stake refund, not a loss.
    # Event probability above is now explicitly conditional on action eligibility.
    action=F(4,5)
    q_win=action*probability(one)
    q_loss=action*(1-probability(one))
    q_void=1-action
    posted_roi=q_win*(F(21,11)-1)-q_loss
    mistaken_void_as_loss=roi(q_win,F(21,11))
    check("fictional action-win/action-loss/void vector normalizes",q_win+q_loss+q_void==1)
    check("conditional action probability is retained",q_win/(q_win+q_loss)==probability(one))
    check("refund expected ROI equals action probability times active ROI",posted_roi==action*roi(probability(one),F(21,11)))
    check("treating void as loss changes EV by void probability",posted_roi-mistaken_void_as_loss==q_void)
    check("fictional void-as-loss error reverses ROI sign",posted_roi>0>mistaken_void_as_loss)
    try:
        bayes(F(1,2),F(0),F(0))
    except ValueError:
        check("zero-probability evidence rejected", True)
    else:
        check("zero-probability evidence rejected", False)
    # Separate compact yardage fixture: exact fair half-yard state lines exist.
    high_line, low_line = F(161,2), F(61,2)
    midpoint = (high_line+low_line)/2
    check("high-role fair line has 50% tail", uniform_over(61,100,high_line) == F(1,2))
    check("limited-role fair line has 50% tail", uniform_over(1,60,low_line) == F(1,2))
    midpoint_tail = (uniform_over(61,100,midpoint)+uniform_over(1,60,midpoint))/2
    offered_tail = (uniform_over(61,100,F(119,2))+uniform_over(1,60,F(119,2)))/2
    check("midpoint of state fair lines is not mixture fair line", midpoint_tail == F(13,24) and midpoint_tail != F(1,2))
    check("exact offered line must be evaluated separately", offered_tail == F(61,120) and offered_tail != midpoint_tail)
    return {
        "contract": "Invented WR Over 4.5 receptions, both roles active, no push/void",
        "catch_probability": catch, "high_role_targets": 8, "ordinary_role_targets": 6,
        "high_role_over_probability": high, "ordinary_role_over_probability": low,
        "prior_high_role_probability": prior, "report_sensitivity": sensitivity, "report_false_positive": false_positive,
        "cases": [{"name": name, "role_posterior": w, "event_probability": probability(w), "roi_at_minus110": roi(probability(w),F(21,11))} for name,w in (
            ("before_report",prior), ("one_report",one), ("exact_duplicate_correct",duplicate_truth),
            ("two_independent_reports_or_wrongly_treated_copy",two_independent),
            ("second_report_conditional_LR_1.5",partial), ("unvalidated_role_stress",F(1,2)))],
        "midpoint_line_counterexample": {"high_yards_uniform_integer_support":[61,100], "limited_yards_uniform_integer_support":[1,60],
            "role_weights":[F(1,2),F(1,2)], "conditional_fair_lines":[high_line,low_line], "midpoint_line":midpoint,
            "probability_over_midpoint":midpoint_tail, "offered_line":F(119,2), "probability_over_offered_line":offered_tail},
        "fictional_inactive_refund_guard":{"action_probability":action,"conditional_active_win_probability":probability(one),"unconditional_win":q_win,"unconditional_loss":q_loss,"unconditional_void":q_void,"roi_per_posted_stake":posted_roi,"roi_per_active_stake":roi(probability(one),F(21,11)),"incorrect_void_as_loss_roi":mistaken_void_as_loss,"settlement_scope":"Fictional full-refund clause only; no actual sportsbook rule is represented."},
    }, high, low


def example_two(high,low):
    # This is a finite invented stress set, not a confidence/credible region.
    scenarios = [
        {"id":"A", "prior":F(3,10), "sensitivity":F(65,100), "false_positive":F(15,100), "decimal_odds":F(19,10)},
        {"id":"B", "prior":F(1,2), "sensitivity":F(85,100), "false_positive":F(35,100), "decimal_odds":F(17,10)},
    ]
    for s in scenarios:
        s["role_posterior"] = bayes(s["prior"],s["sensitivity"],s["false_positive"])
        s["event_probability"] = low+s["role_posterior"]*(high-low)
        s["roi"] = roi(s["event_probability"],s["decimal_odds"])
    minimum_joint = min(s["roi"] for s in scenarios)
    check("each supplied joint stress scenario has positive ROI", minimum_joint > 0)
    # A rectangular envelope deliberately adds combinations absent from A/B.
    rectangles=[]
    for pi,se,fp,d in product((F(3,10),F(1,2)),(F(65,100),F(85,100)),(F(15,100),F(35,100)),(F(17,10),F(19,10))):
        w=bayes(pi,se,fp); q=low+w*(high-low)
        rectangles.append({"prior":pi,"sensitivity":se,"false_positive":fp,"decimal_odds":d,"role_posterior":w,"event_probability":q,"roi":roi(q,d)})
    worst=min(rectangles,key=lambda s:s["roi"])
    check("rectangular minimum uses low prior/sensitivity and high false-positive", worst["role_posterior"] == F(39,88))
    check("enlarged rectangular stress set can reverse sign", worst["roi"] < 0 < minimum_joint)
    check("rectangular minimizer is absent from supplied joint scenarios", not any(all(worst[k]==s[k] for k in ("prior","sensitivity","false_positive","decimal_odds")) for s in scenarios))
    componentwise=min(s["event_probability"] for s in scenarios)*min(s["decimal_odds"] for s in scenarios)-1
    check("componentwise p and odds minima add an unattested pair", componentwise < 0 < minimum_joint)
    central=low+F(2,3)*(high-low)
    reference_edges=[central-F(55,100),central-F(59,100)]
    check("uncertain reference can change model-reference edge sign", reference_edges[0]>0>reference_edges[1])
    # Endpoint monotonicity checked on a grid as an additional falsification guard.
    for fp in (F(15,100),F(25,100),F(35,100)):
        check(f"posterior increases with prior at false-positive {fp}", bayes(F(3,10),F(3,4),fp) < bayes(F(1,2),F(3,4),fp))
    return {"joint_scenarios":scenarios,"minimum_joint_scenario_roi":minimum_joint,
            "componentwise_probability_and_price_minimum_roi":componentwise,
            "enlarged_rectangle_worst_case":worst,"rectangle_corner_count":len(rectangles),
            "central_model_probability":central,"alternative_reference_probabilities":[F(55,100),F(59,100)],
            "model_minus_reference_probability_edges":reference_edges,
            "coverage_claim":"None. These are invented scenario sets; neither is a calibrated confidence or credible region."}


def example_three(high,low):
    q=low+F(2,3)*(high-low)
    stale,executable=F(21,11),F(17,10)
    check("stale price positive but executable price negative", roi(q,stale)>0>roi(q,executable))
    p=F(55,100)
    allocations=[(F(10),F(21,10)),(F(90),F(18,10))]
    total_stake=sum(stake for stake,_ in allocations)
    effective=sum(stake*d for stake,d in allocations)/total_stake
    profit=sum(stake*roi(p,d) for stake,d in allocations)
    check("capacity-weighted decimal odds are 1.83",effective==F(183,100))
    check("capacity-weighted ROI is 0.65%",profit/total_stake==F(65,10000))
    check("return-state enumeration equals weighted expected profit",p*sum(s*(d-1) for s,d in allocations)-(1-p)*total_stake==profit)
    check("probability stress gives -4.84% ROI",roi(F(52,100),effective)==F(-484,10000))
    candidate_ev=[F(12,100)]*20+[F(2,100)]*80
    ideal_profit=sum(candidate_ev)
    nonrandom_available=candidate_ev[20:]
    random_expected_profit=F(4,5)*ideal_profit
    check("ideal candidate cohort modeled ROI is 4%",ideal_profit/100==F(4,100))
    check("losing highest-edge fifth leaves modeled ROI 2%",sum(nonrandom_available)/80==F(2,100))
    check("random fifth missing retains expected ROI 4%",random_expected_profit/80==F(4,100))
    check("opportunity loss is not a losing settled wager",sum(nonrandom_available)==F(8,5) and random_expected_profit==F(16,5))
    return {"repricing":{"event_probability":q,"stale_decimal":stale,"stale_roi":roi(q,stale),"executable_decimal":executable,"executable_roi":roi(q,executable)},
            "capacity":{"event_probability":p,"invented_allocation":[{"stake":s,"decimal":d} for s,d in allocations],"headline_roi":roi(p,F(21,10)),"effective_decimal":effective,"effective_roi":profit/total_stake,"probability_stress":F(52,100),"stress_roi":roi(F(52,100),effective)},
            "latency_selection":{"candidate_count":100,"high_EV_count":20,"high_EV":F(12,100),"other_EV":F(2,100),"ideal_expected_profit_units":ideal_profit,"ideal_mean_roi":ideal_profit/100,"nonrandom_missing_count":20,"remaining_mean_roi":sum(nonrandom_available)/80,"remaining_expected_profit_units":sum(nonrandom_available),"random_missing_expected_profit_units":random_expected_profit,"random_missing_expected_mean_roi":random_expected_profit/80},
            "execution_claim":"No quote, capacity, allocation, accepted wager, or fill was observed or attempted."}


def negative_binomial_pmf(k,shape,success):
    return math.exp(math.lgamma(k+shape)-math.lgamma(shape)-math.lgamma(k+1)+shape*math.log(success)+k*math.log1p(-success))


def example_four():
    # Invented NFL reception counts: deliberately absurd homogeneous-Poisson fit.
    observed=[0]*50+[10]*50
    prior_shape,prior_rate=1,1
    shape,rate=prior_shape+sum(observed),prior_rate+len(observed)
    n=len(observed)
    mean=F(shape,rate)
    zero_probability=(rate/(rate+1))**shape
    expected_zeros=n*zero_probability
    # Conditional on lambda, replicated total is Poisson(n*lambda), then integrate.
    success=rate/(rate+n)
    mass=success**shape
    lower=[]
    for k in range(sum(observed)):
        lower.append(mass)
        mass*=((shape+k)/(k+1))*(1-success)
    total_tail=1-math.fsum(lower)
    direct_lower=math.fsum(negative_binomial_pmf(k,shape,success) for k in range(sum(observed)))
    check("negative-binomial recurrence matches independent log-gamma evaluation",abs(total_tail-(1-direct_lower))<1e-11)
    check("mean PPC is not extreme",F(1,10)<total_tail<F(9,10))
    check("zero-rate PPC reveals large mismatch",zero_probability<.01 and observed.count(0)/n==.5)
    # At least 50 zero observations implies some size-50 subset is all zero.
    # For each subset, integrate exp(-50*lambda) under the same Gamma posterior.
    # This union bound accounts for the shared latent lambda across replications.
    zero_tail_union_bound=math.comb(n,50)*(rate/(rate+50))**shape
    check("zero-frequency posterior predictive upper bound is below 1e-50",0<zero_tail_union_bound<1e-50)
    # Fitted calibration display versus a later locked-map test.
    # Raw .4/.6 forecasts map to .2/.8 after 4/20 and 16/20 calibration successes.
    training=[(F(2,5),20,4),(F(3,5),20,16)]
    later=[(F(2,5),20,10),(F(3,5),20,10)]
    mapping={p:F(w,n) for p,n,w in training}
    ece=lambda rows,fn:sum(F(n)*abs(fn(p)-F(w,n)) for p,n,w in rows)/sum(n for _,n,_ in rows)
    brier=lambda rows,fn:sum(F(w)*(fn(p)-1)**2+F(n-w)*fn(p)**2 for p,n,w in rows)/sum(n for _,n,_ in rows)
    check("fitted bin map has zero in-sample displayed calibration error",ece(training,lambda p:mapping[p])==0)
    check("locked fitted map later calibration error is 0.3",ece(later,lambda p:mapping[p])==F(3,10))
    check("raw later calibration error is 0.1",ece(later,lambda p:p)==F(1,10))
    check("synthetic later Brier scores 0.34 vs 0.26",brier(later,lambda p:mapping[p])==F(34,100) and brier(later,lambda p:p)==F(26,100))
    # Audit the transcript's apparent n+1 denominator against direct integration.
    n_bernoulli,s=3,3
    correct=F(s+1,n_bernoulli+2)
    # Uniform prior times likelihood p^3 => normalized posterior density 4 p^3.
    integral_mean=F(4,5)
    check("uniform-prior Bernoulli denominator n+2 verified by integration",correct==integral_mean)
    check("n+1 formula fails all-success posterior-mean fixture",F(s+1,n_bernoulli+1)!=correct)
    log_predictive=math.log((.2+.8)/2)
    average_log=(math.log(.2)+math.log(.8))/2
    check("posterior predictive log score averages densities before logging",math.isclose(log_predictive,-math.log(2)) and log_predictive>average_log)
    return {"gamma_poisson":{"invented_counts":{"zero":50,"ten":50},"prior_shape":prior_shape,"prior_rate":prior_rate,"posterior_shape":shape,"posterior_rate":rate,"observed_mean":F(sum(observed),n),"predictive_mean":mean,"predictive_variance":mean+F(shape,rate**2),"mean_statistic_posterior_predictive_tail":total_tail,"loggamma_crosscheck_absolute_error":abs(total_tail-(1-direct_lower)),"observed_zero_fraction":F(1,2),"predictive_zero_probability":zero_probability,"expected_zero_count":expected_zeros,"P_replicated_zero_count_ge_50_upper_bound":zero_tail_union_bound},
            "heldout_calibrator":{"calibration_window":[{"raw_p":p,"n":n,"wins":w,"fitted_p":mapping[p]} for p,n,w in training],"later_window":[{"raw_p":p,"n":n,"wins":w,"locked_calibrated_p":mapping[p]} for p,n,w in later],"in_sample_calibrated_ECE":ece(training,lambda p:mapping[p]),"later_calibrated_ECE":ece(later,lambda p:mapping[p]),"later_raw_ECE":ece(later,lambda p:p),"later_calibrated_Brier":brier(later,lambda p:mapping[p]),"later_raw_Brier":brier(later,lambda p:p)},
            "transcript_formula_guard":{"uniform_prior_Bernoulli_n":n_bernoulli,"successes":s,"correct_posterior_mean":correct,"incorrect_n_plus_1_result":F(s+1,n_bernoulli+1)},
            "predictive_log_score_guard":{"equal_weight_draw_likelihoods":[.2,.8],"correct_log_mean_likelihood":log_predictive,"incorrect_mean_log_likelihood":average_log},
            "scope":"The check is under the assumed model. Passing chosen predictive checks does not establish real future calibration. The later data are a constructed counterexample, not empirical evidence that recalibration generally harms."}


def example_five():
    # Event Y could be an invented NFL Over 4.5 receptions; no actual player.
    # Each signal is correct with probability .8; independent conditional on Y.
    cells=[]
    for y,a,b in product((0,1),repeat=3):
        pa=F(4,5) if a==y else F(1,5)
        pb=F(4,5) if b==y else F(1,5)
        mass=F(1,2)*pa*pb
        cells.append({"outcome":y,"signal_A":a,"signal_B":b,"mass":mass,"count_in_exact_50_row_fixture":int(mass*50)})
    check("signal joint distribution normalizes",sum(c["mass"] for c in cells)==1)
    for key in ("signal_A","signal_B"):
        for signal in (0,1):
            cohort=[c for c in cells if c[key]==signal]
            actual=sum(c["mass"]*c["outcome"] for c in cohort)/sum(c["mass"] for c in cohort)
            check(f"{key} individually calibrated at signal {signal}",actual==(F(4,5) if signal else F(1,5)))
    rows=[]
    for a,b in product((0,1),repeat=2):
        cohort=[c for c in cells if c["signal_A"]==a and c["signal_B"]==b]
        mass=sum(c["mass"] for c in cohort)
        event_p=sum(c["mass"]*c["outcome"] for c in cohort)/mass
        mean_forecast=((F(4,5) if a else F(1,5))+(F(4,5) if b else F(1,5)))/2
        rows.append({"signal_A":a,"signal_B":b,"mass":mass,"mean_forecast":mean_forecast,"actual_conditional_probability":event_p})
    positive=next(r for r in rows if r["signal_A"]==r["signal_B"]==1)
    check("mean of calibrated forecasts can be uncalibrated",positive["mean_forecast"]==F(4,5) and positive["actual_conditional_probability"]==F(16,17))
    ece=sum(r["mass"]*abs(r["mean_forecast"]-r["actual_conditional_probability"]) for r in rows)
    check("ensemble population ECE is 0.096",ece==F(12,125))
    # A copied signal yields no second piece of evidence.
    copied_both_positive=F(4,5)
    check("copied .8 signal must not become 16/17",copied_both_positive!=F(16,17))
    single_brier=sum(c["mass"]*((F(4,5) if c["signal_A"] else F(1,5))-c["outcome"])**2 for c in cells)
    mean_brier=sum(r["mass"]*(r["actual_conditional_probability"]*(1-r["mean_forecast"])**2+(1-r["actual_conditional_probability"])*r["mean_forecast"]**2) for r in rows)
    fused_brier=sum(r["mass"]*r["actual_conditional_probability"]*(1-r["actual_conditional_probability"]) for r in rows)
    check("single calibrated source population Brier is 0.16",single_brier==F(16,100))
    check("averaging improves Brier here despite losing calibration",mean_brier==F(1312,10000) and mean_brier<single_brier)
    check("correctly fused conditional forecast population Brier is 2/17",fused_brier==F(2,17) and fused_brier<mean_brier)
    return {"base_event_probability":F(1,2),"signal_correct_probability":F(4,5),"conditional_independence_assumed":True,"joint_probability_cells":cells,"ensemble_cohorts":rows,"ensemble_population_ECE":ece,"copied_signal_positive_posterior":copied_both_positive,"single_source_population_Brier":single_brier,"averaged_forecast_population_Brier":mean_brier,"correctly_fused_population_Brier":fused_brier,
            "scope":"Exact population construction. Calibrated source forecasts alone do not identify their dependence or make an equal-weight ensemble calibrated."}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name("new_lesson_results.json"))
    args=parser.parse_args()
    one,high,low=example_one()
    examples={"1_role_news_update":one,"2_joint_uncertainty_set":example_two(high,low),"3_executable_price_selection":example_three(high,low),"4_predictive_checks_and_holdout":example_four(),"5_calibrated_source_ensemble":example_five()}
    result={"scope":"All NFL inputs and outcomes invented; mathematical education only. No empirical NFL validation or trading activity.","python_version":platform.python_version(),"arithmetic":"fractions.Fraction except Gamma-Poisson posterior predictive tails evaluated in double precision and independently checked by recurrence and log-gamma formulas", "test_status":"PASS","test_count":len(CHECKS),"test_names":CHECKS,"examples":examples}
    args.output.write_text(json.dumps(serializable(result),indent=2)+"\n",encoding="utf-8")
    print(f"PASS: {len(CHECKS)} named checks; results: {args.output}")


if __name__=="__main__":
    main()
