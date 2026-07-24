# Retraction is a rename, not a field

**Applied.** `retracted:` removed from `claims.jsonschema.yaml` and
`deductions.jsonschema.yaml`. A retracted node becomes
`NAME.retracted.md`, body intact.

**Why, and note this reverses me.** I had written the tombstone-stays-
at-its-path design and defended it as "so dependents can be found."
You objected that dependents are *easier* to find when the path
breaks, because the link checker lists them. You were right, and the
probe confirms it: renaming one claim surfaced all five referrers, by
field name. The frame was the bug — tombstone-vs-delete asks whether
the *content* survives, but the tooling tests the *path*, and those are
independent. Keep the body, break the path, and both objections
cancel.

**What to check.** That retraction still feels affordable. It is now a
breaking change across every citer, not a one-file edit. The intended
release valve is repointing a citer at `NAME.retracted.md` — legal,
honest, machine-visible — with the warrant audit's "no live node points
at a tombstone" check preventing permanent deferral. If in practice
you find yourself avoiding retraction because it is too loud, that is
the signal this was wrong.

**Reverse by.** Restoring the `retracted:` property to both schemas and
renaming stones back. Nothing else depends on the choice.

Argued in `../../../claims.kb/retraction-breaks-the-path.md`, derived in
`../../../deductions.kb/path-breakage-propagates-retraction.md`.
