---
rot: wording
provenance:
  ledger: kb-dynamics/docs/dev/claims.kb
  claim: model.kb/an-arrow-carries-its-kind-and-sufficiency.md
  commit: 589ffac
  note: >
    GROUND_RECORD: standing user on "seems good enough to me" over an agent
    draft, the heaviest such claim in the ledger. BASIS_WORDING reads that as
    basis user, wording draft; WORDING_DEBT weights it by what rests on it.
claims:
  ruling:
    basis: user
    wording: draft
    grounds: []
    content: [1]
  d1:
    basis: derived
    wording: settled
    grounds: [ruling]
    content: [2]
  d2:
    basis: derived
    wording: settled
    grounds: [d1]
    content: [3]
  d3:
    basis: derived
    wording: settled
    grounds: [d1]
    content: [4]
---

# An approval of "seems good enough" on an agent draft

The owner endorsed the content and never settled the text. Every claim
grounded on it loads the agent's words as the owner's; the debt is the
draft wording times what rests on it.
