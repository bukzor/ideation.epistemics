---
term: Agda Claim System
aliases: [ACS]
domain: claim-system epistemics
related: [fp2.md, total-ledger.md, refinement-norm.md]
---

A verified claim-ledger kernel in Agda; the central object is a claim
store, not a proof. Statuses described/stipulated/certified plus a
derived obligation view; dependency edges; versioned retraction
propagation. Two-level discipline (the chat's MT): the store is an
object-level value — dynamic, last-wins — while Agda's type theory
certifies only the transition rules, which are monotonic. Build
prompt: `../prompts/acs.md`.
