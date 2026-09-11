---
label: OWNER_VIEW
standing: agent
verify: ../../../../python/tests/test_repayable.py
why:
  - the-five-properties.md
  - ../debt.kb/three-things-void-repayment.md
  - ../debt.kb/no-agent-move-raises-debt-silently.md
  - ../model.kb/the-move-table-is-total-and-an-empty-cell-is-a-finding.md
  - ../debt.kb/basis-and-record-guard-agent-pruning.md
---

# Hidden debt is the owner's view of the ledger minus the record, and it is the sandbox's unrepayable

In the sandbox the queue is computed from the state, so of
`UNREPAYABLE`'s three routes only "no pathway" can occur, and only one
way: an agent move makes the record stop showing rot that is still
there. The harness catches it with a log and a sanction table. The
sanction table is the actor column of the move table: what an agent's
move means in the owner's eyes. An agent settling wording or
stipulating means nothing; an agent adding a `user` claim means adding
it as `proposed`; an agent retracting a `user` claim means nothing
(`PRUNE_GUARD`). Replaying the log under it gives the owner's view, and
`hidden` is, per component, the rot the owner's view has beyond the
record.

Property one is then: agent-only sequences leave `hidden` at zero. The
rules enforce the sanction table; the harness shows where they enforce
too little. The constant-worst agent found two rules on its first run,
only the owner settles wording and only the owner stipulates, each with
recorded states as witnesses (`python/tests/test_necessity.py`), and a
rule the agent never trips has none.

What this cannot see: an agent retracting a settled `user` claim hides
no rot, since a clean claim carries none, yet the owner's content is
gone. That is a loss the components do not count and `ROT_LIST` should
hear about; it needs the log, not the state.
