---
title: "Ongoing Awareness (global CLAUDE.md)"
originators: [bukzor]
sources: [../../../sources.kb/bukzor.md]
converges-on: [RN]
tags: [prior-art, bukzor]
---

Standing instruction in `~/.claude/CLAUDE.md`: track ground truth, user
goals, and "beliefs and assertions (both user and assistant)" against
each other continuously; after corrections, detours, or task
completion, emit a status listing. This is RN's dynamics — the accepted
set is checked for consistency and revised — applied to an entire
conversation as prose discipline, and the status listing is a proto-
flush: a manifest emitted at a context boundary.

Gap: no TL. Beliefs and assertions are tracked as prose, not as
addressable, labeled nodes — nothing here can carry a dependency edge,
so RP has no substrate to walk even if invoked. The status listing is
freeform text, not a queryable ledger; two runs of the same instruction
can't be diffed the way two `claim list` outputs can.

Verify: read the file directly.
