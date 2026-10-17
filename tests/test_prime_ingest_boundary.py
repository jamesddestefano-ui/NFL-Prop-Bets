import copy
import unittest
from scripts.prime_ingest_boundary import synthetic_fixture, validate_batch

class TestPrimeIngest(unittest.TestCase):
    def test_clean_fixture(self):
        result = validate_batch(synthetic_fixture())
        self.assertEqual(result["record_count"], 2)
        self.assertEqual(len(result["batch_sha256"]), 64)

    def test_deterministic_idempotency_key(self):
        a = synthetic_fixture()
        self.assertEqual(validate_batch(a)["batch_sha256"],
                         validate_batch(copy.deepcopy(a))["batch_sha256"])

    def test_live_data_rejected(self):
        a = synthetic_fixture()
        a["fixture_type"] = "LIVE"
        with self.assertRaises(ValueError):
            validate_batch(a)

    def test_missing_side_rejected(self):
        a = synthetic_fixture()
        a["quotes"].pop()
        with self.assertRaises(ValueError):
            validate_batch(a)

    def test_duplicate_rejected(self):
        a = synthetic_fixture()
        a["quotes"].append(copy.deepcopy(a["quotes"][0]))
        with self.assertRaises(ValueError):
            validate_batch(a)

    def test_post_kickoff_rejected(self):
        a = synthetic_fixture()
        a["quotes"][0]["response_received_utc"] = "2026-10-18T17:00:00Z"
        with self.assertRaises(ValueError):
            validate_batch(a)

    def test_missing_timestamp_timezone_rejected(self):
        a = synthetic_fixture()
        a["quotes"][0]["response_received_utc"] = "2026-10-18T12:00:00"
        with self.assertRaises(ValueError):
            validate_batch(a)

    def test_unsupported_market_rejected(self):
        a = synthetic_fixture()
        a["quotes"][0]["market"] = "player_pass_tds"
        with self.assertRaises(ValueError):
            validate_batch(a)

if __name__ == "__main__":
    unittest.main()
