---
label: DEBT
standing: agent
why:
  - model.md
  - imported-terms.md
ontology:
  - component
  - monotone
  - queue
stale-when: a bad state the owner points at whose debt is zero, or a move the owner would endorse that a rule here rejects
---

# debt -- the function no permitted move may raise, and the rules that keep it so

Debt is a vector over the state, one component per kind of rot; good
state is the zero vector. The dynamics claim is one sentence: every
agent move is non-increasing in debt, or raises it with a flag that
lands in the owner's queue. The rules here are the candidate set that
realizes that, split between what a validator checks and what an agent
judges at the move.
