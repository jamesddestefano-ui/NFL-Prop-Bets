"""Offline transactional persistence tests; no MotherDuck credentials needed."""
import copy
import unittest
from scripts.prime_ingest_boundary import synthetic_fixture
from scripts.prime_ingest_persist import persist_synthetic_batch

class Cursor:
    def __init__(self, value): self.value = value
    def fetchone(self): return (self.value,)

class FakeConnection:
    def __init__(self, fail_on_quote=False, exists=0):
        self.calls = []
        self.fail_on_quote = fail_on_quote
        self.exists = exists
    def execute(self, sql, params=None):
        self.calls.append((sql, params))
        if self.fail_on_quote and "INSERT INTO my_db.prime_research.odds_quotes" in sql:
            raise RuntimeError("simulated database failure")
        return Cursor(self.exists if "SELECT COUNT" in sql else 0)

class PersistenceTests(unittest.TestCase):
    def test_two_quotes_atomic(self):
        conn = FakeConnection()
        result = persist_synthetic_batch(conn, synthetic_fixture())
        self.assertEqual(result["status"], "INSERTED_SYNTHETIC")
        self.assertEqual(result["inserted"], 2)
        self.assertEqual(conn.calls[0][0], "BEGIN TRANSACTION")
        self.assertEqual(conn.calls[-1][0], "COMMIT")
        self.assertEqual(sum("INSERT INTO my_db.prime_research.odds_quotes" in s for s,_ in conn.calls), 2)

    def test_existing_batch_is_noop(self):
        conn = FakeConnection(exists=1)
        self.assertEqual(persist_synthetic_batch(conn, synthetic_fixture())["status"], "ALREADY_INGESTED")
        self.assertFalse(any("INSERT INTO" in s for s,_ in conn.calls))

    def test_rollback_on_quote_failure(self):
        conn = FakeConnection(fail_on_quote=True)
        with self.assertRaises(RuntimeError):
            persist_synthetic_batch(conn, synthetic_fixture())
        self.assertEqual(conn.calls[-1][0], "ROLLBACK")

    def test_live_rejected_before_transaction(self):
        conn = FakeConnection()
        fixture = synthetic_fixture()
        fixture["fixture_type"] = "LIVE"
        with self.assertRaises(ValueError):
            persist_synthetic_batch(conn, fixture)
        self.assertEqual(conn.calls, [])

    def test_source_path_gate(self):
        conn = FakeConnection()
        with self.assertRaises(ValueError):
            persist_synthetic_batch(conn, synthetic_fixture(), "live/api.json")
        self.assertEqual(conn.calls, [])

if __name__ == "__main__":
    unittest.main()
