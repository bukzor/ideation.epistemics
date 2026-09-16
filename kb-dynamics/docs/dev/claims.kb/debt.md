---
label: DEBT
standing: agent
why:
  - model.md
  - imported-terms.md
ontology:
  - component
  - queue
  - reduction
stale-when: a bad state the owner points at whose debt is zero, or a move the owner would endorse that a rule here rejects
---

# debt -- the function no permitted move may raise, and the rules that keep it so

Debt is a vector over the state, one component per kind of rot, and the
kinds are the nested `components` theory; a reduction is a move that
lowers a component, and each component names its reductions. Debt is wanted; the dynamics
claim is one sentence: no agent move raises debt that nothing will
surface, so every item of it stays repayable and the owner's queue is
where it waits. The rules here are the candidate set that
realizes that, split between what a validator checks and what an agent
judges at the move.
