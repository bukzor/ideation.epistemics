---
title: "llm-subtask marker commands"
originators: [bukzor]
sources: [../../../sources.kb/bukzor.md]
converges-on: [TL]
tags: [prior-art, bukzor]
---

`Skill(llm-subtask)`'s marker-command pattern (`references/marker-
commands.md`): text like `todo push: DESC` or `subtask pop:`, recognized
wherever it appears — user message, file content, conversation history
— triggers a file edit, with dual access (agent edits via Edit, human
edits the same file in an editor) and zero tool-call overhead. This is
the delivery mechanism `claim *` commands inherit directly, and
`subtask save:`'s end-of-session categorization (tactical →
`todo push:`, strategic → a planning file, trivial → abandon) is the
direct ancestor of `claim flush`'s three-way sort (todo checkbox,
`claims.kb/` node, or drop).

Gap: markers carry no justification concept — a todo item is done or
not-done, with no {certificate, obligation, axiom} distinction, so TL's
status axiom is entirely absent from the mechanism; it converges on
*how claims get entered and persisted*, not on what a claim's standing
means. No labels, no dependency edges — nothing for RP to walk.

Verify: `~/.claude/skills/llm-subtask/references/marker-commands.md`.
