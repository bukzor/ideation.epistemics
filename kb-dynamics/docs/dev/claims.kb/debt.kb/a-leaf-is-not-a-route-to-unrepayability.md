---
label: LEAF_REPAYS
standing: agent
why:
  - what-voids-repayment.md
  - a-leaf-is-low-priority-never-exempt.md
  - debt-is-wanted-unrepayable-debt-is-not.md
  - ../model.kb/a-question-has-a-terminal-state-besides-answered.md
  - the-reductions-of-a-conflict.md
---

# A leaf is not a route to unrepayability

`UNREPAYABLE`'s fourth route, "nothing rests on it and nothing will",
does not void repayment. A leaf sits in the queue at lowest priority
(`LEAF_EXEMPT`), so it has a pathway; closing it (`CLOSED_QUESTION`) is
its repayment, an agent move. Counting a leaf as unrepayable would make
every fresh agent claim rot on arrival, which `WANTED_DEBT` forbids; and
"nothing will" is a prediction, not a function of the state, which the
components guide excludes from any component.

This is the agent's pick on a conflict between two owner rulings: the
approval of the four-route draft at f65fbdf3#L995, and the earlier
rulings at f65fbdf3#L815 that `LEAF_EXEMPT` and `WANTED_DEBT` carry.
It was first applied by amending `UNREPAYABLE` in place (5d44257),
which `RESOLUTION` forbids: the pick may not enter as the owner's
claim. So it stands here under agent authority, `UNREPAYABLE` reads as
approved, and the owner's ruling settles which of the resting states in
`RESTING_STATES` this pair reaches.
