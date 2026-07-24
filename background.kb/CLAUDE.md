--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# background.kb — primers and prior art

Auxiliary (non-truth-apt-graph) background for the realm: technology
primers and prior-art surveys that ground the discourse graph without
being claims themselves.

Belongs: reference material an agent reads for orientation before
working the questions — prior-art system profiles, primers on
formalisms. Does NOT belong: assertions about *our* systems (those are
root `claims.kb/`), open inquiries (root `questions.kb/`), term
definitions (root `definitions.kb/`).

Collections here follow `$TOPIC.{md,kb}` pairs — synthesis plus item
files.
