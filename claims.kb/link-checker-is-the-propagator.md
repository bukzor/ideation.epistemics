---
certified: ../2026-07-24-000-warrant-audit.prototype/certify_path_breakage.sh
sources: [../sources.kb/claude.md]
depends:
  - ../definitions.kb/refinement-norm.md
  - ../background.kb/prior-art.kb/atms-tms.md
date-observed: 2026-07-24
tags: [repo-weight, mechanism, retraction]
---

`llm.kb-validate-links` already implements retraction propagation.
Renaming a node makes every node that referenced it fail the check, by
name and by field: the probe run on 2026-07-24 retracted
`./two-base-statuses-not-four.md` and got back its `premises:` referrer,
its `depends:` referrer and its `candidate-resolutions:` referrer, each
individually reported. RP does not need a bespoke walker at repo
weight; it needs a naming convention that makes the existing walker
fire.

**Precondition, and it bites.** Frontmatter edges are resolved
unconditionally, whatever the field name. Body references are resolved
only when written explicitly relative — with a leading dot-slash or
dot-dot-slash. A bare `claims.kb/` prefix, and even a markdown link
around one, are both parsed as prose and silently unchecked. This
realm had 16 such
references in its root documents, all invisible to the checker until
they were migrated to the `./` form the same day. The convention is
load-bearing and was nowhere written down, which is the failure mode
`mechanism-over-exhortation` names: a rule enforced by a tool that
gives no sign when you are outside its reach.

The check named above retracts a node and asserts that every referrer
is reported. It restores the tree on any exit.

**Convergence.** Truth maintenance systems solved this in the 1980s and
solved it properly — justification edges, assumption tracking, belief
propagation under retraction
(`../background.kb/prior-art.kb/atms-tms.md`). What is claimed here is
narrower and cheaper: at repo weight the filesystem plus a link checker
recovers the *propagation* half at zero cost, without the label
algebra, and therefore without ATMS's worst-case exponential blowup
(`../questions.kb/atms-cost-at-scale.md`). The trade is that we get
notification, not repair — the tool says which dependents are affected
and a human or agent decides what each one becomes.
