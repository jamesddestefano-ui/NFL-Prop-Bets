# BetRivers reception-market pairing diagnostic — October 17, 2026

Classification: source-verified structural finding, cause unresolved. Research only; not a betting recommendation.

The private odds-data repository's immutable `audits/20261017T142736310677Z-pair-diagnostics.json` (blob SHA `669a90ba2ba3231b3b17805fa7f2cdc4fabef794`) shows exactly 124 unpaired groups, all for BetRivers `player_receptions`, each missing an Under. In the same capture BetRivers had 126 paired receiving-yards groups and 61 paired rushing-yards groups, but zero paired receptions groups. The quality audit `audits/20261017T142736310677Z-quality.json` reports 1,178 paired groups of 1,302 total (90.48%).

This does not establish whether the sportsbook source omitted the outcomes or the collector rejected them. The private collector `scripts/odds_api_collect_v2.py` (blob `4026eb3da6fa3259fa29a3f5d156ca5f2baf3b6d`) reports normalization reason counts by sportsbook, market and side. Review that run's actual normalization summary before making a causal claim. The historical run was too large to retrieve completely through the current file interface; no normalization counts were verified in this review.

Proposed falsification: use an offline, redacted aggregate from the original run to count BetRivers reception Under outcomes by normalization reason. Compare independently captured runs. Test any identified normalization issue with synthetic fixtures before changing collector behavior. Keep all incomplete pairs excluded from no-vig consensus; do not synthesize opposite-side quotes, change thresholds, or alter immutable observations.

Status: targeted diagnostic documented; underlying cause remains unknown. No bets, spending, API keys, or authoritative ledgers affected.
