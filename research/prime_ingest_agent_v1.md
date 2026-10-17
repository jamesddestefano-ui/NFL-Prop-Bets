# PRIME Ingest Agent v1 — Synthetic validation boundary

Status: **synthetic-only; no production ingestion enabled**.

Run locally from repository root:
```sh
python -m unittest discover -s tests -p 'test_prime_ingest_boundary.py' -v
python -m scripts.prime_ingest_boundary
```

The boundary rejects unmarked/live data, missing or duplicate quotes, incomplete Over/Under pairs, unsupported markets, invalid odds, missing timezone, and quotes observed at or after kickoff. It returns a deterministic SHA-256 batch fingerprint suitable for future idempotency checks.

Existing MotherDuck destination tables are `my_db.prime_research.ingestion_batches` and `my_db.prime_research.odds_quotes`. This version **does not connect to MotherDuck** and does not claim to have tested database persistence.

Next gated milestone: implement parameterized transactional writes with batch-fingerprint deduplication, quote IDs, source provenance, and rollback-on-error; verify with synthetic records before authorizing any live collector integration. Do not schedule jobs or import actual sportsbook data without separate authorization.

Existing `odds-api-collector.yml` is manual diagnostic and runner-local only; do not misrepresent it as persistent or scheduled.
