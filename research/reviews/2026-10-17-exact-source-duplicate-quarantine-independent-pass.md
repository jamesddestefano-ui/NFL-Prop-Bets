# PRIME exact-source duplicate quarantine independent reproduction — 2026-10-17

**Outcome:** PASS, 4/4 synthetic regression tests; CI status separately UNVERIFIED. Research-only, MODEL_SUSPECT.

## Immutable source provenance

Source accessed via authenticated GitHub connector from private `jamesddestefano-ui/-NFL-Prop-Odds-Data` main on 2026-10-17 ET. Each local copy was checked against the exact Git blob SHA using `git hash-object` before execution:

- `scripts/quote_persistence.py`: `5fbda78894d84c0113990492cbe60c6c029fdc78`
- `scripts/validate_consensus.py`: `73f7b1c5dd27c06dc2d185716dcdeab5047a29e9`
- `tests/test_duplicate_side_quarantine_20261017.py`: `38eb920438ec241dfe5feec6b554b0a780da09f5`

Previous source commits: `c783aaeba71bdfb086a5a40c14d3c288f20966e0` and `ec6e7c25daa1bceee285bc330db84881775d3a09`; synthetic test commit `28ad5ab7af41b9ea8491a2e0f478eff9d068d395`; private CI workflow commit `9be9358d3a294f327d3f8549c9d27db15e9cb8c8`.

## Independent execution

Offline command, isolated local Python environment from copied exact source:

```
python -m unittest discover -s tests -p 'test_duplicate_side_quarantine_20261017.py' -v
```

Actual observed results:

```
test_clean_three_books_remain_eligible ... ok
test_consensus_script_reports_exclusion_and_prevents_false_signal ... ok
test_duplicate_over_quarantines_entire_book ... ok
test_duplicate_under_quarantines_entire_book ... ok
Ran 4 tests in 0.006s
OK
```

No actual private quote snapshots, credentials, network calls, wagers, MotherDuck mutations, or sportsbook prices were used. The test's imaginary books are TEST_A/B/C.

## Conclusions and limitations

PASS for exact-source local synthetic quarantine regression. The regression confirms clean synthetic three-book observations remain eligible, duplicate Over/Under eliminates the contaminated exact-book pair, and consensus does not score a contaminated book as evidence of a favorable quote.

**Not verified:** GitHub Actions execution, prospective price survival, real quote execution, model calibration, out-of-sample profit, or unattended EV Learning handoff provenance. A GitHub commit status query previously returned no CI statuses; absence of statuses is not a failure or a pass. No model or betting gate is promoted. Keep `MODEL_SUSPECT`.

Future work: verify an actual private workflow run/job conclusion; add synthetic tests for as-of misalignment and alias mismatch, and measure matched-book close coverage prospectively before using research EV flags.
