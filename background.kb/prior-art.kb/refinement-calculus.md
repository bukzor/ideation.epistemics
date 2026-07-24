---
title: "Refinement calculus and deductive synthesis (incl. Fiat)"
originators: [Edsger Dijkstra, Ralph-Johan Back, Carroll Morgan, MIT PLV (Fiat)]
sources: [../../sources.kb/knot-theory-chat.md]
likelihood: 0.7
converges-on: [FP2, AU]
tags: [prior-art, methodology, synthesis]
---

Specification → correctness-preserving refinement steps → executable,
each step discharging a proof obligation; Fiat mechanizes it in Coq
(chat.md:36, :66 — superseded branches; the live path builds on it
implicitly). The operator's original "slice the space by constraints"
is this methodology's shape, and FP2 is its ledger-centric
generalization.

Gap: refinement is monotonic forward motion — no retraction, no
budgeted relaxations (Class-R), no empirical discharge engines
alongside the prover.

Verify: Back & von Wright, *Refinement Calculus* (1998); Delaware et
al., "Fiat: Deductive Synthesis of ADTs in a Proof Assistant" (POPL
2015).
