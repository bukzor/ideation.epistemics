---
label: ATOM_CONTENT
standing: agent
why:
  - ../../../states-and-moves/MODEL.kb/atomicity-is-one-basis-and-one-content-per-claim/ATOMICITY.md
  - ../the-sandbox-settles-design-the-field-settles-the-agent/SANDBOX_VS_FIELD.md
---

# In the harness a claim's content is a set of atoms from a small vocabulary

Equal sets are duplicates; a set with more than one atom is non-atomic
and splittable. This collapses judgment to mechanics on purpose: the
harness tests whether the design handles duplicates and factoring
correctly given recognition, not whether an agent recognizes them.
Recognition is a field question (`SANDBOX_VS_FIELD`).

The in-memory model is small: a claim is `{id, basis, wording, grounds:
set[id], content: frozenset[int]}`; the state is a map of them; debt,
the transition, and the rules are functions over that.
