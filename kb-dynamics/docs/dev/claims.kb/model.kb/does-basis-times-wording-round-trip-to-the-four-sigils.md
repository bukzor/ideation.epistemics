---
label: ROUND_TRIP
standing: open
why:
  - standing-factors-into-basis-and-wording.md
  - ../imported-terms.kb/standing.md
---

# Does basis times wording round-trip to the four sigils?

`IMPORTED_STANDING` grades the factoring by whether the two fields
round-trip to the on-disk sigils. Basis alone maps onto them: `user` is
the owner's sigil, `derived` and `evidence` are bare, `proposed` is the
agent's, `question` is open. Wording has no sigil, so a round trip
through the incumbent notation loses it; and the incumbent carries
`verdict:`, `todo:` and `verify:`, which this model's claim does not.

Open until the reconciliation pass through `IMPORTED_TERMS` decides
whether wording becomes a field of the incumbent, or stays a quantity
the model reads off the body's draft callouts.
