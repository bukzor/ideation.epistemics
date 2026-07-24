--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-discourse-graph)
    - ./mission.md
depends:
    - Skill(llm-claim-ledger)
    - Skill(llm-subtask)
---

# ideation.epistemics

Single-purpose realm: claim-ledger epistemics — the {TL, RN} basis and
its rungs: conversational (`Skill(llm-claim-ledger)`), repo weight (the
`.kb/` graphs), and mechanized (ACS, FP2). `mission.md` states what the
realm is *for* and how to rank work — read it before proposing or
executing any; the rungs are not equally valuable. Discourse graph at
root; `background.kb/` holds primers and the prior-art convergence map;
`prompts/` holds transport artifacts addressed to fresh executors
(`prompts.md` for DAG and deltas); `ladder.md` is the
rung-correspondence synthesis; `preservation-audit.md` holds the
incumbent repo-weight design to improves/preserves/obviates. The captured
chat and its mining aids (snapshot, transcript map, codename glossary,
O-ledger) live under `sources.kb/knot-theory-chat.kb/`.

## Current Work

Check `.claude/todo.md` and `.claude/todo.kb/` for active efforts. Load
`Skill("llm-subtask")` for maintenance.
