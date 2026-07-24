---
kind: entailment
conclusion: ../claims.kb/retraction-breaks-the-path.md
premises:
  - ../claims.kb/retraction-is-revision-to-tombstone.md
  - ../claims.kb/link-checker-is-the-propagator.md
sources: [../sources.kb/claude.md]
tags: [repo-weight, retraction, mechanism]
---

The two premises pull in opposite directions only if content and path
are assumed to share a fate.

`retraction-is-revision-to-tombstone.md` requires the **body** to
survive: retraction is revision under last-wins, and what it revises to
is a tombstone that says why. Deleting the file discharges no part of
that. `link-checker-is-the-propagator.md` requires the **path** to die:
a reference is checked by resolution, so the only event that surfaces
dependents for free is a path that stops resolving.

A rename satisfies both, and it is the only operation that does. Field
presence cannot — a `retracted:` flag leaves the path resolving, so
propagation falls back to a walker that does not exist. Deletion cannot
— it takes the body with the path. So the conclusion is forced, not
chosen: retraction at repo weight is `NAME.md` → `NAME.retracted.md`.

Not entailed: the spelling. `.retracted.md` is picked for legibility
(`DS`) and because the stem sorts and greps with its citers; any
suffix that changes the path would satisfy the argument. Also not
entailed: that the `./`-prefix convention should stay a convention
rather than becoming a check — that is a claim about `llm-kb`, filed
in `../.claude/todo.kb/suggestions-to-audit.kb/`.
