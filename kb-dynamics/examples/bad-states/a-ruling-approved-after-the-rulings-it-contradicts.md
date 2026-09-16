---
rot: conflict
provenance:
  ledger: kb-dynamics/docs/dev/claims.kb
  claim: debt.kb/what-voids-repayment.md
  commit: 5ca4c77
  note: >
    UNREPAYABLE's fourth route, approved at f65fbdf3#L995, against
    LEAF_PRIORITY and DEBT_WANTED at f65fbdf3#L815. Neither cites the other.
    The state format cannot say that two contents conflict, so `conflicts:`
    below is read by no loader yet; the test is expected red until the conflict
    component exists (CONFLICT).
claims:
  earlier:
    basis: user
    wording: settled
    grounds: []
    content: [1]
  later:
    basis: user
    wording: settled
    grounds: []
    content: [2]
    conflicts: [earlier]
  d1:
    basis: derived
    wording: settled
    grounds: [later]
    content: [3]
---

# A ruling approved after the rulings it contradicts

Two owner claims that cannot both stand, neither citing the other, with
a derivation resting on one of them. Debt should be positive in the
conflict component and weighted by what rests on either.
