"""Synthetic-only durable ingestion audit writer.

Accepts caller-supplied authenticated DB-API connection; no network setup.
Audit events use deterministic IDs to support replay-safe writes.
"""
import hashlib
import json
from datetime import datetime, timezone

TABLE = "my_db.prime_research.ingestion_audit_events"
ALLOWED = {"INSERTED_SYNTHETIC", "ALREADY_INGESTED", "FAILED"}
ERROR_CLASSES = {"VALIDATION_REJECTED", "CONNECTION_ERROR", "PERSISTENCE_ERROR"}

def make_event(batch_sha256, status, attempt_number=1, error_class=None,
               quote_count=None, code_commit_sha=None, observed_at_utc=None):
    if status not in ALLOWED:
        raise ValueError("unsupported audit status")
    if not isinstance(attempt_number, int) or isinstance(attempt_number, bool) or attempt_number < 1:
        raise ValueError("invalid attempt")
    if status == "FAILED" and error_class not in ERROR_CLASSES:
        raise ValueError("failed events require a classified error")
    if status != "FAILED" and error_class is not None:
        raise ValueError("success events cannot have an error")
    if batch_sha256 is not None and (not isinstance(batch_sha256, str) or
                                    len(batch_sha256) != 64 or
                                    any(c not in "0123456789abcdef" for c in batch_sha256)):
        raise ValueError("invalid batch fingerprint")
    if quote_count is not None and (not isinstance(quote_count, int) or quote_count < 0):
        raise ValueError("invalid quote count")
    observed = observed_at_utc or datetime.now(timezone.utc).isoformat()
    dt = datetime.fromisoformat(observed.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timestamp requires timezone")
    identity = [batch_sha256, status, attempt_number, error_class, observed,
                code_commit_sha]
    event_id = hashlib.sha256(json.dumps(identity, separators=(",", ":")).encode()).hexdigest()
    return {"audit_event_id": event_id, "batch_sha256": batch_sha256,
            "observed_at_utc": observed, "source_type": "SYNTHETIC_TEST_ONLY",
            "status": status, "error_class": error_class,
            "attempt_number": attempt_number, "quote_count": quote_count,
            "code_commit_sha": code_commit_sha}

def persist_audit_event(connection, event):
    """Idempotent audit write. Existing event is never overwritten.

    Audit events should use a separate connection/transaction from quote inserts.
    """
    if event.get("source_type") != "SYNTHETIC_TEST_ONLY":
        raise ValueError("live audit records are not enabled")
    if event.get("status") not in ALLOWED:
        raise ValueError("invalid audit event status")
    keys = ("audit_event_id", "batch_sha256", "observed_at_utc", "source_type",
            "status", "error_class", "attempt_number", "quote_count", "code_commit_sha")
    if any(k not in event for k in keys):
        raise ValueError("incomplete audit event")
    connection.execute("BEGIN TRANSACTION")
    try:
        exists = connection.execute(
            f"SELECT COUNT(*) FROM {TABLE} WHERE audit_event_id = ?",
            [event["audit_event_id"]]).fetchone()[0]
        if exists:
            connection.execute("COMMIT")
            return "ALREADY_RECORDED"
        placeholders = ", ".join("?" for _ in keys)
        connection.execute(
            f"INSERT INTO {TABLE} ({', '.join(keys)}) VALUES ({placeholders})",
            [event[k] for k in keys])
        connection.execute("COMMIT")
        return "RECORDED"
    except Exception:
        connection.execute("ROLLBACK")
        raise
