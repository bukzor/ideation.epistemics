# This realm's schemas now diverge from the shipped skill

**Applied.** `claims.jsonschema.yaml` and `deductions.jsonschema.yaml`
here no longer match `Skill(llm-discourse-graph)`. Both carry a
`MIGRATED, 2026-07-24` header saying so and pointing at the derivation.

**Why local and not upstream.** Dogfood before proposing. The realm
that argues for a schema change should be the first to run it, and
`../../../preservation-audit.md` is only credible if written from
inside. Also practical: `bukzor-agent-skills` had a dirty tree with
in-flight `llm-kb` work, and editing under someone else's uncommitted
changes is how you lose them.

**The divergences.** `status` removed (contested is computed from a
live contradiction deduction, not declared). `likelihood` removed.
`stipulated:` and `certified:` added. Retraction moved from a field to
a filename suffix. Claims may no longer `depends:` on claims.

**What to check.** Whether to promote or revert. If promote: the
argument to carry upstream is `../../../preservation-audit.md`, which
gives each incumbent aspect an improves/preserves/obviates verdict —
8 preserves, 5 improves, 3 obviates, 1 deliberate abstention. If
revert: this realm's nodes need `status:` restored, which is a sed.

**The risk while divergent.** Any agent arriving with the shipped
skill's conventions in context will write `status: asserted` here and
the validator will reject it. That is the intended behaviour but it
will read as a bug. The header comments are the only warning.
