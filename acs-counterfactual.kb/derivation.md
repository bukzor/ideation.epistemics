# Fleet methodology system — clean-room derivation

Derived from the axiom set {TL, RN, IN, MT, SI, DV, FP2} and the stated
problem constraints (files only, short-lived sessions, scarce tokens,
scarcer operator attention, operator fiat). Where a mechanism leans on
a problem constraint rather than an axiom, the constraint is named in
the tag; constraints alone never justify a section-1 entry.

## 1. MUST EXIST

**1.1 Warranted entry record.** Every accepted item on disk carries its
statement plus exactly one warrant: `cert(check-name)`, `obligation`,
or `axiom(source)`. An entry without a warrant is not in the accepted
set — it is at best raw input awaiting intake. Axiom warrants must name
the operator (or the fiat event), because "attributable source" is part
of the warrant's definition. `⟵ TL`

**1.2 Named, re-runnable checks as files.** A "checked certificate"
requires a named check that can be re-run. No long-lived process exists,
so a check must be a file (script, query, test) that any fresh session
can execute. A check that lives only in a session's memory dies by
evening and voids every certificate it issued. `⟵ TL, MT` (+ no-daemon
constraint forces the file form)

**1.3 Verdicts stored with their checker's name.** A stored result is a
pair (verdict, check-name), never a bare "verified". This is what lets
the operator trust without re-checking: the audit trail is "which named
monotonic check said so," and the check can be re-run on demand.
`⟵ MT, TL`

**1.4 Two-layer layout: checker stratum below, ledger above.** Checkers
are monotonic — same input, same verdict, forever — so they live in a
region the ledger's revision process does not rewrite. The ledger is
dynamic and revises freely above them. Mixing the strata (a check whose
meaning drifts with ledger revisions) destroys the seam: certificates
would silently change meaning. Concretely: two disk regions with
different mutation disciplines. `⟵ MT`

**1.5 Dependency edges.** Retraction must propagate "to everything
resting on" a refuted item, which is impossible unless resting-on is
recorded. Every entry that rests on others names them. `⟵ RN`

**1.6 Retraction as a record; invalidation as a query.** A retraction
enters the record (it is itself a revision, and last revision wins).
The set of downstream entries it invalidates is computable from 1.5's
edges, so per DV it must NOT be stored as a status flag on each victim —
flags go stale exactly when a second retraction lands. The invalidated
set is a view over (retractions × edges). `⟵ RN, DV`

**1.7 Obligation view.** "What is asserted but undischarged" is
computable from warrants (1.1), so DV forbids a maintained TODO list
beside the ledger. The obligation queue is a query. RN then acts on this
view: each open obligation is driven toward a certificate (a check gets
written and passed) or toward promotion. `⟵ DV, TL, RN`

**1.8 Total order on revisions.** "Last revision wins" is meaningless
without an order. With 10–20 concurrent sessions writing, the system
needs an ordering primitive — timestamps, commit sequence, monotone
counter — and the choice of primitive is itself a stipulation (see 1.11).
`⟵ RN` (+ parallel-sessions constraint makes it non-trivial)

**1.9 Promotion-to-axiom transition.** RN names two exits for an
obligation: discharge or promotion-to-axiom. Promotion is a fiat event,
so it must be recorded with attributable source like any axiom (1.1).
The system therefore needs a recorded state transition, not just an
edit-in-place that erases the item's history as an obligation. `⟵ RN, TL`

**1.10 Attack intake.** "Revised under attack" presupposes attacks can
be filed. Any session (or the operator) must be able to record a
challenge against an entry; a challenge that lives nowhere on disk is
gone by evening and RN never fires. Without this channel the design
degenerates to the labeled graveyard: warranted entries that nothing
ever revises. `⟵ RN, IN`

**1.11 Stipulation records.** Every arbitrary decision — the file
naming scheme, the ordering primitive of 1.8, any threshold — enters
the record as a stipulation: queryable, retractable, never silent.
Consequence: the system's own layout conventions appear inside the
ledger, retractable like anything else. `⟵ FP2`

**1.12 The base stipulation.** Exactly one stipulation — "we work this
way" — sits at the root, logged, warrant `axiom(operator)`. The system
cannot certify its own adoption; hiding this fact (e.g., a README that
implies the methodology is self-justifying) is the failure FP2 names.
`⟵ FP2, TL`

**1.13 Core/plugin partition.** Methodology claims split into a core
and per-domain plugins. Generality claims about the core are not
asserted; they are earned by porting plugins and measured by how much
core survives each port. So the partition must be visible on disk
(otherwise survival is unmeasurable), and "core is general" is itself
an entry whose warrant is the porting record. `⟵ FP2, TL`

**1.14 Sessions boot from the ledger itself.** SI: the claim store is
not documentation of the system, it IS the system. Therefore there is
no separate "operating instructions" document that the ledger merely
describes — the instructions a fresh session loads ARE accepted entries
(methods held under warrant). A drifting instructions-file beside the
ledger would be exactly the stored-copy-of-derivable-state DV forbids,
applied to the system's own description. `⟵ SI, DV`

**1.15 Degeneracy audit.** IN declares two failure modes, so the design
must be checkable against both: (a) an intake check — no entry without
warrant (mechanizable: a named check over the ledger, per MT); (b) a
liveness check — attacks and retractions actually occur; obligations
age toward discharge rather than accumulating. (a) is a certificate;
(b) is a view over the revision history (DV). A fleet whose ledger only
ever grows has failed IN even if every entry is warranted. `⟵ IN, MT, DV`

## 2. CHOICE POINTS

**2.1 Entry granularity.** One file per entry / one ledger file per
realm / a single database file. TL, RN, DV are satisfied by any of
them. Deciders: merge behavior under parallel writes (1.8), and token
cost of loading a task-relevant slice. `UNDERDETERMINED`

**2.2 Ordering primitive.** Wall-clock timestamps, VCS commit order,
or explicit sequence numbers. RN requires an order but not which one.
Decider: whether clock skew across sessions is plausible; whether the
disk is already under version control. Whichever is chosen must be
logged as a stipulation (1.11). `UNDERDETERMINED`

**2.3 Edge representation.** Dependencies (1.5) inline in the depending
entry, as separate edge records, or parsed from citations in prose.
Deciders: cost of the invalidation query (1.6) and whether checks can
parse the format reliably (1.2). `UNDERDETERMINED`

**2.4 Relevance selection.** How a session finds its "small
task-relevant fraction": directory taxonomy, an index, full-text
search, or embedding retrieval. The axioms are silent; only the
token-scarcity constraint speaks. Note DV pressure: an index is derived
state, so if materialized it must be regenerable and marked as such.
Decider: measured retrieval precision vs. maintenance cost.
`UNDERDETERMINED`

**2.5 Check re-run policy.** Monotonicity (MT) fixes a check's verdict
for fixed inputs, but when an input changes the old certificate is
about a stale input. Re-run on write, on read, on session start, or
lazily when a view asks? Decider: check runtime vs. staleness tolerance
the operator will stipulate. `UNDERDETERMINED`

**2.6 Who may retract what.** RN says refuted items are retracted, but
not by whom. Axioms plausibly retract only by fiat (their warrant is
fiat), but whether an agent session may retract a certificate-backed
entry on the strength of a new failing check, without operator review,
is open. Decider: operator's trust budget; the answer becomes a
stipulation. `UNDERDETERMINED`

**2.7 Attack representation.** Are attacks (1.10) first-class entries
with their own warrants, or annotations on their targets? First-class
is cleaner under TL (an attack is itself a claim) but doubles record
count. `UNDERDETERMINED`

**2.8 Initial core/plugin cut.** FP2 says how the cut is *scored*
(porting survival), not where to draw it first. Decider: run the
measurement — port a second domain early and let survival redraw the
line. `UNDERDETERMINED`

## 3. NOT IMPLIED

- **Prioritization.** Which obligation to discharge first, which attack
  to answer first. RN gives direction, not order.
- **Confidence scores.** TL's warrant is trichotomous; nothing licenses
  probabilities or graded belief. Adding them would need a new axiom.
- **Session transcripts / logs.** The axioms govern the accepted set,
  not raw session history. Keeping transcripts may be useful; nothing
  forces it.
- **Orchestration.** How the 10–20 sessions are launched, scheduled, or
  assigned tasks. The axioms start at the disk.
- **Access control / sandboxing.** No axiom distinguishes agents from
  one another or restricts who reads what (2.6 touches writes only via
  stipulation).
- **Compression / summarization** of loaded context. Token scarcity
  motivates it; no axiom governs it, and a summary is a derived
  artifact that DV would only *constrain* (mark it regenerable), not
  demand.
- **Deduplication and merge** of near-identical claims from parallel
  sessions. Last-revision-wins resolves conflicts on the *same* item;
  nothing detects that two items are the same.
- **Agent performance measurement.** Which sessions err most, which
  methods pay off. Plausibly valuable; the axioms audit claims, not
  claimants. (Noting familiarity-pull here: fleet-ops instinct wants
  this badly; the axioms simply do not reach it.)

## 4. SCALE-DOWN

Smallest honest instance: **one file, one line** — the base stipulation
(1.12), `axiom(operator)`, "we work this way." TL holds vacuously
(every entry warranted), RN holds vacuously (nothing attacked yet), the
Gödel residue is logged rather than hidden. It is a real, degenerate-
but-not-IN-degenerate instance: empty is not a graveyard, because a
graveyard is *unrevisable content*, and there is no content.

Steps down from the full design, and what each loses:

- Drop the checker stratum (1.2/1.4): every certificate demotes to an
  open obligation. Still honest under TL — provided the demotion is
  recorded — but the operator must now re-check everything, failing
  problem-goal (c) while keeping the axioms.
- Drop dependency edges (1.5): retraction cannot propagate. This is not
  a smaller instance; it is an RN violation. Dishonest.
- Drop the attack channel (1.10): the labeled graveyard. IN violation.
- Drop warrants (1.1): unaudited drift. IN violation.
- Drop stipulation logging but keep the base one (1.11 minus): silent
  arbitrary decisions accumulate; FP2 violation in the small even if
  the root is logged.

So the honest scale-down path is narrow: full design → design with all
certificates demoted to obligations → one-line base stipulation.
Everything else on the way down breaks an axiom rather than shrinking
the instance.

## 5. SCALE-UP

At 100× (order 10^3 sessions/day, dozens of realms, thousands of
entries):

- **Last-revision-wins shears first.** With heavy parallel writes, "the
  last revision" becomes contested (2.2's primitive strains: clock skew,
  interleaved commits) and, worse, semantically wrong — two sessions
  revising the same entry for different reasons want a merge, not a
  winner. RN's tie-break must be supplemented by a stipulated ownership
  or partition rule (FP2: that rule enters the record).
- **DV comes under pressure second.** Views (obligations 1.7,
  invalidation 1.6, liveness 1.15b) get expensive over a large record;
  the temptation is materialized caches. DV's letter forbids storing
  the computable *beside* the record; the survivable reading is:
  caches allowed only if marked derived, stamped with generating query
  and input revision (an MT-style pair), and never read when stale.
  Get this wrong and stale obligation lists quietly become the system —
  the drift mode of IN by the back door.
- **Operator fiat becomes the bottleneck.** Promotions (1.9) and
  retraction approvals (2.6) queue against fixed attention. The axioms
  offer one relief valve: fiat can be delegated only by a logged
  stipulation ("sessions may retract cert-backed entries on failing
  re-check"), keeping TL's attribution chain intact.
- **Core/plugin split turns load-bearing.** At dozens of realms the
  porting metric (1.13) stops being a philosophy and becomes the
  primary signal for what belongs in the shared core; realms that fork
  the core reveal it was never general. This mechanism *strengthens*
  at scale — it is the only one that does.
- **Relevance selection (2.4) must be decided.** Grep-scale discovery
  fails; whatever index is adopted becomes critical derived
  infrastructure, inheriting the cache discipline above.
- **The checker stratum scales cleanly.** Monotonic, append-only,
  embarrassingly parallel. MT is the axiom built for scale; the
  dynamic ledger above it is where all the shear concentrates.
