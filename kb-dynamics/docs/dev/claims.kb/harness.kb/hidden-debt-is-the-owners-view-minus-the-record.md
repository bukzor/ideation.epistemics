---
label: OWNER_VIEW
standing: agent
verify: ../../../../python/tests/test_repayable.py
why:
  - the-properties.md
  - ../debt.kb/what-voids-repayment.md
  - ../debt.kb/no-agent-move-raises-debt-silently.md
  - ../model.kb/the-move-table-is-total-and-an-empty-cell-is-a-finding.md
  - ../debt.kb/basis-and-record-guard-agent-pruning.md
---

# Hidden debt is the owner's view of the ledger minus the record, and it is the sandbox's unrepayable

In the sandbox the queue is computed from the state, so of
`UNREPAYABLE`'s three routes only "no pathway" can occur, and only one
way: an agent move makes the record stop showing rot that is still
there. The harness catches it with a log and a sanction table. The
sanction table is the authority column of the move table
(`AUTHORITY_NOT_HANDS`): what an unlicensed move means in the owner's
eyes. Unlicensed settling of wording or stipulation means nothing; an
unlicensed add means adding as `proposed` with draft wording; an
unlicensed retraction of a `user` claim means nothing (`PRUNE_GUARD`);
an unlicensed merge means nothing unless the claims say one thing and
neither is the owner's. Replaying the log under it gives the owner's
view, and `hidden` is, per component, the rot the owner's view has
beyond the record.

Property one is then: agent-only sequences leave `hidden` at zero. The
rules enforce the sanction table; the harness shows where they enforce
too little. The constant-worst agent found two rules on its first run,
only the owner settles wording and only the owner stipulates; the random
agent found three more, one shrunk step at a time: agents never retract
a `user` claim, agents merge only exact duplicates and never drop a
`user` claim, agents add draft wording only, and stipulation covers
adding as `user`. Each rule has a recorded state or a shrunk random run
as its witness (`python/tests/test_necessity.py`), and a rule the agents
never trip has none. The random agent's second find was also a debt bug:
a claim in a cycle was never a proposed root, so a cycle of derivations
had debt zero; now every member of a cycle is a root, pinned by
`examples/bad-states/derivations-that-ground-on-each-other.md`.

What this cannot see: an agent retracting a settled `user` claim hides
no rot, since a clean claim carries none, yet the owner's content is
gone. That is a loss the components do not count and `ROT_LIST` should
hear about; it needs the log, not the state.
