# PRIME NFL prop EV session debrief

## Bottom line

PRIME's current rules already contain the right core discipline: verify the exact contract and price, build a defensible probability, require positive conservative EV, and preserve outcomes separately from process. This session's useful contribution is to make those requirements testable. It does not establish a profitable NFL model or justify new wagers.

The highest-priority clarification is the probability basis for push-capable markets. An unconditional win probability, a conditional-on-no-push probability, and a conservative scenario endpoint answer different questions. Mixing them can reverse an EV calculation or make a calibration chart misleading.

The next priority is evidence quality. A bounded ledger audit found malformed CSV record widths and missing evaluation outcomes in the inspected decision rows. Those issues must be resolved before a reliable automated historical comparison. A reproducible scenario calculation is still an assumption-driven stress test; it cannot fill that evidence gap.

Several agreeing sources may share the same upstream information. Good full-sample calibration may not survive the subset selected as bets. A closing benchmark must be fixed before seeing whether it favors the recommendation.

## Session record and scope

- Date: October 11, 2026, America/New_York; EDT is UTC minus four hours.
- Prepared for the requested 5 PM EDT debrief.
- Source review: October 11, 19:55–20:00 UTC (15:55–16:00 EDT); supplementary bibliographic checks 20:06–20:07 UTC. Earlier work remains separately dated in the prior reports.
- Follow-on calculations, repository audit, synthesis and review: approximately 20:00–20:19 UTC (16:00–16:19 EDT). Work was text/transcript review and calculation, not continuous video playback.
- This record finalized: October 11, 2026, 20:19 UTC (16:19 EDT).
- Material reviewed: creator transcripts, accessible primary technical sources, repository governance, prior educational records, and explicitly hypothetical calculations. Source-by-source access is recorded in [the evidence register](source-register.md).
- Video playback: no continuous viewing or complete one-hour playback is claimed. Transcript access and video metadata are separate observations.
- New empirical NFL model validation: none. No historical backtest, source profitability ranking, live executable quote, or current player recommendation was produced.
- Governance baseline read: main at `36bcb5eab6fdad040dddcc0214c7897657db5249`. See [preservation and review status](#preservation-and-review-status).

This is a follow-on to [the first education report](../2026-10-11-positive-ev-video-lessons.md). A separate [earlier research record](../../ev_education/2026-10-11_first_youtube_ev_study.md) was already present when this report was assembled; it remains preserved as a separately authored source rather than being represented as work newly performed here.

## Evidence language

**Verified mathematical principle** means an identity or counterexample under stated assumptions. **Empirical evidence** means an observed source or repository record, with its scope identified. **Model assumption** means a supplied probability, distribution, dependence structure or benchmark choice. **Analyst opinion** is a source's interpretation. **Untested hypothesis** is a proposed improvement awaiting prospective or held-out evidence. Mathematical correctness does not validate the input probabilities.

## What the additional source review contributed

- [Circles Off's Pizzola–Strober interview](https://www.betstamp.com/education/the-secrets-to-becoming-a-successful-sports-betting-trader) motivates careful contract identity, adverse-selection and calibration checks. Its commentary is practitioner opinion, not audited NFL-prop evidence.
- [Buchdahl's closing-market study](https://football-data.co.uk/blog/steamers_drifters_revisited.php) is an author-reported soccer study. It motivates testing each reference on its actual sample; it does not establish NFL-prop market efficiency.
- [RotoWire's Peabody interview](https://www.rotowire.com/football/article/beating-the-book-qa-with-rufus-peabody-40172) motivates testing incremental model information. Its historical blend weights should not be transplanted into player props.

Publication dates, access methods, transcript timestamps, commercial relationships and technical references are in the [source register](source-register.md). Additional [original counterexamples](educator-counterexamples.md) cover selected-subset calibration, non-identification of true probability from two prices, and cross-threshold coherence.

## Six challenges and what would resolve them

### 1 Keep push probabilities on a consistent basis

**Verified mathematical principle.** With stake-refunded pushes, unit-stake expected ROI is `p_win × d + p_push − 1`, where decimal odds `d` include returned stake. If `q = p_win / (1 − p_push)`, the same ROI is `(1 − p_push) × (q × d − 1)`.

In a hypothetical integer-line fixture, `p_win = .50`, `p_loss = .40`, `p_push = .10`, and −110 gives +5.45% ROI. Treating `.50` as a no-push binary probability gives −4.55%. The incorrect calculation silently turns a push into a loss.

Two complementary same-line prices, de-vigged under a margin-allocation assumption, provide a conditional-on-no-push benchmark. They do not identify push mass. Compare conditional probabilities with conditional benchmarks, or explicitly model all three outcomes. For scoring, either use the full win/loss/push vector under a stated multiclass scoring convention, or score correctly conditioned win forecasts among non-push settlements and evaluate push forecasts on the full eligible cohort. Push calibration cannot be measured on a sample from which pushes were removed. Contractual voids and parlay leg-removal rules need their own handling.

**METHODOLOGY_CHALLENGE.** Existing binary EV and Brier statements need a contract-basis clarification for integer lines. This report proposes it for review; it changes no controlling file. Resolution: deterministic fixtures plus a prespecified settlement/scoring convention.

### 2 A scenario envelope is not a calibrated uncertainty bound

**Verified mathematical principle and model assumption.** Two equally weighted probability scenarios `.53/.57` and `.49/.61` both average to `.55`. At −110 both give +5% average EV. The one-bet predictive win-indicator variance is `.55 × .45 = .2475` in both cases. Wider uncertainty about the probability does not mechanically lower mean EV or raise that single-indicator variance when its mean is unchanged.

A separate worst-scenario policy gives +1.18% EV at `.53` and −6.45% at `.49`. These minima describe the supplied scenarios only. They are neither 95% confidence limits nor coverage-validated downside estimates. Preserve the scenario definition, weights if any, omitted risks, and how the endpoint was chosen. Keep the central predictive probability distinct from the conservative decision input.

**MODEL_UNCERTAINTY.** Resolution: justify and evaluate the uncertainty procedure out of time. Missing uncertainty evidence should remain missing, rather than be replaced by an unexplained precise haircut.

### 3 Check calibration over the full range and the selected bet subset

**Verified mathematical principle.** Brier score is a proper probability score, but lower Brier alone does not isolate calibration: it also rewards resolution. In the synthetic appendix, model B lowers Brier from `.25` to `.17` while worsening the reliability component from `0` to `.01`.

**Untested hypothesis.** PRIME should retain every eligible precommitted forecast, cover the full 0–100% range, and show denominators for each prespecified market, probability bin and selection group. Its current 50%+ buckets omit lower-probability events such as some touchdown and parlay forecasts. A model can be calibrated in aggregate while miscalibrated among the opportunities chosen for apparent edge. Report all eligible forecasts alongside the predeclared selected subset, passes and missed recommendations; distinguish these research panels from actual user bets.

Deduplicate exact repeated records and prespecify the primary forecasting checkpoint. Retain genuine alternate-line contracts, accounting for their dependence rather than treating them as independent games. Do not drop unfavorable injury results after seeing them. Apply contractual void and outcome-eligibility rules declared in advance, with injury-tagged sensitivity results separately.

**METHODOLOGY_CHALLENGE.** Resolution: chronological train/calibration/test separation, frozen selection rules, paired market-baseline comparison, counts, missingness and cluster-aware uncertainty. This session runs no such NFL validation.

### 4 Agreement and line movement can share one cause

**Empirical evidence.** The first report's four Unabated transcripts were one commercial source cluster, not four independent confirmations. More sources add viewpoints; they do not automatically create independent predictive evidence.

**Model assumption and analyst opinion.** A multi-book median limits an isolated outlier's influence, but copied prices can move together. Likewise, multiple analysts can repeat one projection or injury thesis. Track original discovery, upstream model, reposts and affiliation separately. Unknown provenance means unknown independence. A market-only explanation remains credible when an internal forecast exaggerates opportunity or underestimates uncertainty.

**UNVERIFIED_CLAIM.** Resolution: a provenance-aware, timestamped source panel with complete misses and source-tip outcomes. Book weights learned from later consensus measure agreement with that market; they do not independently establish true-probability accuracy. Freeze weights using past data and compare forecasts with held-out settlements as well as later prices. Leave-execution-book-out and shared-source-cluster checks are sensitivity analyses, not automatically superior references. Commercial performance claims and repeated lessons do not demonstrate durable NFL skill.

### 5 Fix the CLV comparison before outcomes are known

**Untested hypothesis.** Prespecify a reference-book panel, cutoff relative to scheduled and actual kickoff, quote freshness, settlement matching, fallback order and missing-data policy. Preserve book-level data and the requested bet contract. A benchmark selected afterward because it makes the entry look good is not a neutral process measure.

Keep signed line movement and same-threshold price movement separate. A threshold move cannot become price-equivalent CLV without a defensible distribution or alternate-line ladder linking the contracts. Report a fixed common-book panel separately from an available-book sensitivity panel when coverage changes. A missing close is unmeasured, never zero. Tag post-entry news rather than rewriting entry assumptions with hindsight.

**Original hypothetical counterexample.** Book probabilities never move: A=.50, B=.54, C=.56, D=.60. Entry coverage A/B/C has median .54; closing coverage B/C/D has median .56. The apparent two-point movement comes entirely from panel composition. Common books B/C show no movement. Report eligible candidates, valid paired closes and missing-close reasons by decision and timing; complete-case CLV describes only the observed subset unless a missingness assumption is justified.

**METHODOLOGY_CHALLENGE.** Resolution: matched entry/close evidence and out-of-time tests of benchmark informativeness. PRIME already treats the close as a benchmark rather than an oracle; this proposal makes that caution measurable.

### 6 Derive play-to boundaries from all applicable gates

**Verified mathematical principle.** For a fixed no-push event, central probability `p_C`, lower scenario `p_L`, edge hurdle `e` and central ROI hurdle `r`, the numerical price constraints are `d ≥ 1/(p_C − e)`, `d ≥ (1 + r)/p_C`, and `d > 1/p_L`, with valid positive denominators. The conservative-EV boundary is strict.

Using exact 4-percentage-point and 5% hurdles only as nominal research fixtures, `p_C=.55` and `p_L=.53` require odds at least decimal `1.960784314`, equivalent to American −104.081633. Whole-number −104 passes the three numerical checks; −105 does not. At −110, central ROI is 5%, but central probability edge is only 2.619 points. These fixtures do not silently turn the framework's approximate starting gates into hardcoded policy.

For pushes, evaluate complete win/push scenario pairs. At decimal 1.85, the hypothetical pair `(.50 win, .10 push)` gives +2.50% ROI, while `(.51 win, .05 push)` gives −0.65%. Choosing only the lowest unconditional win probability would select the wrong adverse case. A proposed conditional-edge extension and full derivation are in [the combined-gate supplement](combined-gates.md).

All market-quality, news and exposure conditions still apply. Recompute if the line changes. A joint-probability model and actual combined payout are required for parlay EV; a story about positive correlation alone is insufficient.

**METHODOLOGY_CHALLENGE.** Resolution: deterministic contract and quote-rounding fixtures, followed by a review-only forward evaluation. Passing illustrative arithmetic does not itself produce a BET.

## What the calculations establish

See [the full probability appendix](probability-appendix.md), [the standard-library calculation script](verify_examples.py), and [the calculation results](results.json).

| Hypothetical demonstration | Result | Meaning |
|---|---|---|
| Same receiving-yards mean and median of 60 | Over 49.5 probabilities .60 versus .51; ROI at −110 +14.55% versus −2.64% | Mean and median together still do not determine a tail probability |
| Eight fixed targets versus equally likely four/twelve targets, catch chance .65 | Same expected receptions 5.2; Over 4.5 probabilities .706399 versus .487246 | Replacing random opportunity by its mean can reverse EV |
| Shared catch-rate beta mixture | More dispersion lowers one threshold probability but raises a farther tail | Extra variance is not a universal reason to favor an Over |
| Same-game QB and WR events | A specified script mixture gives joint probability .37; ROI +11% at +200 but −7.5% at +150 | Dependence and the combined payout both matter |
| Binary versus push-aware calculation | −4.55% versus +5.45% on the same supplied outcome probabilities | Probability basis and settlement are essential |

All inputs above are invented. Exact-arithmetic assertions passed. Independent SciPy distribution checks agreed within `1e−12`; the reported maximum PMF difference was `1.11e−16`. [Combined-gate calculations](combined_gate_checks.py) also passed their boundary fixtures and 168 direct-versus-inverted formula comparisons; [results](combined_gate_results.json) are preserved. These are calculation checks, not historical validation or tests of a production PRIME decision engine.

## A concrete barrier to historical validation

**Empirical evidence, bounded repository audit.** At pinned commit `36bcb5eab6fdad040dddcc0214c7897657db5249`, strict CSV parsing independently confirmed record/header-width mismatches in 6 of 26 decision-ledger records, 3 of 17 pass-ledger records, and all 5 bet-history records. Some decision rows exhibit field drift; the bet-history mismatches appear to be surplus trailing fields, which does not itself invalidate their settlement facts.

Of the 20 width-consistent decision records, 12 have both inspected probability fields, but none have the outcome, actual-result, Brier, closing-line or closing-odds fields populated. The source-EV ledger is header-only. These observations are limited to the inspected files and pinned version; they are not a claim that no supporting evidence exists elsewhere.

Do not calculate model performance by silently shifting columns, filling missing outcomes or treating repeated quotes as independent trials. Preserve the original bytes; propose repairs with record-level source evidence and a validated schema, then audit joins and denominator eligibility before any backtest. No ledger was repaired or overwritten in this session. Exact files, row evidence, parser method and limitations are in [the data-feasibility audit](data-feasibility-audit.md).

## Test status and review order

1. **Completed illustrative checks:** probability masses, means, variances, exact tails, EV, dependence feasibility, Brier decomposition and push identities in the accompanying script. Keep the fixtures as educational counterexamples.
2. **Previously observed consistency failure, unchanged:** the first report's historical +258 recommendation supplied a 26–29% joint-probability range, implying −6.92% to +3.82% ROI. Its positive-conservative-EV conclusion was not established by those inputs. This was one message-level audit, not current quote verification, placement evidence or a system-wide failure-rate estimate.
3. **Completed bounded data-feasibility audit:** structural CSV and evaluation-field checks identified prerequisites for trustworthy validation. This is a data-quality result, not a forecast-skill result.
4. **Proposed review-only checks:** exhaustive gate boundaries, missing probability, no joint model, rounding, moved thresholds, mismatched push basis and missing market truth. The complete T1 decision-validation suite remains unimplemented.
5. **Proposed NFL tests:** T2 exact-threshold probability models; T3 matched CLV benchmark quality; T4 joint co-hit calibration. Freeze eligible observations and selection before outcomes; retain failed variants. None has demonstrated out-of-sample improvement yet.

## Preservation and review status

Read before drafting: [AGENTS.md](../../../AGENTS.md), [methodology](../../../config/methodology.md), [advanced market learning](../../../config/advanced_market_learning.md), [positive EV framework](../../../config/positive_ev_framework.md), [EV account accountability](../../../config/ev_account_accountability.md), [daily education directive](../../../config/ev_daily_education_directive.md), and [sources](../../../config/sources.md).

All remain controlling. This report and its calculator are research-only proposals and educational examples; they are not installed into the decision workflow. No controlling thresholds, bankroll policy, source authority, production code, bet records or historic results were changed. Earlier reports remain intact. Repository preservation makes the work available for review; it does not establish that another conversation or agent has read or adopted it.
