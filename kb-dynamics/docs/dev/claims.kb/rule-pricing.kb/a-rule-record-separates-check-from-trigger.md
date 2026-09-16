---
label: RECORD_FIELDS
standing: user
authority: chat.md#L392, the owner's assignment of types to trigger and check
why:
  - ../imported-terms.kb/rule.md
---

# A rule record separates the check from the trigger, and types each

A candidate rule decomposes into:

- `check` -- what is verified; a function of the state, and for a gate
  also of the proposed move: `(state, move) -> accept | reject | amend`,
  while a scan is `state -> [finding]`.
- `trigger` -- when it fires; a function of the context, the list of
  past turns.
- `scope` -- what the check ranges over, as a function of ledger size.
- `targets` -- which debt component.
- `mode` -- prevent, detect, or repair. Detect does not reduce debt; it
  converts hidden debt to visible debt, worth something and also a cost
  to the owner.
- `surfaces` -- never, on failure, or always: whether the owner sees
  anything.

> [!@bukzor] chat.md#L392
> I'd think check is a function of kb, and trigger is a function of context (which is a list of past turns).
> Point being this seems mechanizable, at least schematically.
> In that frame, "always" is well represented by a `() -> true` function.

Check and trigger are independent choices. "Before admitting, scan for
prior claims that ground it" and "always scan all other claims for
near-duplication" are nearly the same check under different triggers,
and the trigger is the entire difference in firing rate. A constant
trigger is legitimate: it fires at every evaluation point, so its rate
is the evaluation rate, finite and known. The must-read path convention
is already a trigger in disguise; `before/asking-several-questions` is a
predicate over context.
