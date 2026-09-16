---
label: JIT_TRIGGERS
standing: agent
why:
  - ../the-rule-record/RULE_RECORD.md
  - ../../../words-from-outside/IMPORTED_TERMS.kb/load-event/IMPORTED_LOAD_EVENT.md
---

# Triggers as code can be evaluated by a hook and the rule injected just in time

Today the agent evaluates triggers: it reads must-read filenames and
judges relevance, which costs tokens for every rule on every turn and is
not reliable. If triggers are code, a hook evaluates them and injects
the matching rule just in time. Out-of-scope rules never enter context,
the rule is enforced rather than advised, and firing counts become exact
rather than "when the agent noticed".

A separate line of work from rule selection, valuable for context cost
and reliability on its own; do it if must-read context is measurably
heavy. The fleet's `Skill(llm-triggers)` is this line, in its design
phase.
