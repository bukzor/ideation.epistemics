---
label: QUEUE
standing: agent
why:
  - ../no-agent-move-raises-debt-silently/NO_SILENT_RAISE.md
  - ../../../why-ledgers-rot/PROBLEM.kb/review-cost-scales-with-the-ledger-not-the-payoff/REVIEW_RATIO.md
---

# Owner review is a queue sorted by debt contribution, not a wall

The owner's review of a ledger is the list of claims sorted by their
contribution to debt -- claim, effective basis, load-bearing count,
contribution -- so the owner always rules on the highest-payoff claim
next. Review becomes "here are the seven proposed claims that, if wrong,
break the most downstream work: stipulate, amend, or reject each", not
"load weeks of reasoning". A load-bearing report is the same kind of
tool as the reference checker and the acyclicity checker the ledger
already has.

For the existing mature ledgers the fastest route is probably not
repair: extract the `user`-basis claims from the ephemeral ones and let
agents re-derive under the rules when something needs it; give the
durable ones one agent-run pass that applies the permitted debt reductions
exhaustively and hands the owner the residue.
