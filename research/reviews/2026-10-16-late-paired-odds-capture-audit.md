# PRIME paired-capture empirical integrity audit — October 16, 2026

Scope: NFL player props only. This is a retrospective comparison of two API samples already stored on GitHub main, **not a live NJ executable market check**, bet, inferred alpha or new API call.

## Original source artifacts (GitHub connector, file-text access)
- [Capture A, recorded collection-start 19:02:45.187757 UTC](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/main/data/odds_api/2026-10-16T19-02-45Z-sample.json), blob SHA 3579dcdad7f049eef6d89aec1b24686c8e4f607e.
- [Capture B, recorded collection-start 19:03:02.636483 UTC](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/main/data/odds_api/2026-10-16T19-03-02Z-sample.json), blob SHA 3f9616285d81b55fc38cf342f476603d15ff708e.
- [Dot observation-time boundary review](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/main/research/dot_reports/PRIME-DOT-20261016-010/2026-10-16-observation-time-boundary-review.md).
- [Sunday October 18 preregistered shadow pilot](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/main/research/pilots/2026-10-18/PLAN.md).

## Independently reproduced aggregate measurements
Both JSON documents were parsed directly from GitHub through authenticated connector text reads within this research run. Per-capture: 361 quote-side records, seven bookmaker keys (draftkings, fanduel, betmgm, bovada, betonlineag, betrivers, fanatics), three player markets: receiving yards 156, receptions 143, rushing yards 62. Exact same-event/book/player/market/threshold grouping: 187 groups; 174 Over/Under pairs and 13 single-sided groups. Zero quote rows with missing market and book timestamps; zero nonnumeric line or American-odds values.

Comparing row-by-row (same ordering and number) across 361 records: zero non-timestamp field differences. All 361 `observed_at_utc` values changed. 62 `market_last_update` values changed. No observed odds, threshold, side, book, market, player, status, or event changes. Do **not** count market_last_update changes as a bettable price move. The recorded capture times were 17.449 seconds apart.

Using recorded collection-start minus market source-update only, approximate apparent source-age range was 0.294–1.294 minutes, median 0.727 minutes in capture B. These are **not verified quote receipt ages**, because the collector's original observation time precedes HTTP response completion; accurate source staleness/latency awaits response-receipt timestamps. No evidence supports 361 active NJ account offers or any odds drift/CLV.

The records cover Houston Texans at Jacksonville Jaguars, scheduled 2026-10-18 13:30 UTC (9:30 AM ET). It is **not eligible** for an initial 10 AM ET candidate freeze unless an independent actual timestamped pre-kickoff freeze exists. No such freeze was shown by these samples.

## Operational decisions
1. Require exact side-contract identity and compare economic content (line/price/settlement) independent of refresh timestamps; separately store source-update events.
2. Keep request-start, completed odds-response receipt and source update distinct and prove pre-kickoff by response-received < scheduled kickoff.
3. Preserve 13 one-sided groups as missing-opposite-side; never fabricate a no-vig benchmark or call it zero missingness.
4. Require actual NJ price availability and settlement before formal BET; `region_requested=us` is not account executability.
5. Sunday pilot: freeze all screened screenshot contracts prospectively, track missingness and passes, exclude 9:30 game from 10 AM unless genuine earlier freeze.
6. Restrict raw data redistribution as licensing/rights require; publication review remains pending. Neither raw input nor authoritatively recorded user tickets were modified.

This retrospective data-quality audit neither supplies calibrated player win probabilities nor establishes positive EV, Brier quality or CLV. No wagers were placed, no Claude execution claimed, no Dot schedule changed.
