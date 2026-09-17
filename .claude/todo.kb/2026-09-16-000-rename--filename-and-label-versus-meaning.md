---
managed-by: Skill(llm-subtask)
status: done
cost-benefit-sweh:
  timebox:
    "@value": 2
    rationale: "mechanical once the convention question is ruled: git mv, sweep the why arrows and prose, re-run graph and mentions"
    confidence: unsure
  benefit-2w:
    "@value": 1
    rationale: "every mis-named claim costs a re-read at each citation; a dozen of them, cited by agents several times a session"
    confidence: tentative
---

# Rename: filename and label versus meaning in the kb-dynamics ledger

**Priority:** medium, before the next batch of claims lands
**Complexity:** low per rename; one ruling gates the batch
**Context:** `kb-dynamics/docs/dev/claims.kb/`, reviewed 2026-09-16
(session dfc18e9d) after the conflict, reduction, and objective rulings;
re-evaluated and executed the same day in a second sitting.

## Problem Statement

Revision had pulled several labels, filenames, and titles apart from
what the claims say. Three causes:

1. **The filename stated the conclusion, so it churned.** One commit
   (e22adaf) renamed three files for a count or ordinal that had
   changed, and `four-debt-reductions...` still carried a count.
2. **A ruling withdrew the framing the label named.** `TRUST_TEST`'s
   body said "none is trust"; `OWNER_VIEW` was about hidden debt.
3. **The prefix rule blocked a family.** `CONFLICT` forbade
   `CONFLICT_*` and forced `RESOLUTION` onto a claim half about not
   resolving.

## Rulings (owner, dfc18e9d and the executing sitting)

- [x] **Layout: `<slug>/LABEL.md` beside `<slug>/LABEL.kb/`.** The slug
      is llm-kb's self-describing kebab name for the locus, the stem the
      label exactly. A plain directory inside a collection is a prefix on
      its members' names, S3 style; in a ledger a slug holds one label.
      Merits: a `why:` line reads as a citation, definitions are found by
      path, the stem-equals-label check replaces frontmatter parsing, and
      the `grep '^label:'` scan goes away.
- [x] **Theories get a proper slug**, the ontology's locus, never the
      label lowercased: `what-no-move-may-raise/DEBT.md`.
- [x] **The ledger root does not change.** `claims.md` beside
      `claims.kb/` is llm-kb's type marker saying a ledger starts here;
      the rule governs what is inside. Removing the root's `label:` would
      fail the root schema stub, so it stays.
- [x] **Labels are distinct as whole words**, nothing more. The
      no-prefix rule (bukzor-agent-skills 13d53a9, 2026-07-28) came from
      two-letter initialisms; `grep -w` and `\<LABEL` do the work.
      Withdrawn in the claim schema and the flatten check.
- [x] **Think french:** related tokens share a head, modifiers trail.
- [x] **Sense over verbatim** when naming: a name preserves the claim's
      sense under surrounding change; matching the owner's wording is
      lower priority.
- [x] **trash/ stays.** The validator asks git; the ledger reader now
      does too.

## Done

Tooling (bukzor-agent-skills): validator and ledger reader walk plain
directories, schema by enclosing collection, scope from path, stem
equals label; flatten reports duplicates only; schema and skill text
updated. Tests added in both packages.

Ledger: every file moved to `<slug>/LABEL.md`; `why:`, `verify:`, prose
path cites, and label mentions re-pointed; label set and edge set
verified identical to HEAD by label. Labels renamed:

| was | is |
|---|---|
| `TRUST_TEST` | `REVIEW_DONE` |
| `OWNER_VIEW` | `DEBT_HIDDEN` |
| `WANTED_DEBT` | `DEBT_WANTED` |
| `REPAIR_WITNESS` | `REACHABILITY_WITNESS` |
| `PRICING` | `RULE_PRICING` |
| `RESOLUTION` | `CONFLICT_REDUCTIONS` |
| `CYCLIC_CONFLICT` | `CONFLICT_ARITY` |
| `RESTING_STATES` | `CONFLICT_RESTING_STATES` |
| `LEAF_REPAYS` | `LEAF_OUTGROWN` |
| `LEAF_EXEMPT` | `LEAF_PRIORITY` |
| `UNASKED_MOVES` | `AGENT_REDUCTIONS` |
| `SERVICE_RATE` | `GLOBAL_CONDITION` |
| `RECORD_FIELDS` | `RULE_RECORD` |
| `ROT_LIST` | `COMPONENTS_CLOSURE` |
| `VETO_QUEUE` | `QUEUE_VETO` |
| `EMPTY_QUEUE_TRUST` | `QUEUE_EMPTY_TRUST` |

Slugs renamed for the ruled rows only; the rest keep their former stem
as slug. Titles amended: the reachability witness lost "Property
five's"; `AGENT_REDUCTIONS` says "under agent authority" for "need no
ask". `GROUND_RECORD` kept its label, file `the-ground-record/`.

## Left open, by design

- [ ] **Slugs that still state a conclusion** (`a-leaf-is-...`,
      `no-agent-move-raises-debt-silently`, most of the ledger). Each is
      a naming judgment; batch them when the claims are next touched.
- [x] **`EXCHANGE_RATE` body:** criterion first, dollars and the rate
      second, the agent's inference (a rate change re-ranks without
      re-measuring) as a `[!DRAFT]` callout. Done 2026-09-16.
- [x] **`GROUND_RECORD` versus the build:** no finding. The sandbox
      carrying sufficiency per claim and no arrow kind is a
      `FIDELITY_LADDER` rung, replaced when a property demands it;
      `todo:` marks decided-not-built, which this is not.
- [ ] **Fleet:** the validator now reaches `must-read.kb/before/*.md`
      and `when/*.md`; 23 carry `triggers:` frontmatter their bank has
      no schema for (`~/.claude/must-read.kb`, `reference.kb/git`).

## Notes

Not in scope: the `IMPORTED_*` family, whose names are the words they
import; the struck claims (`PAYOUT_TEST`, `TREND_UNIT`,
`TRUST_CORNERS`), which keep their names.

## Acceptance criteria from the 2026-09-17 review (agent-authored, session 9b6f24ad, vetoable)

Each box certifies one concern from the review of `589ffac..6572225`
plus this file. Strike a box to reject the concern; the review stands
addressed when every box is ticked or struck.

Layout and naming, passes 1 to 3:

- [ ] Passes 1 to 3 land as one commit, and the sweep's scope includes
      `python/` and `examples/` as `8d25f9c`'s did: no label or path
      cite in a docstring, test, example, or the examples README points
      at a name that no longer exists
- [ ] The naming rulings that bind future sessions (names are
      questions-sans-answer; the spec/imperative exemption, ruled either
      way; the plural-claims rule; a question's `.kb/` is not a theory)
      are filed in the llm-claims design ledger upstream beside
      `NAME_LOCUS`, in the owner's voice where they are the owner's, and
      this file points at them rather than carrying them
- [ ] The upstream amendment "a question's `.kb/` is not a theory" lands
      before pass 4 files its first `QUESTION.kb/`, so the flatten tool
      does not report every one
- [ ] `HARNESS` keeps its name or is renamed on the owner's word, not
      the agent's form of it; the rule's own "a noun with no obvious
      question is an implicit what" covers keeping it

The veto queue. The owner's reading, 2026-09-17, which the first two
boxes rest on:

> [!@bukzor] 9b6f24ad
> In my imagination, the queue indeed holds ever agent-authority move, but those with excellent warrant have near-zero weight, won't be reviewed until after most everything else.

> [!@bukzor] 9b6f24ad
> And debt is a superset of agent-authority moves: all such moves "should" be reviewed if we require maximal certainty, which is "debt", but there are other categories contributing to debt as well.

- [ ] QUEUE_VETO's commitment is either computed or marked. Computed:
      an unvetoed agent-authority move is a debt component in its own
      right, per the second callout; debt and `queue()` take the state
      and the log, and a corner or trace pins the verdict. Marked:
      QUEUE_VETO carries `todo: true` and `DEBT_HIDDEN` names the gap,
      until then
- [ ] A veto item's weight is a constant until a property demands more,
      and the claim that says so names the field quantity it stands in
      for, warrant, per the first callout and `FIDELITY_LADDER`
- [ ] The two callouts above are filed in the ledger as the owner's
      claim, not left here: a sixth rot kind under `ROT_KINDS` or an
      amendment to QUEUE_VETO, on the owner's word
- [ ] AGENT_REDUCTIONS and PRUNE_GUARD cite QUEUE_VETO in `why:`, as
      QUEUE_VETO says its instances do

Conflict:

- [ ] CONFLICT's "Declined: a conflict record beside the ledger" is
      reconciled with its own "may be cached": either the decline goes,
      or it is marked as the agent's reading and says what it declines
      that a cache is not
- [ ] The conflict relation enters the state before the loader runs
      `queue()` over real ledgers, or the loader's report says the
      conflict component is a stub
