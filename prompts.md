# Transport prompts — ACS / FP2 / STTT-Search / Knot-Search

Extracted verbatim from the captured chat "Knot theory representations
for GPU computation" (2026-07-24, message 054; see
`sources.kb/knot-theory-chat.md`). Each is standalone, <1000 tokens,
addressed to a fresh LLM executor equipped with an appropriate
verifier.

Dependency DAG (acyclic): `acs` ← `fp2` ← {`sttt-search`,
`knot-search`}. Execute upstream first, or supply the upstream
deliverable alongside.

## Deltas — executors inherit these revisions (per RN, last wins)

- **Obligation is derived, not stored** (2026-07-24, operator fiat;
  `claims.kb/obligation-is-derived-not-stored.md`): drop `obligated`
  from ACS's assumed status set. An open claim is obligated exactly to
  the extent conclusions rest on it — an importance-weighted
  reverse-dependency query over the store. Where a prompt says
  "statuses described/stipulated/obligated/certified(checker)", read
  "described/stipulated/certified(checker)" plus an obligation view.
- **Routes/checks are named at discharge time**, never demanded at
  claim entry (same fiat).
