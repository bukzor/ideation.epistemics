---
label: MOVE_TABLE
standing: agent
why:
  - ../imported-terms.kb/move.md
  - ../imported-terms.kb/rule.md
  - ../problem.kb/one-standing-field-confuses-three-situations.md
---

# The move table is total over (state, move, authority); an empty cell is a finding

The moves are add, stipulate, settle wording, reword, derive, split,
merge, retract, and close a question, each tagged with the authority it
carries (`AUTHORITY_NOT_HANDS`). The transition is a literal table:
`transition(state, move) -> state | Reject`, with a cell for every
(state, move, authority). Prose lets a cell
go unconsidered; the table makes the gap visible.

The second confusion is an empty cell: (`basis: user`, agent rewords)
had no entry, so agents defaulted to refusing. "Agents won't touch the
wording" is a missing transition rule, not an agent failure. Enforcement
follows from totality: if the table is the only sanctioned way to change
a claim's fields, an agent cannot set `wording: settled`, because only
the owner's move does that.

> [!@bukzor] chat.md#L230
> hm. I still have a desire I can't quite explain to get these state transitions into code.

If the table does not fit on a screen, the state space is too big, and
the code says so.
