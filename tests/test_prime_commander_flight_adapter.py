import json
import unittest
from datetime import datetime, timezone
from scripts.prime_commander_flight_adapter import assess_latest_flight
from scripts.prime_commander_health_contract import PREFIX
NOW=datetime(2026,10,17,16,0,tzinfo=timezone.utc)
def logs():
    return PREFIX+json.dumps({"status":"PASS","mode":"SYNTHETIC_TEST_ONLY",
      "database_writes":0,"automatic_reimports":0,
      **{k:{"status":"PASS"} for k in ("integrity","reconciliation","orphan_audits","recovery_plan")}})
def run(**kwargs):
    d={"status":"SUCCEEDED","exit_code":0,"ended_at":"2026-10-17T15:02:49Z","run_number":1}
    d.update(kwargs)
    return d
class Tests(unittest.TestCase):
    def test_fresh_success(self):
        self.assertEqual(assess_latest_flight(run(),logs(),NOW)["status"],"PASS")
    def test_stale(self):
        self.assertEqual(assess_latest_flight(run(),logs(),NOW,max_age_minutes=30)["reason"],"STALE_OR_FUTURE_RUN")
    def test_failed(self):
        self.assertEqual(assess_latest_flight(run(status="FAILED",exit_code=1),logs(),NOW)["status"],"UNKNOWN")
    def test_missing_logs(self):
        self.assertEqual(assess_latest_flight(run(),None,NOW)["status"],"UNKNOWN")
    def test_missing_timestamp(self):
        self.assertEqual(assess_latest_flight(run(ended_at=None),logs(),NOW)["status"],"UNKNOWN")
    def test_future_timestamp(self):
        self.assertEqual(assess_latest_flight(run(ended_at="2026-10-18T15:00:00Z"),logs(),NOW)["status"],"UNKNOWN")
if __name__=="__main__": unittest.main()
