---
sources: [../sources.kb/claim-ledger-notation-session.md, ../sources.kb/bukzor.md]
depends:
  - ../definitions.kb/refinement-norm.md
  - ../background.kb/prior-art.kb/agm-belief-revision.md
date-observed: 2026-07-24
tags: [notation, ladder]
---

Retraction is not a distinct primitive — it's revision under RN's own
last-wins rule, restating a label with a tombstone body ("RR:
withdrawn — see chat") instead of new content. This makes revision the
single mechanism and gives labels a property worth naming: labels name
the locus of contention, not the current conclusion, so a claim can
reverse polarity under revision and keep its name — every existing
reference to it stays valid. A label that encodes its answer (e.g. an
earlier draft's "NC: obligations Name their Check") dies at first
revision; a label naming the question ("RR: route requirement")
survives any answer.

This is AGM's contraction seen from the practitioner's side
(`../background.kb/prior-art.kb/agm-belief-revision.md`): the accepted
set changes, and what it changes *to* is the thing that must be
written. Stated at chat weight, where there are no paths. Repo weight
realizes it as a rename — `./retraction-breaks-the-path.md` — because
there the medium has paths and a checker that resolves them.
