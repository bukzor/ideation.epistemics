---
last-updated: "2026-07-26"
---

# The ACS.kb class package

Part 2 of the plan in `../acs-counterfactual.md`: the
filesystem-organization deliverable. ACS.kb is the core of
`./abstract-core.md` plus one assignment of its port parameter vector,
realized as a class over `llm-kb`. A schematic, not a build; every
assignment below is a stipulation standing for ratification unless
marked otherwise. Concrete forms are drawn from
`./greenfield-design.md` §1–§5 and from what this realm has already
landed (`../claims.kb/warrant-by-field-presence.md`,
`../claims.kb/retraction-breaks-the-path.md`,
`../claims.kb/link-checker-is-the-propagator.md`).

## The parameter assignment

| parameter | ACS.kb assignment |
|---|---|
| payload language | a markdown file body — prose, code, schema, anything a file holds |
| checker set | executable files under `checks/`; the link checker is the built-in propagator |
| entry granularity | one file per claim; `$ITEM.md` + `$ITEM.kb/` elaboration |
| ordering primitive | git history — commit order is revision order, author is attribution, `git log` is the prior-states query |
| edge representation | file-relative paths in frontmatter (`rests-on`, `premises`, `depends`, `contests`) |
| relevance / retrieval | llm.kb librarianship kept whole: naming grammar, `ls` as index, synthesis views, attention banks |
| check re-run policy | lazy + CI-on-merge; safe because views carry `as-of` stamps |
| retraction authority | default: any session contests; only fiat retracts a stipulation; a failing named re-check licenses retracting a certificate — **open, choice point 2.6** |
| attack representation | first-class claim bearing `contests: <path>` |
| downgrade target | retraction reopens: dependents of a retracted node fall to *open*, not to described — the body survives in the tombstone, the obligation returns to the queue |
| core/plugin cut | measured: a claim moves to the shared core when the citation check shows ≥2 classes resting on it |

## The status lattice, realized

Statuses are **read off, not declared** — field presence, collection
kind, and path state; no `status:` enum anywhere.

| ACS status | ACS.kb realization |
|---|---|
| described | membership in a non-assertive collection (`sources.kb/`, `definitions.kb/`, glossaries) or unlabeled prose inside a marked view — held as object because it is a file; no commitment because its kind asserts nothing |
| obligated | a claim file with **no warrant fields** — the cheap default; entry costs one file |
| stipulated | `stipulated: <source>, <date>` |
| certified(checker) | `certified: <check-path>` — the verdict never appears without the checker's name |
| (retracted) | rename to `NAME.retracted.md`; the path dies, every citation breaks, the link check is the propagation |

This confirms `../claims.kb/two-base-statuses-not-four.md` at repo
weight: the four-point lattice survives, but as *derived* standing —
only two of its points are ever written down (`stipulated:`,
`certified:`), the rest are absence and location. Part 3 datum: the
lattice is core; an enum representing it is not.

## Node kinds and schema deltas

Kinds: **claim**, **deduction** (premises → conclusion; the recorded
inference), **question** (kept on ergonomics), **source**,
**definition** (described-tier), **view** (synthesis with
`derived-from:` + `as-of: <git rev>`), **check** (executable,
monotonic stratum), **trigger** (symlink into a claims collection).

Deltas against the shipped `llm-discourse-graph` schemas: `status:`
and `likelihood:` leave claims and deductions (standing is computed;
confidence is unlicensed by TL); warrant fields and `contests:` enter;
views gain the `derived-from`/`as-of` stanza. This is the
`llm-discourse-graph` → ACS.kb migration named in the todo.

## The class package shape

```
$CLASS/                     # e.g. tasks/ (today: llm-subtask)
  $CLASS.md                 # VIEW — what a session loads; derived-from + as-of
  teachings.kb/             # the claims, one rule per file
  schema.yaml               # formats this class adds     (monotonic)
  checks/                   # checks this class ships     (monotonic)
  triggers/                 # attention bank; symlinks into teachings.kb
```

Two strata, two mutation disciplines: `schema.yaml` and `checks/`
change only by dated addition plus retraction — never edited in
place — so certificates cannot drift underneath their checkers;
every `.kb/` above revises freely, last commit wins.

A 28-line skill is one claim file with elaboration and no other
apparatus — the scale-down path stays honest.

## The four checks

1. **intake** — every non-described node parses against its schema and
   carries a legal warrant state; nothing normative lives outside a
   claim or a marked view. A gate.
2. **cone** — no live node cites a `.retracted.md` or dangling path;
   a `certified:` whose check or transitive inputs died is flagged.
   The existing link checker is this check's engine.
3. **staleness** — any view whose `as-of` predates a commit touching
   its `derived-from` inputs is stale; stale views are never loaded as
   current.
4. **liveness** — a report over git history: contests get filed,
   retractions occur, open claims age toward discharge or promotion
   rather than accumulating. A ledger that only grows has failed IN.

## Engine verbs demanded of llm-kb

Kept: `llm.kb-validate` (schema), `llm.kb-validate-links` (the
propagator). New demands the class pushes into the engine:

- `kb-edges <node>` — transitive closure over frontmatter paths, both
  directions (the cone and the support tree).
- `kb-trust-base <node>` — the stipulations and checks in its
  transitive support: ACS's signature query.
- `kb-obligations` — warrantless claims, certificates over retracted
  inputs, stale views; ranked by citation count. A query, never a
  file; `.claude/todo.md` keeps only fiat goals no query can derive.
- `kb-stale <view>` — `as-of` vs `git log` of the inputs.
- `kb-liveness` — the revision-history report.
- a **two-strata guard** — reject in-place edits under `schema.yaml`
  and `checks/`.

These run as scripts, not as context: sessions load views and
attention banks; the graph is walked by tooling. That is ACS.kb's
answer to stress finding 3 (loading economics) — llm.kb's synthesis
layer *is* the kernel's missing view layer.

## Scoping (stress finding 2)

The package is layout-agnostic between flat collections and
inquiry-scopes; `../inquiry-scoped-layout.md` is the candidate
answer — placement at LUCA with symlink visibility gives multi-scope
without multi-store, and one versioned repo keeps revision order
total. Multiple repos = multiple stores remains genuinely open at the
kernel level; within one fleet, one repo suffices.

## Stipulations awaiting ratification

The six of `./greenfield-design.md` §9, plus three new from this
assignment: (7) downgrade target = reopen-to-open; (8) re-run policy =
lazy + CI-on-merge; (9) retraction authority split — contest freely /
fiat for stipulations / failing re-check licenses certificate
retraction.
