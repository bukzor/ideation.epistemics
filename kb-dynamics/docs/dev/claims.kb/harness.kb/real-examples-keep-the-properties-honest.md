---
label: REAL_EXAMPLES_GUARD
standing: agent
why:
  - every-piece-starts-as-a-constant-and-climbs-a-fidelity-ladder.md
  - ../imported-terms.kb/example.md
---

# Bad states drawn from real ledgers are what keep the properties honest

The constant can ossify: a random generator passing every property can
be read as "the design is agent-independent" when the properties are
merely weak. The guard is the second property's input -- bad states
taken from real ledgers with their provenance, added as they are found.
Real failures are the only input from outside the sandbox the harness
needs, and this ledger's own staleness condition is that guard failing:
a property that passes under a random generator while a real ledger
still drifts under the same rules.
