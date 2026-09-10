---
label: MOVE_LOG
standing: open
why:
  - replay-computes-firings-and-attribution-when-triggers-are-code.md
  - ../model.kb/the-move-table-is-total-and-an-empty-cell-is-a-finding.md
---

# A move log beside the ledger: append-only, one record per sanctioned move

If the move table is the only sanctioned way to change a claim, logging
is one line in it, not a subsystem: timestamp, actor, move, claim id,
before-state, after-state, session id, and the rule id if a rule
prompted the move. Session id is the join key to transcripts, which is
what makes `REPLAY` possible; rule id is what lets "what did rule R
cause" be read rather than modeled. Git gives state over time; the log
adds who, why, and under what rule. Kept as line-delimited records
beside the ledger, committed with it, strictly events -- the moment it
carries content that should be claims, it is a second ledger.

The same log turns judgment checks into a funnel -- fired, acted,
findings, later confirmed as debt -- so their stochasticity is a recall
rate read from real events, not sampled from a model of the agent. That
answers the owner's suggestion of stochastic triggers with Monte Carlo
or funnel analysis (chat.md#L422): funnel yes, Monte Carlo no.

Open because the owner raised the log and the stochastic triggers on a
message they then superseded (chat.md#L422 to chat.md#L426, superseded by
chat.md#L458), so the owner never ruled, and the live thread deferred the
move table's enforcement until an agent is caught setting a field it
should not.
