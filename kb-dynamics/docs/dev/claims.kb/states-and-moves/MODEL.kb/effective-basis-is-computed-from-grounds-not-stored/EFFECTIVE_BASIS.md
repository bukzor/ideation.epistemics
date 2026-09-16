---
label: EFFECTIVE_BASIS
standing: user
authority: d3d3f372, the owner's ruling of 2026-09-11
why:
  - ../standing-factors-into-basis-and-wording/BASIS_WORDING.md
  - ../../../words-from-outside/IMPORTED_TERMS.kb/stipulated/IMPORTED_STIPULATED.md
  - ../../../words-from-outside/IMPORTED_TERMS.kb/obligation/IMPORTED_OBLIGATION.md
---

# A claim's effective basis is computed from its grounds, never stored

A derived claim is as trustworthy as its weakest ground. Effective basis
is the fold over the grounds: derived from `user` bases all the way down,
by grounds that entail it, is effectively stipulated; `proposed` anywhere
in the ancestry, or grounds that only motivate (`MOTIVATES_IS_PROPOSED`),
is effectively proposed, whatever the agent called the claim. The fold
stops at `user` and `evidence`, the two bases that rest on nothing in
the ledger.

A claim is load-bearing to the extent conclusions rest on it -- its
obligation in the `IMPORTED_OBLIGATION` sense, counted as transitive
descendants weighted toward stipulated ones. Effective basis and
load-bearing count together are the review query: claims whose effective
trust is lower than their downstream importance.

A ledger carries no trust of its own. "All claims trusted" is a state a
ledger can be in, computed by aggregating the folds, never an attribute
the ledger carries; the queue is a separate instrument (`REVIEW_DONE`):

> [!@bukzor] 9b6f24ad
> A ledger can have state "all claims trusted" but that's better represented as a aggregation over the claims, rather than as attribute of the ledger.

> [!@bukzor] d3d3f372
> Yes, accepted. And yes: round-tripping is a work item.

Declined: a stored "well-grounded" value. It would be asserted by the
agent that wanted it, and go stale the moment a ground changed.
