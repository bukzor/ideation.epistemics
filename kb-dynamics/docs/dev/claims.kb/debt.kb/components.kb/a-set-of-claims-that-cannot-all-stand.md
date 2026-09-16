---
label: CONFLICT
standing: user
authority:
  address: dfc18e9d
  words: the fact that the reduction for this component is RESOLUTION makes me think its old name is no longer good. "CONFLICT" seems more appropriate?
  about: the merge of the component as first ruled (f65fbdf3#L815, "That's a good addition, yes.") with the pair-attribute ruling, both the owner's
why:
  - ../../problem.kb/ill-grounded-agent-claims-are-where-distrust-enters.md
  - ../../model.kb/effective-basis-is-computed-from-grounds-not-stored.md
---

# A set of claims that cannot all stand

A conflict is an attribute of a pair of claims, or of a larger minimal
set (`CYCLIC_CONFLICT`), that says they cannot all stand. The common
case is a ruling that lands on one claim while the claims that rested
on the old reading keep it, and the owner named the future form:
dependents that no longer match an import that moved. Neither party is
presumed wrong. Found by comparing a claim's text against rulings newer
than it on the claims it grounds on; prioritized by what rests on any
member. Reduced by `RESOLUTION`.

The attribute is derivable from the claims, expensive to derive, and so
may be cached; a cached conflict is a cache like any other, possibly
stale, and never the thing itself.

> [!@bukzor] dfc18e9d
> This should be treated as a (possibly stale) caching of a (expensive) derivable attribute. Conflict is not a type as much as an _attribute_ of a _pair_ of claims.

> [!@bukzor] dfc18e9d
> Open question: is it possible to have a cyclic conflict where no two claims conflict but the cycle constitutes a conflict? If so, my "pair" is not accurate.

Declined: a conflict record beside the ledger. It would be asserted by
the agent that found it and go stale the moment either claim moved,
which is what `EFFECTIVE_BASIS` declined for trust. The earlier label named one
party's condition where the component counts a relation, and once the
reduction existed the name no longer fit.
