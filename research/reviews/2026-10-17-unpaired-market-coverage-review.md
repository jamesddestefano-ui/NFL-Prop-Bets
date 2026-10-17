# PRIME research review — unpaired sportsbook contracts and consensus selection

Date: 2026-10-17. Classification: VERIFIED STRUCTURAL AUDIT + CODE REVIEW; **not evidence of profitable or executable EV**. Separate from the scheduled 14:00 ET testing and 20:00 ET adversarial-review cycles.

## Primary private evidence (do not copy raw licensed quotes)
- Private `jamesddestefano-ui/-NFL-Prop-Odds-Data`, `audits/20261017T142736310677Z-quality.json`, blob `57c4cc58e00e1de9c9e1702655813efd7133221b`, source capture `data/odds_api/runs/20261017T142736310677Z.json`. Recorded: 13 events, 2,480 observations, 1,178 clean two-sided book/market/player/threshold groups, 124 missing-opposite-side groups, zero duplicate-side groups, 90.48% pair coverage, zero post-kickoff observations, review required. The 90.48% denominator is 1,178 + 124 = 1,302 eligible groups, not the number of raw quote records.
- `audits/20261017T142736310677Z-consensus-validation.json`, blob `5f3271cba685523e90bc80341d4a24bade70ad17`: 344 player markets with at least one valid pair, 158 groups meeting modal-line three-book consensus and 186 lacking it; 976 evaluated sides, 15 positive leave-one-out price deviations, largest listed +1.939 pp, none listed at >=4 pp. This is **LOO deviation, not fair-probability or conservative-EV validation**.
- Source inspection of `scripts/diagnose_pairs.py`, blob `8ed48f3611d3a4d88553698ced81af4884a18176`, confirms an existing offline, per-book/market `missing_over`/`missing_under` diagnostic and three-book same-line coverage. Do not create a redundant tool or presume the 124 reflect a specific book without its actual diagnostic output.

## Novel analytical implication
One-sided missingness can select which sportsbooks and thresholds enter the three-book modal-line cohort. As a result, the 158 consensus groups may not represent the full offered market uniformly. Neither the 124 one-sided groups nor the 186 inadequate-consensus player markets automatically imply a collector bug; possible mechanisms include feed availability, selection of player/threshold, bookmaker suspension, and normalization rejection. Distinguish these hypotheses using captured per-book/market diagnostics and provider rejection telemetry before assigning causes. No claim of systematically biased prices is established from aggregate totals.

The existing `diagnose_pairs.py` builds raw side sets and **does not filter post-kickoff rows or quarantine duplicated sides**; its aggregate coverage may differ from stricter consumer eligibility in future snapshots. For comparability, run it on an identical immutable capture and either annotate the differing basis or propose separately versioned, pre-kickoff, duplicate-quarantined diagnostics with regression fixtures. Do not silently revise the existing immutable audit.

## Next falsifiable investigation (private, offline, zero API spend)
1. Read or generate the append-only `20261017T142736310677Z-pair-diagnostics.json` if permitted; tabulate one-sided fractions by book and market, with counts and denominators. Do not claim the file exists until read back.
2. Cross-tab missing Over vs missing Under; compare to collector rejection reason counters without treating rejected input as observed valid prices. Record unknown attribution separately.
3. Test whether excluding one-sided groups materially changes modal-line book composition by market; no interpolation across thresholds. Run on multiple **precommitted** captures rather than picking a favorable snapshot.
4. Extend a *new* regression/diagnostic version to reject at/after-kickoff quotes and quarantine any duplicate-sided exact contract, while preserving immutable source artifacts.
5. Only after source validation, compare candidate opportunity rates between high-coverage and low-coverage strata. Use fixed denominators and prospective held-out data; a correlation is not a betting advantage.

## Controls
No user-confirmed wagers, settled results, source quotes, model gates, prospective freezes or API credentials changed. No live NJ availability, conservative probability, CLV, or profitability established. Existing 08:00 education / 14:00 testing / 20:00 critical-review purposes remain separate.
