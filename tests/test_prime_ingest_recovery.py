import unittest
from scripts.prime_ingest_reconcile import find_orphan_audit_events, plan_recovery
class Fake:
    def __init__(self,rows): self.rows=rows
    def execute(self,sql):
        assert "a.batch_sha256 IS NOT NULL" in sql
        return self
    def fetchall(self): return self.rows
class RecoveryTests(unittest.TestCase):
    def test_no_orphans(self):
        self.assertEqual(find_orphan_audit_events(Fake([]))["status"],"PASS")
    def test_orphan_detection(self):
        result=find_orphan_audit_events(Fake([("audit1","batch1","FAILED")]))
        self.assertEqual(result["status"],"REVIEW_REQUIRED")
        self.assertEqual(len(result["orphan_audit_events"]),1)
    def test_recovery_never_reimports(self):
        reconciliation={"findings":[{"batch_sha256":"batch1","reasons":["MISSING_SUCCESS_AUDIT"]}]}
        orphans={"orphan_audit_events":[{"audit_event_id":"audit1","batch_sha256":"batch2","status":"FAILED"}]}
        plan=plan_recovery(reconciliation,orphans)
        self.assertEqual(plan["automatic_reimports"],0)
        self.assertEqual(len(plan["tasks"]),2)
    def test_clean_recovery_plan(self):
        self.assertEqual(plan_recovery({"findings":[]},{"orphan_audit_events":[]})["status"],"PASS")
if __name__=="__main__": unittest.main()
