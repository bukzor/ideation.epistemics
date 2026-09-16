---
label: LEAF_OUTGROWN
standing: agent
why:
  - ../what-voids-repayment/UNREPAYABLE.md
  - ../what-priority-a-leaf-gets/LEAF_PRIORITY.md
  - ../debt-is-wanted-unrepayable-debt-is-not/DEBT_WANTED.md
  - ../../../states-and-moves/MODEL.kb/a-question-has-a-terminal-state-besides-answered/CLOSED_QUESTION.md
  - ../the-reductions-of-a-conflict/CONFLICT_REDUCTIONS.md
---

# A leaf is not a route to unrepayability

`UNREPAYABLE`'s fourth route, "nothing rests on it and nothing will",
does not void repayment. A leaf sits in the queue at lowest priority
(`LEAF_PRIORITY`), so it has a pathway; closing it (`CLOSED_QUESTION`) is
its repayment, an agent move. Counting a leaf as unrepayable would make
every fresh agent claim rot on arrival, which `DEBT_WANTED` forbids; and
"nothing will" is a prediction, not a function of the state, which the
components guide excludes from any component.

This is the agent's pick on a conflict between two owner rulings: the
approval of the four-route draft at f65fbdf3#L995, and the earlier
rulings at f65fbdf3#L815 that `LEAF_PRIORITY` and `DEBT_WANTED` carry.
It was first applied by amending `UNREPAYABLE` in place (5d44257),
which `CONFLICT_REDUCTIONS` forbids: the pick may not enter as the owner's
claim. So it stands here under agent authority, `UNREPAYABLE` reads as
approved, and the owner's ruling settles which of the resting states in
`CONFLICT_RESTING_STATES` this pair reaches.
