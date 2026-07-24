--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# glossary.kb — the chat's codename decoder ring

One file per codename the captured chat introduced (`**XX**` bolded
introductions, plus operator-coined terms). Filename = alias + `--` +
full expansion (`HC--hidden-cost.md`), the alias cased as the chat
writes it (`Class-E--certified-rules.md`), so `ls` reproduces the
decoder ring and the double dash marks where the alias ends.

Each entry: `chat.md:NNN` line ref, message number, one-two sentence
meaning, lifecycle notes (retracted/superseded/collision), and a link
to the canonical root node where one exists (definitions.kb, claims.kb,
background.kb). Superseded-branch terms are kept and marked — later
turns sometimes reference them.

Belongs: terms coined *in the chat*. Repo-coined terms get root
`definitions.kb/` entries instead. Colliding aliases (RN, SS) get one
file per sense, cross-linked; the chat's own numbered disambiguations
(CS/CS2, CM/CM2) cross-link likewise.
