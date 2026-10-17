"""Read-only Odds API capture screening. Never imports live quotes into MotherDuck.

This is a source-quality gate, not an executable-price or betting decision gate.
"""
from collections import defaultdict
from datetime import datetime, timezone

MARKETS={"player_receptions","player_reception_yds","player_rush_yds"}

def parse_utc(value):
    if not isinstance(value,str):
        raise ValueError("missing timestamp")
    dt=datetime.fromisoformat(value.replace("Z","+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timezone required")
    return dt.astimezone(timezone.utc)

def screen_capture(payload):
    if not isinstance(payload,dict) or not isinstance(payload.get("quotes"),list):
        raise ValueError("invalid capture envelope")
    event=payload.get("event") or {}
    kickoff=parse_utc(event.get("commence_time"))
    receipt=parse_utc(payload.get("odds_response_received_utc"))
    if receipt>=kickoff:
        return {"status":"QUARANTINED","reason":"NOT_PREGAME","clean_pairs":0,
                "review_groups":0,"eligible_for_motherduck":False}
    groups=defaultdict(list)
    invalid=0
    for q in payload["quotes"]:
        if not isinstance(q,dict):
            invalid+=1; continue
        try:
            if q.get("event_id")!=event.get("id") or q.get("market") not in MARKETS:
                raise ValueError("identity")
            if q.get("side") not in ("Over","Under"):
                raise ValueError("side")
            if not all(isinstance(q.get(k),str) and q[k].strip()
                       for k in ("bookmaker","player")):
                raise ValueError("identifier")
            point=q.get("point")
            price=q.get("odds_american")
            if isinstance(point,bool) or not isinstance(point,(int,float)) or not 0<=point<1000:
                raise ValueError("point")
            if isinstance(price,bool) or not isinstance(price,(int,float)) or not (price<=-100 or price>=100):
                raise ValueError("price")
            if parse_utc(q.get("odds_response_received_utc"))!=receipt:
                raise ValueError("receipt mismatch")
            key=(q["event_id"],q["bookmaker"],q["market"],q["player"],point)
            groups[key].append(q["side"])
        except (ValueError,TypeError,OverflowError):
            invalid+=1
    clean=sum(len(v)==2 and set(v)=={"Over","Under"} for v in groups.values())
    review=len(groups)-clean+invalid
    return {"status":"REVIEW_REQUIRED" if review else "SCREENED_API_OBSERVATIONS",
            "clean_pairs":clean,"review_groups":review,"invalid_rows":invalid,
            "eligible_for_motherduck":False,
            "price_status":"API_OBSERVED_NOT_EXECUTABLE_VERIFIED"}
