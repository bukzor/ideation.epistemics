---
label: CONFLICT_ARITY
standing: bare
why:
  - ../a-set-of-claims-that-cannot-all-stand/CONFLICT.md
---

# A conflict can need more than two claims, so "pair" is the common case, not the definition

Three claims can conflict with no two conflicting. Witness: A says x
precedes y, B says y precedes z, C says z precedes x. Any two are
jointly satisfiable; all three are not. So a conflict is an attribute
of a minimal set of claims that cannot all stand, and a pair is the
smallest such set, not the only one. The owner's question in `CONFLICT`
is answered yes.

Consequence for the record: whatever caches a conflict names a set, and
the queue item that marks one (`CONFLICT_REDUCTIONS`) carries every member.
Finding minimal conflicting sets is the expensive derivation the owner
expected; pairs remain the cheap first pass.
