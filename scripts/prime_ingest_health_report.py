"""PRIME synthetic ingestion health report. Read-only and fail-closed."""
import json
from datetime import datetime, timezone
from scripts.prime_ingest_healthcheck import check_ingestion_integrity
from scripts.prime_ingest_reconcile import reconcile_synthetic, find_orphan_audit_events, plan_recovery

def build_health_report(connection):
    integrity=check_ingestion_integrity(connection)
    reconciliation=reconcile_synthetic(connection)
    orphans=find_orphan_audit_events(connection)
    recovery=plan_recovery(reconciliation,orphans)
    status="PASS" if all(item["status"]=="PASS" for item in (integrity,reconciliation,orphans,recovery)) else "REVIEW_REQUIRED"
    return {"status":status,"mode":"SYNTHETIC_TEST_ONLY",
            "observed_at_utc":datetime.now(timezone.utc).isoformat(),
            "integrity":integrity,"reconciliation":reconciliation,
            "orphan_audits":orphans,"recovery_plan":recovery,
            "database_writes":0,"automatic_reimports":0}

def report_json(connection):
    return json.dumps(build_health_report(connection),sort_keys=True,indent=2)
