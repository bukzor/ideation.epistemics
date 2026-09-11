---
label: SESSION_SIM
standing: agent
why:
  - trace-sim.md
  - law.md
  - ../../../bukzor-agent-skills/docs/dev/claims.kb/design.claims.kb/ask.md
  - ../../../bukzor-agent-skills/docs/dev/claims.kb/design.claims.kb/commitment.md
ontology:
  - hidden set
  - silence
  - stall
stale-when: a reply policy the owner has ruled wrong
---

# session-sim -- the full game with a hidden owner

The full simulated session: an agent choosing moves under rules, an owner
modeled as a hidden set of commitments with a reply policy, and oracles for
contradiction, underdetermination, arrival, and stalls.
