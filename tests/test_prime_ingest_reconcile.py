import unittest
from scripts.prime_ingest_reconcile import reconcile_synthetic
class Fake:
    def __init__(self,rows): self.rows=rows
    def execute(self,sql):
        assert "SYNTHETIC_TEST_ONLY" in sql
        return self
    def fetchall(self): return self.rows
class Tests(unittest.TestCase):
    def test_clean(self):
        self.assertEqual(reconcile_synthetic(Fake([("a",2,2,1,0)]))["status"],"PASS")
    def test_missing_audit(self):
        self.assertEqual(reconcile_synthetic(Fake([("a",2,2,0,0)]))["findings"][0]["reasons"],["MISSING_SUCCESS_AUDIT"])
    def test_quote_mismatch(self):
        self.assertEqual(reconcile_synthetic(Fake([("a",2,1,1,0)]))["findings"][0]["reasons"],["QUOTE_COUNT_MISMATCH"])
    def test_empty(self):
        self.assertEqual(reconcile_synthetic(Fake([]))["synthetic_batches_checked"],0)
if __name__=="__main__": unittest.main()
