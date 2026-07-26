---
certified: ../2026-07-24-000-warrant-audit.prototype/certify_type_topic_conflation.py
sources: [../sources.kb/claude.md]
depends: [../definitions.kb/repo-weight.md]
date-observed: 2026-07-26
tags: [repo-weight, layout, defect]
---

At repo weight a node's **type** and its **topic** are carried by the same
path component, and the tooling cannot separate them. `collection_of()`
in `../2026-07-24-000-warrant-audit.prototype/warrant_audit.py` is defined
as "nearest enclosing `*.kb/`", so any node inside an elaboration scope
reports that scope's name in place of its collection: the ACS glossary
entry under `../sources.kb/knot-theory-chat.kb/glossary.kb/` reports
`glossary`, and `../background.kb/prior-art.kb/atms-tms.md` reports
`prior-art`. Neither is a collection. The certificate asserts both, plus
an unelaborated control that still reports correctly.

The defect is visible in the audit's own published output, which lists
`claims -> prior-art` and `claims -> bukzor` alongside genuine
collections — buckets that look like collections and are elaboration
scopes.

Two consequences. First, the edge-typing diagnostic silently
under-reports: an edge into an elaborated scope is bucketed under a name
that no rule mentions, so a claim → claim `depends:` hiding in a
sub-scope is not counted as the leak it is. Second, and structurally:
the failure is *specific to elaboration*. A flat graph never triggers
it, so the defect grows exactly with the recursion the discourse-graph
design calls for and `../inquiry-scoped-layout.md` proposes to make
routine.

Type and topic are independent facts. Encoding them in one component was
never decided; it is a consequence of collections being directories and
elaboration also being directories.
