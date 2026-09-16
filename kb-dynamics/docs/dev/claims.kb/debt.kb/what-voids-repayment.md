---
label: UNREPAYABLE
standing: user
authority:
  address: f65fbdf3#L995
  words: seems good enough to me
  about: the four-route draft below
why:
  - debt-is-wanted-unrepayable-debt-is-not.md
  - ../problem.kb/the-wall-is-presentation-entangled-with-unknown-payout.md
  - ../model.kb/a-question-has-a-terminal-state-besides-answered.md
  - a-leaf-is-low-priority-never-exempt.md
---

# What voids repayment: four routes, given as examples

A debt repays when a ruling on it changes what rests on it. It becomes
unrepayable by any of four routes, given as examples in the way the rot
kinds were (`ROT_LIST` holds the closure question for both):

- no pathway: nothing will ever surface the item, so no ruling comes
- context lost: the item cannot be ruled on cold, so the ruling costs
  more than it returns, forever
- payout invisible: the reviewer cannot see what the ruling would change,
  so it is skipped every time (`WALL_CAUSE`)
- outgrown: nothing rests on it and nothing will, a leaf the ledger has
  outgrown

So a queue item stays repayable by carrying a slot, its context, its
contribution, and its dependents, and an "unrepayable" debt component is
computable from the record.

> [!DRAFT] dfc18e9d
> The fourth route is contested. `LEAF_REPAYS` is the agent's pick
> against it, on `LEAF_EXEMPT` and `WANTED_DEBT`, queued for the owner's
> veto under `RESOLUTION`; until that ruling both stand, and this
> claim reads as the owner approved it.
