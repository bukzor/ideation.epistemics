# ACS's status set is stale in both directions

**Not applied — needs your call.** Recorded here so it is not lost.

**The question.** `../../../questions.kb/acs-status-set-mirror-chat-weight.md`
asks whether the mechanized rung's status set should mirror chat
weight's.

**The finding.** It currently mirrors neither. Chat weight dropped
`obligated(ROUTE)` on 2026-07-24 per
`../../../claims.kb/obligation-is-derived-not-stored.md`, so ACS is
behind it. And the repo-weight proposal drops stored status entirely in
favour of field presence, so ACS is behind that too — from the other
side. `../../../definitions.kb/acs.md` still describes the old set.

**The call you need to make.** Whether ACS tracks chat weight, tracks
repo weight, or is allowed to differ because a mechanized checker has
constraints the other rungs do not. The third is defensible — ACS lives
below the monotonic/dynamic seam in a way the others do not — but if it
is the answer, `../../../ladder.md` should say why rather than leaving
the divergence looking like drift.

**Blocked on that.** Fixing `definitions.kb/acs.md`, and closing the
question.
