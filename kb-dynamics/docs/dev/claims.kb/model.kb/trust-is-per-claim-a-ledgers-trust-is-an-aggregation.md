---
label: TRUST_PER_CLAIM
standing: user
authority: 9b6f24ad, the owner's ruling of 2026-09-11
why:
  - effective-basis-is-computed-from-grounds-not-stored.md
  - ../debt.kb/owner-review-is-a-queue-sorted-by-debt.md
---

# Trust is per claim; a ledger's trust is an aggregation over its claims

A claim is trusted by its own fold (`EFFECTIVE_BASIS`). "All claims
trusted" is a state a ledger can be in, computed by aggregating, never an
attribute the ledger carries; a ledger-level trusted predicate is a
category error.

> [!@bukzor] 9b6f24ad
> A ledger can have state "all claims trusted" but that's better represented as a aggregation over the claims, rather than as attribute of the ledger.

> [!@bukzor] 9b6f24ad
> a non-empty queue has no (direct) bearing on the state of any particular claim.

So the queue (`QUEUE`) and a claim's trust are separate instruments: the
queue says what the owner has left to rule on, and nothing in it changes
what any well-founded claim is owed. Withdrawn on this ruling: the
harness's ledger-level `trusted` function and its sitting count.
