---
label: UNREPAYABLE
standing: user
authority: f65fbdf3#L995, "seems good enough to me", on a four-route draft; the fourth withdrawn 2026-09-11 by the agent, vetoable
why:
  - debt-is-wanted-unrepayable-debt-is-not.md
  - ../problem.kb/the-wall-is-presentation-entangled-with-unknown-payout.md
  - ../model.kb/a-question-has-a-terminal-state-besides-answered.md
  - a-leaf-is-low-priority-never-exempt.md
---

# Three things void repayment, and they are what a queue item must carry to stay repayable

A debt repays when a ruling on it changes what rests on it. It becomes
unrepayable by any of three routes, given as examples in the way the rot
kinds were (`ROT_LIST` holds the closure question for both):

- no pathway: nothing will ever surface the item, so no ruling comes
- context lost: the item cannot be ruled on cold, so the ruling costs
  more than it returns, forever
- payout invisible: the reviewer cannot see what the ruling would change,
  so it is skipped every time (`WALL_CAUSE`)

So a queue item stays repayable by carrying a slot, its context, its
contribution, and its dependents, and an "unrepayable" debt component is
computable from the record.

> [!DRAFT] LEAF_EXEMPT, WANTED_DEBT, the components maintenance guide
> A leaf is not a fourth route. The draft the owner approved listed
> "nothing rests on it and nothing will: a leaf the ledger has outgrown",
> and that is withdrawn: a leaf sits in the queue at lowest priority
> (`LEAF_EXEMPT`), so it has a pathway, and closing it
> (`CLOSED_QUESTION`) is its repayment, an agent move. Counting a leaf as
> unrepayable would make every fresh agent claim rot on arrival, which
> `WANTED_DEBT` forbids, and "nothing will" is a prediction, not a
> function of the state, which the components guide excludes from any
> component.
