---
label: TRUST_CORNERS
standing: user
verdict: dissolved
authority: 9b6f24ad, the owner's ruling of 2026-09-11
why:
  - any-of-three-conditions-restores-trust.md
  - ../model.kb/trust-is-per-claim-a-ledgers-trust-is-an-aggregation.md
---

# Which reading of each trust condition holds at the corners?

Dissolved: the question presumed trust is an attribute of the ledger,
and the owner rejected the premise (`TRUST_PER_CLAIM`). The two decisions
it posed, whether unruled leaves block trust and whether a sitting counts
items or weight, do not survive it:

> [!@bukzor] 9b6f24ad
> Unrelated unruled leaves don't block trust in claims that are well founded. Obviously?

> [!@bukzor] 9b6f24ad
> Why does it "count", at all?

What the corners in `examples/corners/` witness, restated: `TRUST_TEST`'s
conditions are aggregations over claims that say when the review is done
or doable; a claim's trust is its own fold; and the two come apart, which
`EMPTY_QUEUE_TRUST` states exactly. "Fits one sitting" is a field
quantity the sandbox does not compute. The weak-arrows corner stands as
the property that demands the arrow record (`GROUND_RECORD`).
