"""Aggregate, privacy-minimized diagnostics for Odds API quote screening.

Never logs raw quotes, player names, odds, or secrets.
"""
from collections import Counter, defaultdict
try:
    from scripts.prime_odds_capture_screen import screen_capture, parse_utc, MARKETS
except ModuleNotFoundError as exc:
    if exc.name != 'scripts':
        raise
    from prime_odds_capture_screen import screen_capture, parse_utc, MARKETS

# Observed in BetRivers NJ UI on 2026-10-17; narrowly scoped and provisional.
# This is not a blanket exemption for the sportsbook or other markets.
ONE_SIDED_OVER_MARKETS = {("betrivers", "player_receptions")}

def summarize_capture_failures(payload):
    base=screen_capture(payload)
    if base["status"]=="QUARANTINED":
        return {**base, "diagnostic_version":2,
                "unexpected_review_groups":0, "expected_one_sided_groups":0,
                "expected_one_sided_by_book_market":[],
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
    missing_by_market=Counter()
    missing_by_book=Counter()
    missing_side_by_book_market=Counter()
    groups_by_book_market=Counter()
    expected_one_sided=Counter()
    for key,sides in groups.items():
        groups_by_book_market[(key[1],key[2])]+=1
        if len(sides)==2 and set(sides)=={"Over","Under"}:
            classified["CLEAN_PAIR"]+=1
        elif len(sides)==1:
            classified["MISSING_OPPOSITE_SIDE"]+=1
            missing_by_book[key[1]]+=1
            missing_by_market[key[2]]+=1
            missing_side_by_book_market[(key[1],key[2], 'Under' if sides[0]=='Over' else 'Over')]+=1
            if (key[1],key[2]) in ONE_SIDED_OVER_MARKETS and sides==["Over"]:
                expected_one_sided[(key[1],key[2])]+=1
        elif len(sides)==2:
            classified["DUPLICATE_SIDE"]+=1
        else:
            classified["EXCESS_OR_CONFLICTING_ROWS"]+=1
    review_groups=sum(v for k,v in classified.items() if k!="CLEAN_PAIR")+sum(invalid.values())
    if review_groups!=base["review_groups"] or classified["CLEAN_PAIR"]!=base["clean_pairs"]:
        raise AssertionError("screening and diagnostics disagree")
    unexpected_reviews=review_groups-sum(expected_one_sided.values())
    return {**base, "diagnostic_version":2,
            "status":"REVIEW_REQUIRED" if unexpected_reviews else ("EXPECTED_ONE_SIDED_OBSERVED" if expected_one_sided else "SCREENED_API_OBSERVATIONS"),
            "unexpected_review_groups":unexpected_reviews,
            "expected_one_sided_groups":sum(expected_one_sided.values()),
            "expected_one_sided_by_book_market":[{"bookmaker":b,"market":m,"groups":n,"evidence":"BETRIVERS_NJ_UI_2026-10-17"} for (b,m),n in sorted(expected_one_sided.items())],
            "observed_quote_rows":len(payload["quotes"]),
            "group_counts":dict(sorted(classified.items())),
            "invalid_row_reasons":dict(sorted(invalid.items())),
            "failure_counts":{"missing_opposite_side":classified["MISSING_OPPOSITE_SIDE"],
                              "duplicate_side":classified["DUPLICATE_SIDE"],
                              "excess_or_conflicting":classified["EXCESS_OR_CONFLICTING_ROWS"],
                              "invalid_rows":sum(invalid.values())},
            "missing_opposite_by_market":dict(sorted(missing_by_market.items())),
            "missing_opposite_by_bookmaker":dict(sorted(missing_by_book.items())),
            "missing_side_direction_by_book_market":[{"bookmaker":b,"market":m,"missing_side":side,"count":n} for (b,m,side),n in sorted(missing_side_by_book_market.items())],
            "book_market_group_coverage":[{"bookmaker":b,"market":m,"total_groups":total,"missing_opposite_groups":sum(n for (bb,mm,_),n in missing_side_by_book_market.items() if bb==b and mm==m),"clean_groups":sum(1 for key,sides in groups.items() if key[1]==b and key[2]==m and len(sides)==2 and set(sides)=={"Over","Under"})} for (b,m),total in sorted(groups_by_book_market.items())],
            "raw_quotes_exported":False}
