# PRIME independent exact-source cross-book as-of validation — 2026-10-17

Status: **PASS (6/6)** for synthetic offline regression; **UNVERIFIED** for GitHub Actions execution and historical/provider market impact. `MODEL_SUSPECT` stays in force.

## Reproducible source evidence
Retrieved via authenticated GitHub connector from private `jamesddestefano-ui/-NFL-Prop-Odds-Data` on main on 2026-10-17 ET:
- `scripts/cross_book_alignment.py` exact Git blob `e0b1faa1a894cfabc2449c52d69a245edbb3fda0`.
- `tests/test_cross_book_alignment_20261017.py` exact Git blob `39c12bf78a4f2afd4c68e55766f0a5666aacaa30`.
- CI workflow integration commit `0db5ef9b2bbc01946956064197ad9cdb6f14f6f7`.

A minimal local tree was reconstructed using the exact connector-returned contents. `git hash-object` produced the above two exact blob SHA values *before* test execution. No private quote files, secrets, network or database access were used.

Command: `cd /mnt/data/prime_alignment_repro && python -m unittest discover -s tests -p 'test_cross_book_alignment_20261017.py' -v`.

Observed stdout/stderr summary:
```
test_invalid_missing_timestamp_rejected ... ok
test_mismatched_kickoff_rejected ... ok
test_same_book_sides_misaligned_rejected ... ok
test_same_instant_three_books ... ok
test_staggered_books_rejected ... ok
test_timezone_equivalent_accepted ... ok
Ran 6 tests in 0.000s
OK
```

## Interpretation and remaining limits
PASS only for the narrow *opt-in research diagnostic*: strict normalized cross-book receipt instant equality, same-book side consistency, and kickoff validation on synthetic inputs. The module is not integrated into production consensus or the October 18 locked pilot. This strict equality rule may materially reduce eligibility for asynchronously updated provider feeds, so measure prospective nonauthoritative coverage before considering any integration. The diagnostic assumes prevalidated pairs and does not itself verify every element of contract identity.

GitHub combined status endpoint for workflow commit `0db5ef9b2bbc01946956064197ad9cdb6f14f6f7` returned zero status entries; this is **not** proof of an Actions PASS or failure. No corresponding job log was retrieved. No unattended EV Learning provenance was established from this test.

No wagers, historical odds mutations, authoritative bet records, expenses or model promotions occurred.
