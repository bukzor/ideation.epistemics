---
label: LEAF_EXEMPT
standing: user
authority: f65fbdf3#L815
why:
  - components.md
  - ../problem.kb/most-open-questions-carry-no-obligation.md
  - ../imported-terms.kb/load-event.md
---

# A leaf is low priority for review, never exempt from it

No claim is exempt from the owner's review; a claim nothing rests on is
reviewed last. In a healthy ledger that is what the top of the queue
looks like:

> [!@bukzor] f65fbdf3#L815
> Exempt? No. Why should it be? Low priority, surely yes. But a very-healthy ledger will hopefully have such low-priority as its highest-priority review items, I'd think.

> [!@bukzor] f65fbdf3#L815
> Separately, I'm pretty sure "exempt from user review" is not something that should exist. Or can exist, even? How could that even work?

What the earlier draft called exemption was omission from the queue,
which amounts to the same thing and is withdrawn: `COMPONENTS` now
counts every claim. `MINUTIAE` stands as a fact about priority, not
about exemption. Agent pruning of leaves is permitted only under guards
(`PRUNE_GUARD`).
