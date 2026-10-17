import json
import unittest
from scripts.prime_commander_health_contract import assess_health_run, PREFIX
def payload(**overrides):
    d={"status":"PASS","mode":"SYNTHETIC_TEST_ONLY","database_writes":0,"automatic_reimports":0,
       **{k:{"status":"PASS"} for k in ("integrity","reconciliation","orphan_audits","recovery_plan")}}
    d.update(overrides)
    return PREFIX+json.dumps(d)
class Tests(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(assess_health_run("SUCCEEDED",0,payload())["status"],"PASS")
    def test_failed_run(self):
        self.assertEqual(assess_health_run("FAILED",1,payload())["status"],"UNKNOWN")
    def test_missing(self):
        self.assertEqual(assess_health_run("SUCCEEDED",0,"")["status"],"UNKNOWN")
    def test_duplicate(self):
        self.assertEqual(assess_health_run("SUCCEEDED",0,payload()+"\\n"+payload())["status"],"UNKNOWN")
    def test_review(self):
        self.assertEqual(assess_health_run("SUCCEEDED",0,payload(status="REVIEW_REQUIRED"))["status"],"REVIEW_REQUIRED")
    def test_unsafe(self):
        self.assertEqual(assess_health_run("SUCCEEDED",0,payload(database_writes=1))["status"],"UNKNOWN")
    def test_wrong_scope(self):
        self.assertEqual(assess_health_run("SUCCEEDED",0,payload(mode="LIVE"))["status"],"UNKNOWN")
if __name__=="__main__": unittest.main()
