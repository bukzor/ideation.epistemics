---
label: TRACE_SIM
standing: agent
why:
  - ../../../bukzor-agent-skills/docs/dev/claims.kb/strata.claims.kb/carriage.md
  - budget.md
ontology:
  - trace
  - event
  - recognizer
  - dead carrier
stale-when: a runtime event kind that traces cannot express
---

# trace-sim -- a session as an event trace with carriers loading and junctures firing

The first simulated interaction, with no owner in it. Traces are generated,
carriers load according to their tier, and each juncture is checked for an
arriving directive. Buildable before any question about the owner is settled.
