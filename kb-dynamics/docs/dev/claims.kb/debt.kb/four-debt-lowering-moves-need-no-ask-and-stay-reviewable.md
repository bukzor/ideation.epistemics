---
label: UNASKED_MOVES
standing: user
authority: f65fbdf3#L815
why:
  - the-candidate-rule-set.md
  - ../problem.kb/one-standing-field-confuses-three-situations.md
  - basis-and-record-guard-agent-pruning.md
---

# Four debt-lowering moves need no ask, and every one stays reviewable

An agent may, without asking:

- merge exact duplicates
- split a non-atomic claim into two
- close a leaf question, under `PRUNE_GUARD`
- steelman the owner's shorthand, basis unchanged

> [!@bukzor] f65fbdf3#L815
> Those all look good, yes. I'd want it all to be reviewable of course. And prioritization (and deferral without dismissal) of such reviews I think is the headline missing capability.

Reviewability is git's and the harness's concern, not this layer's. The
capability the owner names as missing is `DEFER_NOT_DISMISS`.
