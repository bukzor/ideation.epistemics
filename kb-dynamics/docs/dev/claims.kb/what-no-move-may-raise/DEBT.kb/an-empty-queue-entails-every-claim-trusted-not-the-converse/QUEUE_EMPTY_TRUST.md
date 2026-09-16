---
label: QUEUE_EMPTY_TRUST
standing: bare
verify: ../../../../../../python/tests/test_trust.py
why:
  - ../../../the-order-of-work/METHOD.kb/when-review-is-done-or-doable/REVIEW_DONE.md
  - ../../../states-and-moves/MODEL.kb/effective-basis-is-computed-from-grounds-not-stored/EFFECTIVE_BASIS.md
  - ../the-kinds-of-rot/COMPONENTS.md
---

# An empty queue entails every claim trusted; the converse fails

The owner conjectured the first and doubted the second:

> [!@bukzor] 9b6f24ad
> A ledger with a fully-empty review queue "should" have "all claims trusted", I think, but I'm not sure. I somehow doubt the converse is true.

In the model both are settled. Forward: every claim whose fold reaches a
proposed claim reaches a proposed root, and every proposed root is a
queue item, so an empty queue leaves no untrusted claim. Converse: a
duplicate pair or a non-atomic claim among settled owner claims is queue
debt with every claim trusted; `examples/corners/rot-among-user-claims-only.md`
is the witness. The test checks the forward direction on every recorded
state, a sample and not an exhaustion (`IMPORTED_COVERAGE`); the argument
above is what covers the rest. It pins the witness for the converse.
