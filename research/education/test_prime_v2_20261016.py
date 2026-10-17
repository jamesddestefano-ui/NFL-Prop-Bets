"""PRIME v2 synthetic arithmetic and market-integrity regression tests.
Run: python -m unittest research/education/test_prime_v2_20261016.py -v
No live bookmaker data or staking.
"""
import unittest

def decimal(odds):
    if odds == 0: raise ValueError("odds cannot be zero")
    return 1 + (100 / abs(odds) if odds < 0 else odds / 100)

def ev(odds, win, push=0):
    if not (0 <= win <= 1 and 0 <= push <= 1 and win + push <= 1):
        raise ValueError("invalid probability simplex")
    return win * decimal(odds) + push - 1

def gate(odds, win, conservative_win, push=0, touchdown=False, calibrated=True, verified=True):
    if not calibrated or not verified: return "WATCH"
    if touchdown or odds < -150 or odds > 150:
        qualifies = ev(odds,win,push) >= .15-1e-12
    else:
        qualifies = win - (1-push)/decimal(odds) >= .04-1e-12
    return "ELIGIBLE_RESEARCH" if qualifies and ev(odds,conservative_win,push) >= -1e-12 else "PASS"

IDENTITY = ("event_id","book","player","market","side","line","odds","settlement")

def changed(before, after):
    return any(before.get(k) != after.get(k) for k in IDENTITY)

class Tests(unittest.TestCase):
    def test_push_correct(self): self.assertAlmostEqual(ev(100,.46,.1),.02)
    def test_push_shortcut_wrong(self): self.assertNotAlmostEqual(ev(100,.46,.1),.46*2-1)
    def test_standard_boundary(self): self.assertEqual(gate(-110,1/decimal(-110)+.04,1/decimal(-110)),"ELIGIBLE_RESEARCH")
    def test_no_roi_gate(self): self.assertEqual(gate(-150,1/decimal(-150)+.04,1/decimal(-150)),"ELIGIBLE_RESEARCH")
    def test_conservative_negative(self): self.assertEqual(gate(-110,.60,.50),"PASS")
    def test_td_below(self): self.assertEqual(gate(200,.37,1/3,touchdown=True),"PASS")
    def test_td_boundary(self): self.assertEqual(gate(200,1.15/3,1/3,touchdown=True),"ELIGIBLE_RESEARCH")
    def test_uncalibrated(self): self.assertEqual(gate(-110,.65,.55,calibrated=False),"WATCH")
    def test_unverified(self): self.assertEqual(gate(-110,.65,.55,verified=False),"WATCH")
    def test_timestamp_only_not_change(self):
        a=dict(event_id='x',book='a',player='b',market='receptions',side='over',line=4.5,odds=-110,settlement='standard',updated='10:00')
        self.assertFalse(changed(a,{**a,'updated':'10:01'}))
    def test_odds_change(self): self.assertTrue(changed({'odds':-110},{'odds':-115}))
    def test_line_change(self): self.assertTrue(changed({'line':4.5},{'line':5.5}))
    def test_binary_identity(self):
        for o in (-150,-110,100,150,200):
            for p in (.3,.5,.7):
                self.assertAlmostEqual(ev(o,p),(p-1/decimal(o))*decimal(o))
    def test_push_edge_not_enough(self): self.assertEqual(gate(100,.46,.45,.1),"PASS")
    def test_probability_validation(self):
        with self.assertRaises(ValueError): ev(-110,.95,.1)

if __name__ == "__main__": unittest.main()
