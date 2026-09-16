---
managed-by: Skill(llm-subtask)
status: not-started
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
(session dfc18e9d) after the conflict, reduction, and objective rulings.
Agent-authored suggestions, every one vetoable.

## Problem Statement

Revision has pulled several labels, filenames, and titles apart from
what the claims now say. Three causes, each with its own remedy:

1. **The filename states the conclusion, so it churns.** The label rule
   (`claim.jsonschema.yaml`) says a label names the locus of contention
   so it survives revision. No rule says what a filename names, and
   this ledger has used the title, which is the current conclusion.
   Result: `three-things-void-repayment.md` became
   `what-voids-repayment.md` when the count changed, and
   `attention-and-tokens-are-priced-in-dollars.md` bakes the chosen
   answer into the path.
2. **A ruling withdrew the framing the label names.** `TRUST_TEST`'s
   body says "none is trust"; `OWNER_VIEW` is about hidden debt.
3. **The prefix rule blocks a family.** No label may prefix another, so
   the bare component label `CONFLICT` forbids `CONFLICT_*` and forced
   `RESOLUTION` onto a claim that is half about not resolving.

## Proposed Solution

Rule first, then the batch under it.

- [ ] **Rule (owner, dfc18e9d; layout the agent's recommendation among
      the owner's three offers, vetoable): `slug/LABEL.md` beside
      `slug/LABEL.kb/`, plain directories transparent.** The label is
      llm-claims' short greppable token, exact, the file's stem; the
      slug is llm-kb's self-describing kebab name, a plain directory
      llm-kb treats as part of the item's name. Both name the locus of
      contention (the open question, the acceptance criteria), never
      the current choice. Acceptance criterion for the convention:
      no rename when new facts or decisions arrive, short of a
      paradigm shift.
      - No special cases. A theory is a claim with multi-atom
        elaboration: `debt/DEBT.md` beside `debt/DEBT.kb/`, its slug
        the ontology's locus, not a sentence. Imports are cited by
        path (vim `gf`) and imported-terms files follow the rule;
        `imported-terms.verify.py`'s `word()` reads the slug segment.
      - Transparency (owner, dfc18e9d): a plain directory is a prefix
        on the names of all its contents, S3 style. No one-item rule;
        `slug/A.md` and `slug/B.md` are two items named `slug/A` and
        `slug/B`. `jsonschema/` holds no items; `trash/` would name
        items `trash/...`, so it moves to the repo root as the
        scratch convention already wants.
      - Validator: `LABEL.md`'s stem equals `label:`, an exact match.
      - Tooling: llm-kb's validators and link checker descend plain
        directories and join the segment into the name; `ledger.py`'s
        claim id follows. No by-label glob resolution: the slug names
        the locus, so full paths stay stable.
      - To rule: the ledger root. `claims.md` + `claims.kb/` is found
        today by its reserved name; under the rule it is
        `<slug>/KB_DYNAMICS.md` + `KB_DYNAMICS.kb/`, recognized by
        shape (a defining claim beside its collection), the tools
        taking the path as they already do.
      - Declined: `{LABEL}--{slug}.md` (parses a string that was
        opaque; slug twice per theory in a recursive listing);
        `slug.kb/LABEL.md` (one collection per claim, so one schema
        stub per claim under llm-kb's sibling-schema lookup, and a bare
        `X.kb/` already means an open theory in the claims-kb skill);
        `LABEL/slug.md` (hides the slug from `ls`).

- [x] **Docs:** checked. `llm-claims/SKILL.md` already says a theory "is
      no second kind of thing: it is a claim", and `llm-claims-kb/SKILL.md`
      says "a claim like any other". The special-casing of theories was
      the agent's, not the docs'; nothing to touch up.

Under that rule, the suggestions. Each row is one `git mv` plus a sweep
of `why:` and prose mentions, then `bin/llm-claims-kb-graph`,
`llm-claims-kb-mentions`, `llm-claims-kb-flatten` (it checks the prefix
rule), and `llm.kb-validate`.

### Strong: name contradicts content

- [ ] `TRUST_TEST` / `any-of-three-conditions-says-review-is-done-or-doable.md`:
      the body withdraws "trust" ("None is trust"). Label
      `REVIEW_DONE`, file `when-review-is-done-or-doable.md`.
- [ ] `OWNER_VIEW` / `hidden-debt-is-the-owners-view-minus-the-record.md`:
      the claim defines hidden debt; the owner's view is the mechanism.
      Label `HIDDEN_DEBT`, file `hidden-debt.md`.
- [ ] `REPAIR_WITNESS` / `the-reachability-witness-is-the-owner-who-rules-yes.md`
      / title "Property five's witness": three nouns for one thing.
      Label `REACHABILITY_WITNESS`, file `the-reachability-witness.md`,
      title without "Property five's".
- [ ] `GROUND_RECORD` / `an-arrow-carries-its-kind-and-sufficiency.md`:
      body says only sufficiency entered, on the claim not the arrow.
      File `the-ground-record.md`; label stays.
- [ ] `PRICING` / `rule-pricing.md`: theory label should match the
      theory name. Label `RULE_PRICING`.

### Conflict family: free the prefix or accept suffixes

- [ ] `RESOLUTION` / `the-reductions-of-a-conflict.md`: the claim
      covers resolve *and* mark. Options: (a) keep `CONFLICT` bare and
      use suffix labels, e.g. `REDUCING_A_CONFLICT`; (b) give the
      component a compound label so `CONFLICT_*` opens up. (a) is
      cheaper; the other components (`DUPLICATE`, `NON_ATOMIC`) are
      bare too.
- [ ] `CYCLIC_CONFLICT` / `a-conflict-can-need-more-than-two-claims.md`:
      names the witness, not the locus, which is how many claims a
      conflict needs. Label `N_ARY_CONFLICT`, file
      `how-many-claims-a-conflict-needs.md`.
- [ ] `LEAF_REPAYS` / `a-leaf-is-not-a-route-to-unrepayability.md`: the
      locus is the contested fourth route. Label `FOURTH_ROUTE`, file
      `the-fourth-route.md`.

### Overfit to the chosen answer

- [ ] `EXCHANGE_RATE` / `attention-and-tokens-are-priced-in-dollars.md`:
      file `the-exchange-rate-between-attention-and-tokens.md`; body
      restructured as acceptance criterion first ("the two currencies
      compare on one scale the owner sets, and changing the scale
      re-ranks rules without re-measuring"), chosen answer second
      (dollars, $150/hour today).
- [ ] `UNASKED_MOVES` / `four-debt-reductions-need-no-ask-and-stay-reviewable.md`:
      "four" is a count, and "unasked" is the wording `VETO_QUEUE`
      asked to retire. Label `AGENT_REDUCTIONS`, file
      `the-reductions-an-agent-may-make-under-its-own-authority.md`.
- [ ] `SERVICE_RATE` / `no-global-condition-only-repayability.md`: label
      names a declined option; under the locus rule that is legal (the
      contention was whether a rate condition exists) but the file is
      the answer. File `the-global-condition-on-debt.md`; label
      `GLOBAL_CONDITION` or keep.
- [ ] `RECORD_FIELDS` / `a-rule-record-separates-check-from-trigger.md`:
      label is generic. Label `RULE_RECORD`, file `the-rule-record.md`.

### Borderline, decide with the rule

- [ ] `LEAF_EXEMPT` / `a-leaf-is-low-priority-never-exempt.md`: label
      reads as asserting exemption; under the locus rule it names the
      contention and the answer is "never". Keep, or `LEAF_PRIORITY`.
- [ ] `ROT_LIST` / `is-the-component-list-exhaustive.md`: "rot" versus
      "component". `COMPONENT_LIST`, or keep as the owner's word.
- [ ] `MINUTIAE` / `most-open-questions-carry-no-obligation.md`: the
      owner's word for the phenomenon; the claim is about leaves and
      obligation. Keep unless the locus rule wants `LEAF_OBLIGATION`.

## Open Questions

- Does the locus rule apply to filenames at all, or only labels? (the
  gating ruling above)
- Should the flatten tool's prefix check be relaxed for a bare label
  and its `LABEL_*` family, or is bare-label-blocks-family the intended
  pressure toward locus-naming?

## Success Criteria

- [ ] Every label and filename names its claim's locus; every title
      states its current conclusion
- [ ] `llm-claims-kb-flatten`, `-mentions`, `llm.kb-validate` clean;
      graph shows no dangling `why:`
- [ ] `EXCHANGE_RATE`'s body opens with its acceptance criterion

## Notes

Not in scope: the `IMPORTED_*` family, whose names are the words they
import; the struck claims (`PAYOUT_TEST`, `TREND_UNIT`,
`TRUST_CORNERS`), which are history and keep their names.
