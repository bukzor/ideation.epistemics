--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-discourse-graph)
depends:
    - Skill(llm-claim-ledger)
    - Skill(llm-subtask)
---

# ideation.epistemics

Single-purpose realm: claim-ledger epistemics — the {TL, RN} basis, its
conversational rung (`Skill(llm-claim-ledger)`), and its mechanized
rungs (ACS, FP2). Discourse graph at root; `background.kb/` holds
primers and the prior-art convergence map; `prompts/` holds transport
artifacts addressed to fresh executors (`prompts.md` for DAG and
deltas); `ladder.md` is the rung-correspondence synthesis. The captured
chat and its mining aids (snapshot, transcript map, codename glossary,
O-ledger) live under `sources.kb/knot-theory-chat.kb/`.

## Current Work

Check `.claude/todo.md` and `.claude/todo.kb/` for active efforts. Load
`Skill("llm-subtask")` for maintenance.
