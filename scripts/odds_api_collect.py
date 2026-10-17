#!/usr/bin/env python3
"""Read-only NFL player-prop API collector; never logs credentials or URLs."""
import datetime as dt, json, os, pathlib, sys, urllib.parse, urllib.request, urllib.error
BASE="https://api.the-odds-api.com/v4"
KEY=os.environ.get("ODDS_API_KEY")
if not KEY:
    sys.exit("Missing ODDS_API_KEY GitHub Actions secret")
MARKET_KEYS=("player_receptions","player_reception_yds","player_rush_yds")
MARKETS=",".join(MARKET_KEYS)
def utc_now():
    return dt.datetime.now(dt.timezone.utc)
def from_iso(value):
    return dt.datetime.fromisoformat(value.replace("Z","+00:00"))
def strictly_pregame(received, kickoff):
    return received < kickoff
def get(endpoint, params):
    query=urllib.parse.urlencode({**params,"apiKey":KEY})
    req=urllib.request.Request(BASE+endpoint+"?"+query,headers={"User-Agent":"PRIME-NFL-Research/1"})
    sent_at=utc_now()
    try:
        with urllib.request.urlopen(req,timeout=20) as response:
            payload=json.load(response)
            received_at=utc_now()
            quota={k:response.headers.get(k) for k in ("x-requests-remaining","x-requests-used","x-requests-last")}
            return payload,quota,sent_at,received_at
    except urllib.error.HTTPError as e:
        sys.exit("Odds API HTTP "+str(e.code)+"; check quota, access and supported markets. URL suppressed.")
    except Exception:
        sys.exit("Odds API request failed; URL and credentials suppressed.")
events,q0,event_sent,event_received=get("/sports/americanfootball_nfl/events",{"dateFormat":"iso"})
upcoming=[e for e in events if strictly_pregame(event_received,from_iso(e["commence_time"]))]
upcoming.sort(key=lambda e:e["commence_time"])
# Free-tier safe: exactly one upcoming game and three markets, one region.
if not upcoming: 
    print("No upcoming NFL events; no paid calls for event odds.")
    sys.exit(0)
event=upcoming[0]
kickoff=from_iso(event["commence_time"])
if not strictly_pregame(utc_now(),kickoff):
    print("Selected game reached scheduled kickoff before odds request; no odds request made.")
    sys.exit(0)
data,q,odds_sent,odds_received=get("/sports/americanfootball_nfl/events/"+urllib.parse.quote(event["id"],safe="")+"/odds",{"regions":"us","markets":MARKETS,"oddsFormat":"american","dateFormat":"iso"})
if not strictly_pregame(odds_received,kickoff):
    print("Odds response completed at/after scheduled kickoff; excluded from pregame archive.")
    sys.exit(0)
if not (event_sent <= event_received <= odds_received and odds_sent <= odds_received):
    sys.exit("Request timestamp ordering anomaly; capture quarantined.")
rows=[]
for book in data.get("bookmakers",[]):
    for market in book.get("markets",[]):
        if market.get("key") not in MARKET_KEYS: continue
        for outcome in market.get("outcomes",[]):
            if outcome.get("name") not in ("Over","Under"):continue
            rows.append({"event_id":event["id"],"commence_time":event["commence_time"],"home_team":event.get("home_team"),"away_team":event.get("away_team"),"bookmaker":book.get("key"),"market":market["key"],"market_last_update":market.get("last_update"),"book_last_update":book.get("last_update"),"player":outcome.get("description"),"side":outcome.get("name"),"point":outcome.get("point"),"odds_american":outcome.get("price"),"observed_at_utc":odds_received.isoformat(),"odds_request_sent_utc":odds_sent.isoformat(),"odds_response_received_utc":odds_received.isoformat(),"region_requested":"us","source":"the-odds-api.com","quote_status":"API_OBSERVED_NOT_EXECUTABLE_VERIFIED"})
folder=pathlib.Path("data/odds_api");folder.mkdir(parents=True,exist_ok=True)
out=folder/(odds_received.strftime("%Y-%m-%dT%H-%M-%S-%fZ")+"-sample.json")
out.write_text(json.dumps({"captured_at":odds_received.isoformat(),"timestamp_semantics":"completed odds response receipt (UTC)","event_request_sent_utc":event_sent.isoformat(),"event_response_received_utc":event_received.isoformat(),"odds_request_sent_utc":odds_sent.isoformat(),"odds_response_received_utc":odds_received.isoformat(),"pregame_eligible":True,"event":{k:event.get(k) for k in ("id","commence_time","home_team","away_team")},"markets_requested":list(MARKET_KEYS),"quotes":rows,"quota":q,"limitations":["Regional US feed not verified equal to NJ executable quotes","No assumption of missing markets as zero","API-observed quote is not a placed wager"]},indent=2)+"\n")
# Screening is read-only; no MotherDuck writes or executable-price promotion.
from prime_odds_capture_diagnostics import summarize_capture_failures
capture=json.loads(out.read_text(encoding="utf-8"))
screen=summarize_capture_failures(capture)
screen_path=out.with_name(out.stem+"-screen.json")
screen_path.write_text(json.dumps({
    "capture_filename":out.name,
    "screened_at_utc":utc_now().isoformat(),
    "screen":screen,
    "mode":"API_OBSERVATION_SCREEN_ONLY",
    "motherduck_writes":0
},sort_keys=True,indent=2)+"\\n",encoding="utf-8")
print("Saved",str(out),"rows",len(rows),"quota remaining",q.get("x-requests-remaining"))
print("Screened",str(screen_path),"status",screen["status"],
      "clean_pairs",screen["clean_pairs"],"review_groups",screen["review_groups"])
print("Screening failure counts",json.dumps(screen.get("failure_counts",{}),sort_keys=True))
print("Screening invalid-row reasons",json.dumps(screen.get("invalid_row_reasons",{}),sort_keys=True))
