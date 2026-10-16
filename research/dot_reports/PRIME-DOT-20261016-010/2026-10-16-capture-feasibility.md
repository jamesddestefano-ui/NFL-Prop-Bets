# PRIME task010 — NFL prop capture feasibility and Sunday readiness

- Task: PRIME-DOT-20261016-010
- Research date: 2026-10-16; public sources retrieved 18:50–18:55 UTC (14:50–14:55 America/New_York).
- Disposition: INCONCLUSIVE for operational readiness. Documentation research completed; successful NFL prop capture, NJ contract matching and historical-close reproduction remain unverified.
- Scope: NFL player-prop education only. No API credentials, paid-quota requests, subscriptions, wagers, production deployment or controlling-rule edits.
- Evidence categories: provider documentation is EMPIRICAL EVIDENCE of a published capability claim, not observed API performance. Proposed tests are UNTESTED HYPOTHESES. Arithmetic below is VERIFIED MATHEMATICAL PRINCIPLE under stated assumptions.

## Answer PRIME needs

Can a reproducible multi-book NFL player-prop feed preserve enough information for prospective screening and matched historical closing comparisons, including New Jersey price and settlement truth?

**Documented technical support is promising, but the operational claim is not established.** The smallest next proof is one successful, safely handled NFL event/market response, matched against the same real NJ sportsbook contract. Paid history is not necessary to establish that first prospective proof. Do not replace the adopted screenshot pilot with an assumed-working collector.

## Actual repository evidence

Instructions reviewed: AGENTS.md; agent_research_handoff; ev_daily_education_directive; methodology; positive_ev_framework; advanced_market_learning; ev_account_accountability; prime_ev_playbook_v2; odds_api_secure_setup; append-only queue; prior task006 operational report.

Task010 was REQUESTED before this work. Its IN_PROGRESS event was appended and read back at commit 0c069994c813dd27049552910a67b8adbc7f97b9. The full recursive tree at that commit was not truncated. The relevant deployment/configuration search found only config/odds_api_secure_setup.md: no collector, .github/workflows files or data/odds_api output appeared. A public Actions-runs read at 18:53 UTC returned total_count=0. This bounds the evidence to the inspected repository and time; it does not establish the state of private credentials or other environments.

The setup document proposes an initial manual workflow and sanitized append-only output under data/odds_api or a research archive. This is a proposed design, not evidence that raw payloads are currently being published. No active data-rights violation is asserted.

## Source comparison

### The Odds API: current prospective capture

The official market list includes NFL player_receptions, player_reception_yds, player_rush_yds, player_pass_yds and touchdown markets, with alternate markets separately identified. Catalog availability does not guarantee each book/player/line is returned. [Market catalog](https://the-odds-api.com/sports-odds-data/betting-markets.html)

Published plans: free 500 credits/month, most books and no history; 20,000 credits/month at USD30, including history. Higher published tiers are 100,000/USD59, 5 million/USD119 and 15 million/USD249 monthly. These are documented prices, not a verified account entitlement or purchase recommendation. [Pricing](https://the-odds-api.com/)

The book list includes DraftKings, FanDuel and BetMGM. Caesars and Fanatics are marked paid-only. Generic Hard Rock coverage is identified as Indiana; its note about other states does not verify NJ equivalence. US categories also contain other kinds of sources. Use a specific eligible-book allowlist rather than treating a region as NJ authorization or identical NJ pricing. [Book coverage](https://the-odds-api.com/sports-odds-data/bookmaker-apis.html)

**Important freshness limitation:** V4 documentation, GET odds → More info, says market last_update records when the provider saw odds; suspended/closed markets can remain about 15 minutes before removal; this is the provider's described behavior, not a universal timing guarantee. Event-odds records carry event, book, market, outcome description/player, side, point and price. The shown schema does not establish a complete jurisdiction/settlement/suspension contract. Current event-odds cost is unique returned markets times regions; historical event-odds cost multiplies that by ten. Requests are per event for props. Specifying up to ten bookmakers counts as one region. No authenticated request was made here. [V4 documentation](https://the-odds-api.com/liveapi/guides/v4/)

Published prop/alternate refresh interval is 60 seconds pregame and in-play. That is not an execution guarantee or proof of maximum end-to-end latency. [Update intervals](https://the-odds-api.com/sports-odds-data/update-intervals.html)

### The Odds API: historical snapshots

Additional-market history, including props, is documented from May 3, 2023 at five-minute intervals, on paid plans. Requested dates resolve to the nearest available snapshot at or before that time. Coverage starts only when the sport/book/market was added; the overall NFL start date must not be misread as the start date for every prop. Store requested time and returned snapshot time separately. A historical snapshot is not automatically the book's actual last executable pre-kickoff quote. Documentation examples reviewed are examples, not an independently verified NFL prop result. [Historical documentation](https://the-odds-api.com/historical-odds-data/)

### Unabated: alternative requiring separate access validation

The odds guide distinguishes board-level update time from line-level modifiedOn, sequence and freshnessExpiresAt, and supplies status/disabled checks. It documents props and alternate lines, IDs, price and points. Missing data can reflect coverage or access scope. These fields are useful comparison requirements for any capture design, not evidence PRIME currently receives them. [Odds guide](https://docs.unabated.com/guides/odds)

Free access is a content-partner offering with delayed data; publication/transport can add age beyond the stated minimum 15-second delay. Concierge covers live NFL and other named leagues, with streaming; Enterprise depends on agreement. No current paid price, historical-closing entitlement, raw redistribution permission or successful request was independently established. Do not assume a free partner account is an unconditional substitute for the current setup. [Access tiers](https://docs.unabated.com/start/access-tiers) · [Quickstart](https://docs.unabated.com/start/quickstart)

### Existing screenshot route

Keep the user-adopted October 18 prospective screenshot process as the fallback. It still needs actual screenshots, source times and exact rules; no current screenshot panel or verified executable quote was produced by this documentation review.

## Public archive rights: review gate, not a legal conclusion

The Odds API terms, last updated August 31, 2026, permit indefinite storage, research, derived values and other specified uses, while restricting standalone raw-data redistribution, including downloadable datasets. A public raw quote archive needs assessment against its actual intended use and those restrictions. Public NFL facts and user permission to publish research do not alone settle a provider's data-license scope. Prefer general methods and aggregate/derived educational results for this report; seek provider clarification before a standalone raw panel if unclear. This does not conclude that all public research or individual quote citation is prohibited. [Official terms](https://the-odds-api.com/terms-and-conditions.html)

## Analytical implications and falsifiable tests

1. **MODEL ASSUMPTION challenged: a returned quote is live.** Retained suspended records can manufacture apparent stale-price edges. Proposed test: compare each sampled API contract with an independently observed NJ contract at the same time; retain API age, actual availability and mismatches. Report unavailable and failed checks, not only matches. Reject production readiness if availability/price discrepancies remain unexplained.
2. **MODEL ASSUMPTION challenged: five-minute history verifies a two-minute survival or exact close.** Illustrative timestamps only: a 12:55 snapshot and 13:00 snapshot cannot show whether a quote survived at 12:57. Missing observations stay unknown. Record a real +2-minute observation if that endpoint matters; do not interpolate a positive result.
3. **UNTESTED HYPOTHESIS: bounded capture can improve matched CLV coverage.** Predefine eligible exact contracts and compare capture completeness, timestamp ages, two-sided matching and pre-kickoff close coverage against the screenshot process. Improvement requires fewer missing/mismatched records, not more attractive backfilled edges.
4. **VERIFIED MATHEMATICAL PRINCIPLE, illustrative budget:** three events × three returned markets × one region × four checkpoints = 36 live credits; the analogous historical requests cost 360. Discovery, retries and other endpoints add usage. This is arithmetic, not an observed bill or proof that 30 contracts will be returned.
5. **VERIFIED MATHEMATICAL PRINCIPLE:** for no-push decimal odds d, EV=p*d−1. A valid market capture still does not supply a calibrated p. Matched two-sided de-vigging requires the same player, threshold, period and settlement basis. Push/void contracts require their actual probabilities and payout treatment.

## Smallest proposed validation protocol

This is a proposal for review, not an installed collector or new schedule.

- Preserve the v2 frozen-cohort target of at least 30 screened contracts if genuinely observable, including PASS/WATCH and capture failures. Prior task006's ten-contract operations example does not supersede this adopted target.
- First obtain one safely handled event/market response through the separately authorized setup. Retain request observation start/end, returned snapshot time when applicable, market update time and quota cost without credentials or credential-bearing URLs.
- Normalize exact player, event, book, jurisdiction verification, period, market, side, threshold, price, opposite-side matching, market status if available and settlement basis. Mark unavailable fields null. Do not infer both sides from a market title.
- Verify the same NJ contract and active price independently. Timestamp that verification separately; API receipt time is not source freshness.
- Preserve cohort freezes and each genuine subsequent checkpoint. Use the existing v2 Sunday timing rather than creating a second schedule. Label a pregame snapshot by its actual time; only call it a defined closing proxy when it meets the precommitted rule.
- Keep raw retention/publication within actual rights and authorization. Record public research conclusions separately from private account context.
- Reconcile postgame against authoritative player results and the book's contract rules. Team scores alone cannot settle a player prop.
- Evaluate all screened records, including missing closes. No extrapolation from the pilot to a validated betting edge, no fill inferred from availability, and no new formal BET without all existing gates.

## Completion evidence still required

1. A successful NFL prop response and demonstrated field mapping, safely handled.
2. Actual eligible NJ book/market coverage and observed price/availability comparisons.
3. Suitable settlement and suspension handling.
4. Historical access and a reproducible matched pre-kickoff example, if history remains necessary.
5. An appropriate retention/publication plan under the selected provider's terms.
6. Deployed/run evidence if claiming automated capture.

Confidence: high in the identified documentation statements and repository observations; moderate in feasibility; insufficient evidence for production readiness, price executability or a specific profitable wager. No private data, raw commercial odds panel or prior denied payload is included.

## Source-access record

All external sources above were original provider webpages reviewed as article/documentation text on October 16, 2026, 18:50–18:55 UTC. No video playback or transcript, X post, paid account, live API response or historical API result was reviewed in this task. Publication dates were not displayed for the documentation pages; the terms explicitly show August 31, 2026. Section anchors/text replace video timestamps. Access limitations and missing publication fields are intentional, not inferred dates.

Repository evidence: [start commit](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/commit/0c069994c813dd27049552910a67b8adbc7f97b9), [secure setup](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/0c069994c813dd27049552910a67b8adbc7f97b9/config/odds_api_secure_setup.md), [v2 overlay](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/0c069994c813dd27049552910a67b8adbc7f97b9/config/prime_ev_playbook_v2.md), [prior006](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/0c069994c813dd27049552910a67b8adbc7f97b9/research/dot_reports/PRIME-DOT-20261014-006/2026-10-15-operational-capture-specification.md).
