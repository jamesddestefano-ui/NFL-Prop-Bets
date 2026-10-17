"""Read-only PRIME MotherDuck ingestion integrity checks.

Caller provides an authenticated connection. No credentials, mutations, or live API calls.
"""
BATCH = "my_db.prime_research.ingestion_batches"
QUOTES = "my_db.prime_research.odds_quotes"

def check_ingestion_integrity(connection):
    """Return aggregate synthetic-only integrity findings; never expose quote contents."""
    sql = f"""
    SELECT
      (SELECT COUNT(*) FROM {BATCH} WHERE source_type='SYNTHETIC_TEST_ONLY') AS batches,
      (SELECT COUNT(*) FROM {QUOTES} WHERE run_id='SYNTHETIC_TEST_ONLY') AS quotes,
      (SELECT COUNT(*) FROM (
         SELECT batch_sha256 FROM {BATCH}
         WHERE source_type='SYNTHETIC_TEST_ONLY'
         GROUP BY batch_sha256 HAVING COUNT(*) > 1
       )) AS duplicate_batches,
      (SELECT COUNT(*) FROM (
         SELECT quote_id FROM {QUOTES}
         WHERE run_id='SYNTHETIC_TEST_ONLY'
         GROUP BY quote_id HAVING COUNT(*) > 1
       )) AS duplicate_quotes,
      (SELECT COUNT(*) FROM {QUOTES} q
         WHERE q.run_id='SYNTHETIC_TEST_ONLY'
           AND q.response_received_utc >= q.commence_time) AS late_quotes,
      (SELECT COUNT(*) FROM {QUOTES} q
         WHERE q.run_id='SYNTHETIC_TEST_ONLY'
           AND NOT EXISTS (SELECT 1 FROM {BATCH} b
             WHERE b.batch_sha256=q.source_sha256 AND b.source_type='SYNTHETIC_TEST_ONLY')) AS orphan_quotes
    """
    row = connection.execute(sql).fetchone()
    if row is None or len(row) != 6:
        raise ValueError("unexpected integrity query result")
    names = ("batches","quotes","duplicate_batches","duplicate_quotes","late_quotes","orphan_quotes")
    metrics = dict(zip(names, map(int,row)))
    metrics["status"] = "PASS" if all(metrics[k] == 0 for k in names[2:]) else "REVIEW_REQUIRED"
    metrics["scope"] = "SYNTHETIC_TEST_ONLY"
    return metrics
