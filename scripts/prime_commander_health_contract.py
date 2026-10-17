"""Fail-closed parser for PRIME Commander ingestion health Flight logs."""
import json

PREFIX="PRIME_HEALTH_REPORT="
SECTIONS=("integrity","reconciliation","orphan_audits","recovery_plan")

def assess_health_run(run_status, exit_code, logs):
    if run_status != "SUCCEEDED" or exit_code != 0:
        return {"status":"UNKNOWN","reason":"RUN_NOT_SUCCESSFUL"}
    lines=[line[len(PREFIX):] for line in logs.splitlines() if line.startswith(PREFIX)]
    if len(lines)!=1:
        return {"status":"UNKNOWN","reason":"MISSING_OR_AMBIGUOUS_REPORT"}
    try:
        report=json.loads(lines[0])
        if not isinstance(report,dict):
            raise ValueError("report is not object")
        if report.get("mode")!="SYNTHETIC_TEST_ONLY":
            return {"status":"UNKNOWN","reason":"INVALID_SCOPE"}
        if report.get("database_writes")!=0 or report.get("automatic_reimports")!=0:
            return {"status":"UNKNOWN","reason":"UNSAFE_SIDE_EFFECTS"}
        if not all(isinstance(report.get(s),dict) and report[s].get("status") in ("PASS","REVIEW_REQUIRED") for s in SECTIONS):
            return {"status":"UNKNOWN","reason":"INCOMPLETE_REPORT"}
        if report.get("status") not in ("PASS","REVIEW_REQUIRED"):
            return {"status":"UNKNOWN","reason":"INVALID_STATUS"}
        if report["status"]=="PASS" and all(report[s]["status"]=="PASS" for s in SECTIONS):
            return {"status":"PASS","reason":"ALL_SYNTHETIC_CHECKS_PASSED"}
        return {"status":"REVIEW_REQUIRED","reason":"HEALTH_FINDINGS"}
    except (ValueError,TypeError,KeyError):
        return {"status":"UNKNOWN","reason":"MALFORMED_REPORT"}
