"""Offline validation regressions for synthetic ingestion audit identity."""
import unittest
from scripts.prime_ingest_audit_db import make_event, persist_audit_event

class RejectConnection:
    def __init__(self): self.calls=[]
    def execute(self, sql, params=None):
        self.calls.append((sql, params))
        raise AssertionError("validation must precede transaction")

class AuditIdentityTests(unittest.TestCase):
    def base_event(self):
        return make_event("a"*64, "INSERTED_SYNTHETIC", quote_count=2,
                          observed_at_utc="2026-10-17T05:00:00+00:00")

    def assert_rejected_before_sql(self, changes):
        event=self.base_event()
        event.update(changes)
        db=RejectConnection()
        with self.assertRaises(ValueError):
            persist_audit_event(db, event)
        self.assertEqual(db.calls, [])

    def test_mismatched_identity(self):
        self.assert_rejected_before_sql({"audit_event_id":"0"*64})
    def test_inconsistent_success_classification(self):
        self.assert_rejected_before_sql({"error_class":"PERSISTENCE_ERROR"})
    def test_invalid_timestamp_and_hash(self):
        self.assert_rejected_before_sql({"observed_at_utc":"2026-10-17T05:00:00"})
        self.assert_rejected_before_sql({"batch_sha256":"x"*64})
    def test_invalid_attempt_and_quote_count(self):
        self.assert_rejected_before_sql({"attempt_number":0})
        self.assert_rejected_before_sql({"quote_count":True})

if __name__=="__main__": unittest.main()
