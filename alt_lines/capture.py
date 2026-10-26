#!/usr/bin/env python3
"""B18 isolated, manually dispatched NFL alternate-line observations (Python 3.11).

Never import PRIME pilot modules, write official ledgers, or print API credentials.
The Odds API event-odds endpoint is billed per market/region; obtain a budget first.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone, timedelta
import json
import os
from pathlib import Path
import sys
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen
from urllib.error import HTTPError

SPORT = "americanfootball_nfl"
BASE = "https://api.the-odds-api.com/v4"
MARKETS = (
    "player_receptions", "player_reception_yds", "player_rush_yds",
    "player_receptions_alternate", "player_reception_yds_alternate",
    "player_rush_yds_alternate",
)
SLOTS = {"freeze": None, "t30": 30, "t15": 15, "t5": 5}

def timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("kickoff must have timezone")
    return parsed.astimezone(timezone.utc)

def allowed_slot(slot: str, kickoff: datetime, observed: datetime, tolerance: int) -> bool:
    if observed >= kickoff:
        return False
    if slot == "freeze":
        # Freeze must be manually authorized; only pregame boundary is enforced here.
        return True
    target = kickoff - timedelta(minutes=SLOTS[slot])
    return abs((observed - target).total_seconds()) <= tolerance * 60

def validate_books(books: str) -> list[str]:
    keys = [x.strip() for x in books.split(",") if x.strip()]
    if len(keys) != 7 or len(set(keys)) != 7:
        raise ValueError("Exactly seven distinct sportsbook API keys required")
    if not all(x.replace("_", "").isalnum() for x in keys):
        raise ValueError("Invalid sportsbook key")
    return keys

def save_new(folder: Path, name: str, record: dict) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    # x => refuse overwrite: historical source responses are immutable.
    with path.open("x", encoding="utf-8") as handle:
        json.dump(record, handle, sort_keys=True, indent=2)
        handle.write("\n")
    return path

def request_odds(event_id: str, key: str, books: list[str]) -> tuple[dict, dict]:
    endpoint = f"{BASE}/sports/{SPORT}/events/{quote(event_id, safe='')}/odds"
    params = urlencode({"apiKey": key, "markets": ",".join(MARKETS),
                        "bookmakers": ",".join(books), "regions": "us",
                        "oddsFormat": "american", "dateFormat": "iso"})
    req = Request(endpoint + "?" + params, headers={"User-Agent": "B18-alt-research/1"})
    try:
        with urlopen(req, timeout=35) as response:
            payload = json.load(response)
            quota = {k: response.headers.get(k) for k in
                     ("x-requests-used", "x-requests-remaining", "x-requests-last")}
            return payload, quota
    except HTTPError as exc:
        raise RuntimeError(f"Odds API HTTP {exc.code}; suppressed request URL") from None
    except Exception:
        raise RuntimeError("Odds API call failed; suppressed request URL") from None

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event-id", required=True)
    parser.add_argument("--kickoff-utc", required=True)
    parser.add_argument("--slot", choices=SLOTS, required=True)
    parser.add_argument("--books", required=True, help="Exactly seven Odds API bookmaker keys")
    parser.add_argument("--out", default="data/alt_lines/runs")
    parser.add_argument("--tolerance-minutes", type=int, default=3)
    parser.add_argument("--execute", action="store_true", help="Explicitly authorize billable API request")
    args = parser.parse_args(argv)
    books = validate_books(args.books)
    kickoff = timestamp(args.kickoff_utc)
    now = datetime.now(timezone.utc)
    if args.tolerance_minutes < 0 or not allowed_slot(args.slot, kickoff, now, args.tolerance_minutes):
        raise ValueError("Outside pregame slot; no API call")
    if not args.execute:
        print("B18 preflight OK; no billable request. Add --execute when authorized.")
        return 0
    key = os.environ.get("ODDS_API_KEY")
    if not key:
        raise ValueError("ODDS_API_KEY secret missing; no request")
    payload, quota = request_odds(args.event_id, key, books)
    received = datetime.now(timezone.utc)
    if not allowed_slot(args.slot, kickoff, received, args.tolerance_minutes):
        raise ValueError("Post-response time outside slot; response rejected")
    observed_books = {b.get("key") for b in payload.get("bookmakers", [])}
    observed_markets = {m.get("key") for b in payload.get("bookmakers", [])
                        for m in b.get("markets", [])}
    stamp = received.strftime("%Y%m%dT%H%M%S%fZ")
    record = {
        "schema": "B18_CAPTURE_V1", "disposition": "RESEARCH_ONLY_NOT_BET_ELIGIBLE",
        "event_id": args.event_id, "kickoff_utc": kickoff.isoformat(),
        "slot": args.slot, "received_utc": received.isoformat(),
        "markets_requested": MARKETS, "bookmakers_requested": books,
        "bookmakers_returned": sorted(observed_books),
        "markets_returned": sorted(observed_markets),
        "missing_bookmakers": sorted(set(books) - observed_books),
        "missing_markets": sorted(set(MARKETS) - observed_markets),
        "quota": quota, "raw_response": payload,
        "limitations": ["Quotes not verified executable in NJ", "Missing quote not zero",
                        "Separate from PRIME pilot and official decision ledger"],
    }
    path = save_new(Path(args.out), f"{stamp}-{args.event_id}-{args.slot}.json", record)
    print(f"B18 saved {path}; books={len(observed_books)}/7 markets={len(observed_markets)}/6")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, RuntimeError, FileExistsError) as exc:
        sys.exit(f"B18 capture aborted: {exc}")
