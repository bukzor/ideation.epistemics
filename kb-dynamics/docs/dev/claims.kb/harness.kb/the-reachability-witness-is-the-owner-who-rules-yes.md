---
label: REPAIR_WITNESS
standing: agent
verify: ../../../../python/tests/test_reachability.py
why:
  - the-properties.md
  - ../debt.kb/four-debt-reductions-need-no-ask-and-stay-reviewable.md
  - ../model.kb/a-question-has-a-terminal-state-besides-answered.md
---

# Property five's witness is the owner who rules yes on every item

Property five asks only that some owner-plus-agent sequence reaches debt
zero, so its constructive witness is the cheapest owner: the unasked
moves first, merging claims that say one thing, splitting a non-atomic
claim, closing a leaf question, then a yes ruling on every proposed root
and a settling of every draft. The harness runs that witness from every
recorded state and from every state the random agent reaches under the
rules, and a state it cannot clear is a stuck state or a missing
transition.

The closing move entered here: a question is closed only as a leaf, and
closing removes it, since the model carries nothing a closed question
would still say. What the witness does not show is that any real owner
would rule yes; the queue's order and the owner's rulings are the
field's.
