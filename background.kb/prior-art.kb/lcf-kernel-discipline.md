---
title: "LCF kernel discipline"
originators: [Robin Milner]
sources: [../../sources.kb/knot-theory-chat.md]
converges-on: [TL, MT]
tags: [prior-art, proof-assistants]
---

Theorems as an abstract type constructible only through a small trusted
kernel's inference rules — TL's "checked certificate" status as an
architectural invariant (cited in
`../../definitions.kb/total-ledger.md`). Every modern proof assistant
inherits it; it's also the ancestor of the MT seam (the kernel is the
monotonic layer).

Gap: certificates only — no open-obligation or declared-axiom statuses
with lifecycle, no revision above the kernel.

In this realm: `../../claims.kb/monotonic-dynamic-seam.md`. It is also
why `certified:` names a re-runnable check rather than storing a
boolean verdict — the check belongs to the monotonic layer, the record
of it to the dynamic one
(`../../claims.kb/warrant-by-field-presence.md`).

Verify: Milner's Edinburgh LCF (1979); uncontroversial, low priority.
