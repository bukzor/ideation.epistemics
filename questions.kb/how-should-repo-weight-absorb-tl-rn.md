---
sources: [../sources.kb/bukzor.md]
candidate-resolutions: [../claims.kb/two-base-statuses-not-four.md]
depends:
  - ../claims.kb/repo-weight-rung-is-unbuilt.md
  - ../claims.kb/incumbent-design-is-evidence-not-canon.md
  - ../claims.kb/obligation-is-derived-not-stored.md
  - ../definitions.kb/repo-weight.md
tags: [repo-weight, notation, strategy]
---

How does repo weight absorb {TL, RN}? Derive the collections, statuses
and edges from the axioms directly, asking whether five collections and
the design/discourse split are what {TL, RN} actually implies.

Open. What is settled is only the method: the shipped design is prior
art and evidence of intent, not canon
(`../claims.kb/incumbent-design-is-evidence-not-canon.md`). The
question was first posed as patch vs. rewrite; that framing is retired,
since both branches measure edit distance from the incumbent and so
presume its authority.

**The semantics, so far.** Applying this realm's settled claims
uniformly gives stored `{asserted, stipulated, retracted}`; derived
views `{certified, obligated}` — certified read off a named re-runnable
check, obligated off importance-weighted reverse dependencies;
`contested` dropped or given a resolution procedure. Today's shipped
schema is `asserted/contested/retracted` plus `likelihood`.

**Constraints.**

- *Preservation audit.* The incumbent has aspects worth keeping. Each
  gets a verdict — improves, preserves, or obviates — argued
  side-by-side. Silence is not a verdict; an aspect dropped without one
  is a regression. This is the deliverable's acceptance test, not a
  postscript to it.
- *Timing.* `bukzor-agent-skills/design-next.kb/` is designing v2's
  epistemic class now (`040-design.kb/class-epistemic.md`), which
  currently inherits v1's vocabulary without reference to this realm.
  Cheapest before v2 solidifies, dearer after.
- *Mechanism, not prose.* Something must walk support edges on
  retraction. Per `mechanism-over-exhortation`, an instruction telling
  agents to propagate is the failure mode v1 already disproved — and
  the cost is demonstrated, not hypothetical: a one-off audit
  (`../2026-07-24-000-warrant-audit.prototype/`) found a live rotted
  edge in `template.python-project`, a deduction still concluding a
  retracted claim.
- *Edge typing.* `depends:` is documented as context ("without
  implying support or refutation") yet is also written claim→claim as
  genuine support. A walker cannot separate them from the data, so the
  edge must be typed.
- *Path conventions.* Two are live at once: file-relative (a leading
  `../`, current per ADR) and collection-relative (a bare `claims.kb/`
  prefix, still in older graphs). Settle this.
- *Dogfood.* This realm's own graph migrates too — a real cost, and
  the only honest test of the result.
- *Scope discipline.* {TL, RN} is a theory of truth-apt content;
  whether it should reach `Skill(llm-design-kb)`'s held/desired tower
  at all is separable, and the conservative answer is no.

Lands in that repo's design tower — its layer semantics, deliberately
not edited from here.
