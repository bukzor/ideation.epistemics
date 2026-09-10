---
label: NEXT_ACTION_TEST
standing: agent
why:
  - ../problem.kb/one-standing-field-confuses-three-situations.md
---

# Two situations are one state exactly when they lead to the same next action

A distinction deserves a state of its own only if it changes the next
action: who reviews, or what the agent is permitted to do. Two
situations with the same next action are one state, whatever else
differs between them. When a new edge case appears, ask whether it needs
a different next action; usually it does not.

This is the discipline that answers the owner's constraint that the
system must not represent anything at all (chat.md#L190, quoted in
`THREE_CONFUSIONS`). It is what collapsed the first two confusions into
one state in `BASIS_WORDING`, and it is the test every proposed field or
value has to pass to enter this model.
