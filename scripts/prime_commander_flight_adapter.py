"""Read-only PRIME Commander MotherDuck Flight health adapter.

Requires caller-supplied Flight metadata and logs; no network, credentials or writes.
"""
from datetime import datetime, timezone
from scripts.prime_commander_health_contract import assess_health_run

def assess_latest_flight(run, logs, now_utc=None, max_age_minutes=240):
    """Fail closed on stale, missing, incomplete or unverified runs."""
    if not isinstance(run, dict):
        return {"status":"UNKNOWN","reason":"MISSING_RUN"}
    if not isinstance(logs, str):
        return {"status":"UNKNOWN","reason":"MISSING_LOGS"}
    if not isinstance(max_age_minutes, int) or not 1 <= max_age_minutes <= 1440:
        raise ValueError("max_age_minutes must be 1..1440")
    completed = run.get("ended_at")
    if not completed:
        return {"status":"UNKNOWN","reason":"RUN_NOT_COMPLETED"}
    try:
        end=datetime.fromisoformat(completed.replace("Z","+00:00"))
        now=now_utc or datetime.now(timezone.utc)
        if end.tzinfo is None or now.tzinfo is None:
            raise ValueError("timezone required")
        age=(now-end).total_seconds()
    except (ValueError,TypeError,AttributeError):
        return {"status":"UNKNOWN","reason":"INVALID_RUN_TIMESTAMP"}
    if age < -60 or age > max_age_minutes*60:
        return {"status":"UNKNOWN","reason":"STALE_OR_FUTURE_RUN"}
    result=assess_health_run(run.get("status"),run.get("exit_code"),logs)
    return {**result,"flight_run_number":run.get("run_number"),
            "completed_at_utc":end.astimezone(timezone.utc).isoformat()}
