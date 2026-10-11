# PRIME positive EV education and validation report

- Research date: 2026-10-11
- Record prepared at: 2026-10-11 15:53 EDT (19:53 UTC)
- Source retrieval window: 2026-10-11 15:48–15:52 EDT (19:48–19:52 UTC); bounded X scan at 15:51 EDT
- Scope: NFL player props only
- Status: educational research and review proposals; no live recommendation
- Repository baseline reviewed: `6afdb3b123e372882ce1bd8fbcf684b0a091fe92` on `main`; AGENTS and the daily education directive re-read after their update, and the five prior config files plus two inspected ledgers confirmed unchanged by blob SHA
- Research cycle: 1
- Methodology changes implemented: none
- Tests performed: arithmetic consistency checks and limited repository evidence inspection
- Forward tests performed: none

## Conclusion

PRIME already contains the central lessons in the material reviewed: exact line and price, conservative expected value, uncertainty, distribution-based probabilities, market comparison, correlation, and separate calibration and CLV review. The strongest next step is to make those requirements reproducible and checkable in each decision. This report proposes tests for review; it does not replace the existing rules or establish that any new method is profitable.

A historical recommendation provides a concrete consistency failure. Its stated joint probability range of 26–29% at +258 implies expected ROI from −6.92% to +3.82%. The lower end fails PRIME's existing positive-conservative-EV gate. A small stake cannot change the sign of expected ROI. This is an audit of the earlier message's own inputs, not verification of a current sportsbook quote or proof that a bet was placed.

## Evidence labels

- **VERIFIED MATHEMATICAL PRINCIPLE**: an identity or deduction under explicit assumptions. This does not verify the input probability.
- **EMPIRICAL EVIDENCE**: an observed record or measured result with its scope and sample disclosed. A small audit does not establish general performance.
- **MODEL ASSUMPTION**: an unobserved quantity or modeling choice required to calculate a result.
- **ANALYST OPINION**: a practitioner's interpretation or recommendation, including commercial claims.
- **UNTESTED HYPOTHESIS**: a proposition to evaluate prospectively or out of sample.

These educational labels supplement the repository taxonomy. Mathematical identities and directly observed records may be `confirmed_fact` within their stated scope; estimated probabilities remain `model_projection`; practitioner views remain `analyst_opinion`; unvalidated predictions remain `speculation`. None of the labels upgrades an unverified price into market truth.

## Source register and access limitations

Four creator-published transcripts were reviewed. They all come from Jack Andrews / Unabated, one commercial provider selling betting tools. They are one source cluster, not four independent confirmations. Embedded YouTube links were verified through the publisher pages. Video playback was unavailable; this report does not claim the videos were watched.

Original YouTube upload dates and video timestamps were unavailable or unverified for every video. Publisher transcript/index dates below are identified separately; index dates were checked on the [official video library](https://www.unabated.com/content/videos). No audited NFL player-prop performance dataset accompanied these lessons.

### S1 Profitable Prop Betting In 3 Easy Steps

- Creator: Jack Andrews / Unabated
- Video: https://www.youtube.com/watch?v=oD4_mcRuHe4
- Reviewed transcript: https://unabated.com/post/profitable-prop-betting-in-3-easy-steps
- Publisher page date: 2026-07-29
- Original video upload date: unavailable
- Video timestamps: unavailable
- Relevant transcript sections: Know Your Means and Medians; The Step-By-Step Process; Tighten Up Your Prop Betting Edges
- Source classification: `analyst_opinion`; commercial education, not verified performance

Three key lessons:
1. A mean projection does not determine the chance of clearing a threshold. **VERIFIED MATHEMATICAL PRINCIPLE**
2. Projection reliability and distribution assumptions drive the apparent edge. **MODEL ASSUMPTION**
3. Compare the exact available prices after modeling the outcome distribution. **ANALYST OPINION**

Correction: the creator's mean-to-median framing is incomplete. Even a median does not price an arbitrary threshold; simulation is one approach, not a mathematical requirement. A sportsbook line need not equal the true median, especially with asymmetric prices. The source's preference for projections over market-derived estimates is practitioner opinion and does not override PRIME's market comparison and shrinkage rules. Confidence is high in the mathematical distinction, low in any untested profitability claim.

### S2 You're Using Closing Line Value Wrong

- Creator: Jack Andrews / Unabated
- Video: https://www.youtube.com/watch?v=MIkpsiJzbcA
- Reviewed transcript: https://www.unabated.com/content/videos/you-re-using-closing-line-value-wrong
- Publisher video-library index date: 2026-07-30
- Original video upload date: unavailable
- Video timestamps: unavailable
- Relevant transcript sections: CLV Test Two; CLV Test Three; CLV Signal
- Source classification: `analyst_opinion`

Three key lessons:
1. Using the close as fair value assumes informative price discovery. **MODEL ASSUMPTION**
2. Liability, follower activity, and thin markets may weaken the interpretation of price movement. **ANALYST OPINION**
3. Investigate why a line moved and assess other process evidence alongside CLV. **ANALYST OPINION**

Limitation: categorical claims that prop markets lack useful sharp information are not established by a dataset in this source. PRIME already treats the close as a benchmark rather than an oracle; this lesson supports testing benchmark reliability, not abandoning CLV. Confidence is moderate in the caution and low in universal claims about all NFL prop markets.

### S3 When You Should Increase Your Bet

- Creator: Jack Andrews / Unabated
- Video: https://www.youtube.com/watch?v=M2ZN_PoFNXg
- Reviewed transcript: https://www.unabated.com/content/videos/when-you-should-increase-your-bet
- Publisher video-library index date: 2026-07-30
- Original video upload date: unavailable
- Video timestamps: unavailable
- Relevant transcript sections: How to Size Your Bets; Knowing Your Sports Betting Edge; The Hybrid Betting Method
- Source classification: `analyst_opinion`

Three key lessons:
1. Kelly calculations depend on payout and the probability supplied. **VERIFIED MATHEMATICAL PRINCIPLE**
2. Overestimating probability can produce excessive sizing. **MODEL ASSUMPTION** about probability accuracy, with a mathematical risk mechanism
3. Conservative sizing is preferable to increasing stakes in response to wins or losses. **ANALYST OPINION**

The transcript contains apparent numerical/transcription errors, so its worked numbers are not reproduced as verified examples. Fractional Kelly is not a guarantee of safety and cannot establish positive EV. PRIME's existing small-unit and exposure controls remain in force. Confidence is high in the algebra and conditional nature of Kelly, not in an untested stake recommendation.

### S4 Betting The NFL Are You Placing The Right Wagers

- Published title: Betting The NFL: Are You Placing The Right Wagers?
- Creator: Jack Andrews / Unabated
- Video: https://www.youtube.com/watch?v=NIRT6F6q_uo
- Reviewed transcript: https://unabated.com/content/videos/are-you-placing-the-right-wagers-when-betting-the-nfl
- Publisher video-library index date: 2026-07-19
- Original video upload date: unavailable
- Video timestamps: unavailable
- Relevant transcript sections: Straight Player Props; Line Shopping
- Source classification: `analyst_opinion`

Three key lessons:
1. For the same contract and stake, better decimal odds improve the winning payoff and EV. **VERIFIED MATHEMATICAL PRINCIPLE**
2. Assess the joint probability and payout before combining correlated props. **MODEL ASSUMPTION** for the joint probability; mathematical pricing requirement
3. News-driven workload changes should be translated into prop opportunity. **ANALYST OPINION**

The creator's preference for straight props does not prove that every parlay is negative EV. Other sports, sides, totals, teasers, and account-expansion suggestions are outside this record. Confidence is high in same-contract price comparison and low in broad commercial performance claims.

### S5 Independent technical reference for exact thresholds

- Creator: SciPy community
- Title: scipy.stats.binom
- URL: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html
- Access: official technical documentation, reviewed as text; not a video
- Publication date: unavailable; retrieved 2026-10-11
- Relevant section: Notes and survival-function documentation; video timestamps not applicable
- **VERIFIED MATHEMATICAL PRINCIPLE:** the binomial PMF and survival function provide a reproducible threshold calculation.
- **MODEL ASSUMPTION:** fixed targets and equal independent catch probabilities are modeling choices, not verified NFL conditions. This source validates the calculation, not NFL profitability.

### S6 Independent technical reference for calibration

- Creator: scikit-learn developers
- Title: 1.16. Probability calibration
- URL: https://scikit-learn.org/stable/modules/calibration.html
- Access: official technical documentation, reviewed as text; not a video
- Publication date: unavailable; retrieved 2026-10-11
- Relevant sections: introductory scoring-rule note, Calibration curves, Calibrating a classifier; video timestamps not applicable
- **VERIFIED MATHEMATICAL PRINCIPLE:** Brier score combines reliability, resolution, and outcome uncertainty; lower Brier alone does not prove better calibration.
- **ANALYST OPINION:** use reliability bins/counts alongside Brier and separate model-fitting, calibration, and final-test data. This is general methodological support, not an NFL model-validation result.

### Bounded X and analyst discovery scan

At 2026-10-11 15:51 EDT, a bounded search checked recent methodological material associated with @RufusPeabody, @robpizzola, @capjack2000, @PlusEVAnalytics, and @4for4_John, including last-90-day searches. Direct profile opens did not yield readable post content. The accessible [Rob Pizzola profile metadata](https://x.com/robpizzola/with_replies) did not supply an original methodological post.

**UNVERIFIED_CLAIM:** no current original X lesson could be verified in this scan. This is an access/evidence limitation, not a finding that no relevant posts exist. No claim of reading their feeds, no source signal row, and no source-performance ranking follows. Mirrors, promotional picks, undated snippets, and unrelated examples were excluded. The substantial educational work for this cycle is the four transcripts and two technical references above.

## Three lessons to apply to PRIME

The calculations and proposed designs below are this report's independent mathematical analysis and operational synthesis. Hypothetical values are illustrative, not current lines or estimated probabilities for named players.

### 1 Price uncertainty before choosing a stake

**VERIFIED MATHEMATICAL PRINCIPLE.** For a binary win/loss wager with decimal odds d, unit stake, and win probability p:

```text
EV per unit = p × (d − 1) − (1 − p) = p × d − 1
break_even_probability = 1 / d
expected_profit = stake × EV
```

At hypothetical −110, d = 1.90909091 and break-even = 52.38095%. A model probability of 55% produces +5.00% expected ROI, while a conservative probability of 52% produces −0.72727%. The 55% and 52% inputs are **MODEL ASSUMPTIONS**, not verified forecasts.

**VERIFIED MATHEMATICAL PRINCIPLE.** Multiplying a negative EV by a smaller positive stake reduces expected monetary loss but leaves expected ROI negative. Bankroll control comes after the value gate.

For a no-push binary contract, the unconstrained single-bet Kelly reference is:

```text
b = d − 1
f_star = (p × b − (1 − p)) / b = (p × d − 1) / (d − 1)
```

A nonpositive value implies no positive allocation under that simplified model. Positive Kelly depends on the model probability being appropriate; it is not permission to place a wager. Simultaneous correlated positions require portfolio treatment. This report does not select a bankroll, unit amount, or new sizing policy.

**NFL application.** A WR receiving-yards idea with uncertain route share should be evaluated across plausible role scenarios before it is described as playable. The adverse plausible probability, current executable payout, injury dependencies, and shared game exposure determine whether the existing PRIME gate can pass.

**Difference from PRIME.** None in the principle. The proposed improvement is a deterministic consistency check that prevents a narrative recommendation from contradicting the reported probability range.

### 2 Model the exact contract and disclose what the market estimate assumes

**VERIFIED MATHEMATICAL PRINCIPLE.** Receptions Over 4.5 requires P(R ≥ 5), not E[R] > 4.5. Receiving yards 53+ requires P(Y ≥ 53), while Over 53.5 requires P(Y ≥ 54) for integer yardage. These are different contracts. An integer line can also have a push, which changes expected-value calculation.

For a unit stake with win, loss, and stake-refunded push probabilities:

```text
p_win + p_loss + p_push = 1
EV = p_win × (d − 1) − p_loss
   = p_win × d + p_push − 1
```

Using p_win × d − 1 while ignoring a possible push understates EV. Voids, partial settlements, and parlay leg-removal rules must be handled under the relevant contract rather than assumed identical.

**VERIFIED MATHEMATICAL PRINCIPLE.** A hypothetical fixed six targets with independent catch chance c = 0.65 gives:

```text
P(R ≥ 5) = 6 × 0.65^5 × 0.35 + 0.65^6 = 0.319079921875
```

That is 31.90799% for Over 4.5 receptions under the stated model, independently recalculated from the [binomial formula](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html). Fixed target count and independent, identical catch probability are **MODEL ASSUMPTIONS**. A realistic alternative would integrate over uncertain target scenarios and test calibration.

**MODEL ASSUMPTION.** A Poisson reception count assumes equal mean and variance; a negative-binomial model permits overdispersion but adds parameters. Either may miss target competition, zero/low-route outcomes, game-script mixtures, and injury risk. There is no evidence here that one model is best for PRIME. Start from opportunity and role, document the distribution, and test it.

**VERIFIED MATHEMATICAL PRINCIPLE.** Multiplicative de-vig normalization is a calculation, not proof of the true probability. For hypothetical same-book, same-time Over −120 / Under +110 at one threshold:

```text
q_over = 120 / 220 = 0.54545455
q_under = 100 / 210 = 0.47619048
p_market_over = q_over / (q_over + q_under) = 0.53389831
```

Treating 53.38983% as a fair market benchmark is a **MODEL ASSUMPTION** about margin allocation and information quality. Mixing opposite prices across books or thresholds invalidates this paired-market interpretation. A median of books can reduce outlier influence but does not make copied prices independent evidence.

**VERIFIED MATHEMATICAL PRINCIPLE.** For two parlay events, P(A and B) = P(A) × P(B given A). Replacing the conditional probability with P(B) requires independence. Same-game QB and receiver overs may share game script, but a correlation story alone does not quantify the joint probability. No defensible joint model means no defensible numerical SGP EV.

**Difference from PRIME.** The exact-threshold, matched-market, shrinkage, and correlation requirements are already present. Proposed improvement: preserve an auditable probability calculation and joint-model basis beside the existing decision record.

### 3 Validate probability quality and benchmark quality without hindsight

**VERIFIED MATHEMATICAL PRINCIPLE.** Binary Brier score is (p − y)², where y is 1 for a win and 0 for a loss. Its expected value under true probability q is (p − q)² + q(1 − q), so it is minimized at p = q. A single win or loss cannot establish calibration. Lower Brier alone also need not mean improved reliability, so report probability-bin counts and observed-versus-predicted rates alongside it, as the [calibration documentation](https://scikit-learn.org/stable/modules/calibration.html) explains. For push-capable markets, prespecify three-outcome scoring or correctly conditioned no-push probabilities; do not silently evaluate an unconditional win probability on a filtered sample.

**MODEL ASSUMPTION.** Closing consensus may approximate fair probability when matching contracts, timestamps, and settlement rules are available. It remains an imperfect benchmark. A five-yard move cannot be converted into a percentage EV improvement without a distribution linking those thresholds.

**ANALYST OPINION.** PRIME should continue examining CLV, calibration, and realized outcomes together under the existing framework. Report line CLV and same-threshold price CLV separately, with missingness. Do not select a favorable closing book retrospectively or manufacture combined CLV when the mapping is unavailable.

**NFL application.** Freeze each forecast before kickoff; preserve injury/role assumptions and all qualifying observations, including serious passes and missed bets. Define outcome eligibility before seeing the result. Unexpected injuries are useful diagnostic tags, but removing unfavorable settled results after the fact can bias calibration. Contractual voids and pushes need their own prespecified handling.

**Difference from PRIME.** The framework already calls for out-of-sample calibration, source accountability, and preserved history. The proposed improvement is a test protocol that makes benchmark selection, missing-data handling, and exclusions explicit before evaluation.

## Evidence inspected in PRIME

### Historical recommendation consistency case

**EMPIRICAL EVIDENCE.** The [historical message at 2026-10-11 16:22:36 UTC](https://chatgpt.com/c/6ac02c17-11f4-83ea-9092-6f746e247e4a?messageId=d8f9a9df-3e4c-4cc6-8b9b-a6a34d47ec2e) described Jameson Williams 53+ receiving yards plus DeMario Douglas 3+ receptions at +258, supplied a 26–29% joint probability range, and called the parlay playable at a small stake.

The surrounding user attachment contents were unavailable to this review. The named legs and price are historical claims in the assistant message, not independently verified sportsbook truth. No current availability, actual placement, settlement, or result is inferred. The 26–29% span is an informal sensitivity range; no reproducible method makes it a statistical confidence interval.

**VERIFIED MATHEMATICAL PRINCIPLE.** Using only that message's own probability range and payout:

| Calculation | Value |
|---|---:|
| Decimal odds | 3.58 |
| Break-even probability | 27.93296% |
| EV at 26% | −6.92% |
| EV at 29% | +3.82% |
| Probability needed for +5% expected ROI | 29.32961% |

**ANALYST OPINION.** The claimed positive conservative edge was not established. On the supplied range, the prior playable conclusion was inconsistent with PRIME's conservative-EV principle. This conclusion does not validate the range itself. The +5% row is a comparison with PRIME's standard-market starting gate, not a new universal parlay threshold. The negative lower-bound EV alone is enough to identify the inconsistency.

Test result: **FAIL**, for arithmetic-to-decision consistency in this one historical example. Preserve the original message and this finding; do not overwrite history or infer the wager's eventual result.

### Limited ledger observations

**EMPIRICAL EVIDENCE.** At the repository baseline:
- [data/ev_source_signals.csv](../../data/ev_source_signals.csv) contained a header and zero data rows. This file cannot yet support an analyst ranking or source edge claim; the observation is limited to this file.
- [data/weekly_attribution.csv](../../data/weekly_attribution.csv) contained one Week 2 review. Its closing-price/CLV fields were blank, and its notes explicitly stated that closing lines and prices were unavailable. No missing close was inferred.
- The Week 2 review also recorded exclusion of a Dart probability from calibration after an injury. This is a reason to review prespecified eligibility and injury sensitivity, not enough evidence to diagnose the entire model or retroactively change ledger treatment.

This was not a complete audit of all ledgers or source history. No new ROI, CLV, win-rate, source ranking, or model-performance claim is made.

## Independent challenges to PRIME

| Classification | Challenge | Evidence needed to resolve |
|---|---|---|
| METHODOLOGY_CHALLENGE | The historical +258 playable conclusion contradicts its own adverse-case EV | Reproducible probability range and recalculated decision using the original exact contract; preserve the original record |
| MODEL_UNCERTAINTY | Narrative opportunity and a mean do not establish a tail or joint probability | Versioned distribution, role scenarios, data cutoff, dependence assumptions, held-out validation |
| UNVERIFIED_CLAIM | Commercial lessons and repeated social claims do not establish profitable NFL forecasting | Independent timestamped forecasts, available prices, complete outcomes, source provenance and uncertainty |
| METHODOLOGY_CHALLENGE | Outcome-driven injury exclusions can distort calibration | Prespecified eligibility, contractual settlement rules, and an all-eligible versus injury-tagged sensitivity review |

No live DATA_CONFLICT or PRICE_CONFLICT was established in this cycle. A credible market-only baseline can be right when the independent model overstates opportunity, underestimates variance, or uses stale role assumptions. Each test below must retain this competing explanation.

## Proposed tests for review

All proposals below are **UNTESTED HYPOTHESES** except the completed arithmetic consistency case above. No test runner, new monitor, schema change, or controlling-methodology edit was installed.

### T1 Enforce arithmetic consistency before actionable language

- **Hypothesis:** a reproducible check will reduce recommendations whose stated uncertainty fails the existing EV gate.
- **Mechanism:** calculate break-even, central EV, and adverse-case EV from the exact contract before deriving a decision label.
- **Evidence:** the one +258 historical inconsistency; this establishes an existence case, not a frequency estimate.
- **Testing:** use a review-only suite of synthetic cases covering positive and negative American odds, zero/negative conservative EV, pushes, missing probability, moved thresholds, and joint-probability absence. Compare expected labels with the existing rules. Then evaluate prospectively without changing live decisions automatically.
- **Failure criteria:** any actionable label despite a failed mandatory gate; unhandled settlement rules; or a calculation that silently substitutes unavailable inputs. Lower-bound probabilities with no evidentiary basis do not make the test pass.
- **Implementation for review:** a validation checklist or later reviewed calculation helper; preserve inputs, output, and failure reason. Code or configuration changes require a separate reviewed proposal.
- **Current result:** the historical fixture fails; the full suite and forward test are not run.

### T2 Compare reproducible exact-threshold models out of time

- **Hypothesis:** explicit opportunity-based distributions improve held-out probability quality relative to a timestamp-matched, de-vigged market baseline.
- **Mechanism:** make route/target/carry assumptions, dispersion, and role uncertainty measurable; fit the raw model on training data and fit calibration/shrinkage choices on a separate calibration set, with the final test set untouched.
- **Evidence:** mathematical need for a distribution; existing PRIME controls. No NFL out-of-sample benefit was demonstrated in this cycle.
- **Testing:** define eligible NFL prop types and a chronological train/calibration/test split before fitting. Freeze model versions, inputs, timestamps, thresholds, raw probabilities, shrinkage, and conservative ranges. Compare paired Brier scores, calibration with bin counts and uncertainty, expected versus realized ROI, and matched CLV; disclose availability and missingness.
- **Failure criteria:** leakage from post-forecast news or closing prices into entry forecasts; no held-out improvement; unstable calibration by role/market; or apparent gains that vanish after realistic available prices and uncertainty.
- **Implementation for review:** a research-only evaluation specification first. Prespecify sample-size or precision targets from outcome variation and clustering by game/week and repeated player or alternate-line observations; do not claim significance from an arbitrary handful of bets. Retain rejected model variants and their versioned results.
- **Current result:** not run.

### T3 Measure whether each CLV benchmark is informative

- **Hypothesis:** timestamp-aligned, same-contract closing consensus is a more reliable process benchmark than whichever closing price is easiest to retrieve.
- **Mechanism:** reduce stale-quote, threshold, settlement-rule, and retrospective selection mismatch.
- **Evidence:** PRIME's blank Week 2 CLV fields and its existing benchmark caution; the source transcript supplies practitioner reasoning, not an NFL validation sample.
- **Testing:** prespecify the reference-book set, closing-window convention, minimum quote evidence, and treatment of late news and missing data. Preserve book-level close and entry quotes; analyze line and price CLV separately by prop type and timing. Test association with held-out calibration and outcomes without claiming causation.
- **Failure criteria:** ambiguous quote times, unverified closes, mismatched thresholds, hindsight-selected books, high missingness that changes conclusions, or no stable relationship to probability quality. A missing close is an unmeasured result, not zero CLV.
- **Implementation for review:** add an educational research worksheet using existing evidence where possible; propose any permanent ledger fields separately.
- **Current result:** not run; available sample does not establish benchmark reliability.

### T4 Require a joint-probability basis for quantified parlay EV

- **Hypothesis:** a frozen joint distribution reduces false precision when multiple NFL props share a game or opportunity thesis.
- **Mechanism:** represent shared game script, player usage, and scenario dependence rather than multiplying marginal probabilities by default.
- **Evidence:** conditional-probability identity; PRIME's existing parlay and exposure rules. The +258 range had no reproducible joint calculation in the inspected message.
- **Testing:** freeze joint simulations or another transparent joint model, marginal probabilities, dependence assumptions, and combined payout before outcomes. Evaluate held-out co-hit calibration against an independence baseline and keep all joint and leg-level results separate from placed straight bets.
- **Failure criteria:** double counting related source evidence, leakage, poor co-hit calibration, unsupported dependence parameters, or an EV result that changes sign across reasonable dependence scenarios.
- **Implementation for review:** mark numerical joint EV unavailable when the joint basis is missing. Preserve the idea for research without promoting it to a BET from narrative confidence.
- **Current result:** not run.

## Confidence and additional evidence needed

- **High confidence:** odds conversion, EV, push-aware EV, exact-threshold distinction, conditional probability, the Brier identity, and the +258 arithmetic.
- **High confidence within limited scope:** the contents of the inspected historical message and two ledger files at the recorded baseline.
- **Moderate confidence:** the proposed audit and validation designs are appropriate ways to test PRIME's existing principles.
- **Low confidence:** any claim that these lessons generate profitable NFL bets, that a particular prop model is superior, that one close is universally efficient, or that a source has durable predictive skill.
- **Not established:** calibrated probabilities for the historical legs; current executable odds; actual wager placement; measured benefits of any proposed test.

Additional evidence needed:
1. Independent, transparent NFL prop studies or datasets rather than repeated material from one commercial provider.
2. Timestamped executable quotes with exact thresholds, both sides where available, and settlement rules.
3. Reproducible opportunity-model inputs, distributions, uncertainty ranges, and joint-probability assumptions.
4. Frozen forecasts, source independence clusters, complete eligible outcomes, pushes/voids, and prespecified exclusions.
5. Matched closing quotes, missingness rates, adequate independent observations, and out-of-sample confidence intervals.
6. Original video upload metadata and timestamps if a future report needs video-level citations; they remain unavailable here.

## Governance and preservation

The following were read before this file was created:
- [AGENTS.md](../../AGENTS.md)
- [Methodology](../../config/methodology.md)
- [Advanced market learning](../../config/advanced_market_learning.md)
- [Positive EV framework](../../config/positive_ev_framework.md)
- [EV account accountability](../../config/ev_account_accountability.md)
- [Preferred research sources](../../config/sources.md)
- [Daily EV education and independent challenge directive](../../config/ev_daily_education_directive.md)

Those files remain controlling. This report introduces no replacement threshold, bankroll rule, reference-book authority, source endorsement, or live bet classification. It makes no change to existing ledgers or historical records. Failed tests and original assumptions should remain preserved alongside later results; new evidence may revise conclusions through a clearly dated follow-on research record.
