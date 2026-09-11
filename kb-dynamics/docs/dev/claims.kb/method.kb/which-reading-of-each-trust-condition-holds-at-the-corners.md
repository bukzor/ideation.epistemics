---
label: TRUST_CORNERS
standing: open
why:
  - any-of-three-conditions-restores-trust.md
  - ../debt.kb/a-leaf-is-low-priority-never-exempt.md
  - ../debt.kb/owner-review-is-a-queue-sorted-by-debt.md
---

# Which reading of each trust condition holds at the corners?

The harness computes `TRUST_TEST`'s conditions under every reading the
ledger's words admit and pins the verdicts on hand-written states in
`examples/corners/` (`python/tests/test_trust.py`). Two decisions are
what the corners reduce to:

1. Do unruled leaves, and rot other than a proposed basis, block trust?
   Condition one is written as "queue empty" and glossed as "no
   load-bearing claim rests on a proposed basis". `LEAF_EXEMPT` puts
   leaves in the queue and `COMPONENTS` puts every rot kind in it, so the
   letter says a ledger with three agent guesses nothing rests on, or two
   owner claims that say one thing, is untrusted, and the gloss says
   trusted. Condition three reads "derivable and disposable" the same two
   ways for a leaf guess. The gloss also calls the recorded bad state of
   confusions 1 and 2 trusted. Recommendation: the letter; the gloss was
   agent wording naming one rot kind for all of them.
2. Does a sitting count items or weight? One guess with ten derivations
   on it is a one-item queue, so condition two calls it trusted while
   everything rests on the guess.

The third corner, a derivation whose arrows only motivate, is settled by
the record: `GROUND_RECORD` puts sufficiency on the arrow and
`FIDELITY_LADDER` admits it when a property demands it, which that corner
does; it is the next rung, not a decision.
