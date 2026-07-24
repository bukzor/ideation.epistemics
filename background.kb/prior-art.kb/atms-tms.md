---
title: "Truth Maintenance Systems (TMS) and Assumption-based TMS (ATMS)"
originators: [Jon Doyle, Johan de Kleer]
sources: [../../sources.kb/knot-theory-chat.md]
converges-on: [TL, RP, SI]
tags: [prior-art, ledger, mechanized-ancestor]
---

Claim nodes, justification edges, assumption tracking, belief
propagation under retraction (Doyle 1979, de Kleer 1986). The chat's TM
(`chat.md:761`): the *implementation* ancestor of the fused
{TL, RN} object — spine inversion and retraction propagation, built in
1980s AI reasoning systems.

Gap: no evidence *terms* (justification logic's contribution), no
principled revision *logic* (AGM's) — machinery without the axioms.
Cost question: classical ATMS label propagation is worst-case
exponential in assumption sets — see
`../../questions.kb/atms-cost-at-scale.md`.

In this realm: `../../claims.kb/link-checker-is-the-propagator.md`
takes the propagation half only, and gets it from the link checker
rather than a label algebra — notification instead of repair, which is
also how it dodges the cost question above.

Verify: read Doyle 1979 ("A Truth Maintenance System") and de Kleer
1986 ("An Assumption-based TMS"); check complexity claims.
