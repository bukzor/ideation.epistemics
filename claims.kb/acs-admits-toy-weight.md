---
sources: [../sources.kb/claude.md]
depends: [../definitions.kb/acs.md]
date-observed: 2026-07-25
tags: [acs, ladder, mechanism]
---

ACS admits a toy-weight modality without modification: its core model
is parameterized along two axes the spec already names — payload
structure (λΠ terms, of which unstructured atomic constants are a
legal degenerate case) and checker strength (`certified(checker)` is
an open set). Setting both to their weak ends — prose ideas as atomic
payloads; checkers drawn from {operator fiat, LLM judge, named
script} — yields a valid ACS instance, not a fork. Everything the toy
is for — obligation views, trust-base queries, retraction propagation,
contradiction cones — lives in the parameter-independent part of the
model.

Consequence for `../prompts/acs.md`: deliverables 2–4 (store,
transitions, retraction drill, query layer) do not depend on
deliverable 1 (the λΠ embedding). The kernel can be built and
acceptance-tested at toy weight first; the embedding upgrades the
payload parameter later.

Boundary: at the degenerate point the system's own verdicts are
structural. Semantic hang-together — does this premise really support
that conclusion — lives in whoever writes the deductions and
certificates (human or LLM judge), and trust-base-of reports exactly
that provenance.
