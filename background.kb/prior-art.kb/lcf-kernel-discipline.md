---
title: "LCF kernel discipline"
originators: [Robin Milner]
sources: [../../sources.kb/knot-theory-chat.md]
likelihood: 0.8
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

Verify: Milner's Edinburgh LCF (1979); uncontroversial, low priority.
