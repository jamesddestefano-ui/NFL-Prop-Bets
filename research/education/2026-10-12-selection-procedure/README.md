# PRIME EV EDUCATION REPORT — Selection is part of the model

Research window: 2026-10-12 09:19–09:23 EDT (13:19–13:23 UTC); prior-work reconciliation at 09:24 EDT. Public NFL-player-prop education only. Prepared for repository handoff; no claim of downstream adoption. No live quote, wager, source-profit ranking or production repair.

## Relationship to prior research

This is a deeper numerical demonstration and experiment-manifest operationalization of existing lessons, not discovery of a new conceptual safeguard. The October 11 [source register](../2026-10-11-advanced-ev-session/source-register.md) already discussed Vehtari selection optimism and nested evaluation. The [test proposals](../2026-10-11-advanced-ev-session/test-proposals.md), Common design items 2–5 and protocol D, already froze selection within training, required untouched outer tests, and distinguished repeated quotes from independent outcomes. Today adds an original JMLR reading, an exact 100-search null example, a duplication-variance calculation and concrete manifest/label-availability fixtures. It does not establish that the prior safeguards were absent or that PRIME violated them.

## Three lessons

1. **VERIFIED MATHEMATICAL PRINCIPLE:** searching many noisy backtests can produce a spectacular winner even when every candidate has negative true betting EV. Record the search, not just its winner.
2. **MODEL ASSUMPTION / proposed evaluation design:** the object to validate is the complete selection-and-decision procedure, including calibration, analyst choice, thresholds and exclusions. Chronology alone does not protect a holdout repeatedly consulted to make those choices.
3. **VERIFIED MATHEMATICAL PRINCIPLE:** repeated offers on one settled player outcome are not additional independent outcomes. Count contracts and underlying player-games separately; dependence can make row-based precision misleading.

## Original educational sources actually reviewed

### S1 — substantive technical article
Gavin C. Cawley and Nicola L. C. Talbot, *On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation*. JMLR 11, pp.2079–2107, published July 2010 (exact day unavailable). [Original PDF](https://jmlr.csail.mit.edu/papers/volume11/cawley10a/cawley10a.pdf). Retrieved 2026-10-12 13:19–13:20 UTC. Medium: accessible PDF text, focused substantive review of introduction, benchmark setup, selection-overfitting discussion, evaluation protocols and conclusion (printed pp.2079–2083,2091–2096,2099–2103); not all equations or references reviewed. Video timestamps: not applicable; no playback.

The authors demonstrate that tuning against a noisy validation criterion can overfit that criterion. Their empirical illustrations use synthetic and thirteen classification benchmarks, not NFL props. Selection performed outside the evaluation folds can leave information from nominal test cases inside the tuned procedure. They argue for evaluating selection together with fitting. **EMPIRICAL EVIDENCE:** benchmark-specific evidence supports the methodological hazard; it does not quantify PRIME's bias or establish an NFL edge. Access/attribution confidence: high. Methodological transfer confidence: high; NFL effect-size confidence: unestablished.

### S2 — original teaching chapter
Rob J. Hyndman and George Athanasopoulos, *Forecasting: Principles and Practice*, third edition, §5.10 Time series cross-validation. Book dated May 2021; online landing page reports update October 11,2026; section-specific revision time unavailable. [Reviewed chapter](https://otexts.com/fpp3/toolbox.html), [metadata](https://otexts.com/fpp3/). Retrieved 2026-10-12 13:20 UTC. Medium: original written teaching, §5.10 text and code inspected; code not executed. No video reviewed; timestamps not applicable.

Rolling-origin evaluation constructs each forecast from earlier observations and can match the intended forecast horizon. In PRIME, a Tuesday forecast and a Sunday-inactives forecast therefore need different as-of information cutoffs. **MODEL ASSUMPTION:** NFL grouping and the nested schedule below are this report's proposed application, not a validated result from the textbook. Access and general-method confidence: high; NFL profitability evidence: none.

### X access scan
At 13:19–13:20 UTC, public original-profile opens for [UnabatedSports](https://x.com/UnabatedSports), [RyanJ_Heath](https://x.com/RyanJ_Heath), [The_Oddsmaker](https://x.com/The_Oddsmaker), and [dwainmcfarland](https://x.com/dwainmcfarland) returned retrieval errors. Bounded indexed searches for current NFL/model/utilization material returned no relevant original post whose content and current timestamp could be verified. Search output included unrelated or old posts; these were excluded. Thus zero new verified analyst tips, zero independent confirmations, no inferred timestamps, lead time, ROI or executable prices. This is an access-limited scan, not proof no useful posts exist.

## Lesson 1: an impressive selected record can be generated by search

**MODEL ASSUMPTION — invented illustration, not historical NFL results.** Consider 100 independent candidate systems, each tested on 100 independent binary reception-prop outcomes with true hit probability 50%, identical −110 prices, no pushes/voids, one unit per selection. Independence is deliberately idealized: real model variants overlap and NFL outcomes cluster.

**VERIFIED MATHEMATICAL PRINCIPLE — exact binomial calculation:** for one system, X~Binomial(100,0.5). P(X≥60)=0.02844397. Across 100 independent systems, P(max X≥60)=1−[1−P(X≥60)]^100=94.4181%. A 60/100 record shows 14.5455% apparent ROI at−110. The expected best record is 62.4762 wins and 19.2727% apparent ROI, yet any system selected only using these past outcomes still has −4.5455% expected ROI on a fresh independent outcome under this null model.

The 94.4% is neither a p-value for PRIME nor the likelihood a real analyst is unskilled. Correlated candidates invalidate this numerical independence formula; identical copies reduce to one experiment. The point is to retain every tried model, subset and rule so a selected result is not presented as a precommitted test. More trials do not mechanically tell us how many percentage points to subtract from a real forecast.

**NFL application:** comparing route-share cutoffs, injury replacement filters, TPRR windows, bookmakers, edge gates and X-account subsets all constitutes search if their results influence which rule is selected. A “new edge” obtained by choosing last week's highest-ROI combination is discovery-stage evidence.

## Lesson 2: evaluate an entire time-stamped procedure

**METHODOLOGY_CHALLENGE, not an accusation of a proven current failure.** PRIME already requires chronological holdouts and forbids same-observation recalibration and evaluation (§13 positive_ev_framework). Yesterday's research already specified untouched outer evaluation of the full selection procedure. Today makes that existing instruction concrete with exact failure examples and an experiment manifest: freeze how the winner is selected, and put all tuning inside an earlier development window. A held-out week loses its role as an untouched confirmation sample once it guides redesign.

**UNTESTED HYPOTHESIS — operationalization of existing T2/protocol D (not a competing hypothesis register):** a bounded inner search and fully frozen outer evaluation will produce less optimistic estimates of PRIME's NFL probability improvement than reporting the best reused validation result.

- Mechanism: selection rewards favorable sample noise; it need not reveal persistent bookmaker mispricing. No systematic NFL market edge is claimed.
- Proposed implementation, for review: before the first prospective week, register candidate family, finite parameter grid, primary paired probability metric, eligibility rules, quote-age policy, and all data-release cutoffs. Preserve failed candidates and search count. Store experiment records only in research; controlling rules unchanged.
- At each outer week, use only earlier available data. Within that earlier window, use rolling-origin inner validation to choose opportunity windows/calibration/thresholds. Refit without outer outcomes, seal predictions and version/hash before kickoff, then evaluate the next chronological week once. Report pooled outer results for the predeclared procedure, rather than selecting its best week.
- Outcome-label availability matters: an early kickoff is not an already settled training label for a later overlapping game. Training inputs require source publication/observation times, and labels require actual availability times. Closing odds are an evaluation target, never a Tuesday/Sunday pregame input unless they were already available at that decision time (normally they were not).
- Keep same game and duplicated player-contract rows together in splitting and uncertainty assessment. Team/player persistence across weeks warrants additional dependence sensitivity; grouping by game does not magically remove every correlation.
- Predeclare a calendar review horizon. Do not stop at a winning week; any early modification becomes a new version with a later untouched evaluation window. Nested chronology does not cure missing quotes, small samples, role drift, bad outcomes or repeated human peeking.
- Primary outcome: paired Brier difference versus timestamp-matched no-vig reference on the same eligible contracts, with coverage and calibration. Secondary: exact-contract CLV and hypothetical flat-unit ROI where executable quotes and settlement are verified. Actual placed-bet returns remain separate. A positive Brier gain alone is not proof of a profitable betting subset.
- Invalidation/non-adoption: no stable outer improvement, estimates too imprecise, dependence-sensitive conclusions, inability to reconstruct as-of inputs, or apparent gains lost after quote eligibility. Report inconclusive if evidence is insufficient; don't invent a numeric sample-size guarantee.
- Evidence required: trustworthy historical/prospective snapshots, complete model-search log, archived probabilities, settlements, aligned book pairs and closes, enough distinct weeks/games to estimate variation. Existing ledger issues were not repaired or retested here.

## Lesson 3: row count is not effective evidence count

**MODEL ASSUMPTION:** 20 independent player-game outcomes, each copied into 5 identical price-observation rows, all with the same binary success event. For p=0.5 the actual variance of their mean is0.25/20=0.0125. Treating 100 rows as independent gives0.25/100=0.0025. The naive standard error is too small by a factor √5. This is an exact duplication demonstration, not an estimate of real NFL correlation.

**Proposed test:** preserve all quotes for execution research, but link them to shared event/contract IDs. Report quote rows, unique contracts, player-games, games and weeks. For model comparison, choose an explicit estimand and weight: a contract-weighted forecast score is not the same as a player-game-weighted score. Use paired game/week-aware sensitivity analysis on loss differences, with uncertainty method chosen in advance. Small numbers of clusters and dependence between weeks can still undermine intervals. No specific bootstrap interval was produced in this study.

## Exact-price teaching example

**MODEL ASSUMPTION:** fictional Receiver R receptions O4.5, fictional Book A simultaneously quotes O−110/U−110. All action is assumed settlement-eligible, with no pushes at4.5. These are invented inputs, not an observed sportsbook market.

- Decimal 1.9090909; sportsbook break-even 52.38095%; multiplicative no-vig benchmark 50%.
- Raw model 60%; hypothetical calibrated/shrunk fair 57%; conservative 54%. These numbers are stipulated for arithmetic, not estimated or certified by this study. They must be justified independently in a real case.
- Central probability edge 4.61905 percentage points; fair odds −132.558; conservative fair odds −117.391.
- Central expected ROI 8.81818%; conservative ROI 3.09091%. Versus no-vig benchmark the central difference is 7 points, which is different from price-relative edge.
- For illustrative exact central edge≥4pp, central ROI≥5%, conservative ROI>0, the decimal price must meet all bounds: d≥1.05/.57, d≥1/(.57−.04), d>1/.54. Binding bound 1.88679245 corresponds to maximum negative-odds magnitude 112.76596; at whole American prices −112 passes these numerical gates,−113 fails the edge gate. This does not authorize a BET without verified market and model evidence.
- If O5.5 instead has stipulated fair 49%/conservative 46%, it fails at−110. Maximum playable line is 4.5 **among the two evaluated thresholds at that price**; no claim about unmodeled alternatives.
- Sensitivity: at conservative 52%, ROI becomes −0.72727%, so PASS even with central 57%. The search-bias lesson says not to label 54% “conservative” just because the best backtest suggests 57%; no validated probability interval is available here.
- Classification: educational arithmetic only, no live candidate. Kelly sizing not applicable: no verified edge/bankroll, and research is not permission to stake.

## PRIME handoff and status

Recommended review-only improvement: add a compact experiment manifest covering every model/rule searched, as-of cutoffs, inner/outer split, shared-event units, untouched test status and failed hypotheses. Adopt only after review. No config, authoritative ledger, forecast, result or wager changed.

18 deterministic checks passed in `checks.py`; exact output is `check-results.json`. They verify arithmetic and tiny illustrative time-eligibility fixtures, not a production validator, NFL model calibration or future returns. No empirical NFL backtest completed. No source ROI independently audited. Evidence-confidence: high for the stated mathematical identities; moderate for usefulness of the proposed process change; unestablished for improved NFL betting results. No immediate material correction or actionable price opportunity established, so routine publication should remain quiet.
