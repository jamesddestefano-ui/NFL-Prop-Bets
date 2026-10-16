# PRIME ↔ Claude ↔ NFL Prop Dot: independent forecast handoff
Date: 2026-10-16. Purpose: ensure the user's separate Claude analysis and PRIME/Dot research can be compared on the same precommitted NFL player-prop contracts. This protocol does not claim direct Claude connectivity.

## Before sending to either model
Freeze a cohort_id, immutable contract_id, game, player, market, side, threshold, book, odds, screenshot_capture_at_et, source_timestamp (if available), kickoff, settlement terms and snapshot link or source provenance. Do not replace or silently edit an original contract after a price move. Every screened contract stays in the denominator. Any international game already started is excluded unless a real earlier frozen record exists.

## Give both models the same prompt
"Using ONLY the attached frozen contract screenshot(s) and any independently cited as-of pregame information, analyze each listed NFL player prop. For each contract, return: contract_id; exact book/line/side/odds and screenshot time; expected role and injury dependencies; projected mean AND distribution/spread assumptions; p_win, p_push, p_loss with settlement basis; p_fair (and source/calibration status); conservative probability and EV; break-even probability; central edge in percentage points; central and conservative ROI; BET or PASS under PRIME v2 (-150 through +150 requires central edge >=4pp and conservative EV>=0; longer odds/TD requires central ROI>=15% and conservative EV>=0); maximum playable line/juice if supportable; uncertainty and sources. Do not invent missing prices, sportsbook access, model precision or final outcomes. Explicitly state PASS/UNDETERMINED if required evidence is missing. Do not revise answers after seeing results." 

## PRIME records independent outputs
Record ChatGPT and Claude as separate sources, each with received_at, forecast_as_of, exact matched contract_id, model label/version if known, estimated probabilities, distribution, EV, decision, reason and original user-provided response evidence. Do not count a Claude answer until actually received. If Claude suggests a different contract, preserve it as a new unfrozen observation rather than silently merging.

## Dot assignment
The Dot can investigate discrepancies and methods using only publicly available sources, and write an immutable review report. It must not fabricate Claude's response, change user tickets, place bets, or overrule verified book quotes. Queue new research only for material, falsifiable disagreements.

## Postgame comparison
Grade all frozen candidates including passes. Compute proper scoring (Brier only for appropriately defined binary probabilities; handle pushes/voids explicitly), calibration and matched closing-line value where original and closing evidence is complete. Report missingness and effective sample size. Never select only the winning model's picks, assume shadow bets were placed, or use one Sunday to claim a profitable edge.
