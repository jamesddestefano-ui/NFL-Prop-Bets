"""Synthetic timestamp boundary regressions for PRIME NFL player-prop collector.

Run: python -m unittest discover -s tests -p 'test_odds_capture_boundary.py' -v
No API key, HTTP calls, or live sportsbook lines required.
"""
import ast
import datetime as dt
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "scripts" / "odds_api_collect.py"
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
FUNCTIONS = {node.name: node for node in TREE.body if isinstance(node, ast.FunctionDef)}
fn = FUNCTIONS["strictly_pregame"]
module = ast.Module(body=[fn], type_ignores=[])
scope = {}
exec(compile(ast.fix_missing_locations(module), str(SOURCE), "exec"), scope)
K = dt.datetime.fromisoformat("2026-10-18T13:30:00+00:00")


class CaptureBoundaryTests(unittest.TestCase):
    def test_receipt_before_kickoff(self):
        self.assertTrue(scope["strictly_pregame"](K - dt.timedelta(microseconds=1), K))

    def test_receipt_exactly_at_kickoff_rejected(self):
        self.assertFalse(scope["strictly_pregame"](K, K))

    def test_receipt_after_kickoff_rejected(self):
        self.assertFalse(scope["strictly_pregame"](K + dt.timedelta(seconds=1), K))

    def test_started_before_and_finished_after(self):
        sent = K - dt.timedelta(seconds=10)
        received = K + dt.timedelta(seconds=1)
        self.assertTrue(sent < K)
        self.assertFalse(scope["strictly_pregame"](received, K))

    def test_exact_membership_not_substring(self):
        assignment = next(n for n in TREE.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "MARKET_KEYS" for t in n.targets))
        allowed = ast.literal_eval(assignment.value)
        self.assertIn("player_rush_yds", allowed)
        self.assertNotIn("player_rush", allowed)
        self.assertNotIn("player_reception", allowed)

    def test_capture_semantics_present(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn('strictly_pregame(odds_received,kickoff)', src)
        self.assertIn('"observed_at_utc":odds_received.isoformat()', src)
        self.assertIn('"odds_response_received_utc":odds_received.isoformat()', src)


if __name__ == "__main__":
    unittest.main()
