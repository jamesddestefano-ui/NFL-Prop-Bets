"""Aggregate, privacy-minimized diagnostics for Odds API quote screening.

Never logs raw quotes, player names, odds, or secrets.
"""
from collections import Counter, defaultdict
from scripts.prime_odds_capture_screen import screen_capture, parse_utc, MARKETS

def summarize_capture_failures(payload):
    base=screen_capture(payload)
    if base["status"]=="QUARANTINED":
        return {**base, "diagnostic_version":1,
                "failure_counts":{"NOT_PREGAME":1},
                "group_counts":{}, "observed_quote_rows":len(payload["quotes"])}
    event=payload["event"]
    receipt=parse_utc(payload["odds_response_received_utc"])
    groups=defaultdict(list)
    invalid=Counter()
    for q in payload["quotes"]:
        if not isinstance(q,dict):
            invalid["NON_OBJECT_ROW"]+=1
            continue
        if q.get("event_id")!=event.get("id") or q.get("market") not in MARKETS:
            invalid["BAD_IDENTITY_OR_MARKET"]+=1
            continue
        if q.get("side") not in ("Over","Under"):
            invalid["BAD_SIDE"]+=1
            continue
        if not all(isinstance(q.get(k),str) and q[k].strip()
                   for k in ("bookmaker","player")):
            invalid["MISSING_IDENTIFIER"]+=1
            continue
        point,price=q.get("point"),q.get("odds_american")
        if isinstance(point,bool) or not isinstance(point,(int,float)) or not 0<=point<1000:
            invalid["BAD_POINT"]+=1
            continue
        if isinstance(price,bool) or not isinstance(price,(int,float)) or not (price<=-100 or price>=100):
            invalid["BAD_PRICE"]+=1
            continue
        try:
            if parse_utc(q.get("odds_response_received_utc"))!=receipt:
                raise ValueError("mismatch")
        except (ValueError,TypeError,OverflowError):
            invalid["BAD_RECEIPT"]+=1
            continue
        key=(q["event_id"],q["bookmaker"],q["market"],q["player"],point)
        groups[key].append(q["side"])
    classified=Counter()
    for sides in groups.values():
        if len(sides)==2 and set(sides)=={"Over","Under"}:
            classified["CLEAN_PAIR"]+=1
        elif len(sides)==1:
            classified["MISSING_OPPOSITE_SIDE"]+=1
        elif len(sides)==2:
            classified["DUPLICATE_SIDE"]+=1
        else:
            classified["EXCESS_OR_CONFLICTING_ROWS"]+=1
    review_groups=sum(v for k,v in classified.items() if k!="CLEAN_PAIR")+sum(invalid.values())
    if review_groups!=base["review_groups"] or classified["CLEAN_PAIR"]!=base["clean_pairs"]:
        raise AssertionError("screening and diagnostics disagree")
    return {**base, "diagnostic_version":1,
            "observed_quote_rows":len(payload["quotes"]),
            "group_counts":dict(sorted(classified.items())),
            "invalid_row_reasons":dict(sorted(invalid.items())),
            "failure_counts":{"missing_opposite_side":classified["MISSING_OPPOSITE_SIDE"],
                              "duplicate_side":classified["DUPLICATE_SIDE"],
                              "excess_or_conflicting":classified["EXCESS_OR_CONFLICTING_ROWS"],
                              "invalid_rows":sum(invalid.values())},
            "raw_quotes_exported":False}
