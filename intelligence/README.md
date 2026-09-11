# Intelligence Feed

This directory is reserved for machine-readable external intelligence, including Grok/X-style research feeds.

Intelligence is advisory only. It may identify news, analyst signals, projection changes, or possible prop edges, but it may not overwrite verified sportsbook line truth or create an authoritative bet without independent verification.

Recommended files if a Grok Pulse is added later:
- `grok_pulse_latest.json` — latest completed pass
- `grok_pulse_history.jsonl` — append-only completed-pass history

Recommended signal fields:
- `status`
- `completedAt`
- `source`
- `sourceHandle`
- `sourceUrl`
- `publishedAt`
- `classification`
- `player`
- `team`
- `game`
- `market`
- `signal`
- `verificationStatus`
- `propImpact`

A completed pass should be considered new only when it is explicitly marked complete/live and its completion timestamp differs from the most recently processed pass.
