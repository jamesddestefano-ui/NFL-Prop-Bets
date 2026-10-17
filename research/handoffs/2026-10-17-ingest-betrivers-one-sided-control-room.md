# PRIME Integration Control Room — Ingest handoff

**AGENT:** PRIME Ingest / Odds API Diagnostic Research
**EXECUTION TIME (UTC):** 2026-10-17, after 20:13 UTC (exact execution timestamp unavailable from this chat tool; GitHub commit and run timestamps are authoritative)
**TASK:** Classify BetRivers NFL player-reception one-sided observations without fabricating Under quotes; repair failing CI and communicate governance boundary.
**STATUS:** PARTIAL PASS — collector validation succeeded; synthetic E2E suite still pending at handoff preparation.

## Verified evidence
- Manual diagnostic run #6: https://github.com/jamesddestefano-ui/NFL-Prop-Bets/actions/runs/39052295970 — 315 observed quote rows, 151 clean Over/Under pairs, 13 unmatched; all 13 BetRivers `player_receptions` missing Under; zero invalid or duplicate-side groups. Quota remaining 19,594 at capture. Source is one game / one time, not a whole-slate census.
- User-provided BetRivers NJ screenshots showed standard reception Over-only offers and a separate two-sided rushing+receiving market. Screenshot evidence is contextual; not proof that all future reception markets are one-sided.
- Research code `scripts/prime_odds_capture_diagnostics.py` now narrowly classifies `betrivers/player_receptions` Over-only groups as `EXPECTED_ONE_SIDED_OBSERVED`, preserving original `review_groups`, missing-side counts and `eligible_for_motherduck=False`.
- Counterexample regression tests cover BetRivers Under-only, other books, and other BetRivers markets.
- Initial commits 43d5d457 and 5eb52553 produced CI failures. Follow-up correction commit `bef09ccd92742306f35c6ace4af388b958a6e2d8` fixed missing result fields.
- Collector validation run 39065861919 on correction commit: **SUCCESS**. Synthetic E2E run 39065861917 was **IN PROGRESS** when first checked; verify its final conclusion before promotion.
- Private `jamesddestefano-ui/-NFL-Prop-Odds-Data/PRIME_SYSTEM_STATUS.md` confirms a separate authoritative scheduled collector/audit pipeline; do not duplicate it or move raw odds into this public research repo.

## Artifacts
- `scripts/prime_odds_capture_diagnostics.py`
- `tests/test_prime_odds_capture_diagnostics.py`
- `research/prime_betrivers_missing_under_2026-10-17.md`

## External sources / provenance
- GitHub Actions diagnostic run #6 above, source time 2026-10-17T17:06:32Z.
- User-provided BetRivers New Jersey sportsbook screenshots from 2026-10-17.
- No additional live API calls made in this corrective work. **API credits consumed by this handoff: 0**.

## Blockers and next action
- Verify synthetic E2E CI run 39065861917 and capture final result; if failing, fix and independently retest.
- Keep expected one-sided groups separately visible in completeness metrics; no synthetic Under, no BetRivers same-book no-vig on unmatched quotes, no claim of executable NJ prices.
- Coordinate with PRIME Commander and Integration Control Room through this GitHub handoff; a commit does not automatically wake another chat.
- No user intervention required for routine code/test work.

## PRIME HANDOFF
* AGENT: PRIME Ingest / Odds API Diagnostic Research
* EXECUTION TIME: 2026-10-17 UTC; see GitHub commit timestamp for exact time
* TASK: BetRivers one-sided reception classification and CI correction
* RESULT: INCONCLUSIVE (collector PASS; E2E pending at preparation)
* VERIFIED EVIDENCE: Diagnostic #6, collector CI #39065861919
* COMMIT SHA: bef09ccd92742306f35c6ace4af388b958a6e2d8 (code); handoff SHA is separate
* MODEL / DATA VERSION: Diagnostic classification v2; one-game API snapshot #6
* BLOCKERS: Final E2E CI result pending
* NEXT ACTION: Verify E2E, retain one-sided provenance and avoid duplicate collectors
* USER INTERVENTION REQUIRED: NO
