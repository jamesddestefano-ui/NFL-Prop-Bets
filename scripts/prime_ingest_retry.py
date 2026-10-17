"""PRIME ingestion retry policy: synthetic-only, bounded, never retries bad data.

This module does not schedule jobs, connect to MotherDuck, or persist records.
"""
from dataclasses import dataclass

RETRYABLE = frozenset({"CONNECTION_ERROR"})
TERMINAL = frozenset({"VALIDATION_REJECTED", "PERSISTENCE_ERROR"})

@dataclass(frozen=True)
class RetryDecision:
    action: str
    next_delay_seconds: int | None
    reason: str

def decide_retry(error_class, attempt, max_attempts=3):
    if not isinstance(attempt, int) or isinstance(attempt, bool) or attempt < 1:
        raise ValueError("attempt must be positive integer")
    if not isinstance(max_attempts, int) or isinstance(max_attempts, bool) or not 1 <= max_attempts <= 5:
        raise ValueError("max_attempts must be 1..5")
    if error_class in TERMINAL:
        return RetryDecision("REVIEW_REQUIRED", None, "non-retryable failure")
    if error_class not in RETRYABLE:
        return RetryDecision("REVIEW_REQUIRED", None, "unknown failure classification")
    if attempt >= max_attempts:
        return RetryDecision("REVIEW_REQUIRED", None, "retry budget exhausted")
    return RetryDecision("RETRY_LATER", min(60 * (2 ** (attempt - 1)), 900),
                         "bounded transient connection retry")
