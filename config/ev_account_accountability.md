# PRIME — X / EV Analyst Accountability Module
Adopted: 2026-10-11
Scope: NFL player props only. Companion to AGENTS.md, methodology.md, advanced_market_learning.md, and positive_ev_framework.md; those controls take precedence.

## Capture, not endorsement
Grok may monitor EV-focused X accounts. Following an account does not validate its model, record, book quote, or independence. Ingest claims as `analyst_opinion` or `model_projection`, never `confirmed_fact` merely because several analysts agree. Do not overwrite verified market snapshots, tickets, settlement, or PRIME classifications. A Grok pass is NEW only if status=live and completedAt differs from the last processed completedAt; individual recycled posts must also be deduplicated.

## Per-tip source evidence
Record one row per original actionable analyst tip in `data/ev_source_signals.csv`. Preserve: observed and posted times in UTC, X handle and permalink, original-vs-repost distinction, NFL week/game/player and standardized prop type, Over/Under, named sportsbook, quoted line/odds and quote timestamp, whether executable and independently verified, reference market/consensus, stated projection or fair probability (with method when known), explicit source rationale, causal evidence, dependency thesis ID, first detected and last checked time, PRIME independent fair probability and conclusion, max playable price/line, eventual closing line/odds, CLV, settlement, and verification caveats. Leave unavailable fields blank. Never fill missing historical values by inference.

## Independence and duplicate attribution
Fingerprint a claim by `game|player|prop_type|side|line|odds|sportsbook|original_permalink`. Also cluster shared upstream projections, affiliate links, retweets, same screenshots, repost chains, and nearly simultaneous identical thesis into one `independence_cluster`. Credit original discovery separately from amplification; do not count ten reposts as ten independent confirmations. Distinguish `FIRST_MOVER`, `INDEPENDENT_CONFIRMATION`, `FOLLOWER`, `REPOST`, and `UNCLEAR`. Missing evidence => UNCLEAR, not independence. Source consensus is contextual, never sufficient to clear EV gate.

## Timestamp and market-lead tests
To evaluate a tip as an early discovery, require both the original publication timestamp and verifiable pre/post quotes from a named book (or a clearly identified market aggregate). Measure minutes from original tip to first verified favorable market movement, and whether the offered price was still executable at PRIME detection. No source gets early-credit for already moved/stale prices. Compare normalized movement using both LINE_CLV and PRICE_CLV; calculate COMBINED_CLV only where defensibly measurable. Keep movement direction appropriate to Over/Under and treat pushes/alternate thresholds appropriately. Never conflate a line at a different sportsbook or timestamp.

## Scorecard and meaningful samples
Report each source's: original tips; uniquely attributable tips; independently verified actionable tips; quote verification rate; stale-at-detection rate; pre-move discovery rate; median lead minutes; median/average CLV, positive-CLV rate; settled hit rate, stakes-normalized flat-stake ROI (where verifiable); Brier score only for explicitly precommitted probabilities; and performance broken down by prop type and timing bucket. Distinguish source-tip hypothetical returns from user-placed bet_history performance. Show sample sizes and missingness. Avoid ranking small samples confidently or promoting ROI alone; include confidence intervals/uncertainty when enough observations accumulate. Track misses and passes without survivorship bias.

## Decision rules
Run PRIME's independent opportunity, projection, no-vig, conservative EV, injury, market-truth, and exposure checks before BET. If the original quote disappeared, mark `PASS_AFTER_MOVE` and track as missed opportunity only if it was once genuinely verifiable and qualified. Store actionable maximum playable line and max juice; never chase steam. Same-thesis edges count once for portfolio exposure even across several analysts. Discord/X claims of 'locks', win streaks, ROI, or insider news receive no automatic boost.

## Operational cadence
On each new live Grok Pulse, extract newly discovered original EV posts, link to independently verified quotes and existing candidate IDs, append evidence rows and update eventual outcomes. For Sunday overnight, 8/9/10 AM, 11:30 AM inactives, 12:30 PM, late/SNF/MNF mini-slates, prioritize genuinely new pricing or material thesis changes; otherwise stay silent. Do not fabricate automated ingestion or historical tracking: this module is a specification, and rows are written only when actual evidence is obtained.
