import json
import tempfile
import unittest
from pathlib import Path
from scripts.prime_ingest_boundary import synthetic_fixture
from scripts.prime_ingest_runner import run_ingestion
from tests_support_prime import FakeConnection

class AuditTests(unittest.TestCase):
    def test_success_and_duplicate_audit(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "audit.jsonl"
            db = FakeConnection()
            first = run_ingestion(db, synthetic_fixture(), path)
            second = run_ingestion(db, synthetic_fixture(), path)
            self.assertEqual(first["status"], "INSERTED_SYNTHETIC")
            self.assertEqual(second["status"], "ALREADY_INGESTED")
            rows = [json.loads(line) for line in path.read_text().splitlines()]
            self.assertEqual(len(rows), 2)
            self.assertTrue(all("quotes" not in r for r in rows))

    def test_failure_classification_and_audit(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "audit.jsonl"
            fixture = synthetic_fixture()
            fixture["fixture_type"] = "LIVE"
            with self.assertRaises(ValueError):
                run_ingestion(FakeConnection(), fixture, path)
            row = json.loads(path.read_text().strip())
            self.assertEqual(row["error_class"], "VALIDATION_REJECTED")
            self.assertEqual(row["status"], "FAILED")

if __name__ == "__main__":
    unittest.main()
