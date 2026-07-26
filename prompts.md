# Transport prompts — ACS / FP2 / STTT-Search / Knot-Search

Extracted verbatim from the captured chat "Knot theory representations
for GPU computation" (2026-07-24, message 054; see
`./sources.kb/knot-theory-chat.md`). Each is standalone, <1000 tokens,
addressed to a fresh LLM executor equipped with an appropriate
verifier.

Dependency DAG (acyclic): `acs` ← `fp2` ← {`sttt-search`,
`knot-search`}. Execute upstream first, or supply the upstream
deliverable alongside.

## Deltas — executors inherit these revisions (per RN, last wins)

- **Obligation is derived, not stored** (2026-07-24, operator fiat;
  `./claims.kb/obligation-is-derived-not-stored.md`): drop `obligated`
  from ACS's assumed status set. An open claim is obligated exactly to
  the extent conclusions rest on it — an importance-weighted
  reverse-dependency query over the store. Where a prompt says
  "statuses described/stipulated/obligated/certified(checker)", read
  "described/stipulated/certified(checker)" plus an obligation view.
- **Routes/checks are named at discharge time**, never demanded at
  claim entry (same fiat).
- **Toy-weight modality is admitted; phases reorder** (2026-07-25,
  derived, not fiat; `./deductions.kb/toy-weight-is-a-degenerate-point-of-acs.md`):
  payload structure and checker strength are parameters, not
  commitments. Atomic constants are legal λΠ payloads and
  `certified(checker)` is an open set, so a store of prose-atom claims
  checked by fiat/LLM-judge/script is a valid ACS instance —
  trust-base-of keeps weak certificates visibly weak. Consequence:
  deliverables 2–4 (store, transitions, retraction drill, queries) may
  be built and acceptance-tested at toy weight before the λΠ embedding
  (deliverable 1) exists; the embedding upgrades payloads, it does not
  gate the kernel.
