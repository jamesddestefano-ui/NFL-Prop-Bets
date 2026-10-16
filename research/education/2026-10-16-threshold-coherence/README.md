# PRIME EV EDUCATION REPORT — threshold-coherent disagreement
Research window: October 16, 2026, 08:21–08:25 EDT (12:21–12:25 UTC).
Scope: NFL player-prop educational research; review-only proposal. No actual player probability, executable price, wager, backtest, source ranking or adopted rule.

## Three lessons
1. **VERIFIED MATHEMATICAL PRINCIPLE:** probabilities for nested reception outcomes must be ordered. A model cannot assign more probability to six-or-more receptions than five-or-more under the same information, eligibility and settlement basis.
2. **VERIFIED MATHEMATICAL PRINCIPLE:** combining full distributions with shared nonnegative weights summing to one preserves this ordering; choosing weights separately to favor each prop can destroy it. Coherence is necessary, not sufficient for calibrated or profitable forecasts.
3. **UNTESTED HYPOTHESIS:** logging threshold-coherence failures and decision sensitivity before Sunday's pilot is more informative than forcing a preferred projection into a precise probability. Do not learn weights on the same ten contracts used to claim success.

## Source register and substantial learning pass
All access below occurred October 16, 2026, 12:22–12:24 UTC. Video timestamps are not applicable; no video playback or video transcript was reviewed in this pass. A substantial original technical-paper section served as equivalent education.

- Yuling Yao, Aki Vehtari, Daniel Simpson, Andrew Gelman, [Using stacking to average Bayesian predictive distributions](https://arxiv.org/html/1704.02030), original v1 April 6, 2017; reviewed v3 September 16, 2017. Access: original HTML paper, introduction/§1.1–1.3 and §2.1 equations 2.1–2.3 in depth; selected later passages, not a claim to have read every example or reproduced the paper. [Metadata](https://arxiv.org/abs/1704.02030).
  - Method: learn a convex combination of predictive distributions using out-of-sample proper-score objectives rather than merely averaging point estimates.
  - Reasoning: the predictive distribution, not just its mean, is the object that must describe future outcomes. The paper distinguishes its predictive-weight objective from Bayesian posterior model probabilities.
  - Limitation: its examples are not an NFL player-prop validation. Ordinary leave-one-out fitting does not automatically honor football's as-of time structure; the proposed application below uses earlier-only folds. Confidence: high for the described mathematical framework, unestablished for NFL gains.
- Scikit-learn developers, [Probability calibration](https://scikit-learn.org/stable/modules/calibration.html), retrieved documentation labeled 1.9.1; publication/update date absent. Access: official written documentation, calibration definition, reliability-diagram discussion and opening calibration-method section. It explains that Brier loss reflects reliability and resolution together, so a lower total score does not by itself prove better calibration. Confidence: high for this methodological distinction; no software was installed or run.
- San Francisco 49ers / Kyle Shanahan, [October 15 press conference](https://49ers.1rmg.com/transcripts/head-coach-kyle-shanahan-press-conference_10-15-26/). Access: official written transcript, injury opening and receiver-opportunity discussion; clock time absent. [Official depth chart](https://www.49ers.com/team/depth-chart), updated October 13, cross-read. Neither source supplies current route percentages.
- Original-X scan: search for UnabatedSports calibration/player-prop material yielded an out-of-scope historical WNBA self-report and profile/mirror results. Direct [original account replies](https://x.com/UnabatedSports/with_replies) returned an internal retrieval error. No relevant original NFL methodological post or verified before/after quote admitted; mirrors/reposts were not counted as confirmations. Task003 remains NEEDS_MORE_EVIDENCE.
- [Washington official Week 6 injury report](https://www.commanders.com/news/commanders-vs-49ers-week-6-injury-report-2026) appeared in search dated October 15; direct open failed. This source is discovery-only, not an independently read injury table.

## New depth versus existing PRIME work
Read AGENTS, methodology, advanced market learning, positive-EV framework, account accountability, sources, daily education, handoff, append-only task history, education index, October11 advanced ensemble report, and Sunday PLAN. Baseline main: c4aefce51f9a3811798a8c86b780f73079993b72.

Existing work already separates mean from tail probability, model averaging from calibrated aggregation, and training from held-out evaluation. This follow-on adds an explicit **cross-threshold invariant**, a deliberately failing ladder, and a test of whether a repair changes classifications. It does not claim that PRIME currently has this bug. It challenges any future implementation that independently shrinks or calibrates alternate thresholds without checking the joint result.

Queue resolution: 001/002 ACCEPTED_FOR_TEST; 003 NEEDS_MORE_EVIDENCE; 004/005 COMPLETE research deliverables; 006 INCONCLUSIVE actual capture feasibility; 007 REQUESTED pending authorization reconciliation; 008 REQUESTED for Sunday. Today's standalone education does not change those statuses, perform CSV repairs, or pretend Sunday's collection occurred.

## Reproducible hypothetical counterexample
**MODEL ASSUMPTION:** an active fictional receiver's count R has only support 4,5,6. No push/void state exists for the fictional half-point contracts. Model A's masses are (.30,.10,.60); model B's are (.60,.10,.30). These deliberately simple distributions illustrate logic, not realistic fitted NFL tails.

A gives P(R≥5)=.70 and P(R≥6)=.60. B gives .40 and .30.
If an analyst uses A-weight .10 for ≥5 but .90 for ≥6:
- P(R≥5)=.43
- P(R≥6)=.57
- implied P(R=5)=.43−.57=−.14, impossible.

For any count variable, S(k)=P(R≥k) satisfies S(k)≥S(k+1); the difference is P(R=k). For a shared weight w, S_mix(k)=w S_A(k)+(1−w)S_B(k). Its adjacent difference is a nonnegative weighted sum of the component masses. This proves coherence for this operation. Different weights across players/games are permissible; the proof concerns thresholds within one common forecast context.

A shared w=.70 yields S(5)=.61, S(6)=.51, and exactly-five mass .10.
The equal-distance monotone projection of the bad pair (.43,.57) onto a nonincreasing pair is (.50,.50); squared displacement totals .0098. This mathematical repair implies zero mass at exactly five, although both input models allocated .10 there. A visually smoother curve therefore is not necessarily a better football model. Preserve raw values; any repair must be a separately versioned proposal, scored later.

## Exact-price illustration, not a recommendation
**MODEL ASSUMPTION:** Fictional Book A simultaneously quotes Over/Under 4.5 receptions at −110 each. Assume no push or void. Shared w=.70 is an illustrative central weight, not learned or calibrated. Adverse w=.30 is a stress scenario, not a confidence bound.

| Quantity | Value |
|---|---:|
| Offered decimal price | 1.90909091 |
| Sportsbook implied/break-even p | 52.380952% |
| Same-book proportional no-vig p | 50% |
| Raw mixture model p | 61% |
| Calibrated PRIME p | Unavailable |
| Assumption-only conservative p | 49% |
| Central edge versus break-even | +8.619048 percentage points |
| Central difference versus no-vig | +11 percentage points |
| Central expected ROI | +16.454545% |
| Adverse expected ROI | −6.454545% |
| Central fair American odds | −156.410256 |
| Adverse fair American odds | +104.081633 |

EV=p×d−1; fair decimal price=1/p. Equality at a fair price gives zero EV, not a qualifying bet. With the adverse p, positive EV requires a payout better than +104.081633; this does not cure unvalidated probability or role uncertainty. No operational maximum acceptable juice or playable line is established. Within the invented central model and only the two examined lines, 4.5 is the higher qualifying line for positive EV at −110; at 5.5, p=.51 gives −2.636364%. Under the adverse scenario neither examined line clears −110. Never transfer .61 mechanically to the higher threshold.

The central-to-adverse weight change reverses EV, so this example returns **PASS** under the supplied conservative-EV gate. Fractional Kelly cannot repair a negative edge, and no bankroll or stake is supplied.

## Current NFL application: role disagreement is unresolved
**EMPIRICAL EVIDENCE / confirmed_fact about what was said and published:** Shanahan's October15 transcript lists Evans and Samuel out of that day's practice and Kirk limited. It describes Watkins and Cooks gaining opportunities with injured teammates. The October13 depth chart lists Cowing behind Evans and Watkins/Cooks behind Samuel. These sources describe different aspects of role and are not contradictory.

**MODEL ASSUMPTION / MODEL_UNCERTAINTY:** Neither depth-chart position nor a teammate absence determines a particular receiver's routes, TPRR or reception distribution. A future prop model should preserve alternative route-allocation scenarios rather than assign all vacated targets to one player. No Friday final designation, current route share, exact prop price or fair probability was established here. Practice participation is not game clearance; this is a Monday-game research case, not a Sunday locked selection. Quantitative role allocation remains unavailable.

## Falsifiable test proposal for PRIME review
Hypothesis: coherence-aware distribution combination reduces impossible ladders and prevents marginal false-positive decisions without sacrificing later predictive quality.

Mechanism: independently chosen threshold weights can make mutually nested events inconsistent, especially when selecting the most optimistic analyst or calibrator for each line.

1. Preserve each raw model's full PMF/CDF or available thresholds, exact player/game/stat/eligibility, as-of cutoff, source-family ID and weights before outcomes. Missing probabilities remain missing.
2. On the same player/game/context, check [0,1] bounds, adjacent tail ordering, complementary sides on identical contracts, and mass sums only where a full distribution exists. Do not compare different timestamps, participation conditions, void rules or markets as one ladder.
3. Log raw violation size and any proposed repaired output separately. Record all classifications, including unchanged PASS and missing-quote cases. For comparable contracts, compare unrepaired output, fixed common-weight mixture, and separately fitted monotone repair.
4. Sunday is an operational diagnostic only: up to ten contracts cannot establish predictive superiority or fit defensible new source weights. Freeze any illustrative variant before results and label it uncalibrated.
5. For later empirical work, use chronological, game-grouped holdouts; fit weights/calibration/repair only on earlier training folds. Prespecify one primary paired Brier comparison on identical settlement-eligible contracts, plus reliability bins/counts, threshold-specific errors, log loss with documented zero-probability handling, missingness and matched-close coverage. Alternative lines sharing one outcome are clustered, not independent trials.
6. Failure conditions: any supposedly coherent mixture still crosses; improvement exists only on its own fitting sample; apparent gain disappears on the identical covered cohort; repair worsens prespecified held-out scores or high-value-tail reliability. Wide uncertainty means INCONCLUSIVE, not adoption.
7. Proposed acceptance after a separately preregistered adequate study: no logical violations and a paired held-out score improvement whose uncertainty excludes no improvement, without material prespecified calibration/coverage degradation. Choose practical tolerance and sample horizon before fitting; they are not supplied by this small fixture.

## Verification, confidence and missing evidence
[JavaScript verifier](verify_coherence.js) executed in the research JavaScript runtime: **35 synthetic assertions passed**. [Recorded output](coherence_results.json). Checks cover valid masses, ordered tails, the deliberate crossing, complete hypothetical price arithmetic and the two-point projection. They are not production tests or empirical NFL validation.

Confidence: high in algebra and counterexample; moderate in usefulness as an engineering diagnostic; low/unestablished for actual NFL performance benefit. An independent arithmetic review cross-checked the central/adverse example and noted that repair can alter calibration; this caution is retained.

No empirical outcome/forecast pairing, calibration estimate, live price, CLV or ROI was added today. No prior forecasts or failed hypotheses were deleted. Task006's missing admissible quote panel remains open. Educational publication is a repository handoff only, not evidence another ChatGPT hub read or adopted it.
