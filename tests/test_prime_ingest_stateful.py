"""Synthetic-only stateful persistence regression; no external database."""
import copy
import unittest
from scripts.prime_ingest_boundary import synthetic_fixture
from scripts.prime_ingest_persist import persist_synthetic_batch

class Cursor:
    def __init__(self, n=0): self.n=n
    def fetchone(self): return (self.n,)

class FakeDB:
    def __init__(self, fail_quote=None):
        self.batches={}; self.quotes={}; self.pending=None
        self.fail_quote=fail_quote; self.attempts=0
    def execute(self, sql, params=None):
        if sql=="BEGIN TRANSACTION":
            self.pending=(copy.deepcopy(self.batches),copy.deepcopy(self.quotes))
        elif sql.startswith("SELECT COUNT(*)"):
            return Cursor(int(params[0] in self.pending[0]))
        elif "INSERT INTO my_db.prime_research.ingestion_batches" in sql:
            self.pending[0][params[0]]=params
        elif "INSERT INTO my_db.prime_research.odds_quotes" in sql:
            self.attempts+=1
            if self.attempts==self.fail_quote: raise RuntimeError("injected failure")
            self.pending[1][params[1]]=params
        elif sql=="COMMIT":
            self.batches,self.quotes=self.pending
            self.pending=None
        elif sql=="ROLLBACK": self.pending=None
        else: raise AssertionError(sql)
        return Cursor()

class StatefulTests(unittest.TestCase):
    def test_rows_and_duplicate(self):
        db=FakeDB()
        self.assertEqual(persist_synthetic_batch(db,synthetic_fixture())["inserted"],2)
        self.assertEqual({v[7] for v in db.quotes.values()},{"Over","Under"})
        self.assertEqual((len(db.batches),len(db.quotes)),(1,2))
        self.assertEqual(persist_synthetic_batch(db,synthetic_fixture())["status"],"ALREADY_INGESTED")
        self.assertEqual((len(db.batches),len(db.quotes)),(1,2))
    def test_rollback_and_retry(self):
        db=FakeDB(fail_quote=2)
        with self.assertRaises(RuntimeError): persist_synthetic_batch(db,synthetic_fixture())
        self.assertEqual((len(db.batches),len(db.quotes)),(0,0))
        db.fail_quote=None
        self.assertEqual(persist_synthetic_batch(db,synthetic_fixture())["inserted"],2)
        self.assertEqual((len(db.batches),len(db.quotes)),(1,2))
    def test_identity_mismatch_is_rejected_before_transaction(self):
        db=FakeDB(); fixture=synthetic_fixture()
        fixture["quotes"][1]["point"]=6.5
        with self.assertRaises(ValueError): persist_synthetic_batch(db,fixture)
        self.assertIsNone(db.pending)

if __name__=="__main__": unittest.main()
