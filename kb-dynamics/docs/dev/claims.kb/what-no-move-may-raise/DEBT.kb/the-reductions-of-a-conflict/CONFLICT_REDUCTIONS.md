---
label: CONFLICT_REDUCTIONS
standing: user
authority:
  address: dfc18e9d
  words: agent may _pick_ a winner, given sufficient cause. It may not create a user-authority claim due to this pick, is all.
  about: the question "what may an agent do to a user claim that a later ruling contradicts?"
why:
  - ../the-kinds-of-rot/COMPONENTS.kb/a-set-of-claims-that-cannot-all-stand/CONFLICT.md
  - ../every-agent-authority-move-is-queued-for-veto/QUEUE_VETO.md
  - ../../../states-and-moves/MODEL.kb/a-move-is-tagged-by-the-authority-it-carries-not-the-hands/AUTHORITY_NOT_HANDS.md
---

# The reductions of a conflict: resolve under agent authority, or mark it; either lands in the queue

Two claims that conflict must eventually be resolved, and either may be
the wrong one: the newer ruling is the likelier survivor, not the
certain one. An agent meeting the conflict has two moves, both queue
items under `QUEUE_VETO`:

- resolve: pick a winner, given sufficient cause, and file the pick as
  an agent-authority claim queued for veto. The pick never enters as a
  user-authority claim, and never amends one.
- mark: record the conflict as it stands and queue it, well-rankable,
  for the owner.

Which the agent should choose depends on the context available and the
agent's instructions. A resolution is the better move when the veto is
cheaper than the conflict, cost against benefit, and when the veto is
the more uncertain of the two; the owner gave both conditions as
examples, not a closure.

> [!@bukzor] dfc18e9d
> it's most likely that the new ruling is correct and the old is outmoded, but it's possible that the new thing is the one that's wrong.
> in either case we (eventually) need to resolve them.

> [!@bukzor] dfc18e9d
> agent may _pick_ a winner, given sufficient cause. It may not create a
> user-authority claim due to this pick, is all. It may (per already-standing
> rules) create a agent-authority claim that represents its pick, queued for
> veto review.

> [!@bukzor] dfc18e9d
> There's two distinct ways to do that:
>
> 1. choose an agent-authorized resolution and queue _that_ for veto
> 2. mark and queue the conflict as-is
>
> Which one the _I want_ agent to pick sensitively depends on available context
> and agent instruction.

> [!@bukzor] dfc18e9d
> As above, agent may resolve it, but that resolution is enqueued. The move is
> good if the veto has better cost/benefit than the conflict. I'd also think the
> veto needs to be more uncertain than the conflict. (not exhaustive)

These are the reductions `CONFLICT` lacked: the other components each
name theirs, and this one named none. The list is open; a fifth
reduction is a bullet here, not a new label.
