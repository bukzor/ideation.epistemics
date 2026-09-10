---
label: IMPORTED_OBLIGATION
standing: agent
why:
  - ../../../../../claims.kb/obligation-is-derived-not-stored.md
  - ../../../../../claims.kb/warrant-by-field-presence.md
---

# A claim's obligation is derived from what rests on it, never stored

A claim with no warrant field is an open obligation, and its obligation is
derived rather than stored: it is obligated exactly to the extent
conclusions rest on it, an importance-weighted reverse-dependency query
over the store. Here that query is the count of what rests on a claim, and debt is what
it sums. Distinct from `oblige.md`, which is what a rule requires of
a move. Outer argument not restated.
