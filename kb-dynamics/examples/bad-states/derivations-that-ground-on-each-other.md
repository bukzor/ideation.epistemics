---
rot: proposed-basis
provenance:
  address: python/tests/test_repayable.py, the random agent's second find on 2026-09-11
  note: an agent merge left a derivation grounded on itself, and no claim in a cycle was a proposed root
claims:
  first:
    basis: derived
    wording: settled
    grounds: [second]
    content: [1]
  second:
    basis: derived
    wording: settled
    grounds: [first]
    content: [2]
---

# Derivations that ground on each other

Two derived claims, each the other's only ground. Neither rests on
anything, so both are effectively proposed, and a root must be found
inside the cycle or the queue never sees either.
