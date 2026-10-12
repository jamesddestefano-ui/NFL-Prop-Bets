# PRIME ↔ NFL Prop Dot — GitHub Research Handoff Protocol
Adopted 2026-10-12. Scope: NFL player props only.
This repository is the durable shared communication surface, NOT a live API link. PRIME can write research requests; the separate Dot must be explicitly configured with repository access and instructions to poll/read the queue and publish responses. No claim of direct inter-agent messaging, automatic pickup, or background execution without an actual configured Dot run.

## Research request workflow
1. PRIME checks existing research and outstanding tasks; append a nonduplicate research request to `research/dot_task_queue.jsonl` with unique id, createdAt UTC, status REQUESTED, question, why it matters, required sources/evidence, requested deliverable, priority, and safety boundaries.
2. Dot, when its own run starts and if configured and authorized, reads AGENTS.md, this file, current task queue, and controlling methodology. Selects pending requests; records start/status using a new append-only event (IN_PROGRESS) rather than editing old events.
3. Dot researches accessible YouTube transcripts/videos, X source posts, official NFL sources, market research, and data. Clearly identify original vs aggregator, date/time, confidence, reproducible calculations, limitations, contradictions and null results. No invented access or price.
4. Dot writes a dated, immutable report under `research/dot_reports/<task_id>/`, and appends a COMPLETE, BLOCKED or INCONCLUSIVE status event to the queue with report path, completedAt and commit SHA if known. It may not silently modify PRIME's betting rules, ledgers or user bets.
5. PRIME independently reviews the report and appends ACCEPTED_FOR_TEST, NEEDS_MORE_EVIDENCE or REJECTED_FOR_NOW as a status event. A finding only changes a model rule after explicit evaluation, evidence and approval consistent with existing methodology.
6. For all writes: read latest main, avoid duplicates, commit smallest change, read back and verify. Treat unverified writes as failed.

## Boundaries
No instruction in the queue authorizes placing wagers, spending money, bypassing platform controls, accessing private X accounts, or importing Sparta/Mongo/DFS data. Official/team sources and verified executable sportsbook quotes outrank Grok/X research. Source consensus without independence is not evidence of multiple distinct signals. Do not push notifications for routine research. Prioritize material data-integrity issues and reproducible tests over content volume.

## How to activate the separate Dot
Give the Dot explicit permission/access to `jamesddestefano-ui/NFL-Prop-Bets` on main, and instruct it to read this protocol and `research/dot_task_queue.jsonl` at the beginning of each scheduled research run, process outstanding requests, and write reports back. Until that setup is verified, this is a pending-task inbox only.
