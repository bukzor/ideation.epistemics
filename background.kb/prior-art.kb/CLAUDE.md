--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# prior-art.kb — partially-convergent prior work

One file per external system/theory that independently arrived at part
of the realm's design. Frontmatter per `../prior-art.jsonschema.yaml`;
body states: what it is, the convergent facet, the divergent gap
("what it lacks that {TL, RN} adds"), and the verification route.

Provenance discipline: `sources:` says who characterized it —
model-memory entries (via the captured chat) carry likelihood ≤ 0.7
until someone reads the actual literature; when that happens, add the
paper as a root `sources.kb/` node, cite it here, and raise likelihood.
Operator-contributed entries cite `../../sources.kb/bukzor.md`.

Belongs: external prior work. Our own systems (ACS, FP2, the skill) are
definitions/claims at root, not prior art.
