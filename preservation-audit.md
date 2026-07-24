---
last-updated: "2026-07-24"
---

# Preservation audit — what the incumbent gets right

`Skill(llm-discourse-graph)` is prior art and evidence of intent, not
canon (`./claims.kb/incumbent-design-is-evidence-not-canon.md`). This is
the side-by-side it owes: what the shipped design does well, and what
the derivation in `repo-weight-derivation.md` does with each — so that
nothing is lost by inattention. Verdicts are **improves**,
**preserves**, or **obviates**; an entry with no verdict is a
regression.

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
  → **improves.** Kept whole and made load-bearing: it becomes the one
  walkable edge, and the leak that let claims connect around it closes.
- **Function is contextual, not intrinsic.** ADR-000 declined separate
  Warrant/Rebuttal types, quoting Clark et al.: "one publication's
  backing is another's warrant." That is the same move as this realm's
  warrant-mix-at-point-of-use and
  `./claims.kb/obligation-is-derived-not-stored.md`, made three months
  earlier on other grounds.
  → **preserves.** No role annotations added; obligation stays a query.
- **Derived state over stored state.** Questions carry no status field:
  `resolved` means answered, `candidate-resolutions` means under
  investigation, neither means open. State is read off field presence.
  → **improves.** Generalized from questions to claims, which is the
  whole of TL's representation: warrant by field presence, no enum.
  The incumbent's own best move, applied one collection over.
- **Open world.** ADR-005: absence of a claim is not a claim. RN needs
  this — a revisable set cannot treat silence as commitment — and it is
  the standing rebuttal to reading a graph's gaps as findings.
  → **preserves.** Also the reason absence is a legal warrant state
  rather than an error.
- **Machine-checked schemas beside the collections.** Five
  `$COLLECTION.jsonschema.yaml`, enforced by `llm.kb-validate`. This is
  `mechanism-over-exhortation` already honored.
  → **improves.** Same surface, three more checks: no claim→claim
  `depends:`, no live node pointing at a retracted one, no certificate
  standing on a retracted premise.

## Sound and orthogonal — kept, and why

- **File-per-node, addressable by path.** TL needs every claim
  individually labelable and citable; a path is that name. Also what
  makes `ls` and `grep` the query language.
  → **preserves.**
- **`$ITEM.md` + `$ITEM.kb/` elaboration, any node type.** ADR-002:
  convention over configuration, no `scope` field to keep in sync, and
  the parent node *is* the roll-up. Explicitly rejected IBIS's
  questions-only hierarchy as forcing artificial reframing.
  → **preserves.** Untouched by the axioms.
- **`./sources.kb/` as reusable provenance, including `kind: user` and
  `kind: assistant`.** ADR-2026-07-03-001 refused a parallel singular
  `source` field and extended the existing enum instead.
  → **improves.** Becomes load-bearing rather than optional: TL's
  declared-axiom cell is warrant by fiat, and a fiat is unreadable
  without an attributable declarer, so `stipulated:` requires a source.
- **`./definitions.kb/`.** Outside {TL, RN}'s remit — a definition is not
  truth-apt — and valuable anyway.
  → **preserves**, on independent grounds, stated as such: the axioms
  do not imply everything a working graph needs.
- **The design/discourse split.** `Skill(llm-design-kb)` holds
  *held/desired*, this holds *true/false*.
  → **preserves.** The boundary is the reason not to reach into the
  design tower from here.
- **"Claim" as the term** (ADR-003), aligned with Toulmin, Chan,
  micropublications, schema.org.
  → **preserves.** Free interoperability; no reason to spend it.

## Live tension — resolved by the derivation

- **`depends:` leaks around the deduction spine.** Documented as
  context "without implying support or refutation," but nothing stops
  it being written claim → claim as real support, and it is: this
  realm's own graph has 11 claims, 9 such edges, and zero deductions.
  So the design states an invariant (ADR-006: deductions are the sole
  mechanism connecting claims) and simultaneously ships the field that
  breaks it. **This is the defect, and it is internal to the design** —
  no usage statistics needed to see it. The counts only show the hole
  is reachable in practice, by agents who know the design.
  → **improves.** `depends:` survives for context and is forbidden
  claim→claim, enforced by schema. The intent was right; only the
  enforcement was missing.
- **`likelihood: 0–1`, default 1.0.** Neither a status nor a computed
  warrant-mix but a third, stored thing.
  `./claims.kb/two-base-statuses-not-four.md` says warrant is read off
  the premise chain at point of use; a scalar written by hand and never
  recomputed cannot be that.
  → **obviates, pending fiat.** "How sure" is not a warrant; genuine
  probabilistic content belongs in the claim text, where it is itself
  checkable. Flagged in `repo-weight-derivation.md` as the entry most
  likely to draw disagreement.
- **`contested`.** Names a state with no resolution procedure.
  → **obviates.** A contested claim is one with a live contradiction
  deduction aimed at it — computed, not declared, and with the attack
  itself on the record.
- **`status` on deductions.** ADR-006 added it so a disputed inference
  could be marked.
  → **obviates.** The same fact is the undercut the ADR itself
  introduced: a contradiction deduction whose `conclusion` is the
  disputed deduction. Two representations that can disagree, reduced to
  the one that cannot.
- **Path conventions.** ADR-2026-07-03-000 chose file-relative and
  accepted the cost: moves break references. Older graphs still carry
  collection-relative paths, so both resolve in the wild.
  → **preserves** file-relative, per the ADR; the migration converts
  the stragglers, since a walker that guesses is a walker that lies.

## Deferred, carry as-is

- **Similarity groups** (`similars` / `holotype`, ADR-004, status
  `deferred`). Never implemented. {TL, RN} says nothing about claim
  identity across formulations.
  → **no verdict, deliberately.** The axioms give no reason to
  resurrect it and none to bury it; it stays deferred where it is.
