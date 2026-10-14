# PRIME Sunday 2026-10-18 — prospective NFL prop shadow pilot
Created 2026-10-14. This is a precommitted RESEARCH pilot, not a placed wager, proof of EV, or model-policy replacement.

## Scope and execution
On Sunday October 18, 2026 (America/New_York), use a bounded set of NFL player props with verifiable current prices and official schedule/participants. Focus on standard receiving yards, receptions and rushing yards; allow other props only with explicit justification and separate grouping. Select up to 10 candidate contracts *before viewing results*, and preserve all examined candidates, including PASS/AVOID and failed quote attempts. Do not cherry-pick only apparent winners. No deposits, bets, account actions or automatic stakes.

10:00 AM ET initial capture: official injuries, role data, projection sources and original market observations. 11:30 AM ET inactives refresh for early games (the existing hourly Watch handles the interval); 12:30 PM ET final prelock verification, fresh lines, odds, maximum playable price and decisions. Late games and SNF are separate mini-slates if verifiable. Monday/Tuesday grade final stats, settlement terms and available matched closing lines without backfilling unknown prices.

## For every evaluated contract
Capture game, player, team, exact standardized prop, threshold/comparator (Over vs 5+), sportsbook, odds, observed timestamp, *source update timestamp if available*, quote source and confidence, market status, book/jurisdiction settlement rule and push eligibility. Store matching opposite-side odds only when same-book/same-contract. Record role/news sources with publication and observation timestamps, independent projections and uncertainty, modeled p_win/p_loss/p_push when justified, conditional/no-vig benchmark when valid, break-even p, central and conservative EV, exposure and correlation tags, classification BET/LEAN/WATCH/PASS/AVOID, and play-to line/max juice. Missing values stay null; no synthetic lines or pseudo-fills.

## Shadow grading
A shadow BET means the model qualified a *quoted candidate*; it is not an actual ticket. Distinguish quote-at-capture, price rechecked before lock, and confirmed user ticket. Record outcomes and unit-return hypothetical separately from user P/L. Grade process quality independently of wins. Report observed-frame denominator, quote freshness and failure/missingness, selection rate, win/loss/push/void counts, line/price CLV coverage, Brier calibration coverage, and all blockers. If no verifiable executable price or reliable p, mark WATCH/PASS and report an inconclusive pilot rather than manufacturing action.

## Success conditions
Operational success means a reproducible as-of audit trail and honest denominators, not a profitable week. The sample is far too small to claim predictive superiority. Preserve a dated immutable pilot report and any verified evidence in research/pilots/2026-10-18/; do not rewrite canonical historical ledgers, settlement, or existing governing methodology without reconciliation and review.
