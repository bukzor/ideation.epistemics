---
last-updated: "2026-07-26"
---

# The ACS counterfactual

**What if ACS had existed, ready to use, before
`bukzor-agent-skills`?** (operator, 2026-07-26). Running that question
against the real fleet serves six purposes (operator): stress-test the
ACS design; examine `bukzor-agent-skills` in depth; examine
extending/replacing llm.kb, the fleet's current primitive; validate
ACS against a (mostly) working system; force a concrete look at how an
ACS workspace would be organized; inform ACS's currently
under-specified filesystem organization. Deliverables are schematics,
not ready-to-use systems (operator). Unmarked statements here are
open, per `./claims.kb/warrant-by-field-presence.md`.

## The frame

ACS is defined representation-independently; a realization is a
**port** of one core (operator, 2026-07-26):

| port | realization | status |
|---|---|---|
| ACS.chat | `Skill(llm-claim-ledger)` | runs today |
| ACS.kb | claims as files over `llm-kb` — this effort | being designed |
| ACS.agda | `./prompts/acs.md` | research rung |

What survives every port is the kernel, and porting survival is the
kernel's validation metric. The rungs of `./ladder.md` are this port
set (`./claims.kb/acs-rungs-are-ports-of-one-core.md`).

In `design-next.kb` class vocabulary, ACS.kb is a **class** over
`llm-kb`'s substrate (`./claims.kb/acs-kb-is-a-class-over-llm-kb.md`).
llm.kb answers librarianship — naming, discovery, loading,
maintenance — and carries no epistemics in the primitive; ACS is the
missing half — warrant, dependency, revision, query
(`./claims.kb/acs-and-llm-kb-are-complementary-halves.md`). So ACS.kb
competes with the semantic classes, never with
`llm-kb` itself, though it pushes new demands into the engine: a
revision index, edge walking, view/query verbs, a two-strata mutation
discipline. (Taxonomy note: design-next's "spec" level is
formats-only; the ACS core is a *semantics* spec — a level the class
system didn't previously name.)

FP2 is not a lens here — its search engine has no fleet analog
(operator; concurred) — and what generalizes from it (stipulations for
arbitrary decisions, the porting metric, the Gödel residue) is already
part of the working basis.

## Where each incumbent skill stands

- **`llm-discourse-graph`** — the predecessor: ACS.kb is roughly what
  it becomes after absorbing {TL, RN}, and
  `./repo-weight-derivation.md` already moved it most of the way. The
  todo's "land {TL, RN} in the fleet" item *is* this migration.
- **`llm-design-kb`** — reached by ACS with one real seam: decisions
  are stipulations and `why:` chains are dependency edges, but
  normative content restricts the palette (a goal cannot be refuted,
  only re-fiated; `certified()` applies only as conformance). Either
  ACS.kb carries two palettes or design-kb stays a sibling class on
  the shared core. Open.
- **`llm-claim-ledger`** — the sibling port, not a competitor; its
  shared-core-block becomes transport between ports.
- **`llm-collab`** — ADRs are stipulation records, absorbed (agreeing
  with design-next's dissolution verdict); devlogs are session
  narrative, outside ACS's reach.
- **`llm-subtask`** — splits: fiat tasks stay client-side; derivable
  obligation views move into ACS.kb.
- **`llm-vitals`** — a client: entries are data claims with
  attributable source; its cadence/debt machinery is orthogonal.
- **Attention layer** (`llm-must-read-kb` / `llm-triggers`) — kept
  ergonomics, orthogonal to the axioms; trigger bodies become claim
  files so a retracted rule cannot keep firing.

## Evidence — `./acs-counterfactual.kb/`

Gathered under a two-agent clean-room protocol: a deriver saw only a
frozen axiom payload (`derivation-prompt.md`) and never the incumbent;
an inventorist saw only the incumbent; the join screened the
derivation for incumbent echoes and found none. Protocol details and
verdicts: `./acs-counterfactual.kb/preservation-audit.md`. Live
caveats on this evidence: one deriver, no replication yet; the frozen
payload stated two axioms with corollaries attached (state them bare
in any re-run); the inventory is verified by sample (5/5 checked).

- `derivation.md` — fifteen mechanisms the axioms force, eight choice
  points they leave open, eight things they do not reach, and the
  scale-down/scale-up analyses. The mechanisms are the candidate
  abstract core.
- `incumbent-inventory.md` — 113-aspect register of the fleet, with
  stated intent cited per aspect.
- `preservation-audit.md` — the join: per-aspect verdicts
  (improves/preserves/obviates), per-mechanism presence, and the
  convergence table against `design-next.kb`.
- `greenfield-design.md` — an earlier schematic drawn from the reduced
  axiom basis; its concrete forms (claim-file, prose as
  staleness-checked view, two strata, the verbs, the kept-on-merit
  list) are working material for the ACS.kb class package.
- `abstract-core.md` — plan part 1, done: the thirteen-point
  representation-independent core (the mechanisms joined with the full
  spec), the port parameter vector, and the mechanism↔spec join table.
- `acs-kb-class-package.md` — plan part 2, done: ACS.kb's assignment
  of the parameter vector, the read-off status realization, node
  kinds and schema deltas, the class-package shape, the four checks,
  and the engine verbs demanded of llm-kb.

## What the evidence established

- **The fleet's documented drift is predicted, not incidental.**
  Teachings live as prose outside any ledger — no warrant, no
  dependents, nothing fails when they change — and every drift
  instance the inventory catalogued lives in exactly that layer. The
  incumbent recorded the same lesson empirically: "disproved one bet:
  that prose emphasis can enforce behavior."
- **`design-next.kb` is the axiom set, re-derived from operational
  pain.** The clean room reproduced its goal vocabulary without
  seeing it (mechanism-over-exhortation ≡ MT,
  single-source-improvement ≡ DV, self-application ≡ SI,
  classes-detach-cleanly ≡ core/plugin). Two derivations from
  independent directions agree; what ACS adds on top: warrants on
  teachings, certificates with named checkers, core membership by
  measurement, attack intake, liveness.
- **The attention layer is underdetermined** — the axioms are silent
  on relevance selection. It is load-bearing ergonomics, kept on
  merit and logged as such, not derived.
- **Scale-down passes; scale-up shear is already visible at 1×**
  (claude-realignment's 28-line skill is a real degenerate instance;
  "improvements had to be re-landed per skill" is the predicted
  parallel-write/DV shear arriving early).

## ACS stress and validation, so far

1. **`described` is load-bearing and under-specified.** Most fleet
   mass is non-propositional (procedures, schemas, templates, trigger
   bodies, definitions) and can only enter as `described` — yet ACS
   records dependencies only for non-described claims, so a
   procedure's resting-on goes unrecorded and drift re-enters through
   the described door. Kernel-change candidate: edges on described
   items, or procedures as claim bundles.
2. **Multi-store scoping is unspecified.** ACS is "a claim store,"
   singular and versioned; a fleet is dozens of scopes with placement
   judgments. Prior art: `./inquiry-scoped-layout.md`.
3. **Loading economics are absent.** `trust-base-of` is a graph
   query; a token-scarce session cannot load the graph. llm.kb's
   synthesis files and the attention banks become ACS.kb's
   view/retrieval layer — a realization concern the kernel never
   names.
4. **Retraction's downgrade target is unstated.** The spec says the
   cone is "invalidated (downgraded)" but not to what — `certified →
   obligated` reopens the obligation, `→ described` abandons it. The
   abstract core makes the target a recorded per-port transition rule
   (`./acs-counterfactual.kb/abstract-core.md` §6).
5. **Validation: the kernel's parameterization points hold.** Payload
   embedding and `certified(checker)` admit prose payloads and
   shell-script checkers without bending the kernel; ACS.chat already
   runs as a degenerate port with a one-to-one status map.
   Domain-freedom survives first contact.

## Plan — three parts, one artifact each

1. **Abstract core** — done:
   `./acs-counterfactual.kb/abstract-core.md`. The fifteen mechanisms
   joined with the full spec (`./prompts/acs.md`) into thirteen core
   points; two spec gaps surfaced (attack intake and the degeneracy
   audit are forced by the basis but absent from the spec text), plus
   stress finding 4; the eight choice points became the port
   parameter vector part 2 must assign.
2. **The ACS.kb class package** — done:
   `./acs-counterfactual.kb/acs-kb-class-package.md`. The parameter
   assignment (git as revision order, frontmatter paths as edges,
   tombstone renames as retraction), the status lattice realized by
   field presence + collection kind + path state rather than an enum,
   the four checks, and six new engine verbs; nine stipulations
   awaiting ratification.
3. **Port-comparison ledger** — chat / kb / agda: what each port
   strengthens, weakens, or cannot express; stress findings 1–4
   adjudicated as kernel change vs realization choice vs client-side
   workaround.
