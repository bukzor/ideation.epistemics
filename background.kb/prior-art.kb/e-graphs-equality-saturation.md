---
title: "E-graphs and equality saturation (egg)"
originators: [Ross Tate et al. (equality saturation), Max Willsey et al. (egg)]
sources: [../../sources.kb/knot-theory-chat.md]
converges-on: [Class-E, FP2]
tags: [prior-art, rewriting, engines]
---

Congruence-closure structures holding an exponential space of
equivalent terms compactly; saturate with rewrite rules, then extract
the best representative under a cost model. The chat's EG
(`chat.md:378`): the operator's slicing schema "already exists in
mechanized form" — one of FP2's three discharge engines.

Gap: equivalence-preserving rules only (all Class-E) with trusted,
uncertified application; no obligation ledger, no Class-R relaxations
— which is what BR adds. Scale interacts with the ATMS cost question
(`../../questions.kb/atms-cost-at-scale.md`).

Verify: Willsey et al., "egg: Fast and Extensible Equality Saturation"
(POPL 2021).
