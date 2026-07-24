---
sources: [../sources.kb/bukzor.md]
candidate-resolutions: [../claims.kb/two-base-statuses-not-four.md]
depends:
  - ../claims.kb/repo-weight-rung-is-unbuilt.md
  - ../claims.kb/obligation-is-derived-not-stored.md
  - ../definitions.kb/repo-weight.md
tags: [repo-weight, notation, strategy]
---

How does repo weight absorb {TL, RN} — by patch or by rewrite? Live as
of 2026-07-24: the operator is considering re-deriving
`Skill(llm-discourse-graph)` (and possibly `Skill(llm-design-kb)` and
others) from this realm's work, rather than amending the existing
schemas.

**The semantics, either way.** Applying this realm's settled claims
uniformly gives stored `{asserted, stipulated, retracted}`; derived
views `{certified, obligated}` — certified read off a named re-runnable
check, obligated off importance-weighted reverse dependencies;
`contested` dropped or given a resolution procedure. Today's shipped
schema is `asserted/contested/retracted` plus `likelihood`.

**The fork.**

- *Patch* — add statuses and a certificate field to the existing
  schemas. Cheap, non-breaking, leaves the five-collection vocabulary
  and its edge semantics untouched. Risks bolting {TL, RN} onto a
  shape not derived from it — the accretion the operator's own
  "subtract, don't accrete" value warns against.
- *Rewrite* — derive the collections and edges from {TL, RN} directly.
  Aligns the daily substrate with the axioms, and is the moment to ask
  whether five collections and the design/discourse split are what the
  axioms actually imply. Costs a migration of every existing `.kb/`,
  this realm's graph included.

**Inputs to the decision.**

- *Timing.* `bukzor-agent-skills/design-next.kb/` is designing v2's
  epistemic class now (`040-design.kb/class-epistemic.md`), which
  currently inherits v1's vocabulary without reference to this realm.
  A rewrite is cheapest before v2 solidifies, dearer after.
- *Mechanism, not prose.* Whatever ships, something must walk
  `depends:` on retraction; `llm.kb-validate` is the existing surface.
  Per `mechanism-over-exhortation`, an instruction telling agents to
  propagate is the failure mode v1 already disproved.
- *Dogfood.* Self-application means this realm's own graph migrates
  too — a real cost, and the only honest test of the result.
- *Scope discipline.* The design/discourse split is deliberate
  (held/desired vs. truth-apt). {TL, RN} is a theory of truth-apt
  content; whether it should reach the design tower at all is a
  separable question, and the conservative answer is no.

Settles by operator decision, in that repo's design tower — its layer
semantics, deliberately not edited from here.
