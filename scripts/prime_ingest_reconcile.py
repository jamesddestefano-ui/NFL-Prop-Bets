"""Read-only synthetic ingestion reconciliation across batches, quotes and audit.

This module never mutates MotherDuck or interprets synthetic records as prices.
"""
BATCH="my_db.prime_research.ingestion_batches"
QUOTE="my_db.prime_research.odds_quotes"
AUDIT="my_db.prime_research.ingestion_audit_events"

def reconcile_synthetic(connection):
    """Identify batches missing successful audit and inconsistent quote counts."""
    sql=f"""
    WITH quote_counts AS (
      SELECT source_sha256, COUNT(*) AS quote_count
      FROM {QUOTE} WHERE run_id='SYNTHETIC_TEST_ONLY'
      GROUP BY source_sha256
    ), audit_counts AS (
      SELECT batch_sha256,
        COUNT(*) FILTER (WHERE status IN ('INSERTED_SYNTHETIC','ALREADY_INGESTED')) AS success_events,
        COUNT(*) FILTER (WHERE status='FAILED') AS failure_events
      FROM {AUDIT} WHERE source_type='SYNTHETIC_TEST_ONLY'
      GROUP BY batch_sha256
    )
    SELECT b.batch_sha256, b.record_count,
           COALESCE(q.quote_count,0) AS actual_quotes,
           COALESCE(a.success_events,0) AS success_events,
           COALESCE(a.failure_events,0) AS failure_events
    FROM {BATCH} b
    LEFT JOIN quote_counts q ON q.source_sha256=b.batch_sha256
    LEFT JOIN audit_counts a ON a.batch_sha256=b.batch_sha256
    WHERE b.source_type='SYNTHETIC_TEST_ONLY'
    ORDER BY b.batch_sha256
    """
    rows=connection.execute(sql).fetchall()
    findings=[]
    for batch,expected,actual,success,failed in rows:
        reasons=[]
        if expected != actual: reasons.append("QUOTE_COUNT_MISMATCH")
        if success == 0: reasons.append("MISSING_SUCCESS_AUDIT")
        if reasons:
            findings.append({"batch_sha256":batch,"reasons":reasons})
    return {"status":"PASS" if not findings else "REVIEW_REQUIRED",
            "synthetic_batches_checked":len(rows),"findings":findings}
