# PRIME — pre-normalization rejection telemetry gap (October 17, 2026)

**Classification:** verified code audit and private snapshot correlation; root cause of missing sportsbook outcomes remains unverified. No model or wager action.

## Source and evidence
Private `jamesddestefano-ui/-NFL-Prop-Odds-Data`, `scripts/odds_api_collect_v2.py`, inspected on main, blob `4026eb3da6fa3259fa29a3f5d156ca5f2baf3b6d`. Inside `flatten()`, `side=o.get("name")` followed by `if side not in ("Over","Under"): continue` occurs **before** the `normalization_counts` update. Consequently a nonliteral name or missing name is invisible to recorded rejection telemetry. Recognized Over/Under outcomes with invalid player, point, or price can be counted as rejected. This is a specific instrumentation gap, **not proof of the cause** of the BetRivers reception missing Unders.

The immutable `audits/20261017T142736310677Z-pair-diagnostics.json` (blob `669a90ba2ba3231b3b17805fa7f2cdc4fabef794`) reports 124 BetRivers player_receptions one-sided groups, all missing Under, with zero paired BetRivers player_receptions groups; receiving-yards and rushing-yards remain paired. The associated quality audit (blob `57c4cc58e00e1de9c9e1702655813efd7133221b`) records 2,480 quotes, 1,178 clean pairs, and 90.48% coverage.

## Smallest safe proposed correction
Instrument aggregate counts for unrecognized/missing outcome name **before** the early `continue`. Count by book and market with reason `UNRECOGNIZED_SIDE`, but never persist raw unrecognized values, untrusted provider payloads, API keys, or individual identifiers in public reporting. Keep the accepted quote set, pairing policy, and exact contract identity unchanged; retain an independent count of recognized accepted/rejected sides. Count total outcomes by book/market so the categories reconcile.

## Synthetic regression contract
1. A BetRivers player_receptions payload with `Over` and unexpected `Under ` (trailing space) records one accepted Over and one `UNRECOGNIZED_SIDE` count, **not** a paired book.
2. A payload with no Under outcome records no `UNRECOGNIZED_SIDE`; observed normalized one-sidedness remains the same.
3. A proper literal `Under` yields a clean pair.
4. Test missing outcome name, invalid price, and separate books and thresholds; preserve all rejected reasons and verify total raw outcomes equal accepted + rejected counts.
5. Apply to subsequent independently captured runs; prior immutable captures cannot retroactively distinguish upstream absence from early normalization drops.

## Explicit limits
The run JSON could not be retrieved completely through the connected GitHub file interface, so the exact run's normalization counts were **not verified**. Do not assert BetRivers' raw payload format or modify historical records. Research-only; zero API requests, zero wagering, no decision-gate changes. This investigation does not substitute for separate 08 ET education, 14 ET testing, and 20 ET critical-review cycles.
