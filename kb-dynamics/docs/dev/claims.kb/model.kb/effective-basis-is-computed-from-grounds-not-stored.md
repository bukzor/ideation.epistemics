---
label: EFFECTIVE_BASIS
standing: agent
why:
  - standing-factors-into-basis-and-wording.md
  - ../imported-terms.kb/stipulated.md
  - ../imported-terms.kb/obligation.md
---

# A claim's effective basis is computed from its grounds, never stored

A derived claim is as trustworthy as its weakest ground. Effective basis
is the fold over the grounds: derived from `user` bases all the way down
is effectively stipulated; `proposed` anywhere in the ancestry is
effectively proposed, whatever the agent called the claim. The fold
stops at `user` and `evidence`, the two bases that rest on nothing in
the ledger.

A claim is load-bearing to the extent conclusions rest on it -- its
obligation in the `IMPORTED_OBLIGATION` sense, counted as transitive
descendants weighted toward stipulated ones. Effective basis and
load-bearing count together are the review query: claims whose effective
trust is lower than their downstream importance.

Declined: a stored "well-grounded" value. It would be asserted by the
agent that wanted it, and go stale the moment a ground changed.
