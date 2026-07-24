---
title: "Dedukti / λΠ-calculus modulo rewriting"
originators: [Gilles Dowek, Deducteam]
sources: [../../sources.kb/knot-theory-chat.md]
converges-on: [CP, MT, Class-E]
tags: [prior-art, transport, proof-assistants]
---

A universal logical framework: encode Coq/HOL/Lean/Agda theories in a
small λΠ-modulo kernel, recheck and translate proofs between systems
(Logipedia/Lambdapi ecosystem). The chat's fourth derivation
(`chat.md:857-893`): its declaration forms mirror ACS claim statuses;
its role is the certified-status *port*, not the ledger (DM — checkers
are monotonic; HG — it can't host).

Gap: monotonic by construction — no retraction, no budgeted (Class-R)
rules, no obligation lifecycle.

Likelihood 0.6: ecosystem-maturity claims (Lean 4 export status,
verified checkers) are exactly what O8/O9 exist to verify — see
`../../questions.kb/cross-prover-certificate-exchange.md` and the
chat's O-ledger
(`../../sources.kb/knot-theory-chat.kb/obligations.kb/`).
