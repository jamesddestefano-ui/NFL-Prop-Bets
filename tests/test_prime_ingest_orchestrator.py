import unittest
from scripts.prime_ingest_boundary import synthetic_fixture
from scripts.prime_ingest_orchestrator import ingest_with_durable_audit
from tests_support_prime import FakeConnection

class Cursor:
    def __init__(self, n): self.n=n
    def fetchone(self): return (self.n,)
class AuditDB:
    def __init__(self, fail=False):
        self.events=set(); self.pending=None; self.fail=fail
    def execute(self, sql, params=None):
        if sql=="BEGIN TRANSACTION": self.pending=None
        elif sql.startswith("SELECT COUNT(*)"): return Cursor(int(params[0] in self.events))
        elif sql.startswith("INSERT INTO"):
            if self.fail: raise RuntimeError("audit unavailable")
            self.pending=params[0]
        elif sql=="COMMIT":
            if self.pending: self.events.add(self.pending)
            self.pending=None
        elif sql=="ROLLBACK": self.pending=None
        return Cursor(0)

class OrchestratorTests(unittest.TestCase):
    def test_success_and_duplicate(self):
        q=FakeConnection(); a=AuditDB()
        first=ingest_with_durable_audit(q,a,synthetic_fixture())
        second=ingest_with_durable_audit(q,a,synthetic_fixture())
        self.assertEqual(first["inserted"],2)
        self.assertEqual(second["inserted"],0)
        self.assertEqual(len(a.events),2)

    def test_invalid_fixture_creates_failure_audit(self):
        q=FakeConnection(); a=AuditDB()
        fixture=synthetic_fixture(); fixture["fixture_type"]="LIVE"
        with self.assertRaises(ValueError):
            ingest_with_durable_audit(q,a,fixture)
        self.assertEqual(len(a.events),1)

    def test_audit_unavailable_fails_closed(self):
        q=FakeConnection(); a=AuditDB(fail=True)
        with self.assertRaises(RuntimeError):
            ingest_with_durable_audit(q,a,synthetic_fixture())
        self.assertEqual(len(a.events),0)
        # A successful quote commit may have occurred; reconciliation is required.
        self.assertEqual(len(q.fingerprints),1)
if __name__=="__main__": unittest.main()
