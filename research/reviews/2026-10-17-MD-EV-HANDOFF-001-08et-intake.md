# MD-EV-HANDOFF-001 — October 17 EV Learning research intake
Checked: 2026-10-17T17:04:27Z. Scope: NFL player props; research only; MODEL_SUSPECT.

## Source and provenance
- Candidate new research: research/education/2026-10-17-08et-duplicate-side-consensus-quarantine.md.
- Original Git commit: ea77ff6af449d4a4a90a903e036e2a2a893563e5, 2026-10-17T12:49:15Z.
- Git source blob: b899e7d08314bf5abb544f2c61aa2af06177ee73. Read by commit and from current main, exact content matched.
- The October 16 permission and assignment commits were interactive setup, NOT an unattended EV Learning result. The 08 ET title, commit time, and owner account are compatible with a scheduled run but do not prove agent authorship. **Unattended execution: UNVERIFIED**, pending a verifiable task-run ID or run-to-commit attestation.

## Reproduced claim and falsification
The handoff identified a duplicated one-sided book-price contamination path in leave-one-out consensus. Full-pair quarantine prevents falsely treating the remaining opposite side as a valid two-sided independent book.

Independently executed Python standard-library synthetic calculation, using only imaginary books A/B/C and no downloaded NFL odds. Observed tuples are (paired books, apparent edge probability, hypothetical net EV per stake):
- Legacy first-price retention: (3, 0.09999999999999998, 0.25).
- Duplicate pair quarantined: (2, 0.0, 0.0); three-book consensus is ineligible.
- Clean control: (3, 0.09999999999999998, 0.25); clean three-book rule remains eligible.
**Arithmetic/policy counterexample: PASS** (three checks). An initial exact-floating-point equality assertion failed due to binary floating representation, then passed using math.isclose with 1e-12 absolute tolerance. All amounts are synthetic, NOT executable odds or verified EV.

Independently inspected genuine private GitHub Actions job logs for successful run 39046046489, head fdef0dcaab633571e96ad437159fb4446039b810. Tests: duplicate quarantine 4/4, cross-side as-of 7/7, cross-book alignment 9/9, coverage 3/3 — total 23/23 passed. The current two consumer script blobs and quarantine/as-of test blobs match that run's commit exactly. Separate prior independent technical review already exists in research/reviews/2026-10-17-exact-source-duplicate-quarantine-independent-pass.md; this intake is nonduplicate because it audits EV Learning provenance and actual CI evidence. The provider v4 specification was checked directly on 2026-10-17; market last-update is not proof of a price change.

## Additional bounded CI repair
An unrelated, newly observed private research CI failure (run 39051716160) was traced from its actual logs to import-path incompatibility when a history module was imported as scripts.rolling_backtest. Small dual-mode import patch committed as 3661adb4c56d1b9828994c4fd8c9ec2f1d5a3743, with exact Git read-back. GitHub Actions run 39051974690 completed **SUCCESS**, with passing logs for boolean/NaN outcome rejection, push-count reconciliation, and pregame tests. This is evidence for CI passing, not model profitability.

## Decision / remaining blockers
Handoff numerical claim: PASS; production synthetic CI regression: PASS; attribution to unattended EV Learning: UNVERIFIED; real NJ prices, market agreement and calibrated positive EV: NOT ESTABLISHED. Do not modify forecast locks, historic source evidence, book-count eligibility gates, MODEL_SUSPECT status, wager records, or bankroll. HF public research access was available, but Superpowers skill enumeration returned no skills; neither provides NFL forecast validation by itself.

Next: obtain task-run provenance binding the 08 ET artifact to the unattended agent. Track time-aligned paired books and quarantined duplicates prospectively, retaining fixed denominators and missingness. No licensed odds or API credentials are included here.
