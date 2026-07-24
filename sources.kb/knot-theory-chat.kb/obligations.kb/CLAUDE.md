--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# obligations.kb — the chat's O-ledger

One file per O-numbered obligation from the captured chat, recording
its statement, line refs, revision history (narrowed/refined/extended),
and where it went (promoted to a root `questions.kb/` node, transferred
to a prompt executor, or still open here).

Belongs: only obligations the chat itself numbered. New debts arising
from repo work belong in root `questions.kb/`, not here. When an
obligation discharges, update its file to say how and by what evidence
— don't delete it; this collection is the source-side index.
