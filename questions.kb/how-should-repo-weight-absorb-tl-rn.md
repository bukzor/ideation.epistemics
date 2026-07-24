---
sources: [../sources.kb/bukzor.md]
candidate-resolutions:
  - ../claims.kb/warrant-by-field-presence.md
  - ../claims.kb/two-base-statuses-not-four.md
  - ../claims.kb/retraction-breaks-the-path.md
  - ../claims.kb/link-checker-is-the-propagator.md
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

Open, with a proposal on the table: `../repo-weight-derivation.md`
carries the derivation, `../preservation-audit.md` the side-by-side
against the incumbent, and `../claims.kb/warrant-by-field-presence.md`
the core of it. Two points are held for operator fiat — whether
`likelihood` survives, and whether `questions.kb/` stays given that the
axioms merge open claims with questions.

Method settled first: the shipped design is prior art and evidence of
intent, not canon
(`../claims.kb/incumbent-design-is-evidence-not-canon.md`). The
question was first posed as patch vs. rewrite; that framing is retired,
since both branches measure edit distance from the incumbent and so
presume its authority.

**The semantics, so far.** No status field survives. Warrant is field
presence — absence is the open cell, `stipulated:` is fiat, `certified:`
names a re-runnable check — and retraction is a rename to
`NAME.retracted.md`, so the path dies and the existing link checker
propagates it. `obligated` is a reverse-dependency view, `contested` a
live contradiction deduction; both computed, neither stored. Today's
shipped schema is `asserted/contested/retracted` plus `likelihood`.

**Constraints.**

- *Preservation audit.* The incumbent has aspects worth keeping,
  inventoried in `../preservation-audit.md`. Each gets a verdict — improves, preserves, or obviates — argued
  side-by-side. Silence is not a verdict; an aspect dropped without one
  is a regression. This is the deliverable's acceptance test, not a
  postscript to it. Five entries are convergent: the incumbent reached
  a {TL, RN} principle from argumentation prior art, months earlier and
  on other grounds. Breaking one of those is evidence against the
  derivation, not against the incumbent.
- *Timing.* `bukzor-agent-skills/design-next.kb/` is designing v2's
  epistemic class now (`040-design.kb/class-epistemic.md`), which
  currently inherits v1's vocabulary without reference to this realm.
  Cheapest before v2 solidifies, dearer after.
- *Mechanism, not prose.* **Largely discharged.** Something must walk
  support edges on retraction; per `mechanism-over-exhortation`, an
  instruction telling agents to propagate is the failure mode v1 already
  disproved, and the cost is demonstrated — a one-off audit
  (`../2026-07-24-000-warrant-audit.prototype/`) found a live rotted
  edge in `template.python-project`, a deduction still concluding a
  retracted claim. The walker turns out to exist already:
  `llm.kb-validate-links` resolves every frontmatter edge, so retracting
  by rename surfaces all dependents at zero cost
  (`../claims.kb/link-checker-is-the-propagator.md`, certified). What
  remains bespoke is the narrower audit of deferred debt.
- *Edge typing.* The typed support edge already exists —
  `premises`/`conclusion` on deductions, with polarity. The problem is
  that `depends:` leaks around it, documented as context yet written
  claim→claim as support, contradicting the design's own rule that
  deductions are the sole mechanism connecting claims. Close the leak
  rather than inventing an edge.
- *Path conventions.* Two are live at once: file-relative (a leading
  `../`, current per ADR) and collection-relative (a bare `claims.kb/`
  prefix, still in older graphs). Settle this — and note it is now
  load-bearing rather than cosmetic, since only the explicitly-relative
  form is resolved in body text, so the bare form is silently unchecked
  (`../.claude/todo.kb/suggestions-to-audit.kb/relative-path-prefix-is-unwritten-law.md`).
- *Dogfood.* **Done, 2026-07-24.** This realm's own graph migrated:
  local schemas diverged, `status`/`likelihood` stripped, the last
  claim→claim `depends:` promoted to a deduction. All three checks pass
  against it.
- *Scope discipline.* {TL, RN} is a theory of truth-apt content;
  whether it should reach `Skill(llm-design-kb)`'s held/desired tower
  at all is separable, and the conservative answer is no.

Lands in that repo's design tower — its layer semantics, deliberately
not edited from here.
