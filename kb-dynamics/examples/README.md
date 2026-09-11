# examples -- the sandbox's only outside input

Language-neutral states, one per file, consumed by every implementation.
Each file is YAML front matter over a short prose note. The front matter
carries the provenance (which ledger, address, or owner remark the state is
drawn from), the state itself under `claims:`, and for a bad state the
`rot:` component the design says must be positive on it.

- `bad-states/` -- states the owner would call rotten; property two says
  each has debt above zero in the named component.
- `good-states/` -- states the owner would trust; property three says
  each has debt zero.
- `corners/` -- queue shapes: states where the review conditions
  (`TRUST_TEST`, read as aggregations over claims) and per-claim trust
  come apart. Each pins the verdict the implementation gives under every
  reading, with a note on what the state witnesses.
- `traces/` -- move sequences with an expected debt trajectory; every
  fixed counterexample lands here.

A claim is `{basis, wording, grounds, content}`; content is a set of
integer atoms standing in for recognized meaning (`ATOM_CONTENT` in
`../docs/dev/claims.kb/harness.md`).
