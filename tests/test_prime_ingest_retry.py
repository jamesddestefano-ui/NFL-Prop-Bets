import unittest
from scripts.prime_ingest_retry import decide_retry

class RetryTests(unittest.TestCase):
    def test_transient_connection(self):
        self.assertEqual(decide_retry("CONNECTION_ERROR",1).next_delay_seconds,60)
        self.assertEqual(decide_retry("CONNECTION_ERROR",2).next_delay_seconds,120)
    def test_budget_exhausted(self):
        self.assertEqual(decide_retry("CONNECTION_ERROR",3).action,"REVIEW_REQUIRED")
    def test_validation_never_retried(self):
        self.assertEqual(decide_retry("VALIDATION_REJECTED",1).action,"REVIEW_REQUIRED")
    def test_persistence_never_blindly_retried(self):
        self.assertEqual(decide_retry("PERSISTENCE_ERROR",1).action,"REVIEW_REQUIRED")
    def test_unknown_fail_closed(self):
        self.assertEqual(decide_retry("UNKNOWN",1).action,"REVIEW_REQUIRED")
    def test_invalid_attempt(self):
        with self.assertRaises(ValueError): decide_retry("CONNECTION_ERROR",0)
if __name__=="__main__": unittest.main()
