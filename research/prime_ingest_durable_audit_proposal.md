# PRIME durable ingestion audit — proposed schema, NOT EXECUTED

The current local JSONL audit is not durable across ephemeral GitHub runners. Proposed future MotherDuck table:

```sql
CREATE TABLE IF NOT EXISTS my_db.prime_research.ingestion_audit_events (
  audit_event_id VARCHAR PRIMARY KEY,
  batch_sha256 VARCHAR,
  observed_at_utc TIMESTAMPTZ NOT NULL,
  source_type VARCHAR NOT NULL,
  status VARCHAR NOT NULL,
  error_class VARCHAR,
  attempt_number INTEGER NOT NULL,
  quote_count BIGINT,
  code_commit_sha VARCHAR
);
```

Proposed policies: append-only audit events; never log credentials or full API responses; synthetic/live provenance explicitly separated; idempotency by audit_event_id; persist audit failures independently of the quote transaction; monitor write failures; fail closed if audit storage is unavailable. Database writes and table creation require explicit separate approval.

Retry policy is code-only and does not itself schedule retries: only connection errors are eligible, at most three attempts with 60/120 second delays; validation errors, unknown errors, and persistence errors go to manual review. A later production design must also address concurrent workers, unique constraints, source-of-truth reconciliation, and secret management.
