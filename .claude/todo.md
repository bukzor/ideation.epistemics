# TODO

Ranked by `mission.md`: reach the rungs the operator runs on first.

- [ ] Land {TL, RN} at repo weight — decide
      `questions.kb/how-should-repo-weight-absorb-tl-rn.md` (patch vs.
      rewrite; operator is weighing a re-derivation of
      `Skill(llm-discourse-graph)`, maybe `Skill(llm-design-kb)` too),
      then land it in `bukzor-agent-skills/`. Highest leverage: reaches
      every `.kb/` in the fleet
      (`claims.kb/repo-weight-rung-is-unbuilt.md`)
- [ ] Give RP a mechanism at repo weight — something that walks
      `depends:` on retraction (`llm.kb-validate` is the existing
      surface). Prose telling agents to propagate is the failure mode
      v1 already disproved. Folds into a rewrite if that's the call
- [ ] Adjudicate open `questions.kb/` items as evidence lands, including
      `questions.kb/acs-status-set-mirror-chat-weight.md` (one-line
      operator call; candidate answer recorded in the node)

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
