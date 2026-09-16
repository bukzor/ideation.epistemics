---
label: PRUNE_GUARD
standing: user
authority:
  address: f65fbdf3#L995
  words: seems good enough to me
  about: the draft below
why:
  - ../what-priority-a-leaf-gets/LEAF_PRIORITY.md
  - ../../../why-ledgers-rot/PROBLEM.kb/agents-mistake-the-owners-content-for-fabrication/PRUNE_BIAS.md
  - ../the-candidate-rule-set/CANDIDATE_RULES.md
---

# Two guards on an agent's pruning of a leaf: basis, and a record in the queue

An agent never prunes a claim with `basis: user`, and every prune lands
in the review queue as a deferred item, reversible on sight. The owner
permits agents to close or delete leaves and asked for checks:

> [!@bukzor] f65fbdf3#L815
> I'd want checks and guards for that. Often what agents would choose to prune is what I struggled to get admitted, and simply is not-yet grounded into the kb enough to make its value clear.

Of four separable guards, two are taken:

- basis: a claim with `basis: user` is never pruned by an agent
- record: every prune lands in the review queue as a deferred item, so it
  is reversible on sight (`DEFER_NOT_DISMISS`)

Declined: an age guard, a proxy for "not yet grounded enough" that the
record guard covers directly; and propose-only pruning, which
reintroduces the turn-waste the owner named for shorthand.
