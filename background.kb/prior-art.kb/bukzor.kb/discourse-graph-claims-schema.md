---
title: "llm-discourse-graph claims.kb schema"
originators: [bukzor]
sources: [../../../sources.kb/bukzor.md]
converges-on: [TL, RP]
tags: [prior-art, bukzor]
---

`Skill(llm-discourse-graph)` — the five-collection epistemic graph
(questions/claims/deductions/sources/definitions) this very realm's
root `claims.kb/` runs on. Its `claims.jsonschema.yaml`: a typed claim
node with `status ∈ {asserted, contested, retracted}`, `likelihood`,
`sources`, and `depends` edges — TL's "claim as addressable, statused
node" as shipped infrastructure, and `depends` is exactly RP's
substrate (edges to walk on retraction), predating RP by name.

Gap: three statuses, not TL's tripartite {checked certificate, open
obligation, declared axiom} — `asserted` conflates a silently-trusted
claim with a genuinely open one, no discharge-route concept. `contested`
names a state with no resolution procedure (Advocate/Skeptic/Arbiter
lives in a separate, uncoupled instruction). `depends` edges exist but
nothing in the skill *walks* them on retraction — RP is latent in the
schema, not implemented; this realm's root graph is the schema plus
{TL, RN} patched on top, live.

Verify: `~/.claude/skills/llm-discourse-graph/jsonschema/claims.jsonschema.yaml`.
