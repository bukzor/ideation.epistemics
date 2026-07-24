# The `./` prefix is load-bearing and undocumented

**Applied here.** 16 body references across `CLAUDE.md`, `ladder.md`,
`mission.md`, `preservation-audit.md`, `prompts.md` and
`repo-weight-derivation.md` were rewritten from `` `claims.kb/x.md` ``
to `` `./claims.kb/x.md` ``. All 23 such references are now enforced.

**Not applied — this is for you.** `llm-kb` itself is untouched; its
tree was dirty with in-flight work.

**The finding.** `llm.kb-validate-links` resolves frontmatter edges
unconditionally, whatever the field name — that part is excellent, and
it is what makes retraction-by-rename work at all. But it resolves
*body* paths only when they begin `./` or `../`. A bare
`` `claims.kb/x.md` `` is treated as prose. So is a markdown link
around one. Both pass silently, forever.

Discovered by accident: the certification probe reported two referrers
missing, which looked like a propagation gap and was actually a
recognition gap. Sixteen references in this realm's most-read documents
had never been checked.

**Suggested fix, in preference order.** (1) Resolve any path containing
a `.kb/` segment, prefix or not — the segment is unambiguous enough.
(2) Failing that, warn on path-shaped text the checker declined to
resolve, so being outside its reach is visible. (3) Failing that,
document the convention. Option 3 alone is exhortation, and this is
precisely the failure it produces: a rule with teeth that gives no sign
when you step outside it.

**What to check.** Whether other realms have the same silent rot. The
probe is `../../../2026-07-24-000-warrant-audit.prototype/certify_path_breakage.sh`
and it is realm-agnostic.
