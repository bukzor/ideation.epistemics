---
title: "verified-claim.kb / observation.kb split"
originators: [bukzor]
sources: [../../../sources.kb/bukzor.md]
converges-on: [TL]
tags: [prior-art, bukzor]
---

Convention in the `prototype.chatfs` repo
(`.claude/verified-claim.kb/CLAUDE.md`): a claim backed by a re-runnable
verification (`sha256sum`, `diff`, `find`, shown with enough output to
re-run) is filed in `verified-claim.kb/`; an unverified observation
goes in the sibling `observation.kb/`. This is TL's "checked
certificate" status — the chat's CD (certificate discipline) — lived in
practice before either was named.

Gap: this is exactly the anti-pattern
`../../../claims.kb/obligation-is-derived-not-stored.md` corrects.
Certification is encoded as *which directory the file lives in* — a
structural, stored decision — not a status field on one claim node.
Promoting a claim means moving the file, not transitioning a status;
there is no revision path back if a verification goes stale (no RN),
and no dependency edges to propagate that staleness to downstream
claims (no RP). Two directories is the status lattice's `{described,
certified}` pair, flattened into filesystem location.

Verify: `prototype.chatfs/.claude/verified-claim.kb/CLAUDE.md`.
