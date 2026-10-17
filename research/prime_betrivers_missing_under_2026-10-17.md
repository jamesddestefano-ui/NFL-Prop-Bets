# PRIME BetRivers missing Under — verified diagnostic #6

**Source:** GitHub Actions manual Odds API sample run #6: https://github.com/jamesddestefano-ui/NFL-Prop-Bets/actions/runs/39052295970

**Capture time:** 2026-10-17T17:06:32Z. **Scope:** One upcoming NFL event, US region, three requested player-prop markets; this is not a whole-slate or all-bookmakers census.

## Observations

- 315 API quote rows; 151 clean Over/Under pairs (302 rows); 13 unmatched rows; classification `REVIEW_REQUIRED`.
- Every unmatched row: bookmaker key `betrivers`, market `player_receptions`, **missing Under**. All 13 BetRivers receptions groups have an Over without a matching Under: **0/13 clean pairs, 13/13 incomplete**.
- No invalid rows, duplicate-sided groups, or excess/conflicting groups.
- BetRivers receiving yards: 13/13 complete; rushing yards: 5/5 complete.
- API quota remaining after request: 19,594.
- Previous manual run #5 (https://github.com/jamesddestefano-ui/NFL-Prop-Bets/actions/runs/39048234890) also showed 13 BetRivers player-reception missing opposite sides, but lacked direction-specific logging.
- Quote-level complete-pair coverage for run #6: 302/315 = 95.87%; group-level clean-pair coverage: 151/164 = 92.07%. Distinguish these denominators.

## Interpretation and safeguards

This is an **upstream feed / sportsbook representation completeness anomaly**, not yet proof that BetRivers itself lacks Under markets. Do not impute a missing Under from other sportsbooks, compute BetRivers no-vig probabilities on those 13 groups, or delete the valid Over observations. Mark each unmatched quote `MISSING_OPPOSITE_SIDE`, retain provenance and timestamp, and keep the 151 complete pairs eligible only for subsequent independent quality gates. No API observation is automatically executable in NJ.

**Next research:** compare another independently timed capture and investigate upstream provider documentation/support before attributing root cause. Avoid repetitive credit-consuming diagnostics without new hypothesis. Keep synthetic and live records separate; no production MotherDuck ingestion authorized by this note.
