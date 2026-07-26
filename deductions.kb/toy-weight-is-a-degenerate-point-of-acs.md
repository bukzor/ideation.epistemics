---
kind: entailment
conclusion: ../claims.kb/acs-admits-toy-weight.md
premises:
  - ../claims.kb/two-base-statuses-not-four.md
  - ../claims.kb/monotonic-dynamic-seam.md
  - ../claims.kb/link-checker-is-the-propagator.md
sources: [../sources.kb/claude.md]
depends:
  - ../definitions.kb/acs.md
  - ../background.kb/prior-art.kb/atms-tms.md
tags: [acs, ladder, mechanism]
---

An informal existence proof, four legs, each showing one component of
`../prompts/acs.md` survives degenerate instantiation.

**Payloads.** The spec requires λΠ terms, and an opaque constant is a
λΠ term. Declaring each scratched-out idea as an atomic constant is
the degenerate embedding: the deep structure goes unused, not missing.
No line of the spec demands payloads *exploit* their structure.

**Checkers.** `certified(checker)` is parameterized precisely because
checkers have unequal trust profiles — the definition's own
cubical/univalence carve-out concedes that certified(X) ≠
certified(Y). Weak checkers (operator fiat, LLM judge, a named script)
extend the same axis downward. `monotonic-dynamic-seam.md` says the
load-bearing wall is the *boundary's placement*, not the checker's
strength: a weak check still runs below the seam and is still named,
so "trust base per claim must be a graph query" is what keeps weak
certificates honest — a claim certified by an LLM judge is visibly so
in every trust-base answer.

**Statuses.** Per `two-base-statuses-not-four.md`, everything below
certified involves no checking at all: stipulated is fiat, open is the
unmarked default, certified is read off at point of use. A store
holding only stipulated and open claims is therefore a valid ACS state
— one every real build passes through before its first discharge. Toy
weight is a sub-lattice the full system must support anyway.

**Propagation and queries.** Retraction cones, obligation views and
trust bases read edges, not payloads. The spec's own cited lineage
(`../background.kb/prior-art.kb/atms-tms.md`) ran exactly this store
over opaque propositional atoms in the 1980s; and
`link-checker-is-the-propagator.md` is the parameterization running
*today*, certified, in this realm's own graph.

So the toy is not a modification of ACS but a point in its parameter
space, and the phases reorder: deliverables 2–4 can precede
deliverable 1.

Not entailed: that the degenerate point answers semantic coherence.
Structural verdicts are the system's; entailment judgment at toy
weight belongs to whoever authors deductions and certificates. Also
not entailed: any change to ACS's status set — that question
(`../questions.kb/acs-status-set-mirror-chat-weight.md`) is orthogonal
and stays open.
