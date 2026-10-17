# PRIME two-snapshot coverage review — October 17, 2026

**Classification:** Source-verified offline structural comparison; **no confirmed profitable or executable EV**.

## Evidence and scope
Private `jamesddestefano-ui/-NFL-Prop-Odds-Data` immutable audits for capture runs `20261017T142736310677Z` and `20261017T152003815605Z`. Latest audit commit `58be06859e3382ef47bd892f84f35879ae17ad41` read from GitHub main on October 17. Earlier quality and pair-diagnostic audits were independently read from main in the prior cycle.

Both captures report 2,480 quote observations, 1,178 clean exact two-sided book groups, 124 groups missing an opposite side, and 90.48% pair coverage. Pair diagnostics attribute all 124 missing Under groups specifically to BetRivers `player_receptions` in **each** capture, with zero BetRivers complete `player_receptions` pairs. Receiving-yards (126 clean pairs) and rushing-yards (61 clean pairs) at BetRivers were paired in each capture. This is **repeat observation**, not proof of source-vs-normalization causality or independent statistical replications.

Same-line consensus eligible player markets changed from 158 of 344 to 151 of 347; 186 and 196 respectively lacked three-book same-line modal support. Equal aggregate pair coverage therefore does not imply equal consensus opportunity coverage. Possible explanations include threshold movement and changes to market composition; none is established without contract-level aligned analysis.

## Analytical implications and next falsifiable checks
1. Inspect the **latest run's actual normalization_summary** by book/market/side/result. The source collector contains aggregate unrecognized-side telemetry, but historical cause is unknown until source evidence is checked. Compare BetRivers `player_receptions` accepted Over, accepted Under, invalid Under and unrecognized outcome counts. Do not infer missing raw Under from silence in accepted quotes.
2. Compute same-contract overlap between captures using event, market, normalized player ID, threshold and bookmaker, noting line changes separately. Do not conflate changed thresholds with missing prices or infer a causal price movement from provider `last_update` alone.
3. Audit code and synthetic regressions for receipt-before-kickoff and exact-market contract integrity before downstream probability scoring. Retain missingness as a covariate and monitor independently by book/prop type across prospective snapshots.
4. Do not impute any BetRivers Under, reconstruct historical raw payloads, edit immutable captures, or promote leave-one-out deviations to positive EV.

## Controls
Separate 8 AM education / 2 PM testing / 8 PM critical-review assignments. No wagers, spending, prospective locks, historical ledgers, or model gates were altered. The original price source was not independently verified executable in New Jersey.
