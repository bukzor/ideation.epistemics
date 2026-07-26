---
last-updated: "2026-07-26"
---

# Preservation audit — the arbiter join

Join of `./derivation.md` (clean room) with
`./incumbent-inventory.md`, per `../acs-counterfactual.md`.
Verdicts are **improves / preserves / obviates**; every register aspect
is covered by its family's verdict unless named as an exception, so
silence below means the family verdict, not no verdict.

## Contamination screen (the derivation)

- **No incumbent echoes found in MUST EXIST.** The derivation is
  representation-free exactly where the incumbent is most distinctive:
  no files-per-item, no directories, no naming grammar, no markdown,
  no frontmatter, no trigger banks. Incumbent-like forms appear only
  as neutral alternatives inside choice points (2.1, 2.4), which is
  where they belong.
- **Four entries are payload restatements, not derivations**, and are
  excluded from convergence evidence: 1.3 (MT's verdict-plus-name
  clause), 1.7 (DV's "obligation is a view" clause), 1.11 and 1.12
  (FP2's laws, near verbatim). Method defect, logged: the payload
  shipped two axioms with their corollaries attached, so the deriver
  could only hand them back. A re-run should state axioms bare.
- **One familiarity pull, self-flagged** (agent performance
  measurement) and correctly quarantined in NOT IMPLIED.
- **No replication.** One deriver ran once; the payload makes the
  derivation *reproducible by design*, but nothing has reproduced it.
  Open obligation.

## Testimony verification (the inventory)

Five register claims sampled, five confirmed by direct inspection:
the `requires:`/`depends:` `setup:` split (llm-kb and
llm-discourse-graph prescribe `requires:`; llm-collab, llm-subtask,
llm-design-kb prescribe `depends:`); claude-realignment at exactly 28
lines; the 0-byte ADR; `must-read.d` surviving in
`claude-realignment/SKILL.md` and `llm-kb/SKILL.kb/CLAUDE.md`;
`failure-modes.kb/` and `principles.kb/` referenced but absent.
The register is accepted at decision grade; exhaustive verification is
a non-goal (`../mission.md`).

## Join I — the fifteen derived mechanisms, against the incumbent

| Derived (clean room) | Incumbent realization | Reading |
|---|---|---|
| 1.1 warranted entry | Full at chat weight (`llm-claim-ledger` statuses); partial at repo weight (discourse-graph status enum); **none for the fleet's own teachings** | strong convergence at chat weight; the instruction layer is the gap |
| 1.2 checks as files | `jsonschema-beside-collection`, `llm.kb-validate(-links)`, `bin/` | strong convergence — design-next's mission states the disproved bet ("prose emphasis can enforce behavior"): MT, learned empirically |
| 1.3 verdict + checker name | absent at repo weight; no `certified:` anywhere | gap; `../repo-weight-derivation.md` already proposes it |
| 1.4 two strata, two disciplines | de facto (`bin/`+schemas churn by ADR; `.kb/` churns freely), never stated | partial; make the discipline explicit |
| 1.5 dependency edges | `premises`/`conclusion` (polarized); `why:` chains in design towers | strong convergence, two independent forms |
| 1.6 invalidation as query | absent — nothing walks the edges | gap; rename-breaks-path + link checker closes it |
| 1.7 obligation view | *(restatement — screened out)* `todo.md` is a stored queue | live tension; verdict in family E |
| 1.8 total order on revisions | `dated-record-naming` + newest-wins / last-wins, ADR-logged | strong convergence, with the stipulation properly logged |
| 1.9 recorded promotion | chat weight `claim accept`; repo weight absent | partial |
| 1.10 attack intake | contradiction deductions exist; `contested` has no procedure | partial; the liveness half is missing |
| 1.11 stipulation records | ADR practice, fleet-wide | strong convergence; implementation frayed (two formats, one lifecycle-maintained) |
| 1.12 base stipulation | nearest: design-next `010-mission.md`'s logged bets; the required-reading stanza is exhortation, not record | partial |
| 1.13 core/plugin, porting-scored | design-next `core-and-classes` (`classes-detach-cleanly`, `coupling-is-adapter-only`) | strong convergence on the partition; the *metric* (porting survival as the warrant for "core is general") is absent |
| 1.14 sessions boot from the ledger | **absent.** SKILL.md prose is an instruction store beside, not inside, any ledger — no warrants, no edges, no retraction discipline | the central gap; finding 1 |
| 1.15 degeneracy audit | `self-audit-battery` ≈ the intake half, in prose; liveness half absent | partial; audits are exhortation-side |

## Join II — verdicts on the incumbent's aspects, by family

**A. The `.kb/` substrate** (collection-anatomy, item-plus-elaboration,
naming grammar, dated records, skeletons, CLI grammar,
category-as-query-filter, recognizing-the-shape) — **preserves**, as
logged stipulations. Granularity, edge representation and layout are
underdetermined (choice points 2.1/2.3); these are the incumbent's
answers, mostly ADR-logged already — which *is* FP2's stipulation law
honored. Exception: **ls-is-the-index / claudemd-is-a-maintenance-guide
/ no-enumeration → improves** — it gains a warrant: an enumeration is
derived state that goes stale, `ls` recomputes it; the incumbent's own
rationale ("`ls` stays current, documentation becomes stale instantly")
was a DV argument before DV had a name.

**B. Enforcement** (schemas, validators, `managed-by` const,
loud-missing-directory, strict CLI grammar) — **improves**: this is the
checker stratum; add certificates (1.3) so verdicts persist with their
checker's name, and state the two-strata discipline (1.4).
**self-audit-battery → improves**: mechanizable audits become named
checks with stored verdicts; judgment audits stay procedures. That
split is MT's seam: enforce the mechanical, surface the judgment.

**C. The instruction layer** (SKILL.md prose, IMPERATIVE stanzas,
required-reading stanza) — **improves; the central verdict.** Under
1.14 teachings become warranted ledger entries with dependency edges
and retraction discipline. Evidence this is needed rather than nice:
every drift instance the inventory catalogued lives in this layer,
and the sample verified 5/5. Exception: **shared-core-block → preserves as a
named exception** — the claude.ai preference pane cannot reference
files, so the copy-paste merge is a platform constraint; log it as a
stipulation (or obviate by generating both copies from one source).

**D. The attention layer** (must-read banks: filename-is-the-trigger,
junctures, ANY-prefix, symlink-aliasing, body cap; llm-triggers: floor,
condition vocabulary) — **preserves, named as the fleet's answer to
choice point 2.4** (relevance selection), where the axioms are silent.
The fleet's most distinctive invention is ergonomics — load-bearing
ergonomics, kept on its merits, not derivable. Two principle-level
convergences inside it anyway: **interpretation-not-compilation** is DV
independently derived ("a compiled artifact re-introduces … the exact
staleness class"), and **the-floor-is-the-semantics** is MT's seam
restated (meaning above, mechanism strengthens below).

**E. The task layer** (four tiers, checkboxes, todo.md/todo.kb,
ideas.kb, sweh frontmatter) — **preserves for operator-fiat tasks**,
which are not derivable from any ledger and are legitimately stored.
**Improves at the boundary**: entries that mirror ledger debt
(discharge lines, flush targets, uncommitted-`[x]`) should be the
obligation *view*, not a hand-maintained mirror. The fiat-task /
derivable-obligation line is one the derivation draws (1.7, DV) and the
incumbent does not.

**F. The records layer** (ADRs, devlogs, audience separation, tiered
detail, temporal ordering) — **ADRs → improves**: they are 1.11's
stipulation records; unify the two formats and make lifecycle
maintenance total, so supersession is recorded on the record it
supersedes. **Devlogs → preserves on independent grounds**: session
narrative is NOT IMPLIED (§3) — consistent with design-next's own
residue-test verdict that llm-collab dissolves while its decisions
survive as settled questions. Temporal ordering → preserves (= 1.8).

**G. The epistemics layer** (llm-discourse-graph, llm-claim-ledger) —
already audited at one-schema scale (`../preservation-audit.md`); those
verdicts stand, and this join independently re-confirms the two big
ones: status enum → warrant-by-field-presence (1.1), and
nothing-walks-the-edges → invalidation-as-query (1.6). The good-smells
ledger (seven of its own nine criteria self-marked open) —
**preserves**, exemplary TL practice.

**H. Standalone** (llm-vitals, claude-realignment, llm-chat-librarian)
— **preserves**; mostly beyond the axioms' reach. Named:
**automation-boundary → preserves** (it is TL's attributable-source
requirement at the data layer — confabulated data is a false warrant);
**claude-realignment → preserves** (the fleet's living scale-down
proof: 28 lines, verified); **chat-librarian's `commands/` → obviates
or repair**: a dispatch mechanism the platform demonstrably never
fires is dead weight wearing a mechanism costume — bind it or retract
it.

## Join III — the design-next convergence (strongest single result)

The deriver never saw `design-next.kb/`. The mapping between its
goal/requirement vocabulary and the axiom set:

| design-next (incumbent's own v2) | axiom / derived mechanism |
|---|---|
| mechanism-over-exhortation | MT |
| single-source-improvement, spec-cited-never-restated | DV |
| self-application | SI |
| filesystem-as-database | SI + the no-daemon constraint |
| degrade-gracefully | scale-down (§4) |
| classes-detach-cleanly, coupling-is-adapter-only | 1.13 core/plugin |
| validators-outlive-migrations | MT's monotonic stratum |
| dated-records-are-primitive | 1.8 total order |

Reading: the incumbent re-derived most of the axiom set *empirically,
from operational pain* ("improvements had to be re-landed per skill";
"disproved one bet: that prose emphasis can enforce behavior"), while
the clean room re-derived design-next's goals *from the axioms*. Two
derivations from independent directions meeting in the middle is the
consistency result this exam was commissioned to produce.

What the derivation adds that design-next lacks: warrants on teachings
(1.1/1.14), certificates (1.3), porting-survival as the warrant for
"core is general" (1.13), attack intake and the liveness view
(1.10/1.15b), recorded promotion (1.9). What design-next has that the
axioms do not reach: the class taxonomy itself, the engine verb set,
memory-policy — choice-point and NOT-IMPLIED territory, and design-next
already carries them as `status: proposal` with open `[!QUESTION]`s,
which is the correct FP2 handling.
