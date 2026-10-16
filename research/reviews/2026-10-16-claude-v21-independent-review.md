# PRIME independent review of Claude v2.1 research memo
Date: October 16, 2026. Scope: NFL player-prop EV research only. Source: user-pasted Claude report in conversation, NOT independently sourced or verified research by PRIME. No production betting rule changed, no bet placed, no historical tickets edited.

## Supported mathematical findings
- For a binary no-push contract, EV = (p - 1/d)*d. At standard odds a 4 percentage-point edge entails ROI of 0.04*d. V2's gate at +150 (4pp edge, 10% ROI) versus +151 (15% ROI) is discontinuous and not supported by an economic discontinuity. This warrants testing, not an unapproved replacement.
- The sample-size values Claude gives are approximately correct under a simplified independent equal-stake -110 model, SD≈0.955, normal approximation, alpha 5%, 80% power: 5% ROI about 2,250 one-sided or 2,860 two-sided; 3% ROI about 6,260 or 7,950. Values are planning illustrations, not guaranteed power in correlated changing-odds NFL props. Earlier ~1,450 is a two-standard-error point-estimate illustration, not 80% power.
- Different distributions with the same projected mean can yield materially different threshold probabilities. Simulation family and spread assumptions must be preserved. Claude's exact simulated percentages were not independently rerun in this review.
- Correlated same-game bets reduce effective sample size. Design effect 1+(m-1)rho applies under a simple equal-size equicorrelated cluster model, not as a universal correction.
- Market-derived de-vig probability is a baseline estimate, not a known true probability. Multi-book consensus can be misleading if books copy feeds, are stale, or use different contracts. Two AI opinions with shared data are not independent evidence.

## Findings that require validation before governing-rule changes
1. **Market anchoring**: test market-only against fixed prespecified 25% AI blend and independent AI-only predictions, using as-of matched book quotes and future outcomes. Do not adopt weight 0.25 without evidence; if market-only is not available, label baseline missing rather than inventing it.
2. **Conservative probability**: Claude's p_central - 1.5 * forecast error is a proposed heuristic. Distinguish aleatoric player-outcome variance from epistemic uncertainty in probability estimates; an SD of player yards cannot be subtracted from a probability. Derive uncertainty from historically calibrated probability errors or explicit role/news scenarios. Before data exist, retain PASS/UNDETERMINED for weak estimates.
3. **Continuous gates**: pre-register a smooth price-aware risk/ROI gate to compare with current v2 piecewise gate on the SAME frozen contracts, scoring CLV, calibration, exposure and selection rate. Do not choose the best threshold from Sunday's test and call it validated.
4. **Price feed**: user-provided screenshots can support limited as-of testing but cannot alone guarantee a full historical quote panel. Evaluate actual data vendors for NFL player-prop contract coverage, bookmaker identity, timestamps, market suspension, settlement and legal terms, cost and retention. The user's statement that a vendor has five-minute snapshots is a research lead, not a verified entitlement or adequate quote.
5. **Promotions**: boosts/bonus bets still require a credible probability benchmark and settlement/terms; positive EV is not automatic, and not all promo EV is risk-free. Treat opportunity cost and capped stake explicitly.
6. **CLV**: important early process proxy, but not always a calibrated truth or faster-to-converge metric; require matched contract and timestamp, measure its variance, missingness and possible selection bias. Proper scores require genuine precommitted probabilities; no p means no Brier, not p=0.5.
7. **Tax claim**: Claude asserts a US federal 90% gambling-loss deduction cap beginning tax year 2026. This was NOT independently verified in this research review and must not be treated as tax advice or an authoritative current tax rule without primary-law verification.

## October 18 pilot adjustments proposed, not backfilled
- Freeze objective contract selection and retain all attempted observations, including passes and missing quote attempts.
- Aim for 30+ screened contracts if real evidence permits; do not fabricate to reach quota.
- ChatGPT and Claude should analyze the exact same timestamped screenshots independently, blind to the other's calls. Claude results exist only when user supplies them.
- Include the market as a third *baseline forecast* where a comparable two-sided, timely no-vig market is available; do not mistake that for a third independent research agent.
- Retain separate precommitted fields for market baseline, ChatGPT, Claude, and experimental market-shrunk blend; do not post-hoc choose a winner.
- Require official postgame results and exact settlement/void handling; closing quote observations must be contemporaneous or marked missing.
- The 9:30 AM international game cannot be part of a 10 AM pregame cohort without genuine earlier captured evidence.
- If 30/30 matched quotes or 80% closes are not achieved, mark operational pilot INCOMPLETE/INCONCLUSIVE, not proof of model failure or edge.

## Review conclusion
**ACCEPT FOR TEST DESIGN, NOT PRODUCTION ADOPTION.** Highest leverage is reliable quote capture, frozen forecast provenance and market-baseline comparison. Retain v2 controlling betting gates until a user-approved, explicitly versioned change after evidence. Preserve the Dot's already-open quote feasibility and Sunday tasks; add only nonduplicate bounded assignments.

Source: user-provided Claude response in conversation on 2026-10-16; cross-reference config/prime_ev_playbook_v2.md and research/pilots/2026-10-18/PLAN.md.
