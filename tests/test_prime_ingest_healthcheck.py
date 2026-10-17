import unittest
from scripts.prime_ingest_healthcheck import check_ingestion_integrity

class Cursor:
    def __init__(self, row): self.row=row
    def fetchone(self): return self.row
class Fake:
    def __init__(self, row): self.row=row; self.sql=None
    def execute(self, sql): self.sql=sql; return Cursor(self.row)

class IntegrityTests(unittest.TestCase):
    def test_clean(self):
        conn=Fake((1,2,0,0,0,0))
        result=check_ingestion_integrity(conn)
        self.assertEqual(result["status"],"PASS")
        self.assertIn("source_type='SYNTHETIC_TEST_ONLY'",conn.sql)
    def test_orphan_detected(self):
        self.assertEqual(check_ingestion_integrity(Fake((1,2,0,0,0,1)))["status"],"REVIEW_REQUIRED")
    def test_duplicate_detected(self):
        self.assertEqual(check_ingestion_integrity(Fake((2,4,1,0,0,0)))["status"],"REVIEW_REQUIRED")
    def test_late_quote_detected(self):
        self.assertEqual(check_ingestion_integrity(Fake((1,2,0,0,1,0)))["status"],"REVIEW_REQUIRED")
    def test_malformed_response(self):
        with self.assertRaises(ValueError):
            check_ingestion_integrity(Fake((1,2)))
if __name__=="__main__": unittest.main()
