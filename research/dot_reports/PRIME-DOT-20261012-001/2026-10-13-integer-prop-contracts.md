# Integer NFL prop contracts: win, loss, push, and the probability basis

Task: PRIME-DOT-20261012-001. Research date: October 13, 2026. Source retrieval: 12:29–12:31 UTC (08:29–08:31 EDT); calculations and report: 12:31–12:35 UTC. Research-only proposal, not a live wager or a controlling-rule change.

## Answer and incremental contribution

For a cash-stake straight prop that refunds the full stake on a push, expected net return per unit originally staked is `p_win × (decimal_odds − 1) − p_loss`, not automatically `p_win × decimal_odds − 1`. The latter is valid only for a binary event with no refund state, or as a conditional return when the probability is explicitly conditional on decisive settlement.

The October 11 [probability appendix](../../education/2026-10-11T20-19-00Z-session/probability-appendix.md) and [combined gates](../../education/2026-10-11T20-19-00Z-session/combined-gates.md) already established the basic identity, conservative-scenario caveat and non-identification of push mass. This assignment extends that work with actual jurisdiction-specific grading rules, half-unit support, noncomplementary settlement, conditional Kelly, score denominators, a proposed contract schema and 29 executable regression checks. It does not claim the original insight is new.

## Source register and access limits

All sources below were accessed through public web text/PDF extraction, not video playback. No YouTube/X content is claimed reviewed for this mathematical assignment; those media belong to the separate educator assignment. No sportsbook account, live quote or historical ticket was accessed. Publication times absent from a source remain unknown; retrieval date is not publication date.

1. **Fanatics Sportsbook, House Rules, Tennessee.** Publication/effective date not located. Retrieved 2026-10-13 approximately 12:30–12:31 UTC; full page opened, focused American-football sections reviewed (defensive props; passing/rushing/receiving; settlement). https://sportsbook.fanatics.com/legal/tn/house-rules/ . Representative official grading evidence: whole-number defensive totals push on equality; sacks can push at a half-unit line; defensive tackle totals exclude special teams. The retrieved page also describes NFL cumulative-yardage Over early-win treatment unaffected by subsequent negative yardage, while Under uses the final box score. That provision means a superficially paired Over/Under need not be complementary. It is Tennessee evidence, not proof of New Jersey terms or any particular ticket. The treatment of an exact integer yardage equality under that early-win wording needs contract-specific confirmation; do not extrapolate the defensive rule to resolve it.
2. **FanDuel, Sportsbook House Rules—New Jersey**, effective July 30, 2026. Retrieved 12:29–12:30 UTC; full page opened, focused American-football propositions and general hierarchy reviewed. https://www.fanduel.com/fanduel-sportsbook-house-rules-nj . Football normally includes overtime; the general player-prop participation provision requires a snap, with market exceptions. Its tackles-plus-assists definition includes defense and special teams. Thus its label cannot be presumed identical to the Fanatics Tennessee label. This is a rule comparison, not a price comparison or a recommended book. Specific-market rules control over general rules; preserve the actual version applicable to the contract.
3. **DraftKings, General Rules / Market Rules.** Publication/effective date unknown. Retrieved 12:29–12:30 UTC. https://sportsbook.draftkings.com/help/general-betting-rules and https://sportsbook.draftkings.com/help/general-betting-rules/market-rules . Search-indexed official text described stake-refunded pushes and parlay exceptions, but direct general-rule retrieval returned a navigation shell and the market-rule page returned HTTP403. These are partial-access leads, not a fully verified contract. They are not relied on to settle any example or ticket.
4. **J. L. Kelly Jr., A New Interpretation of Information Rate**, Bell System Technical Journal, July 1956, pp917–926. Retrieved 12:30 UTC; university-hosted authorized reproduction PDF, focused pp917–920 plus arbitrary-odds context. https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/7/36891/files/2017/07/Kelly1956-1uwz47o.pdf ; publication DOI https://doi.org/10.1002/j.1538-7305.1956.tb03809.x . Primary foundation for maximizing expected logarithmic growth rather than expected wealth alone. The push-state derivation below is this report's application, not a quoted NFL result from Kelly.
5. **Tilmann Gneiting and Adrian E. Raftery, Strictly Proper Scoring Rules, Prediction, and Estimation**, JASA102, March2007, pp359–378. Retrieved 12:29–12:30 UTC; author-hosted PDF, focused §2.3 and §3.1/Example1. https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf . Primary support for categorical probability vectors and proper quadratic scoring, and for comparing scores on matched forecast situations. The settlement-target applications and arithmetic below are original deductions.
6. **Penn State STAT414, Lesson08, Mathematical Expectation.** Publication date unknown. https://online.stat.psu.edu/stat414/Lesson08 . Official indexed result retrieved 12:30 UTC; direct open failed. Definition-level corroboration only, not a claim of full lesson review.

Evidence confidence: high for algebra under the stated payoff assumptions; high for the specifically retrieved rule wording, but limited to source/jurisdiction/version; untested for improvement to NFL forecasting or realized profitability.

## 1. Derive the event and payoff before estimating probability

**VERIFIED MATHEMATICAL PRINCIPLE.** Let `w`, `l`, `t` be unconditional probabilities of a decisive win, decisive loss and threshold push on the declared eligible cohort. They are nonnegative and sum to one. A standard cash stake returns net `b=d−1` on a win, `−1` on a loss and `0` on a push. Therefore:

- `EV = wb − l = wd + t − 1`.
- If `w+l>0`, `q=P(win | win or loss)=w/(1−t)`.
- `EV=(1−t)(qd−1)`.
- Fair decimal price `d_fair=(1−t)/w=1/q`, if `w>0`.
- `1/d` is the conditional break-even probability. The equivalent unconditional win hurdle, given push mass, is `(1−t)/d`.

With refunded contractual voids, use a separate `v` and `w+l+t+v=1`; EV remains `wb−l`, with decisive probability `s=w+l` and `EV=s(qd−1)`. Do not label a did-not-participate void a threshold push. Cashouts, bonus stakes, insurance, early payouts, dead heats and multi-leg tickets require their actual payoff functions; these equations do not silently price them.

**MODEL ASSUMPTION.** For a standard final-count reception Over5, the win event is receptions≥6, equality5 pushes, and ≤4 loses. “5+” with inclusive milestone settlement wins at5; it is not Over5. Over4.5 and Over5.5 cannot push if the official count is integer-valued. Push capability depends on the support of the graded statistic, not whether the displayed line ends in .5. A 1.5-sack total can have equality because sacks can be credited in half units [source1].

## 2. Worked hypothetical receiving contract

Every number here is invented. Assume a final-count cash-stake Over5-receptions contract with w=.46, t=.16, l=.38 and −110 (d=21/11). No claim this price is offered.

- Raw price-implied conditional break-even:52.380952%.
- Model unconditional win:46%; model conditional decisive win:54.761905%.
- Model conditional edge:2.380952 percentage points; unconditional equivalent edge:2.0 points.
- Correct per-original-stake ROI:+3.818182%.
- Wrong binary computation using .46:−12.181818%, understating ROI by exactly16 percentage points.
- Conditional decisive-stake ROI:+4.545455%; reporting that as all-stake ROI overstates this example.
- Fair price:1.826086957, about−121.052632. This is a mathematical break-even boundary, not maximum acceptable juice under PRIME's additional gates.

No opposite price was supplied, so no no-vig market probability is available. With a hypothetical same-book −110/−110 complementary pair, proportional normalization gives conditional market benchmark50%, not unconditional50%; it still cannot identify t. No independently justified conservative probability scenario was supplied for this reception example, so conservative EV and a formal play-to price are unavailable. Its central ROI and conditional edge are below PRIME's nominal5%/4-point gates anyway. There is no BET.

At the same invented price and distribution, Over4.5 ROI is+18.363636%; Over5.5 ROI is−12.181818%. For point mass t at5, moving from Over5.5 to Over5 gains t, while moving Over5 to Over4.5 gains bt. Crossing both half lines gains dt. Do not transfer a probability or CLV conversion across these contracts without the threshold mass.

For a separate conservative-scenario fixture at d=1.85, scenario A(w=.50,t=.10,l=.40) gives+2.5%; scenario B(.51,.05,.44) gives−0.65%. Minimizing unconditional win alone chooses the wrong adverse scenario. Evaluate coherent full scenario vectors. For target all-stake ROI r and a given vector, the price boundary is `d≥(1+r−t)/w`; require strict inequality at r=0 for positive EV. For multiple allowed vectors take the largest required price, alongside every other policy gate. Scenarios are assumptions, not confidence intervals.

## 3. Why two prices may not define one binary benchmark

**VERIFIED MATHEMATICAL PRINCIPLE.** Complementary final-threshold Over/Under prices, normalized under a vig-allocation assumption, identify only a conditional benchmark. Every push mass t<1 paired with w=(1−t)q and l=(1−t)(1−q) has the same fair odds. Identical fair prices can therefore have different per-stake ROI magnitudes and capital-turnover implications.

**EMPIRICAL EVIDENCE / METHODOLOGY_CHALLENGE.** Source1's early-win Over wording is a reason to test complementarity, not assume it. Synthetic yardage path40→51→49 with threshold50.5 can satisfy an early-crossing Over and a final-result Under simultaneously. A complementary two-cell devig calculation is then misspecified. Require a contract rule flag and joint payoff-state model; do not normalize these prices as though both bets refer to disjoint exhaustive decisive states. Applicability must be verified at the actual book/jurisdiction/market. Nothing here implies an executable arbitrage or actual dual payout.

## 4. Kelly is conditional too, but not an automatic stake

**VERIFIED MATHEMATICAL PRINCIPLE.** For one isolated bet with known probabilities, no financing cost and no concurrent exposures, expected logarithmic bankroll growth for stake fraction f is:
`g(f)=w log(1+bf)+l log(1−f)+t log(1)`.
Differentiating gives interior optimum `f*=(bw−l)/(b(w+l))=(bq−(1−q))/b`. Clip to the permitted nonnegative stake interval; when w+l=0 every fraction has zero growth and the formula is undefined, so the practical action is no stake. The reception fixture's full-Kelly reference is5%, not a proposed stake. Refunded voids have the same zero-log payoff but remain separate records.

Holding q fixed, multiplying both decisive probabilities by the same positive factor rescales expected growth without changing the isolated optimizer. That does not imply indifference to time locked up, limits, model uncertainty, simultaneous correlated bets or alternative opportunities. These assumptions fail in portfolios; sum-of-individual Kelly fractions is not portfolio optimization. PRIME's fixed-unit policy, quarter-Kelly upper reference and exposure controls remain unchanged. No bankroll amount is inferred.

## 5. Score the probability actually forecast

**VERIFIED MATHEMATICAL PRINCIPLE / PROPOSAL.** Preserve the central full vector, not just a conservative gate value. Options must be declared before outcomes:

- Full three-class Brier: `sum_k(p_k−1{outcome=k})²` over win/loss/push on the eligible nonvoid cohort. Here the sum convention ranges0–2. A realized push in the reception fixture scores1.0616. A half-scaled convention is also proper, but cannot be mixed without labeling; two-class summed Brier is twice the usual binary Brier.
- Conditional binary Brier: score q on decisive settlements only. Also evaluate push forecasts against the push indicator over the complete eligible cohort. Never score unconditional w against a win fraction after dropping pushes. Publish all denominators and void/missing-outcome counts.
- If forecasting void probability, predefine a four-class target or separate eligibility model; do not turn a missing outcome into a void. Keep settled and revised outcomes with timestamps and grading-source versions.

A smaller Brier is not proof of better calibration alone, and results across different cohorts are not directly comparable. Evaluate reliability/counts and properly scored central forecasts on a chronological holdout with game/player clustering. Do not reclassify an injury loss as a void for model convenience.

## 6. What is confirmed versus only a possible bug

**EMPIRICAL EVIDENCE.** The retrieved controlling positive-EV framework §2 and §15 present binary EV/Kelly formulas without an explicit push-conditioned variable definition. Advanced learning §17 allows pushes to be excluded or handled separately but does not specify the probability transformation. These are documentation/contract-basis gaps, already identified in October11 research, not newly discovered losses.

**UNTESTED HYPOTHESIS.** Potential implementation bugs are (a) treating pushes as losses, (b) conditioning outcomes but not forecasts, (c) inferring no-push from a half line regardless of statistic support, (d) matching different grading contracts, and (e) normalizing a noncomplementary pair. This assignment did not execute PRIME's production calculator or grade its actual tickets. It cannot assert those bugs occurred in production. Existing malformed CSV observations remain a separate, unapproved repair matter.

Proposed additive research schema for PRIME review: `contract_id`, book/jurisdiction, rule URL/effective/retrieved time, `settlement_rule_version`, statistic definition/support, period/overtime, comparator/inclusive flag, eligibility, early-settlement flag, `complementarity_verified`, `probability_basis`, w/l/t/v, conditional q, model/calibration version, quote timestamp, central/per-scenario ROI, `roi_denominator`, score convention/cohort, settlement/source/time and correction-of ID. Null means unknown, not zero. A boolean `push_capable` alone is insufficient.

## 7. Tests, implementation proposal and falsification

Run `python verify_push_contracts.py` in a scratch copy; it writes `test-results.json`. Standard-library Fraction arithmetic verifies29 named fixtures, with a floating-point local expected-log check. All29 passed. During authoring, a hand-entered expected Brier value was wrong; the test failed and the oracle was corrected to the directly summed1.0616 before the successful run. This is a synthetic calculator check, not an NFL backtest or production test suite.

Proposed acceptance sequence:
1. PRIME reviews exact contract and probability-basis definitions before any rule change.
2. A production candidate must reproduce every fixture and reject missing/invalid probability bases and rule mismatches, including half-unit sacks and noncomplementary early-win markets.
3. Freeze a prospective eligible cohort of integer and adjacent half-line props, rules, central predictions, calibration procedure and scoring convention before games. Preserve all forecasts and passes, not just selected wins.
4. Evaluate paired push-aware versus current calculations, audit settlement correctness and compare held-out multiclass/conditional scores. Test whether independently estimated threshold mass improves held-out probabilities and all-stake ROI forecasts, with uncertainty and clustering. Algebraic correction is necessary even if forecast skill does not improve.
5. Reject an empirical improvement claim if it depends on hindsight, changed eligibility, missing closes treated as zero, small selected samples, incompatible contracts or unverified outcomes. Report inconclusive when data is insufficient. No numeric sample size or statistical power claim is fabricated here.

This note answers the mathematical assignment and supplies reproducible tests. It does not demonstrate a profitable strategy. Prior reports, failed hypotheses, controlling methodology and authoritative records remain unchanged. Repository publication must be verified separately by the coordinating publisher before the queue is marked COMPLETE.
