import unittest
from scripts.prime_ingest_health_report import build_health_report
class Cursor:
    def __init__(self,row=None,rows=None): self.row=row; self.rows=rows
    def fetchone(self): return self.row
    def fetchall(self): return self.rows
class Fake:
    def __init__(self,integrity,batches,orphans):
        self.values=[Cursor(row=integrity),Cursor(rows=batches),Cursor(rows=orphans)]
        self.calls=0
    def execute(self,sql):
        self.calls+=1
        assert sql.lstrip().upper().startswith(("SELECT","WITH"))
        return self.values[self.calls-1]
class Tests(unittest.TestCase):
    def test_healthy(self):
        db=Fake((1,2,0,0,0,0),[("batch",2,2,1,0)],[])
        report=build_health_report(db)
        self.assertEqual(report["status"],"PASS")
        self.assertEqual(report["database_writes"],0)
        self.assertEqual(db.calls,3)
    def test_orphan_requires_review(self):
        db=Fake((1,2,0,0,0,0),[("batch",2,2,1,0)],[("audit","other","FAILED")])
        self.assertEqual(build_health_report(db)["status"],"REVIEW_REQUIRED")
    def test_mismatch_requires_review(self):
        db=Fake((1,2,0,0,0,0),[("batch",2,1,1,0)],[])
        self.assertEqual(build_health_report(db)["status"],"REVIEW_REQUIRED")
    def test_duplicate_requires_review(self):
        db=Fake((1,2,1,0,0,0),[("batch",2,2,1,0)],[])
        self.assertEqual(build_health_report(db)["status"],"REVIEW_REQUIRED")
if __name__=="__main__": unittest.main()
