---
label: LEAN_DEFERRED
standing: user
authority: chat.md#L632
why:
  - ../imported-terms.kb/coverage.md
  - ../harness.kb/the-five-properties.md
---

# Lean pays back only after the design stops changing; Python first, possibly forever

The first implementation is Python, with a Lean port left room for and
not started until the design has stopped churning.

> [!@bukzor] chat.md#L632
> I think I'll put this in a subpath of my bukzor/ideation.epistemics GitHub repo, leaving room for both a Python and Lean implementation side by side. Initially (and possibly forever) Python only.

The steelman for Lean, recorded so it need not be rebuilt: the
properties are universal claims over move sequences, which generation
samples and a proof covers (`IMPORTED_COVERAGE`); monotonicity as a
theorem holds for the rare sequence sampling misses, which is exactly
the drift that started this; minimality becomes a pair of theorems,
sufficiency and a necessity witness per rule; an exhaustive match makes
an empty cell a compile error; a changed debt function breaks every
dependent proof at compile time where generation might silently keep
passing; and the structural match is deep -- a stipulated claim is an
axiom, a derived claim a theorem, effective basis is `#print axioms`.

Why not now: proofs are the most expensive artifact to redo, and the
owner expects to redo the design repeatedly (`SANDBOX_FIRST`). What a
proof would verify is the model, which was never the source of
uncertainty; the risks are outside it (`SANDBOX_VS_FIELD`). And bounded
exhaustive enumeration in Python is proof-strength for a bounded depth
at test cost.

When: the move table has not changed in a while, the rules have survived
real ledgers, and generation passes but is still not trusted. Then Lean
freezes the design as its permanent checkable spec, for the structural
subset of claims only; most real claims are conventions and preferences
and are not formalizable.
