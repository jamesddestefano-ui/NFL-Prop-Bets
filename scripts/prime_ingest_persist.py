"""Synthetic-only MotherDuck persistence for PRIME ingest v1.

Requires an authenticated DuckDB/MotherDuck connection supplied by the caller.
Never opens a connection, reads API keys, or schedules ingestion.
"""
import hashlib
import json
from scripts.prime_ingest_boundary import validate_batch

BATCH_TABLE = "my_db.prime_research.ingestion_batches"
QUOTE_TABLE = "my_db.prime_research.odds_quotes"

def _quote_id(batch_hash, q):
    identity = [batch_hash, q["event_id"], q["bookmaker"], q["market"],
                q["player_id"], q["side"], q["point"], q["response_received_utc"]]
    return hashlib.sha256(json.dumps(identity, separators=(",", ":")).encode()).hexdigest()

def persist_synthetic_batch(connection, fixture, source_path="synthetic/prime_v1_fixture.json"):
    """Atomic idempotent insert; raises on failure and rolls back.

    Caller must supply a connection pointing at MotherDuck my_db with write access.
    No live data is accepted by validate_batch.
    """
    validated = validate_batch(fixture)
    fingerprint = validated["batch_sha256"]
    if not source_path.startswith("synthetic/") or len(source_path) > 512:
        raise ValueError("synthetic source path required")
    connection.execute("BEGIN TRANSACTION")
    try:
        exists = connection.execute(
            f"SELECT COUNT(*) FROM {BATCH_TABLE} WHERE batch_sha256 = ?", [fingerprint]
        ).fetchone()[0]
        if exists:
            connection.execute("COMMIT")
            return {"status": "ALREADY_INGESTED", "batch_sha256": fingerprint, "inserted": 0}
        # Existing schema has no fixture-status column. Mark synthetic provenance in
        # both source_path and source_type; never present these rows as real prices.
        connection.execute(
            f"INSERT INTO {BATCH_TABLE} (batch_sha256, source_path, source_type, ingested_at_utc, record_count) "
            "VALUES (?, ?, ?, CURRENT_TIMESTAMP, ?)",
            [fingerprint, source_path, "SYNTHETIC_TEST_ONLY", validated["record_count"]]
        )
        for q in validated["quotes"]:
            connection.execute(
                f"INSERT INTO {QUOTE_TABLE} "
                "(source_sha256, quote_id, run_id, event_id, bookmaker, market, player_id, "
                "side, point, odds_american, response_received_utc, commence_time, paired, raw_response_sha256) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                [fingerprint, _quote_id(fingerprint, q), "SYNTHETIC_TEST_ONLY",
                 q["event_id"], q["bookmaker"], q["market"], q["player_id"],
                 q["side"], q["point"], q["odds_american"],
                 q["response_received_utc"], q["commence_time"], True, fingerprint]
            )
        connection.execute("COMMIT")
        return {"status": "INSERTED_SYNTHETIC", "batch_sha256": fingerprint,
                "inserted": validated["record_count"]}
    except Exception:
        connection.execute("ROLLBACK")
        raise
