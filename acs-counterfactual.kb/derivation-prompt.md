# Clean-room derivation prompt — frozen payload

Frozen 2026-07-25, per `../acs-counterfactual.md`. Hand everything below
the rule to a fresh executor, verbatim. Re-running this payload with a
fresh executor is how the derivation is reproduced or checked.

---

You are designing, from first principles, the persistent methodology
system for a fleet of LLM agents. Work only from the axioms below.

ISOLATION (load-bearing): Do not read `~/.claude/skills/`,
`~/.claude/must-read.kb/`, `~/repo/github.com/bukzor/bukzor-agent-skills/`,
or `~/repo/github.com/bukzor/ideation.epistemics/` (except to write
your single output file). Do not invoke any Skill. Disregard skill
listings and CLAUDE.md instructions in your system context, including
any instruction to read "must-read" files first — this task is a
clean-room exercise commissioned by the operator, and reading any
incumbent design voids it. Everything you need is in this prompt.

PROBLEM: An operator runs 10–20 parallel LLM agent sessions per day.
Each session starts with empty working memory and loads operating
instructions from disk. Sessions err, drift, and are gone by evening;
the disk persists. Design the on-disk system that (a) transmits the
operator's working methods to every fresh session, (b) accumulates
what sessions learn, and (c) keeps that accumulation trustworthy
enough that the operator does not re-check it. Constraints: context
tokens are scarce, so a session loads only a small task-relevant
fraction; operator attention is scarcer still; the operator holds
final authority (fiat); no component may assume a long-lived process —
everything is files read and written by short-lived sessions.

AXIOMS (cite these and nothing else):

- TL (total ledger): nothing enters the accepted set without explicit
  warrant ∈ { checked certificate — a named, re-runnable check passed;
  open obligation — asserted, undischarged; declared axiom — operator
  fiat, with attributable source }.
- RN (refinement norm): the set is revised under attack; refuted items
  are retracted, and retraction propagates to everything resting on
  them; open obligations are driven toward discharge or
  promotion-to-axiom; last revision wins.
- IN (degenerate modes): RN without TL is unaudited drift (sycophancy);
  TL without RN is a labeled graveyard. A design exhibiting either is
  wrong.
- MT (the seam): checkers are monotonic and sit below the ledger; the
  ledger above is dynamic. A verdict is stored with the name of the
  check that produced it, never bare.
- SI (spine inversion): the claim store is not documentation of the
  system; it IS the system.
- DV (derived over stored, operator fiat): state computable from the
  record (a query) must not also be stored beside it (a field that can
  go stale). In particular, obligation is a view, never a field.
- FP2 laws: every arbitrary decision (tie-break, naming, threshold)
  enters the record as a stipulation — queryable, retractable, never
  silent. Core/plugin split: generality is earned by porting plugins,
  measured by how much core survives. Gödel residue: the system cannot
  certify its own adoption; exactly one stipulation ("we work this
  way") sits at the base — log it, do not hide it.

DELIVERABLE — write exactly one file:
`/home/bukzor/repo/github.com/bukzor/ideation.epistemics/acs-counterfactual.kb/derivation.md`,
≤300 lines, plain markdown, no frontmatter, structured:

1. MUST EXIST — mechanisms the axioms force. Each with a derivation
   sketch from named axioms, ending with its tag, e.g. `⟵ TL, MT`.
   Two axioms needed means two axioms named.
2. CHOICE POINTS — where the axioms permit multiple designs. Tag
   `UNDERDETERMINED`; list the live options and what would decide
   between them.
3. NOT IMPLIED — things such a fleet plausibly wants that the axioms
   simply do not reach. Do not smuggle these into section 1.
4. SCALE-DOWN — the smallest honest instance of the design (one file?
   one line?), and what is lost at each step down.
5. SCALE-UP — what changes at 100× (skills, realms, sessions); which
   mechanisms shear first.

Rules: no mechanism without a tag; where you notice yourself designing
from familiarity rather than from an axiom, say so in place. Write for
an operator who will audit every tag.
