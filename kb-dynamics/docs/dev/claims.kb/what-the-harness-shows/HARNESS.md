---
label: HARNESS
standing: agent
why:
  - ../what-no-move-may-raise/DEBT.md
  - ../states-and-moves/MODEL.md
  - ../words-from-outside/IMPORTED_TERMS.md
ontology:
  - property
  - generator
  - counterexample
  - fidelity ladder
  - rung
  - stub
  - trace
  - atom
  - sandbox
non-claim-tokens:
  - TDD
stale-when: a property that cannot fail under any generator this harness can express
---

# harness -- what the model is shown to satisfy, and by what

The harness is a property-based test of the design, not a simulation of
the agent. The agent is replaced by a generator of moves, the properties
are universal claims over move sequences, and coverage is disclosed
(`IMPORTED_COVERAGE`): generation samples, bounded enumeration exhausts
to a depth. Every fixed counterexample becomes a trace with an expected
debt trajectory, an example in the `IMPORTED_EXAMPLE` sense once the
owner has ruled on it.
