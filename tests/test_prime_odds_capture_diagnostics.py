import unittest
from scripts.prime_odds_capture_diagnostics import summarize_capture_failures
def fixture():
    b={"event_id":"E","bookmaker":"book","market":"player_receptions","player":"TEST",
       "point":5.5,"odds_american":-110,"odds_response_received_utc":"2026-10-18T12:00:00Z"}
    return {"event":{"id":"E","commence_time":"2026-10-18T17:00:00Z"},
            "odds_response_received_utc":"2026-10-18T12:00:00Z",
            "quotes":[{**b,"side":"Over"},{**b,"side":"Under"}]}
class Tests(unittest.TestCase):
    def test_clean(self):
        r=summarize_capture_failures(fixture())
        self.assertEqual(r["clean_pairs"],1)
        self.assertEqual(r["review_groups"],0)
        self.assertNotIn("TEST",str(r))
    def test_missing_side(self):
        f=fixture();f["quotes"].pop()
        r=summarize_capture_failures(f)
        self.assertEqual(r["failure_counts"]["missing_opposite_side"],1)
        self.assertEqual(r["missing_opposite_by_market"],{"player_receptions":1})
        self.assertEqual(r["missing_opposite_by_bookmaker"],{"book":1})
        self.assertEqual(r["missing_side_direction_by_book_market"][0]["missing_side"],"Under")
        self.assertEqual(r["book_market_group_coverage"][0]["missing_opposite_groups"],1)
    def test_duplicate_side(self):
        f=fixture();f["quotes"][1]["side"]="Over"
        self.assertEqual(summarize_capture_failures(f)["failure_counts"]["duplicate_side"],1)
    def test_extra_rows(self):
        f=fixture();f["quotes"].append(dict(f["quotes"][0]))
        self.assertEqual(summarize_capture_failures(f)["failure_counts"]["excess_or_conflicting"],1)
    def test_invalid(self):
        f=fixture();f["quotes"][0]["odds_american"]=0
        r=summarize_capture_failures(f)
        self.assertEqual(r["failure_counts"]["invalid_rows"],1)
        self.assertEqual(r["failure_counts"]["missing_opposite_side"],1)
    def test_nonpregame(self):
        f=fixture();f["odds_response_received_utc"]="2026-10-18T17:00:00Z"
        self.assertEqual(summarize_capture_failures(f)["status"],"QUARANTINED")
if __name__=="__main__": unittest.main()
