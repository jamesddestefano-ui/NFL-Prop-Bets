"""Synthetic-only ingestion orchestration with independent durable audit.

Caller supplies distinct authenticated DB connections for quotes and audit.
No live sportsbook data, API requests, secret management, or scheduling.
"""
from datetime import datetime, timezone
from scripts.prime_ingest_boundary import validate_batch
from scripts.prime_ingest_persist import persist_synthetic_batch
from scripts.prime_ingest_audit_db import make_event, persist_audit_event
from scripts.prime_ingest_runner import classify

def ingest_with_durable_audit(quote_connection, audit_connection, fixture,
                              source_path="synthetic/prime_v1_fixture.json",
                              attempt_number=1, code_commit_sha=None):
    """Persist quote transaction then independent audit event.

    If audit persistence fails after quotes commit, raise and require reconciliation
    by batch fingerprint. Do not retry the quote transaction blindly.
    """
    fingerprint = None
    quote_count = None
    try:
        checked = validate_batch(fixture)
        fingerprint = checked["batch_sha256"]
        quote_count = checked["record_count"]
        result = persist_synthetic_batch(quote_connection, fixture, source_path)
        event = make_event(fingerprint, result["status"],
                           attempt_number=attempt_number,
                           quote_count=result["inserted"],
                           code_commit_sha=code_commit_sha)
        audit_status = persist_audit_event(audit_connection, event)
        return {"status": result["status"], "batch_sha256": fingerprint,
                "inserted": result["inserted"], "audit_status": audit_status,
                "audit_event_id": event["audit_event_id"]}
    except Exception as exc:
        # Do not mask the original exception if the independent audit write fails.
        # The caller must reconcile the quote transaction before any retry.
        failure = make_event(fingerprint, "FAILED", attempt_number=attempt_number,
                             error_class=classify(exc), quote_count=quote_count,
                             code_commit_sha=code_commit_sha)
        try:
            persist_audit_event(audit_connection, failure)
        except Exception:
            pass
        raise
