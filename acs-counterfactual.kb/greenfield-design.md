---
last-updated: "2026-07-26"
superseded-by: ../acs-counterfactual.md # concrete forms (§1–§5) feed the ACS.kb class package
---

# The green-field bukzor-agent-skills — a schematic

What a fresh skill fleet looks like when the claim-store principles
are the foundation rather than an aspiration. A schematic, not a build
plan — per the operator (2026-07-26): "I care more about schematics
than ready-to-use systems, for now." It is built from the clean-room
requirements (`./derivation.md`) and keeps what the audit said to keep
(`./preservation-audit.md`). Every choice the principles don't force
is marked **(stipulation)** and stands for ratification.

## 1. The one primitive: the claim file

Everything normative in the fleet — a teaching, a convention, a design
decision, a trigger body — is a **claim file**: a short markdown file
stating one thing, whose standing is read off which fields are
present. A real teaching, migrated:

```markdown
---
stipulated: operator, 2025-11-25    # was prose in llm-subtask/SKILL.md
rests-on:
    - ../../spec/task-inventory.md
---
# Bare list items are invisible

A task written `- pick an oss project` is invisible to the task
inventory; only `- [ ]` / `- [~]` / `- [x]` are scanned. Real work
has surfaced weeks late because of a bare hyphen.
```

- **No warrant fields** — an open claim: asserted, undischarged,
  perfectly legal. Entry stays cheap.
- **`stipulated:`** — operator fiat, with who and when.
- **`certified: <check>`** — a named check under `checks/` passes;
  the verdict never appears without the checker's name.
- **Retraction is a rename** to `NAME.retracted.md`: the reasoning
  survives in the body, the path dies, and everything still citing it
  fails the link check. Propagation for the price of a rename.

This is the scheme this realm already landed for `.kb/` content. The
new part is scope: **the fleet's own teachings live under it.** Today
the checkbox rule above is a paragraph of SKILL.md prose — no
provenance, no dependents, nothing that fails when it changes. Here it
is one file with all three.

## 2. What a "skill" becomes: a class package

```
tasks/                          # the class (today: llm-subtask)
  tasks.md                      # VIEW — the readable synthesis
  teachings.kb/                 # the claims, one rule per file
    bare-items-are-invisible.md
    lightest-tier-first.md
    todo-belongs-to-its-repo.md
  schema.yaml                   # formats this class adds   (monotonic)
  checks/                       # checks this class ships   (monotonic)
    inventory-sees-all-tasks
  triggers/                     # attention bank             (kept)
    before/marking-a-task-done.md -> ../teachings.kb/…
```

**The prose does not go away — it is demoted.** `tasks.md` is what a
session actually loads, exactly like SKILL.md today: short, readable,
opinionated. The difference is one frontmatter stanza:

```yaml
derived-from: teachings.kb/
as-of: <git rev>
```

A view that names its inputs can be **checked for staleness**: a
one-line check flags any synthesis older than a claim beneath it. That
converts the fleet's best-documented failure — prose drifting from
reality — from an archaeology find into a red check the same day,
while keeping the thing the incumbent got most right: an agent orients
by reading two pages, not fifty files.

## 3. Two strata, two mutation disciplines

- **Below, monotonic:** `spec/` (the claim scheme, file formats) and
  every `checks/` directory change only by dated addition plus
  retraction — never edited in place — so a certificate's meaning
  cannot drift underneath it.
- **Above, dynamic:** every `.kb/` revises freely; last revision wins.
- **Revision order is git history** (stipulation). The fleet is
  already a repo: commits are the total order, `git log` the revision
  record, the commit author the attribution. No new machinery.

## 4. The verbs

- **contest** — file a claim with `contests: <path>`. A claim is
  contested iff a live contest points at it: computed, never a status
  field, and the attack itself is on the record.
- **retract** — the rename; dependents surface via the link check.
- **promote** — the operator adds `stipulated:`; the commit records
  the event.
- **obligations** — a query, never a maintained list: every claim
  without warrant, every certificate resting on a retracted path,
  every stale view — ranked by how much cites it. `.claude/todo.md`
  keeps only what no query can derive: goals the operator set by
  fiat. (That split — derivable debt is queried, fiat work is stored —
  is new; today's todo files mix the two.)
- **two standing audits** — *intake*: nothing normative lives outside
  a claim or a marked view (a gate); *liveness*: contests and
  retractions actually occur, open claims age toward discharge or
  promotion (a report). A ledger that only ever grows has failed,
  even if every entry is warranted.

## 5. Kept on merit — said plainly, not smuggled

The principles do not imply any of these. They stay because they
work, each logged as a stipulation:

- file-per-item; `ls` as the only index; `$ITEM.md` + `$ITEM.kb/`
  elaboration; the naming grammar and dated-record scheme.
- **the attention layer, wholesale** — must-read banks, junctures,
  filename-is-the-trigger. The axioms are silent on relevance
  selection; this is the fleet's best invention and it transfers
  unchanged, except that trigger bodies become claim files (so a
  retracted rule can't keep firing: its trigger symlink dangles and
  the link check says so).
- the task tiers and marker commands; the design-tower layers.
- small skills stay small: a 28-line procedure is one claim file with
  elaboration, and that is the whole package.

## 6. Day one, and year three

**Day one is one file.** `fleet.md` — "we work this way",
`stipulated: operator` — the base stipulation the system cannot prove
for itself, logged instead of hidden. Claims accumulate as unmarked
files; no tooling exists yet and nothing needs it. The honest
scale-down path: certificates demote to open claims, never to
silence.

**Year three:** dozens of classes. Core membership is *measured*, not
asserted — a claim moves to `core.kb/` when the citation check shows
two or more classes resting on it, so "the core is general" carries a
porting record as its warrant. Checks run in CI; syntheses regenerate
on merge. The first shear point is known in advance: parallel
sessions revising the same claim (git conflicts are the symptom), and
the partition rule that resolves it will be a logged stipulation, not
folklore.

## 7. A real incident, replayed

The summary→synthesis rename was ratified, and two schema files still
teach the old name; the incumbent's mission names exactly this as the
failure to stop. Under the schematic: the naming convention is one
claim; the rename is a retraction plus a new claim; both citing
schemas fail the link check in the same commit; every synthesis
rolled up before the change goes stale-flagged. Four findings become
four red checks, same day, zero vigilance spent.

## 8. Relation to design-next

Same skeleton — spec, engine, class packages, data — which the clean
room reproduced without ever seeing it. This schematic is design-next
**plus warrants**: teachings as claims, certificates with named
checkers, core membership by measurement, contest and liveness. Its
open `[!QUESTION]`s (engine verb set, teaching consolidation) stay
open here; nothing above depends on how they resolve.

## 9. Stipulations awaiting ratification

1. Git history as the revision order (§3).
2. One file per claim as the granularity (§1).
3. Frontmatter file-relative paths as the dependency edges (§1).
4. Prose synthesis kept as a marked, staleness-checked view (§2).
5. The attention layer kept wholesale (§5).
6. Fiat tasks in todo files; all derivable debt by query only (§4).
