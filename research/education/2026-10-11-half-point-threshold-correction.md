# Half-point rush-attempt thresholds and stale evidence

As of **2026-10-11 22:51 UTC / 6:51 PM EDT**. Separate educational correction to the preserved [5:06 PM ET checkpoint](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/a08d2ab522de49fcc3f47aecd28cb8c708013c3f/research/watch_reports/2026-10-11-week5-snf-mnf-checkpoint.md). This note does not change its NO BET conclusion or verify any quoted price or reported probability.

## Mathematical correction

The checkpoint correctly refused to transfer a reported 59% probability from Henry Under 20.5 rush attempts to Under 19.5, but its explanation that the thresholds have “different push settlement” is incorrect.

**VERIFIED MATHEMATICAL PRINCIPLE — high confidence.** Let X be the settled integer rush-attempt count. Conditional on the wager being action-eligible:

- Under 19.5 wins when X ≤ 19.
- Under 20.5 wins when X ≤ 20.
- Neither half-point threshold can equal X, so neither has a threshold push.
- P(X < 20.5) − P(X < 19.5) = P(X = 20).

The relevant difference is the probability mass at exactly 20 attempts. At that outcome, Under 19.5 loses and Under 20.5 wins. Separate void or eligibility clauses require their own verification; none is inferred here. The reported 59% is not validated, and P(X = 20) is unknown, so no replacement probability, EV or actionable play-to is calculated.

**MODEL ASSUMPTION — invented check only.** Assign probability 0.31 to X = 19, 0.08 to X = 20 and 0.61 to X = 21. Then the two Under probabilities are 0.31 and 0.39, differing by 0.08. These values are unrelated to Henry's forecast.

Reproduction check on 2026-10-11 at 22:52 UTC: exact-rational arithmetic verified this example; an enumeration over integer counts 0–50 verified that the difference between the two win indicators is exactly the indicator for X = 20, with no threshold equality. The general identity follows from the disjoint event decomposition, not the finite enumeration. No NFL outcomes were tested.

## Public feed metadata observation

**EMPIRICAL EVIDENCE — repository observation only; high confidence in the retrieved fields.** The [pinned public feed](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/a08d2ab522de49fcc3f47aecd28cb8c708013c3f/intelligence/grok_pulse_latest.json), read at 22:51 UTC, reports status `live`, completedAt `2026-09-12T17:05:00Z`, and nflWeek `1`. It is not current Week 5 evidence. The checkpoint already recognized its stale timestamp and did not treat it as a new pulse. These fields do not establish anything about an external service's current state or the cause of the stale file.

**ANALYST OPINION:** Preserve the refusal to transfer probabilities across thresholds, with the corrected probability-mass explanation. Preserve rejection of the stale feed as current evidence.

**UNTESTED HYPOTHESIS:** None about NFL performance is advanced. The reported probability, live market availability and feed-production cause remain unassessed. Original records, feed files, controls and ledgers are unchanged.
