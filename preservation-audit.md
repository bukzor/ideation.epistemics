---
last-updated: "2026-07-24"
---

# Preservation audit — what the incumbent gets right

`Skill(llm-discourse-graph)` is prior art and evidence of intent, not
canon (`claims.kb/incumbent-design-is-evidence-not-canon.md`). This is
the left column of the side-by-side it owes: what the shipped design
does well, so that the derivation from {TL, RN}
(`questions.kb/how-should-repo-weight-absorb-tl-rn.md`) can be held to
**improves / preserves / obviates** on each line rather than losing
things by inattention. Verdicts land here as the derivation produces
them; an entry that ends up with no verdict is a regression.

Read from `SKILL.md`, `jsonschema/*.yaml`, and `docs/dev/adr/` — the
ADRs are the intent evidence, and several record reasoning stronger
than the schema that came out of it.

## Convergent — the incumbent already holds a {TL, RN} principle

These are the strongest entries. Each was reached independently, from
argumentation-theory prior art rather than from the axioms, and lands
in the same place. A derivation that breaks one of these is more likely
wrong than they are.

- **Deductions mediate every inter-claim relation.** ADR-000 folded
  Evidence into claims; ADR-006 then made deductions carry polarity
  (`kind: entailment | contradiction`) and let `conclusion` target
  another deduction, so support, opposition and undercut are one
  mechanism. This is an explicit refusal of `supports`/`opposes` fields
  on claims. **This is RP's substrate**: `premises` → `conclusion` is a
  typed, directed, polarized support edge — exactly what a retraction
  walker needs — and it is already schema-enforced. The gap is that
  nothing walks it, not that it is missing.
- **Function is contextual, not intrinsic.** ADR-000 declined separate
  Warrant/Rebuttal types, quoting Clark et al.: "one publication's
  backing is another's warrant." That is the same move as this realm's
  warrant-mix-at-point-of-use and
  `claims.kb/obligation-is-derived-not-stored.md`, made three
  months earlier on other grounds.
- **Derived state over stored state.** Questions carry no status field:
  `resolved` means answered, `candidate-resolutions` means under
  investigation, neither means open. State is read off field presence.
  Same principle, already shipped.
- **Open world.** ADR-005: absence of a claim is not a claim. RN needs
  this — a revisable set cannot treat silence as commitment — and it is
  the standing rebuttal to reading a graph's gaps as findings.
- **Machine-checked schemas beside the collections.** Five
  `$COLLECTION.jsonschema.yaml`, enforced by `llm.kb-validate`. This is
  `mechanism-over-exhortation` already honored, and it is the obvious
  home for the retraction check that is missing.

## Sound and orthogonal — keep unless the derivation forces otherwise

- **File-per-node, addressable by path.** TL needs every claim
  individually labelable and citable; a path is that name. Also what
  makes `ls` and `grep` the query language.
- **`$ITEM.md` + `$ITEM.kb/` elaboration, any node type.** ADR-002:
  convention over configuration, no `scope` field to keep in sync, and
  the parent node *is* the roll-up. Explicitly rejected IBIS's
  questions-only hierarchy as forcing artificial reframing.
- **`sources.kb/` as reusable provenance, including `kind: user` and
  `kind: assistant`.** ADR-2026-07-03-001 refused a parallel singular
  `source` field and extended the existing enum instead. {TL, RN} makes
  this *more* load-bearing, not less: `stipulated` is warrant by
  operator fiat, which is unreadable without an attributable asserter.
- **`definitions.kb/`.** Outside {TL, RN}'s remit — a definition is not
  truth-apt — and valuable anyway. A scope observation, not a defect:
  the axioms do not imply everything a working graph needs.
- **The design/discourse split.** `Skill(llm-design-kb)` holds
  *held/desired*, this holds *true/false*. Matches the realm's own
  scope discipline; the boundary is the reason not to reach into the
  design tower.
- **"Claim" as the term** (ADR-003), aligned with Toulmin, Chan,
  micropublications, schema.org. Free interoperability; no reason to
  spend it.

## Live tension — the derivation must argue these, not assume them

- **`depends:` leaks around the deduction spine.** Documented as
  context "without implying support or refutation," but nothing stops
  it being written claim → claim as real support, and it is: this
  realm's own graph has 11 claims, 9 such edges, and zero deductions.
  So the design states an invariant (ADR-006: deductions are the sole
  mechanism connecting claims) and simultaneously ships the field that
  breaks it. A walker following only the typed spine will miss real
  support; one following `depends:` too will propagate through mere
  context. **This is the defect, and it is internal to the design** —
  no usage statistics needed to see it. The counts only show the hole
  is reachable in practice, by agents who know the design.
- **`likelihood: 0–1`, default 1.0.** Neither a status nor a computed
  warrant-mix but a third, stored thing.
  `claims.kb/two-base-statuses-not-four.md` says warrant is read
  off the premise chain at point of use; a scalar that is written by
  hand and never recomputed cannot be that. Improve, or obviate — but
  argue it.
- **`contested`.** Names a state with no resolution procedure. Drop it
  or give it one.
- **`status` on deductions.** ADR-006 added it so a disputed inference
  could be marked. Under {TL, RN} the same fact is already expressible
  as a contradiction deduction pointing at it (the undercut the ADR
  itself introduced), so the stored status may be redundant with the
  graph. Redundancy that can disagree with itself is a defect; decide
  which representation is primary.
- **Path conventions.** ADR-2026-07-03-000 chose file-relative and
  accepted the cost: moves break references. Older graphs still carry
  collection-relative paths, so both resolve in the wild. Settle it.

## Deferred, carry as-is

- **Similarity groups** (`similars` / `holotype`, ADR-004, status
  `deferred`). Never implemented. {TL, RN} says nothing about claim
  identity across formulations, so the axioms give no reason to
  resurrect it and none to bury it.
