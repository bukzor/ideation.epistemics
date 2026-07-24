--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# prior-art.kb — partially-convergent prior work

One file per external system/theory that independently arrived at part
of the realm's design. Frontmatter per `../prior-art.jsonschema.yaml`;
body states: what it is, the convergent facet, the divergent gap
("what it lacks that {TL, RN} adds"), and the verification route.

Provenance discipline: `sources:` says who characterized it.
Model-memory entries (via the captured chat) carry **no** `certified:`
field — absence is the open cell, meaning "recalled, not read." When
someone reads the actual literature, add the paper as a root
`sources.kb/` node, cite it here, and set `certified:` to name what was
checked. Operator-contributed entries cite `../../sources.kb/bukzor.md`.

This replaced a `likelihood` number on 2026-07-24. The old field's own
gloss — "inherits the chat source's 0.7 until independently verified
against the actual literature" — described an open obligation with a
named discharge route, not a confidence, so it is now said directly
(`../../repo-weight-derivation.md`).

Belongs: external prior work. Our own systems (ACS, FP2, the skill) are
definitions/claims at root, not prior art.

Operator-authored antecedents that predate this project — convergent by
provenance, not by literature — nest under `bukzor.kb/` rather than
sitting flat here: same shape, schema `bukzor.jsonschema.yaml` (stub of
`prior-art.jsonschema.yaml`), but verified by reading the artifact, not
by discounted recall. See `bukzor.kb/CLAUDE.md`.
