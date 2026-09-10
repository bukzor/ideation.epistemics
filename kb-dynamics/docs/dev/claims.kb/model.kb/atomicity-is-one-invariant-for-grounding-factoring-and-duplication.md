---
label: ATOMICITY
standing: agent
why:
  - standing-factors-into-basis-and-wording.md
---

# Poor grounding, poor factoring, and duplication are one failure of atomicity

A claim is atomic when it has exactly one basis and each of its grounds
supports the whole claim. The owner's three complaints are that
invariant failing three ways:

> [!@bukzor] chat.md#L259
> Changing focus: another problem I have is that the claims are poorly grounded, poorly factored (should be split to have different grounding per piece, for example) or duplicate (or, worse, near-duplicate).

- a claim that should be split is one whose grounds cannot be given as a
  single set supporting all of it;
- an ungrounded claim has an empty set and no `user` or `evidence`
  basis;
- a duplicate, properly grounded, would rest entirely on the claim it
  duplicates -- identical ground sets, or X grounds Y and Y adds only
  wording -- so it adds nothing and the graph can flag it.

One test, three failure modes; the mechanical part of it is in the
validator and the judgment part is a rule at the move that creates the
risk (`CANDIDATE_RULES` in `../debt.md`).
