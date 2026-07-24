--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# glossary.kb — the chat's codename decoder ring

One file per codename the captured chat introduced (`**XX**` bolded
introductions, plus operator-coined terms). Filename = alias + full
expansion (`hc-hidden-cost.md`), so `ls` reproduces the decoder ring.

Each entry: `chat.md:NNN` line ref, message number, one-two sentence
meaning, lifecycle notes (retracted/superseded/collision), and a link
to the canonical root node where one exists (definitions.kb, claims.kb,
background.kb). Superseded-branch terms are kept and marked — later
turns sometimes reference them.

Belongs: terms coined *in the chat*. Repo-coined terms get root
`definitions.kb/` entries instead. Colliding aliases (RN, SS, CS, CM)
get one file per sense, cross-linked.
