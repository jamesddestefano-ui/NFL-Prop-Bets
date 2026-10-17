import unittest
from scripts.prime_ingest_audit_db import make_event, persist_audit_event

class Cursor:
    def __init__(self, value): self.value=value
    def fetchone(self): return (self.value,)
class Fake:
    def __init__(self, fail=False):
        self.ids=set(); self.pending=None; self.fail=fail
    def execute(self, sql, params=None):
        if sql=="BEGIN TRANSACTION": self.pending=None
        elif sql.startswith("SELECT COUNT(*)"): return Cursor(int(params[0] in self.ids))
        elif sql.startswith("INSERT INTO"):
            if self.fail: raise RuntimeError("injected failure")
            self.pending=params[0]
        elif sql=="COMMIT":
            if self.pending: self.ids.add(self.pending)
            self.pending=None
        elif sql=="ROLLBACK": self.pending=None
        else: raise AssertionError(sql)
        return Cursor(0)
class Tests(unittest.TestCase):
    def event(self):
        return make_event("a"*64,"INSERTED_SYNTHETIC",quote_count=2,
                          observed_at_utc="2026-10-17T05:00:00+00:00")
    def test_insert(self):
        self.assertEqual(persist_audit_event(Fake(),self.event()),"RECORDED")
    def test_duplicate(self):
        db=Fake(); event=self.event()
        self.assertEqual(persist_audit_event(db,event),"RECORDED")
        self.assertEqual(persist_audit_event(db,event),"ALREADY_RECORDED")
        self.assertEqual(len(db.ids),1)
    def test_rollback(self):
        db=Fake(fail=True)
        with self.assertRaises(RuntimeError): persist_audit_event(db,self.event())
        self.assertEqual(len(db.ids),0)
    def test_invalid_status(self):
        with self.assertRaises(ValueError): make_event(None,"BET")
    def test_failure_classification(self):
        self.assertEqual(make_event(None,"FAILED",error_class="CONNECTION_ERROR")["status"],"FAILED")
    def test_live_rejected(self):
        event=self.event(); event["source_type"]="LIVE"
        with self.assertRaises(ValueError): persist_audit_event(Fake(),event)
if __name__=="__main__": unittest.main()
