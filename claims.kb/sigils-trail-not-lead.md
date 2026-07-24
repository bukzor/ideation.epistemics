---
status: asserted
sources: [../sources.kb/claim-ledger-notation-session.md]
depends: [../definitions.kb/total-ledger.md]
tags: [notation]
---

Standing sigils (`!` fiat/certified, `?` open) trail the label rather
than lead it: a leading `!` reads as negation to anyone with
programming reflexes, and a trailing sigil keeps the label a clean
greppable prefix (`grep XY` finds `XY`, `XY!`, `XY?`, and every
reference). `'` was rejected in the same pass — reserved by convention
for revision-marking, and mangled by chat-client smart-quoting. Landed
in `Skill(llm-claim-ledger)` SKILL.md.
