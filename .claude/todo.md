# TODO

Ranked by `mission.md`: reach the rungs the operator runs on first.

- [ ] **Audit what was decided on your behalf.** Every suggestion applied
      2026-07-24 has an entry in `todo.kb/suggestions-to-audit.kb/`
      saying what changed, why, what to check, and how to reverse it.
      Start here — the rest assumes these stand
- [ ] Operator fiat on two points in `repo-weight-derivation.md`: does
      `likelihood` survive (recommendation: obviate, and applied here
      pending your call), and does `questions.kb/` stay given that the
      axioms merge open claims with questions (recommendation: keep, on
      ergonomic grounds). Both block landing the schema
- [ ] Land {TL, RN} at repo weight in `bukzor-agent-skills/` —
      `repo-weight-derivation.md` is the proposal, `preservation-audit.md`
      the side-by-side, `claims.kb/warrant-by-field-presence.md` the core.
      Highest leverage: reaches every `.kb/` in the fleet
      (`claims.kb/repo-weight-rung-is-unbuilt.md`). Dogfooded here first;
      this realm now has zero claim→claim `depends:` and passes all three
      checks. In the counterfactual frame this is the
      `llm-discourse-graph` → ACS.kb migration
      (`acs-counterfactual.md`)
- [~] `kb-dynamics/`: an executable model of a claim ledger under
      change -- moves, rules, a debt function the moves must not raise --
      tested by generated sequences, not a modeled agent (origin: the
      2026-09-09 chat under `docs/dev/chats/`). Landed: the ledger --
      `imported-terms` (the one place a `why:` may leave the subpath,
      certified by `imported-terms.verify.py`) plus six theories
      (problem, model, debt, harness, rule-pricing, method) that replace
      the chat as the entry point. Grounded 2026-09-11: the spine now rests
      on the owner's word (the reviews are the cause, debt is wanted and
      only unrepayable debt is rot, no claim is exempt from review, a
      nested `components` theory holds the five rot kinds); open:
      `ROUND_TRIP`, `ROT_LIST`. Built 2026-09-11: `examples/` and
      `python/` (debt vector, effective-basis fold, queue, trust
      conditions), properties two and three green on the owner's
      confusions. Ruled 2026-09-11: trust is per claim, a ledger's
      trust an aggregation (now in `TRUST_TEST` and `EFFECTIVE_BASIS`); the harness settled the
      owner's conjecture (`EMPTY_QUEUE_TRUST`: empty queue entails all
      trusted, converse fails, witness pinned). Also
      vetoable, 2026-09-11: `UNREPAYABLE`'s fourth route withdrawn (a
      leaf is repaid by closure, not voided), `PROPERTY_SET` 3 and 4
      re-scoped, `NO_SILENT_RAISE` and `FIELDS_NOT_CARRIED` re-signed
      bare. Built later 2026-09-11: sufficiency on the claim (the
      weak-arrows corner is a bad state); property one as hidden debt,
      the owner's view of the log minus the record (`OWNER_VIEW`), with
      `transition`, `rules`, and the constant-worst agent; property four
      as the flip test. The random agent (hypothesis, `strategies.py`)
      then found three more rules and a debt bug (cycles had no root).
      Ruled: a move is tagged by the authority it carries, not the hands
      (`AUTHORITY_NOT_HANDS`); the rules are now two, owner-only changes
      need owner authority and unlicensed merges preserve content, each
      with a witness. Property five holds with the yes-owner as witness
      (`REPAIR_WITNESS`) and a closing move for leaf questions. All five
      properties run. Next: bounded enumeration, or real ledgers through
      the loader (`ROUND_TRIP` blocks the latter).
      Reconciliation with `session-model/` and the {TL, RN} schema is a
      deliberate later pass, through that theory. Two agent choices to
      audit: `todo.kb/suggestions-to-audit.kb/kb-dynamics-*.md`
      Review sitting 2026-09-16 (dfc18e9d): the grounding table read
      against the ledger; ruled and filed: `VETO_QUEUE`, `RESOLUTION`,
      `RESTING_STATES`, `CONFLICT` (absorbs `STALE`), `CYCLIC_CONFLICT`,
      `OBJECTIVE`, `EXCHANGE_RATE`; "lowering" is "reduction";
      `UNREPAYABLE` restored to four routes with `LEAF_REPAYS` (agent)
      as the contested pick; `authority:` may be an object (schema and
      reader in bukzor-agent-skills); "verbatim" is "faithful" (VOICE);
      three bad states drawn from this ledger, the conflict one
      expected red. Next, in order:
      - [ ] The conflict relation in the state, so the red example
            (`a-ruling-approved-after-the-rulings-it-contradicts`) goes
            green and `CONFLICT` is a computed component
      - [ ] The adapter from `ledger.py` to `State`, so the grounding
            table gains a wording column and runs `queue()` over real
            ledgers (rung 2; `ROUND_TRIP` is the blocker it answers)
      - [ ] Normalize the remaining string `authority:` fields to the
            object form (about thirty files, mechanical)
      - [ ] debt.py weights dependents uniformly; `EFFECTIVE_BASIS` says
            weighted toward stipulated ones. Needs the owner's number
      - [ ] `todo.kb/2026-09-16-000-rename--filename-and-label-versus-meaning.md`:
            one ruling on what a filename names, then a batch of renames
- [ ] `session-model/`: the ownership scan (now runnable here) reports two
      trespasses -- `law.kb` says "silence", owned by `session-sim.kb`;
      `budget.kb` says "trace", owned by `trace-sim.kb`. Cull, move,
      admit, or uniquify each (`llm-claims-kb-ownership --trespass`)
- [~] ACS counterfactual (operator, 2026-07-26): "what if ACS
      existed, ready to use, before the fleet" — stress-test and
      validate ACS against `bukzor-agent-skills`, derive its
      filesystem organization. Deliverables are schematics, not
      ready-to-use systems, graded on rigor and comprehensibility.
      `acs-counterfactual.md`: frame (ports, ACS.kb as class),
      per-skill standings, findings; evidence done in
      `acs-counterfactual.kb/` (clean-room derivation, incumbent
      inventory, preservation audit); all three plan parts done
      (`acs-counterfactual.kb/`: abstract-core, acs-kb-class-package,
      port-comparison). Net output: four-item ACS spec amendment
      list. Awaiting operator: ratify/attack the nine class-package
      stipulations and the spec amendments (then land them in
      `prompts/acs.md`). Method debt: no replication run yet; state
      axioms bare in any re-run payload
- [x] Give RP a mechanism at repo weight — done, and cheaper than
      expected: retraction is a rename, so `llm.kb-validate-links` is
      the propagator (`claims.kb/link-checker-is-the-propagator.md`,
      certified by `2026-07-24-000-warrant-audit.prototype/certify_path_breakage.sh`).
      `warrant_audit.py` keeps the narrower job — deferred debt, live
      nodes pointing at tombstones — and still catches the live
      violation in `template.python-project`
- [ ] Operator call on `inquiry-scoped-layout.md` (proposal, 2026-07-26):
      scopes become inquiries rather than types, node type moves to a
      filename suffix, placement is computed at the LUCA of citers and
      visibility is projected by symlink. Sequence it with the landing
      item above — both change repo weight, and landing the schema
      first means migrating twice. Rests on a certified defect
      (`claims.kb/path-conflates-type-and-topic.md`); the honest gap is
      that it is not yet dogfooded, unlike the schema proposal
- [ ] Fix `llm.kb-validate-links` to resolve bare `claims.kb/x.md` body
      paths, or warn on path-shaped text it declined to resolve. Today
      only `./`-relative body paths are checked, silently; 16 references
      in this realm's own root docs had never been validated
      (`todo.kb/suggestions-to-audit.kb/relative-path-prefix-is-unwritten-law.md`)
- [ ] Adjudicate open `questions.kb/` items as evidence lands, including
      `questions.kb/acs-status-set-mirror-chat-weight.md` (one-line
      operator call; candidate answer recorded in the node and in
      `todo.kb/suggestions-to-audit.kb/acs-status-set-is-stale-both-ways.md`)

## Research rung — pays out later, sharpens meanwhile

- [ ] Execute `prompts/` in fresh contexts (acs → fp2 → sttt-search,
      knot-search), applying deltas per prompts.md

## Later

- [ ] No capture/export path exists for the notation-design session
      itself (`sources.kb/claim-ledger-notation-session.md`) the way
      chatfs captured the knot-theory chat — claims sourced to it rest
      on synthesis, not a re-checkable transcript. Revisit if a
      Claude-Code session capture pipeline ever exists.

- [ ] Decompose the captured chat's remaining ledger into claims.kb —
      indexed now by `sources.kb/knot-theory-chat.kb/glossary.kb/` and
      `.../obligations.kb/`; candidates: HC, VH, DP, CC, CD, CP
- [ ] Verify prior-art characterizations against actual literature
      (per-entry verification routes in background.kb/prior-art.kb/;
      discharges the chat's O4 item-by-item). Decision-grade only, and
      only where it would change our ontology — novelty is a non-goal
      (`mission.md`)
