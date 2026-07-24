---
sources: [../sources.kb/bukzor.md, ../sources.kb/claude.md]
depends: [../background.kb/prior-art.kb/lakatos-proofs-and-refutations.md]
date-observed: 2026-07-24
tags: [repo-weight, notation, retraction]
---

At repo weight a node is retracted by **renaming** it: `NAME.md`
becomes `NAME.retracted.md`. No status field, no deletion.

**The framing that made this hard.** The choice looked like tombstone
vs. delete, i.e. *does the content survive?* That is the wrong
variable. What the tooling tests is the **path**, and path survival is
independent of content survival. Once separated, the trade disappears:
keep the body, break the path, and the two objections cancel. Deletion
buys free propagation and loses the refutation; a tombstone left at its
old path keeps the refutation and needs a walker nobody has written.
Renaming gets both.

**What it satisfies.** RN wants three things of a retraction. *Exit the
accepted set* — the suffix is the status, visible in `ls`, which is how
this system is browsed. *Propagate* — every dependent breaks the link
check, per `./link-checker-is-the-propagator.md`, at zero
implementation cost. *Retain the refutation* — the body survives, so a
successful attack stays knowledge and the dead branch is not
re-derived. This is the part deletion throws away, and it is the part
Lakatos is about: refuted conjectures are not discarded, they are
refined under attack, and the refutation that forced the refinement is
the content
(`../background.kb/prior-art.kb/lakatos-proofs-and-refutations.md`). The stem survives too, so `grep` still finds the stone and its
citers together — `NM`'s actual benefit, intact. `NM` protects a label
through polarity reversal, which retraction is not.

**The property worth having.** An unpropagated retraction becomes
unrepresentable without error. The rotted edge found in
`template.python-project`
(`../2026-07-24-000-warrant-audit.prototype/`) survived because
retraction there was a frontmatter flag that nothing checked. Under
renaming that state fails validation the moment it is created.

**Cost, and the release valve.** Retraction is a breaking change across
every citer, not a one-file edit; it cannot be landed half-done. Under
RN that is correct rather than unfortunate — an unpropagated retraction
*is* the defect — but it changes what retracting feels like. The valve:
a citer not ready to be fixed may repoint at `NAME.retracted.md`. That
reference is honest — "this rested on something withdrawn" — it
validates, and it is machine-visible, so the warrant audit's *no live
node points at a tombstone* check is what keeps the deferral from
becoming permanent. Two checks compose: the link checker catches the
moment of retraction, the audit catches what is deferred after it.

Chat weight has no paths, so it tombstones in place
(`./retraction-is-revision-to-tombstone.md`); repo weight has paths and
a checker, so it tombstones by rename. Same axiom, different medium.
