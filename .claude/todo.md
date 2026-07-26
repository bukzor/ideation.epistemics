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
