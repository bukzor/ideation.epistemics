---
last-updated: "2026-07-26"
---

# Inquiry-scoped layout

A proposal, not a decision. Where `./repo-weight-derivation.md` asked what
a claim node should *contain*, this asks where nodes should *live*. The two
are independent and this one is not derived from {TL, RN} — said plainly in
"What the axioms do not imply" below, because the axioms are silent on
layout and a proposal that pretended otherwise would be smuggling.

## The proposal, in three parts

1. **Scopes are inquiries, not types.** `$ITEM.md` + `$ITEM.kb/` is
   promoted from exception to rule. Today `Skill(llm-discourse-graph)` says
   "most nodes should NOT have elaboration"; under this proposal
   elaboration *is* the structure, and a scope's directory is named for the
   question it pursues.
2. **Type moves to the filename.** `NAME.claim.md`, `NAME.question.md`,
   `NAME.deduction.md` — with the same suffix on the paired directory
   (`NAME.question.kb/`) so `ls -F` types a scope without opening it.
3. **Placement is at LUCA; visibility is by symlink.** A node's canonical
   home is the least common ancestor scope of everything that cites it.
   Anywhere else it should be *seen*, it is projected with a symlink.

## What drives it

`./mission.md` ranks operator productivity apex and names the bottleneck:
an operator running 10–20 parallel sessions, bottlenecked on trusting what
the fleet believes. Layout bears on that directly, because a scope is the
unit of delegation. Under collections, handing off "the retraction
propagation question" means assembling a file list from four directories —
constructed by hand, stale on the next edit. Under inquiries it is
`Agent(prompt="work in ./retraction-propagation.kb/")`, and the handoff is
a path.

The operator's three stated wants — self-similar, divide-and-conquerable,
`cd`-and-focusable — are one want seen from three sides, and question
decomposition is literally the divide step.

Second driver, and the harder evidence: a certified defect,
`./claims.kb/path-conflates-type-and-topic.md`. Type and topic share one
path component today, so `collection_of()` returns the elaboration scope
instead of the collection for any nested node. That failure is *specific to
elaboration* — a flat graph never triggers it — which means the incumbent
layout degrades precisely as the recursion increases. Part 2 of the
proposal fixes it as a side effect: a filename suffix is symlink-invariant
and nesting-invariant.

## The trade that dissolved

The obvious objection to inquiry-scoping is that cross-cutting nodes have
no home. `./claims.kb/monotonic-dynamic-seam.md` is a premise to the
toy-weight deduction, load-bearing for `./ladder.md`, and relevant to repo
weight; under one-node-one-place it must either sit in a privileged global
directory or be arbitrarily assigned to one inquiry.

That is a fake trade, of the kind
`~/.claude/must-read.kb/when/redesigning-something-that-already-exists.md`
warns about: two independent variables fused into one. **Where a node lives
and where it can be seen are separable.** Symlinks are in-bounds within a
repo, git versions them natively, so:

- **Placement** is canonical, single, and computed (LUCA of citers).
- **Visibility** is plural and chosen (project into any scope that wants it
  in view).

This is the same shape as the insight that settled retraction:
`./claims.kb/retraction-breaks-the-path.md` turned on content survival and
path survival being independent. Here it is canonical path and visible path.
Once separated, the objection cancels — no privileged root directory is
needed, which matters because under a genuinely self-similar structure
"global at root" is not a thing. Root is simply where LUCA lands when
usage is universal.

## Placement is computed, not chosen

`Skill(llm-discourse-graph)` already states the rule — "content lives at
the narrowest scope containing all its uses" — and files it under placement
judgment, "a judgment made once, not a mechanism to lean on." Every edge is
machine-readable, so it need not be a judgment at all:

> A node belongs at or above the LUCA of its citers. Flag any node placed
> inside a strict sub-branch of that LUCA.

Placed *above* LUCA is at most advisory — wider than needed, harmless.
Placed *inside a sub-branch* is the real defect: some citer must go up and
back down through a sibling branch, which is the long upward chain the
skill warns against reaching through, and which the file-relative ADR
makes expensive.

This is the move this realm keeps making — obligation derived not stored,
contested computed not declared, warrant read off field presence — applied
to the filesystem. It is also nearly free: LUCA and the obligation view
consume the identical reverse-dependency edge set, so one traversal yields
both. A node with no citers has no LUCA and floats where authored, which is
the same set the obligation view already ranks at zero.

## Projection, and its discipline

Three rules, each with a reason rather than a preference behind it:

- **Projections carry no epistemic weight.** A symlink means "this scope
  wants this in view," never "this supports that." Support stays in
  deductions. Without this rule the `depends:` leak reopens in a form the
  audit cannot see, since `Path.resolve()` collapses the link. (Projection
  and `depends:` overlap but do not substitute: `depends:` is node → node,
  projection is scope → node.)
- **Same-named only.** Renaming through a symlink breaks both the type
  suffix and grep-ability at once.
- **Files, not directories.** Directory links risk double traversal and
  loops under `rglob`; file links do not.

Retraction interacts better than expected. Renaming a node dangles every
symlink pointing at it — `ls -F` shows it, `ls -L` errors, the link checker
fails. Projection therefore *amplifies* propagation: every scope that cared
enough to project a node gets a visible break. That is
"prefer the mechanism that already exists" paying out twice, since
`./claims.kb/link-checker-is-the-propagator.md` bought propagation at zero
cost and this extends its reach for free.

## Preservation audit

Verdicts against the incumbent layout. Silence is not a verdict, so every
aspect worth keeping gets one.

| Incumbent aspect | Verdict | Argument |
|---|---|---|
| Five collections | **preserves** | They survive as node kinds; they stop being the primary *axis*. A scope still holds questions, claims, deductions — now as suffixes, not directories |
| `ls claims.kb/` enumerates claims | **improves** | Becomes `ls **/*.claim.md`. Works at every scope, including nested ones where the collection form silently misreports today |
| `grep -rL resolved: questions.kb/*.md` | **preserves** | Becomes a glob over `*.question.md`; same query, wider reach |
| Path-derived type (`collection_of`) | **improves** | Fixes the certified defect; suffix is nesting- and symlink-invariant |
| `$ITEM.md` + `$ITEM.kb/` elaboration | **preserves** | Unchanged mechanically, promoted from exception to rule |
| Roll-up: parent node is the summary | **preserves** | Untouched, and load-bearing — an inquiry scope's parent is its answer |
| "Narrowest scope containing all uses" | **improves** | Advice becomes a computed check |
| File-relative paths (ADR-2026-07-03-000) | **preserves, stressed** | Still correct; reorganization now costs rename storms. Noisy but safe — the link checker catches every break |
| Link checker as propagator | **preserves, extended** | Untouched: it resolves frontmatter edges by field name, indifferent to layout. Gains dangling-symlink coverage |
| Warrant by field presence; retraction by rename | **preserves** | Fully orthogonal; `.retracted.md` composes with the type suffix as `NAME.claim.retracted.md` |
| One node, one location | **obviates** | The rabbit-and-cage aspect. Single placement was never a requirement, only an assumption; projections satisfy every need it was serving |
| `depends:` as context edge | **preserves** | Different arity from projection; not substitutable. Worth revisiting separately, not here |

## What the axioms do not imply

Nothing above. {TL, RN} constrains what is representable in a claim store;
it says nothing about directory shape, and a layout proposal is not a
derivation. The justification is entirely `./mission.md`'s ordering plus one
certified defect. Legitimate — ergonomic keeps are legitimate — but it must
be named rather than dressed as entailment.

Specifically not implied, and needing fiat: that inquiries are the right
scoping principle *rather than* some other topic taxonomy. Questions are
chosen because `./claims.kb/two-base-statuses-not-four.md` already holds
that an open claim is effectively a question, so inquiry-scoping merges two
things the realm believes are one. That is an argument, not a proof.

## Cost

**Migration is the largest this realm has proposed.** Every node is renamed
(type suffix) and most move (LUCA placement); under file-relative paths
that rewrites every edge. Mechanical, and the link checker verifies it, but
it is not the two hours `./repo-weight-derivation.md` cost.

**Tooling, itemized and small.** In `warrant_audit.py`: `load_nodes` globs
`*.md` with no deduplication, so a projected file is collected twice —
dedupe by resolved path. And line 150 stores `path.resolve()` while
computing `collection_of(path)` on the *unresolved* path, so a projection
would report the projecting scope while carrying the real path. Both
evaporate once type comes from the suffix.

**Not yet dogfooded, and that is a real gap.** `repo-weight-derivation.md`
earned its verdicts by migrating this realm the same day; this proposal has
not. Until it does, its cost estimate is an estimate. Migrating this realm
is the first thing that should happen if the proposal is accepted, and the
first place it will bite.

## Open for fiat

- **Depth cap.** Initially proposed at 2–3 levels on the theory that deep
  trees force long relative chains. Withdrawn as probably too conservative:
  projections make depth cheaper to live with, since a deep node can be
  surfaced anywhere it is needed. Genuinely undecided, and it wants the
  dogfooding run before a number is picked.
- **Type suffix on directories.** `NAME.question.kb/` is self-labeling in
  `ls -F` but means a re-typed node renames twice. Recommendation: yes,
  legibility wins.
- **Whether `sources.kb/` and `definitions.kb/` in fact rise to root here.**
  Under LUCA this is empirical per node, not a policy. Most sources
  probably do; some — the knot-theory chat's glossary — plainly do not, and
  already live inside an elaboration scope today.
