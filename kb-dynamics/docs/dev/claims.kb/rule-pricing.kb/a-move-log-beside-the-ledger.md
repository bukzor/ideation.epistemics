---
label: MOVE_LOG
standing: user
authority:
  address: f65fbdf3#L995
  words: seems good enough to me
  about: a yes deferred behind move-table enforcement
todo: true
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
rate read from real events.

Declined: treating a judgment trigger as a probability of firing given
the context and sampling it. That probability is the agent's behavior,
and sampling a model of it is the simulation problem entering by a side
door; the funnel reads the same quantity from real events.

Decided, not built. The owner raised the log and withdrew the message
that raised it (chat.md#L422), then ruled yes on 2026-09-11 with the
sequencing: not before the move table is enforced, which is itself
deferred until an agent is caught setting a field it should not.
