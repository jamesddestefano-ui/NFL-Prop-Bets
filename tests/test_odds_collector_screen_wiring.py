"""Offline collector screening wiring test. No API calls or credentials."""
import ast
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
COLLECTOR=ROOT/"scripts"/"odds_api_collect.py"

class WiringTests(unittest.TestCase):
    def test_direct_script_import_is_resolvable(self):
        tree=ast.parse(COLLECTOR.read_text(encoding="utf-8"))
        imports=[n for n in ast.walk(tree) if isinstance(n,ast.ImportFrom)]
        self.assertTrue(any(n.module=="prime_odds_capture_diagnostics" and
                            any(a.name=="summarize_capture_failures" for a in n.names)
                            for n in imports))
        self.assertTrue((ROOT/"scripts"/"prime_odds_capture_diagnostics.py").is_file())
    def test_screening_is_after_capture(self):
        source=COLLECTOR.read_text(encoding="utf-8")
        self.assertLess(source.index("out.write_text("),source.index("summarize_capture_failures(capture)"))
        self.assertIn('"motherduck_writes":0',source)
if __name__=="__main__": unittest.main()
