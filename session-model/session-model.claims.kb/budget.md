---
label: BUDGET
standing: agent
why:
  - ../../../bukzor-agent-skills/docs/dev/claims.kb/strata.claims.kb/carriage.md
ontology:
  - load event
  - weekly cost
stale-when: a carrier whose load frequency cannot be read from its tier
---

# budget -- the instruction layer priced, arithmetic only

The cheapest model in the family: no trace, no owner. Each directive times
its carrier's load frequency, summed over the layer.
