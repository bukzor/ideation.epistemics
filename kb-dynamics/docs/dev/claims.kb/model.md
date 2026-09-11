---
label: MODEL
standing: agent
why:
  - imported-terms.md
  - problem.md
ontology:
  - effective basis
  - atomic
  - duplicate
  - authority
stale-when: a situation the owner meets in practice that needs a different next action and has no state here
---

# model -- what a claim is, and what a state and a move are made of

A state is a ledger (`IMPORTED_STATE`): its claims, each claim's fields,
and the grounds between them. A claim carries a basis and a wording; the
trust it is owed, its effective basis, is computed from its grounds and
never stored. A move (`IMPORTED_MOVE`) is one edit to that state, tagged
with the authority it carries -- the owner's, under a license, or the
agent's own. The claims here fix those
fields and the discipline that keeps the state space small.
