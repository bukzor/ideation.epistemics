--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-discourse-graph)
    - ./mission.md
depends:
    - Skill(llm-claim-ledger)
    - Skill(llm-subtask)
git-caution: personal
---

# ideation.epistemics

Single-purpose realm: claim-ledger epistemics — the {TL, RN} basis and
its rungs: conversational (`Skill(llm-claim-ledger)`), repo weight (the
`.kb/` graphs), and mechanized (ACS, FP2). `mission.md` states what the
realm is *for* and how to rank work — read it before proposing or
executing any; the rungs are not equally valuable. Discourse graph at
root; `./background.kb/` holds primers and the prior-art convergence map;
`prompts/` holds transport artifacts addressed to fresh executors
(`prompts.md` for DAG and deltas); `ladder.md` is the
rung-correspondence synthesis; `repo-weight-derivation.md` proposes the
repo-weight schema from the axioms and `preservation-audit.md` holds it
against the incumbent, improves/preserves/obviates;
`inquiry-scoped-layout.md` is its companion, proposing where nodes
*live* rather than what they contain — inquiry scopes, type in the
filename, placement at LUCA, visibility by symlink — with its own
audit; `acs-counterfactual.md` asks what the fleet would be had ACS
shipped first — the ports frame (chat/kb/agda), per-skill standings,
ACS stress findings, evidence in `acs-counterfactual.kb/`. The
captured
chat and its mining aids (snapshot, transcript map, codename glossary,
O-ledger) live under `./sources.kb/knot-theory-chat.kb/`.

## Current Work

Check `.claude/todo.md` and `.claude/todo.kb/` for active efforts. Load
`Skill("llm-subtask")` for maintenance.

## session-model/

The framework ledger for the session-model family (`Skill(llm-claims-kb)`),
the mechanized rung's first concrete client; its priors live in
bukzor-agent-skills' design and strata ledgers. Code lands beside the ledger.

## kb-dynamics/

An executable model of a claim ledger under change -- moves, rules, and a
debt function the moves must not raise -- tested by generated sequences
rather than a modeled agent. Its ledger is `kb-dynamics/docs/dev/claims.md`;
the subpath stays independent of its siblings, and the outer vocabulary it
uses enters only through the `imported-terms` theory there.
