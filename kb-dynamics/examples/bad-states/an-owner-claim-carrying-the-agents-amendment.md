---
rot: non-atomic
provenance:
  ledger: kb-dynamics/docs/dev/claims.kb
  claim: debt.kb/three-things-void-repayment.md
  commit: 5ca4c77
  note: >
    UNREPAYABLE as it stood before 2026-09-16: three approved routes plus an
    agent-derived withdrawal of the fourth, in one file signed user. Atom 1
    is the approved content; atom 2 is the withdrawal, which follows from
    the two owner claims and not from the approval. Two bases in one claim
    (ATOMICITY); the split move separates them.
claims:
  leaf-exempt:
    basis: user
    wording: settled
    grounds: []
    content: [3]
  wanted-debt:
    basis: user
    wording: settled
    grounds: []
    content: [4]
  approved:
    basis: user
    wording: settled
    grounds: [leaf-exempt, wanted-debt]
    content: [1, 2]
---

# An owner claim carrying the agent's amendment

One file, two warrants: the owner's approval covers one part and an
agent derivation the other. The claim cannot be ruled on as a unit.
