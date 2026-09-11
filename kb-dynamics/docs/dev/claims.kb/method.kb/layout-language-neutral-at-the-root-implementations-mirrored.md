---
label: LAYOUT
standing: agent
todo: true
why:
  - the-core-stays-pure-and-total.md
  - ../imported-terms.kb/example.md
---

# Layout: language-neutral data at the root, implementations mirrored module for module

Everything language-neutral lives at the subpath root, and the two
implementations mirror each other module for module so the port is one
to one.

```
kb-dynamics/
  README.md
  docs/dev/claims.md, claims.kb/    this ledger; the dogfood
  examples/                         language-neutral, consumed by every implementation
    bad-states/                     one file each; front matter records provenance
    good-states/                      (which ledger, which commit, which confusion)
    traces/                         move sequences with expected debt trajectory;
                                      every fixed counterexample lands here
  python/
    pyproject.toml
    src/kb_dynamics/
      model.py        transition.py  rules.py  debt.py     the port surface
      enumerate.py    bounded exhaustive reachability
      examples.py     loader for ../../examples
      agents/         constant.py  random.py  biased.py    the fidelity ladder's rungs
    tests/
      strategies.py   test_repayable.py  test_examples.py
      test_necessity.py  test_reachability.py              the five properties
  lean/
    KbDynamics/       Model  Transition  Rules  Debt  Repayable  Necessity
```

- `examples/` is the bridge to the field and the only outside input the
  sandbox takes. A bad state found in a real ledger is recorded once,
  with provenance, and checked by every implementation forever; traces
  are the harness's regression residue.
- The four core modules are the whole port surface. `agents/` and
  `tests/` have no Lean counterpart: the Lean side replaces sampling
  with theorems, so `test_repayable.py` maps to `Repayable.lean`, not to
  a test file.
- Left out: a collection of rule-pricing records. That is the field-side
  artifact and belongs beside the must-read tooling, not in the sandbox.

Decided and partly built: the ledger, `examples/` (bad and good states,
no traces yet), and `python/` with `model`, `debt`, `examples`, and
`test_examples`. `transition`, `rules`, `agents/`, the four remaining
property tests, and `lean/` wait on the property that demands each.
