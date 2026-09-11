---
verdicts:
  queue-empty: true
  no-load-bearing-on-proposed: true
  skeleton-right: true
  all-trusted: true
note: >
  Identical in the model to the good state: a derived claim on two owner
  rulings whose arrows may only motivate. DERIVED_TRUST says unread trust
  needs sufficiency, GROUND_RECORD puts it on the arrow, and the model's
  arrow carries nothing yet; this state is the property that demands it.
  It becomes a bad state once the arrow carries sufficiency.
claims:
  ruling-a:
    basis: user
    wording: settled
    grounds: []
    content: [1]
  ruling-b:
    basis: user
    wording: settled
    grounds: []
    content: [2]
  reading:
    basis: derived
    wording: settled
    grounds: [ruling-a, ruling-b]
    content: [3]
---

# A derivation whose arrows only motivate
