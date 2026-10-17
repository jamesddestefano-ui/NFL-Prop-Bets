"""PRIME synthetic ingestion runner with append-only local audit.

Caller supplies an authenticated DB-API connection. No secrets, network setup,
live sportsbook data, or scheduled jobs are handled here.
"""
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from scripts.prime_ingest_persist import persist_synthetic_batch

def classify(exc):
    if isinstance(exc, ValueError):
        return "VALIDATION_REJECTED"
    if isinstance(exc, (ConnectionError, TimeoutError)):
        return "CONNECTION_ERROR"
    return "PERSISTENCE_ERROR"

def append_audit(path, event):
    """Append one fsynced JSON line. Failure propagates to caller."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(event, sort_keys=True, separators=(",", ":")) + "\n"
    with target.open("a", encoding="utf-8") as out:
        out.write(line)
        out.flush()
        os.fsync(out.fileno())

def run_ingestion(connection, fixture, audit_path, source_path="synthetic/prime_v1_fixture.json"):
    """Execute once; audit outcome, including failures, without exposing quote data.

    Audit file is local to caller; not automatically uploaded or committed.
    """
    started = datetime.now(timezone.utc).isoformat()
    event = {"timestamp_utc": started, "mode": "SYNTHETIC_TEST_ONLY",
             "source_path": source_path}
    try:
        result = persist_synthetic_batch(connection, fixture, source_path)
        event.update({"status": result["status"], "batch_sha256": result["batch_sha256"],
                      "inserted": result["inserted"]})
        append_audit(audit_path, event)
        return event
    except Exception as exc:
        event.update({"status": "FAILED", "error_class": classify(exc),
                      "exception_type": type(exc).__name__})
        append_audit(audit_path, event)
        raise
