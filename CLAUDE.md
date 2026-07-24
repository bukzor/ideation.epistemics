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
rungs (ACS, FP2). Discourse graph at root; `prompts/` holds transport
artifacts addressed to fresh executors (`prompts.md` for DAG and
deltas); `ladder.md` is the rung-correspondence synthesis.

## Current Work

Check `.claude/todo.md` and `.claude/todo.kb/` for active efforts. Load
`Skill("llm-subtask")` for maintenance.
