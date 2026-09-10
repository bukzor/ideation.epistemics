---
label: PURE_AND_TOTAL
standing: agent
why:
  - the-harness-core-is-the-implementation.md
  - lean-pays-back-only-after-the-design-stops-changing.md
---

# The core stays pure and total: no I/O, no exceptions, exhaustive matches

`transition`, `debt`, and the rules are pure functions over the state,
total on their domain, with every match exhaustive. That keeps the
in-memory and on-disk backings interchangeable (`CORE_IS_IMPLEMENTATION`)
and makes the eventual Lean translation mechanical, an agent's job
rather than a redesign (`LEAN_DEFERRED`). An exhaustive match is also
the move table's empty-cell check enforced by the language.
