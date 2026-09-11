---
label: IMPORTED_TERMS
standing: bare
verify: kb-dynamics/docs/dev/claims.kb/imported-terms.verify.py
ontology:
  - rule
  - state
  - move
  - permit
  - oblige
  - example
  - flip
  - coverage
  - load event
  - weekly cost
  - stipulated
  - certified
  - obligation
  - standing
stale-when: an outward link that no longer resolves, or an outer theory whose ontology no longer lists a word imported here
---

# imported-terms -- the outer words this project says

Every word this ledger takes from outside `kb-dynamics/` is a claim in
this theory, one per word, resting on the outer claim that coins it. This
theory alone carries `why:` links that leave the subpath; every other
theory imports these words by citing this file. The claim's filename is
the word, so `ls` is the list.

Each claim gives the sense as this project reads it and how the project
uses it. It goes bare where it restates the outer claim and cites it, so
the fold reads the outer standing through it and the weak link, if any,
is located in the outer ledger where it belongs. Three sign `+` for now
-- `certified`, `obligation`, `stipulated` -- because their outer nodes
are discourse-graph claims the ledger tools cannot yet read as claims;
they go bare when the repo-weight rung lands. Reconciliation of sense
with the outer projects is a separate pass: reading each outer theory
against the use made of its word here, and recording each divergence.
