# PRIME-DOT-20261012-002 — Prospective same-contract de-vig comparison

Research window: October 13, 2026, 12:28–12:35 UTC (08:28–08:35 EDT). Author: Dot. Requested deliverable: a falsifiable experimental protocol and data-availability audit. **Design delivered; empirical NFL experiment has not run.** No live bet, model replacement, new data-collection schedule, ledger repair or private account information is included.

## Answer and three lessons

1. **VERIFIED MATHEMATICAL PRINCIPLE:** two posted prices do not uniquely reveal true outcome probabilities. De-vig methods impose margin-allocation assumptions. Test them on identical observations; never select whichever produces the desired recommendation.
2. **MODEL ASSUMPTION / UNTESTED HYPOTHESIS:** aligned, complementary, executable contracts and precommitted shrinkage may matter more than small differences between de-vig transformations. The study below measures both quote completeness and method differences rather than attributing all errors to the probability formula.
3. **EMPIRICAL REPOSITORY EVIDENCE:** today's five-file hash check matches the October 11 audited bytes. A newer MNF snapshot supplies an arithmetic example, but no quote-level timestamp or internal probability. It cannot be promoted to a live paired efficacy observation. Missingness remains a real prerequisite, not a reason to invent outcomes, closes or fills.

## Sources actually reviewed

- Stephen Clarke, Stephanie Kovalchik, Martin Ingram, *Adjusting Bookmaker’s Odds to Allow for Overround*, published December 25, 2017. Publisher bibliography/abstract reviewed 12:30 UTC: https://www.sciencepg.com/article/10.11648/10026106 . Original author-uploaded full-text extraction reviewed sections 2–5 and appendix, article pp46–49, 12:30–12:31 UTC: https://www.researchgate.net/publication/326510904_Adjusting_Bookmaker%27s_Odds_to_Allow_for_Overround . PDF fetches from publisher and commercial mirror failed; no audiovisual playback or PDF screenshot inspection claimed. The paper supplies proportional, additive and power definitions and binary Shin/additive equivalence. Its empirical domain is ATP bookmaker-average prices plus two racing-tote datasets, not NFL props. Reported table/narrative inconsistencies and absence of NFL validation remain as preserved in the October 11 deep audit. Confidence: high for algebra checked below; low for NFL transfer.
- Gavin C. Cawley and Nicola L. C. Talbot, *On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation*, JMLR11, July2010,2079–2107. Original PDF text, abstract and introduction pp2079–2080 reviewed 12:30 UTC: https://www.jmlr.org/papers/volume11/cawley10a/cawley10a.pdf . This focused revisit supports treating method selection as part of the evaluated procedure. It does not dictate our NFL sampling plan. Full paper was reviewed in Monday's separate education; this pass does not claim a new full-paper review. Confidence: high for methodological warning, empirical NFL effect unknown.
- PRIME governing files and research index read fresh, 12:28–12:30 UTC. Public prior audit: https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/main/research/education/2026-10-11T20-19-00Z-session/data-feasibility-audit.md . Current inspected blob identities in `input-identities.json`. These are observed repository facts, not independently reverified sportsbook records.
- Public October12 MNF archive and its separate no-vig correction read 12:30 UTC: https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/main/intelligence/archive/2026-10-12T19-44-14Z-prime-watch.json and https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/main/intelligence/archive/2026-10-12T19-44-14Z-no-vig-correction.md . The archive reports an article publication time but null quote observation time. Publication/retrieval time is not a sportsbook update time. Later missing checkpoints are not reconstructed here.

All external research here is written original-source material. The companion task003 supplies this cycle's substantial original educational transcript and X-access register. No market quote in this report is independently verified as presently executable.

## Formulas and identifiability

For decimal odds d_i, q_i=1/d_i, S=q_1+q_2. On complementary no-push two-outcome contracts:
- Proportional: p_i=q_i/S.
- Additive: p_i=q_i−(S−1)/2. In the ordinary valid two-price binary domain this remains within [0,1]; the familiar negative-probability problem occurs in broader multi-outcome applications. Binary Shin duplicates additive and is not a fourth independent method in this experiment.
- Power: p_i=q_i^k, with k>0 solving sum(q_i^k)=1; for S>1, k>1. Use bisection, record tolerance and residual.

These outputs are market benchmarks, not proof of the bookmaker's beliefs or true probability. S<1 is flagged separately as an underround/data-quality/market-structure case, not silently pooled with the primary positive-margin panel. Missing one side means no two-way calculation. Reject nonfinite/out-of-range inputs and noncomplementary settlement rules.

**Critical target distinction:** integer thresholds with pushes require a conditional nonpush benchmark unless an independently modeled push mass is available. Nominal half-points are not universally push-free: the statistic's support and settlement rule control. Use task001's contract note before admitting any market. Over/Under labels can conceal special early-settlement terms. An exact pair must be mutually exclusive and exhaustive within the declared action/nonpush population; naming the same book/line is insufficient.

For no-push action: expected ROI=p*d−1. Conditional on action but allowing pushes: ROI=p_win*(d−1)−p_loss. Never compare an unconditional win probability with conditional 1/d without correcting the basis. Keep no-action refunds separate.

## New deterministic sensitivity example (invented NFL receptions contract)

Assume reference raw probabilities .75/.30, same hypothetical half-point reception contract, and a separate offered decimal1.40 price (American−250). No quote is live. Let a hypothetical independent calibrated estimate be .79, market weight .5, and a .02 adverse scenario deduction. These weights/deduction are illustrative assumptions, not fitted parameters or uncertainty coverage guarantees.

| Method | Market p | Blended central p | Conservative p | Edge vs71.4286% | Central ROI | Conservative ROI |
|---|---:|---:|---:|---:|---:|---:|
| Proportional |71.4286%|75.2143%|73.2143%|3.7857pp|5.3000%|2.5000%|
| Additive |72.5000%|75.7500%|73.7500%|4.3214pp|6.0500%|3.2500%|
| Power |73.0822%|76.0411%|74.0411%|4.6125pp|6.4575%|3.6575%|

Only additive/power clear an illustrative strict4pp central-edge gate; all three clear5%central ROI and positive conservative EV. PRIME's existing sensitivity rule calls for downgrade/PASS, not choosing the favorable transformation. All nonnumeric gates remain unverified, so none is a recommendation.

Fair decimal odds from these blended probabilities are 1/p; these are estimates, not offered odds. For a target central edge e=.04, central ROI r=.05 and conservative EV>0, a candidate price must satisfy d≥max[1/(p−e),(1+r)/p] and d>1/p_conservative. This produces a price boundary for this specific contract; a maximum playable threshold cannot be calculated without probabilities at alternative thresholds. Publish that field as unknown, not inherited from a different line.

Important challenge: changing de-vig alone cannot change ROI if PRIME keeps the same independent p and the same offered d. Here a flip occurs because the market is an explicit shrinkage input. A study that silently changes the raw model, weights and odds at the same time cannot isolate a de-vig effect.

## Proposed prospective protocol, version1 (not installed)

### Phase0: feasibility and frozen manifest

Before collecting a confirmatory sample, approve a manifest specifying one market class: full-game NFL receptions at half-integer thresholds, overtime included, standard action and final-stat grading, no promotions/early-win terms. Exclude contracts that fail complementarity even if their label matches. Keep rushing/pass/yardage/TD expansions separate prospective amendments.

Select and name the reference books and their jurisdictions before collection; do not invent accessible feeds or assume book access. Preserve official rules URL/version/hash. Define candidate universe as every available eligible player-contract on the chosen books at one daily scheduled checkpoint, including PASS. If no licensed/exportable timestamped quote source is available, feasibility remains BLOCKED for collection; no additional polling authorization is inferred from this design.

Proposed primary freshness rules: both sides updated within60seconds of capture and within30seconds of each other, same book. Multi-book reference timestamps within60seconds. These are conservative design choices to assess in a pilot, not empirically proven safe intervals. Quotes predating material news are rejected for a post-news decision even within this clock window; capture both sides anew. Record suspension, unavailable markets and failed captures, rather than carrying forward stale numbers. Record sensitivity panels at15/30/120seconds descriptively without cherry-picking the best interval.

Freeze one primary observation per game/player/stat/threshold at the checkpoint. Related thresholds/players in the same game remain dependent. Store every discovery and rejection with reason; do not create extra independent samples from repeat snapshots. A fixed reference-book panel defines the benchmark; offered/execution book is excluded from its own reference panel where possible, with fallback recorded and analyzed separately.

Pilot duration: two NFL weeks after data access/manifest approval, operational only. Publish denominator of all attempted pairs, structural validity, timestamp completeness, complementary-rule eligibility, paired outcome availability and missing-close rates. Suggested readiness gate: ≥95% valid identity/rule fields and ≥90% timestamp-qualified pairs; these are proposed engineering tolerances, not evidence of profitability. Failure means revise collection and start a new pilot, not erase invalid attempts.

### Phase1: paired forecast comparison

Prespecify proportional as baseline, power as primary challenger, additive as secondary. Compare all on the exact same eligible observations without target-odds/fair-probability adjustments chosen after results. Primary outcome: paired Brier difference (power minus proportional), with Brier=(p−y)^2 and y=1 for Over. Do not score both complementary sides as independent rows. Secondary: log loss, calibration plots with counts, signed residuals and performance by prespecified odds range, book and week. These are forecast tests, not profit tests.

Use a fixed chronological development block to choose any model calibration, blending weights and scenario construction, then a sealed later evaluation block. Freeze transformations and parameter selection procedure before observing that block. Never train at t with outcomes only known after t. If models update, replay the entire update rule walk-forward and retain model hashes. Game/week cluster dependence and repeated-player dependence must be reported; use paired week-block bootstrap where enough blocks exist, plus game-cluster sensitivity. Few weeks cannot support tight asymptotic significance claims.

Precision planning: estimate variance of the *paired score difference* and clustering from pilot/development, choose a practical improvement threshold before lock (proposal .001 Brier), compute required independent-block precision by simulation preserving cluster sizes, and register a fixed end date/sample target. Do not infer N from win-rate SE or pretend thousands of correlated snapshots are independent. If feasible calendar size cannot resolve .001, state the design is underpowered and retain the baseline; do not repeatedly inspect and extend until significance.

Decision criterion proposal: accept power **for further testing only** if the predeclared paired confidence interval lies below−.001, data-quality gates hold, and no prespecified subgroup shows a material documented failure. If interval excludes an improvement that large, reject a claim of material superiority for this domain. If it overlaps, INCONCLUSIVE. Multiple secondary claims require adjusted inference or exploratory labels. A source paper favoring power elsewhere cannot substitute for this endpoint.

### Phase2: conservative EV policy, separate endpoint

Freeze the independent raw model, calibration and shrinkage procedure. Compute each method's p_market, p_raw, p_internal and scenario-bound p_conservative separately. Log both positive and negative EV and every gate failure. Standard numeric gates remain PRIME's existing policy; no proposed change is adopted here. Forecast-skill gains need not improve decision-policy returns.

Shadow decisions only, with no actual bets. After qualifying quote capture, reverify the chosen price at a fixed recorded execution-latency checkpoint using an authorized source. Missing executable evidence means no verified fill; report hypothetical available-at-capture and verified-at-latency cohorts separately. No assumed stake, capacity or execution. Outcome assessment is flat one-unit research arithmetic and is not the user's P/L. Include pushes/voids per frozen rules. Record dollar-capacity data only if authorized; no private limit/account data belongs in public reports.

Primary policy endpoint proposal: paired difference in net research return per eligible opportunity, with zero exposure for policy PASS; also report ROI per unit risked, selection rate and exposure by game/thesis. Different policies choose different bet subsets, so comparing only both-bet cases is insufficient. Preserve all eligibility/selection records. Block uncertainty intervals and downside/exposure distributions matter; a positive small-sample ROI alone fails promotion.

For CLV, preserve line movement and price movement separately. Use prespecified final unsuspended pre-kickoff quote no older than5minutes; absent exact-contract close => missing. Reprice the original contract only when that precise threshold is observed or a separately validated interpolation model is available. News after entry is tagged; favorable movement is descriptive, not proof of superior private information. No post-kickoff prices or nearest available alternate line silently substituted. Closing panel leave-one-book-out sensitivity tests dependence; close remains a benchmark rather than truth.

## Bounded data-availability audit and weekly continuity

Five files fetched from main at12:30:26UTC exactly match October11 audited blob SHAs (`input-identities.json`): line_history, decision_ledger, pass_ledger, bet_history, ev_source_signals. This establishes unchanged bytes for those files, not completeness of all archives. The prior audit's six/five/three width anomalies therefore persist; no new diagnosis or repair performed. The existing56 line-history rows have23 recorded two-sided same-threshold pairs but no guaranteed source-update/close/action-rule provenance. The source ledger remains header-only. Existing priors do not support a fresh source ROI ranking, probability calibration claim or method efficacy test.

The public October12 archive records Kincaid4.5 Over−111/Under−120, but quote time is unknown and the sportsbook number is article-reported. Calculation: (111/211)/[(111/211)+(120/220)]=49.0952955%, rounded49.10%; the separate correction already fixes the original49.61%. This report verifies arithmetic, does not issue another correction, and does not turn an archived article price into an executable snapshot. That archive's absent internal fair probability prevents model-vs-market Brier; missing matched closing data prevents CLV. PASS_AFTER_MOVE is a preserved research decision, not an actual ticket or proof of profitable discipline.

Weekly synthesis: Sunday's injury-contingent role/forecast case studies and Monday's selection-procedure study remain hypotheses and observations. Tuesday adds an explicit prospective design and source-data prerequisites. Original forecasts, failed examples and correction records remain unchanged. No aggregate Week5 betting P/L, calibrated win rate, source winner or empirical model improvement can responsibly be claimed from this inspected panel.

## Test and adoption status

`verify_protocol.py` and `test-results.json` contain deterministic synthetic checks: method normalization/symmetry, zero-margin/equal-price behavior, archived correction arithmetic, gate sensitivity, invariant EV with fixed independent p, and rejected mismatched/stale/future/one-sided pairs. Independent review identified that an initial fixed power-search bound could fail extreme valid inputs; dynamic bracketing and a .999/.999 regression were added. All62 final named checks passed. Tests exercise a research fixture only, not production ingestion, legal settlement implementation or observed NFL performance.

PRIME assumptions challenged: power universally preferred; latest capture equals fresh quote; same market label implies same settlement; missing closes are random; more repeated snapshots mean larger independent sample; conservative scenario is a calibrated lower confidence bound. Each requires evidence above. Proposed improvements remain review-only. Task deliverable can be COMPLETE as a protocol; the experiment itself is PROPOSED and its substantive outcome is unknown.
