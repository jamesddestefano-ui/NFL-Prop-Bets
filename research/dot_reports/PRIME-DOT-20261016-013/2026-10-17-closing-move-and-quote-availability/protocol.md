# Proposed closing-move and checkpoint-availability protocol

Research design for task013, not an installed collector, authorized API purchase, new poll schedule or replacement for the October 18 pilot. **ANALYST OPINION / MODEL ASSUMPTION:** the numerical design choices below require prospective review and freeze; they are not validated defaults. Preserve the existing [pilot plan](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/b0c61f91b3b6bfa15bb724d24c3e3e8cafe7829a/research/pilots/2026-10-18/PLAN.md).

## 1. Define the observable universe before scoring

Use a dated manifest of eligible game/player/market/threshold contracts, source order, reference-book panel, rule basis, filters and attempt budget, frozen before either model's verdict. Retain every screened contract and every failed source attempt. The v2 goal is at least 30 screened contracts if observable, not 30 bets; a smaller genuine cohort is preferable to invented additions. Exclude a game from a pregame cohort if its freeze occurs after actual kickoff.

For this first measurement subset, use standard full-game integer-stat props at half-integer thresholds, with the evaluated initial side priced from −150 through +150 inclusive, matching binary settlement and separately documented eligibility voids. This price restriction defines the study subset, not a new betting gate. Integer-threshold/push, early-win/early-exit, boosts, pick'em and parlay contracts remain separate until their outcome vectors and price basis are explicitly implemented. Exclusion is a research-design choice, not a blanket claim those markets cannot be evaluated.

Use one canonical orientation (Over) per economic contract for probability-movement analysis. An Under is its complement only where settlement permits; do not count both as independent successes. Candidate offers from different books stay separate observations nested within the same economic contract/game. Freeze one entry snapshot per contract for the primary endpoint; later forecast revisions form separate cohorts, never overwrite the original.

## 2. Separate clocks and freeze the forecast

Required times: source publication/update, request start, completed receipt, durable recording, model input cutoff, forecast recording, decision/freeze, requested checkpoint, actual checkpoint and actual kickoff. The last completed receipt, not request start, determines whether an observation is pregame. A publisher's market-level update may not be an individual price-change time; preserve its scope rather than relabel it.

Illustrative strict quality choices to review before capture: source age ≤120 seconds at freeze; opposing-side source-time skew ≤5 seconds; receipt-to-freeze lag ≤30 seconds. Unknown source time fails this strict subset while remaining in the attempt log; this does not override PRIME's broader handling of an authentic timestamped screenshot. A missed or delayed checkpoint is recorded at its actual time, never backdated.

Lock ChatGPT and Claude forecasts independently before sharing their outputs. Record prompts, model/version if known, all input sources, their market visibility and overlaps. Independence means separate output procedures, not statistically independent information. No external model call or fabricated forecast is authorized by this protocol. Missing Claude remains null. No hindsight substitution of a later answer, article revision or injury report.

## 3. Freeze entry and closing references

Let M be the entry benchmark and C the close benchmark for exactly the same threshold, orientation and settlement basis. De-vig each same-book complementary pair separately; then take a predeclared equal-weight median across a fixed eligible reference panel. Never combine one book's Over with another book's Under into a fictional two-sided pair.

Primary diagnostic excludes the candidate execution book from that panel at both times. Its available membership must be identical for M and C, with at least two named reference books in this proposed subset. If this cannot be formed, record the missing reference rather than select a more favorable panel after seeing the close. Book count is not source independence. Retain a prespecified full-panel sensitivity result separately, without promoting whichever looks better.

Define C as the latest qualifying completed, active, same-contract reference capture strictly before actual kickoff and strictly later than the frozen entry/forecast decision, with source age and kickoff lag reported. An older pregame observation cannot be reused as a subsequent close. Proposed maximum kickoff lag is 5 minutes; do not call a12:30 capture the close merely because a12:55 attempt failed. If the entry threshold is unavailable at close, matched PRICE_CLV/movement is missing. Preserve changed lines separately; no unvalidated interpolation or probability transfer. Publication timing alone does not prove a price was executable.

## 4. Baselines, estimands and held-out comparison

On the probability scale, compare each locked model A with:

- **B0 no change:** M.
- **B1 fixed momentum:** clip(M + (M−M_previous), 0, 1), using a predeclared earlier capture at approximately 10 minutes before entry, within ±1 minute and the same panel. No earlier matched capture means B1 unavailable, not zero momentum.
- **B2 fixed mean reversion:** 0.50 for this standard near-even-price contract subset. This is deliberately simple, not a claim every prop is50%. A learned market-type mean or momentum coefficient belongs to a separate earlier-week-trained version, locked before later-week evaluation.

Record A−M and C−M, but raw correlation and a positive regression slope are diagnostic secondary summaries. Primary per-contract difference is D=(B−C)²−(A−C)², where positive favors A. This is squared-error prediction of a market estimate, not a proper binary-outcome score. Score price movement separately from threshold movement and from eventual football outcomes.

The confirmatory primary cohort is the common set with both model forecasts, all three baselines and the matched close present. Report its size and coverage before scores; if empty, the confirmatory comparison is unavailable. Pair-specific available-case comparisons may be reported as supplementary descriptive results, with each distinct eligibility mask disclosed; they cannot establish an all-universe or common-cohort superiority claim. Also report each model's forecast coverage over the entire frozen universe. Do not compare different missingness-selected subsets as if paired. Optionally precommit a complete operational pipeline with a market fallback for missing forecasts; its performance answers a different question and must have its own label.

**Validation schedule:** Sunday is an operations pilot only. Before a later multiweek evaluation, lock training weeks, test weeks, minimum relevant effect and endpoint family. All learned baseline coefficients, reference weights, calibrators and feature choices use earlier training data, with time-appropriate out-of-sample training predictions where needed. Later data are assessment only. Include a no-news-change stratum and a new-news stratum descriptively, using immutable publication and observed times. Future news is not an entry covariate, and excluding losses after seeing later news is forbidden. This is predictive evaluation, not a causal estimate of whose information moved the market.

**Paired uncertainty:** primary target is the equal-game mean of within-game mean D. Preserve all rows from a game together when estimating uncertainty. Report game count, week count, effective weight concentration and contract counts. If residuals may depend across games within a week, include whole-week resampling/sensitivity while retaining the same equal-game target; do not silently switch to equal-week weighting. Repeated players across weeks and common market/provider shocks may require longer blocks or a different clustering structure. A handful of weeks cannot justify asymptotic certainty.

**Success/failure criteria proposed for future preregistration:** choose δ = 0.0001 in squared-probability-loss units as an illustrative minimum improvement, not a profit equivalent. For two models × three baselines, report six paired intervals with familywise error addressed, e.g. Bonferroni two-sided 99.1667% individual intervals for a 95% six-comparison family, using a justified cluster-aware method. Continue to label Sunday descriptive; no automatic p-value after 200/300 rows. A lower bound aboveδ supports that model/baseline *close-prediction* comparison on the covered cohort; an upper bound belowδ rules out that chosen improvement at the interval's stated assumptions; an interval crossingδ is inconclusive. To call a model incrementally better than all baselines, every required comparison must meet the criterion, without post-hoc switching. Width, missingness or dependence invalidating the interval makes the result inconclusive. This is not a stake or adoption rule.

Later official outcomes form a distinct endpoint: for settled no-push, action-eligible contracts, preserve frozen conditional forecast basis and compute paired Brier/log loss where defined. Report voids and unresolved grading separately. If unconditional win/loss/push/void vectors are forecast, use appropriate multicategory scores. Never grade a void as an ordinary loss or compare conditional and unconditional probabilities without conversion. Task011 owns the broader four-forecaster outcome study; this task specifies the boundary, not its completion.

## 5. Checkpoint availability, not invented continuous survival

Predeclare requested delays +2,+5,+15,+60 **minutes** from the completed initial capture, with a proposed ±15 second observation window. This document does not schedule requests or authorize spending. At each actually observed checkpoint retain:

1. Exact-contract source quote present/absent/unknown.
2. Composite original-or-better opportunity availability for the chosen side: yes when the exact contract is confirmed present at decimal price at least the initial price; no when it is confidently absent or confirmed present at worse odds; unknown when source coverage or price cannot establish the answer. A known absence is not an invented worse price. Report price quality conditional on presence only as a separate endpoint with its smaller denominator.
3. Direct jurisdiction-specific active display evidence if independently available; otherwise unknown.
4. Source health/status: complete/partial/error/denied/market suspended, plus changed price/line and the actual time.

A failed request is unknown. A known source outage is not a book suspension. A disappeared threshold is a known absence only if the source coverage is sufficient to establish it; it is never a fabricated worse offer. Report original eligible denominator, number at risk before kickoff, known yes/no, unknown, late observations and reasons at each checkpoint. A delay extending beyond kickoff is administratively ineligible for that pregame endpoint, explicitly counted rather than treated as survival failure.

For each eligible checkpoint cohort of N with K known successes and U unknowns, report [K/N,(K+U)/N], plus K/(N−U) clearly labeled observed-case availability. These finite-cohort bounds assume the known classifications are correct, not random missingness. No independent-censoring or population-coverage claim follows. Reappearance means checkpoint presence cannot establish uninterrupted availability or locate a first loss between the last positive and first negative poll. If a quote lifetime is defined from confirmed-active entry t0, a later absence at U can support the coarser first-loss interval (t0,U]; it does not tighten the lower endpoint to a later active poll. Any first-failure analysis must separately justify its event-history, censoring and observation assumptions. No accepted fill or capacity is inferred anywhere.

## 6. Minimal append-only field groups and fail conditions

| Group | Required fields / event semantics |
|---|---|
| Identity | manifest_id, contract_id, event/player IDs and alias-map version, stat, threshold, comparator/side, period/overtime, book, jurisdiction, settlement-rule version/hash, source URL/artifact digest |
| Observation | request_start, receipt_complete, source_update and its scope, recorded_at, active/suspended/unknown, exact raw odds and decimal price, paired-side IDs/skew, provenance kind, all missing reasons |
| Forecast | model/prompt/data versions, input cutoff, output_recorded_at, decision_at, probability basis and win/loss/push/void vector if available, raw original output, source-overlap tags, unavailable reason |
| Evaluation | frozen baseline version, reference panel and de-vig method, exact close observation IDs, kickoff/lag, paired mask, loss definition, contract/game/week cluster IDs, official outcome/rule evidence, grading revisions |
| Recheck | requested/actual delay, eligibility before kickoff, quote/price-or-better classifications, source-health state, absence versus unknown reason, no presumed fill |

Fail the measurement test if any included entry uses a future input, post-decision forecast, post-kickoff receipt, mismatched contract, invented opposite side, selected close/panel, backdated recheck or undocumented after-the-fact exclusion. Preserve the failed row and why. If forecast/close panels are unavailable, publish the coverage failure rather than a superiority estimate. These checks test a measurement design; they do not prove a production system implements it.
