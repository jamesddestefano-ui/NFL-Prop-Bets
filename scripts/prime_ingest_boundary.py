"""PRIME v1 synthetic-only ingestion boundary. No network or database writes."""
import hashlib
import json
from datetime import datetime, timezone
from collections import Counter

ALLOWED_MARKETS = {"player_receptions", "player_reception_yds", "player_rush_yds"}

def utc(value):
    if not isinstance(value, str):
        raise ValueError("timestamp must be ISO-8601 text")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp missing timezone")
    return parsed.astimezone(timezone.utc)

def validate_batch(batch):
    """Validate a synthetic fixture, returning deterministic records and fingerprint.

    No actual sportsbook observations may pass this boundary.
    """
    if batch.get("fixture_type") != "SYNTHETIC_TEST_ONLY":
        raise ValueError("live or unmarked data prohibited")
    quotes = batch.get("quotes")
    if not isinstance(quotes, list) or not quotes:
        raise ValueError("nonempty quotes list required")
    normalized = []
    seen = set()
    for q in quotes:
        required = ("event_id", "bookmaker", "market", "player_id",
                    "side", "point", "odds_american", "response_received_utc",
                    "commence_time")
        if any(k not in q or q[k] is None for k in required):
            raise ValueError("missing required quote field")
        if q["market"] not in ALLOWED_MARKETS or q["side"] not in ("Over", "Under"):
            raise ValueError("unsupported market or side")
        if not all(isinstance(q[k], str) and q[k].strip() for k in
                   ("event_id", "bookmaker", "player_id")):
            raise ValueError("invalid identifier")
        if isinstance(q["point"], bool) or not isinstance(q["point"], (int, float)) or not 0 <= q["point"] < 1000:
            raise ValueError("invalid point")
        odds = q["odds_american"]
        if isinstance(odds, bool) or not isinstance(odds, (int, float)) or not (-10000 <= odds <= 10000) or -100 < odds < 100:
            raise ValueError("invalid American odds")
        received, kickoff = utc(q["response_received_utc"]), utc(q["commence_time"])
        if received >= kickoff:
            raise ValueError("post-kickoff quote prohibited")
        key = (q["event_id"], q["bookmaker"], q["market"], q["player_id"],
               q["side"], q["point"], received.isoformat())
        if key in seen:
            raise ValueError("duplicate quote")
        seen.add(key)
        normalized.append({**q, "response_received_utc": received.isoformat(),
                           "commence_time": kickoff.isoformat()})
    counts = Counter((q["event_id"], q["bookmaker"], q["market"], q["player_id"],
                      q["point"], q["response_received_utc"]) for q in normalized)
    sides = {}
    for q in normalized:
        k = (q["event_id"], q["bookmaker"], q["market"], q["player_id"],
             q["point"], q["response_received_utc"])
        sides.setdefault(k, set()).add(q["side"])
    for k, n in counts.items():
        if n != 2 or sides[k] != {"Over", "Under"}:
            raise ValueError("incomplete or non-clean Over/Under pair")
    canonical = json.dumps(normalized, sort_keys=True, separators=(",", ":"), allow_nan=False)
    fingerprint = hashlib.sha256(canonical.encode()).hexdigest()
    return {"batch_sha256": fingerprint, "record_count": len(normalized),
            "quotes": normalized, "classification": "SYNTHETIC_VALIDATED"}

def synthetic_fixture():
    common = {"event_id": "TEST_GAME_001", "bookmaker": "TEST_BOOK",
              "market": "player_receptions", "player_id": "TEST_PLAYER",
              "point": 5.5, "response_received_utc": "2026-10-18T12:00:00Z",
              "commence_time": "2026-10-18T17:00:00Z"}
    return {"fixture_type": "SYNTHETIC_TEST_ONLY",
            "quotes": [{**common, "side": "Over", "odds_american": -110},
                       {**common, "side": "Under", "odds_american": -110}]}

if __name__ == "__main__":
    print(json.dumps({k: v for k, v in validate_batch(synthetic_fixture()).items()
                      if k != "quotes"}, indent=2))
