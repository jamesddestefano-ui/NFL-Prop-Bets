import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from capture import MARKETS, allowed_slot, validate_books, save_new

class B18CaptureTests(unittest.TestCase):
    def test_six_markets(self):
        self.assertEqual(len(MARKETS), 6)
        self.assertEqual(len(set(MARKETS)), 6)

    def test_seven_books(self):
        self.assertEqual(len(validate_books("a,b,c,d,e,f,g")), 7)
        with self.assertRaises(ValueError):
            validate_books("a,b,c")

    def test_slot_boundary(self):
        kickoff = datetime(2026, 11, 1, 21, tzinfo=timezone.utc)
        self.assertTrue(allowed_slot("t30", kickoff, kickoff-timedelta(minutes=30), 3))
        self.assertFalse(allowed_slot("t30", kickoff, kickoff-timedelta(minutes=20), 3))
        self.assertFalse(allowed_slot("freeze", kickoff, kickoff, 3))

    def test_append_only(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            save_new(root, "one.json", {"id": 1})
            with self.assertRaises(FileExistsError):
                save_new(root, "one.json", {"id": 2})
