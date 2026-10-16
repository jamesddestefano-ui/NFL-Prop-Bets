#!/usr/bin/env python3
"""Read-only NFL player-prop API collector; never logs credentials or URLs."""
import datetime as dt, json, os, pathlib, sys, urllib.parse, urllib.request, urllib.error
BASE="https://api.the-odds-api.com/v4"
KEY=os.environ.get("ODDS_API_KEY")
if not KEY:
    sys.exit("Missing ODDS_API_KEY GitHub Actions secret")
MARKETS="player_receptions,player_reception_yds,player_rush_yds"
def get(endpoint, params):
    query=urllib.parse.urlencode({**params,"apiKey":KEY})
    req=urllib.request.Request(BASE+endpoint+"?"+query,headers={"User-Agent":"PRIME-NFL-Research/1"})
    try:
        with urllib.request.urlopen(req,timeout=20) as response:
            payload=json.load(response)
            quota={k:response.headers.get(k) for k in ("x-requests-remaining","x-requests-used","x-requests-last")}
            return payload,quota
    except urllib.error.HTTPError as e:
        sys.exit("Odds API HTTP "+str(e.code)+"; check quota, access and supported markets. URL suppressed.")
    except Exception:
        sys.exit("Odds API request failed; URL and credentials suppressed.")
now=dt.datetime.now(dt.timezone.utc)
events,q0=get("/sports/americanfootball_nfl/events",{"dateFormat":"iso"})
upcoming=[e for e in events if dt.datetime.fromisoformat(e["commence_time"].replace("Z","+00:00"))>now]
upcoming.sort(key=lambda e:e["commence_time"])
# Free-tier safe: exactly one upcoming game and three markets, one region.
if not upcoming: 
    print("No upcoming NFL events; no paid calls for event odds.")
    sys.exit(0)
event=upcoming[0]
data,q=get("/sports/americanfootball_nfl/events/"+urllib.parse.quote(event["id"],safe="")+"/odds",{"regions":"us","markets":MARKETS,"oddsFormat":"american","dateFormat":"iso"})
rows=[]
for book in data.get("bookmakers",[]):
    for market in book.get("markets",[]):
        if market.get("key") not in MARKETS: continue
        for outcome in market.get("outcomes",[]):
            if outcome.get("name") not in ("Over","Under"):continue
            rows.append({"event_id":event["id"],"commence_time":event["commence_time"],"home_team":event.get("home_team"),"away_team":event.get("away_team"),"bookmaker":book.get("key"),"market":market["key"],"market_last_update":market.get("last_update"),"book_last_update":book.get("last_update"),"player":outcome.get("description"),"side":outcome.get("name"),"point":outcome.get("point"),"odds_american":outcome.get("price"),"observed_at_utc":now.isoformat(),"region_requested":"us","source":"the-odds-api.com","quote_status":"API_OBSERVED_NOT_EXECUTABLE_VERIFIED"})
folder=pathlib.Path("data/odds_api");folder.mkdir(parents=True,exist_ok=True)
out=folder/(now.strftime("%Y-%m-%dT%H-%M-%SZ")+"-sample.json")
out.write_text(json.dumps({"captured_at":now.isoformat(),"event":{k:event.get(k) for k in ("id","commence_time","home_team","away_team")},"markets_requested":MARKETS.split(","),"quotes":rows,"quota":q,"limitations":["Regional US feed not verified equal to NJ executable quotes","No assumption of missing markets as zero","API-observed quote is not a placed wager"]},indent=2)+"\n")
print("Saved",str(out),"rows",len(rows),"quota remaining",q.get("x-requests-remaining"))
