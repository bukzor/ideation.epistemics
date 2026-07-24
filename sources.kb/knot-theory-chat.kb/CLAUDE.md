--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# knot-theory-chat.kb — source elaboration scope

Elaboration of `../knot-theory-chat.md` (the captured claude.ai chat).
Contents serve one purpose: make mining the transcript cheap for later
agents.

- `chat.md` — **verbatim snapshot**; authoritative target of every
  `chat.md:NNN` line reference in this repo. Never edit or reformat it:
  line numbers are load-bearing. Its `messages/...` links are dead by
  design (raw capture stays in the chatfs repo; see the parent node).
- `transcript-map.md` — the live-path arc, one row per exchange.
- `glossary.kb/` — decoder ring for the chat's codenames.
- `obligations.kb/` — the chat's numbered O-ledger and where each went.

Distillation *out* of the chat (claims, questions, definitions) lands
at repo root, citing `chat.md:NNN`; this scope only indexes inward.
