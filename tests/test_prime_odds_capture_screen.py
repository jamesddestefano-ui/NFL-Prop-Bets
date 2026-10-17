import unittest
from scripts.prime_odds_capture_screen import screen_capture
def fixture():
    event={"id":"GAME","commence_time":"2026-10-18T17:00:00Z"}
    base={"event_id":"GAME","bookmaker":"test_book","market":"player_receptions",
          "player":"TEST PLAYER","point":5.5,"odds_american":-110,
          "odds_response_received_utc":"2026-10-18T12:00:00Z"}
    return {"event":event,"odds_response_received_utc":"2026-10-18T12:00:00Z",
            "quotes":[{**base,"side":"Over"},{**base,"side":"Under"}]}
class Tests(unittest.TestCase):
    def test_clean_pair(self):
        r=screen_capture(fixture())
        self.assertEqual((r["clean_pairs"],r["review_groups"]),(1,0))
        self.assertFalse(r["eligible_for_motherduck"])
    def test_duplicate_side(self):
        f=fixture();f["quotes"][1]["side"]="Over"
        self.assertEqual(screen_capture(f)["review_groups"],1)
    def test_missing_opposite(self):
        f=fixture();f["quotes"].pop()
        self.assertEqual(screen_capture(f)["review_groups"],1)
    def test_postkickoff(self):
        f=fixture();f["odds_response_received_utc"]="2026-10-18T18:00:00Z"
        self.assertEqual(screen_capture(f)["status"],"QUARANTINED")
    def test_bad_identity(self):
        f=fixture();f["quotes"][0]["event_id"]="WRONG"
        self.assertGreater(screen_capture(f)["review_groups"],0)
    def test_receipt_mismatch(self):
        f=fixture();f["quotes"][0]["odds_response_received_utc"]="2026-10-18T11:00:00Z"
        self.assertGreater(screen_capture(f)["review_groups"],0)
if __name__=="__main__": unittest.main()
