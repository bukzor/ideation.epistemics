# claims.kb -- maintenance guide

A claim ledger (`Skill(llm-claims-kb)`): one claim per file, standing in
frontmatter, `why:` arrows to premises. `../claims.md` defines it.

## What belongs here

Design commitments of the kb-dynamics model: what a state, move, rule, and
debt are here, and what the harness must show about them. A theory per
vocabulary, beside its `.kb/`.

## What does NOT belong here

A `why:` that leaves `kb-dynamics/`. Only `imported-terms.kb/` may carry
one; a claim needing an outer word imports `imported-terms.md`.
Code: it sits beside the ledger under `kb-dynamics/`, not inside it.

## When

Add a claim when a design choice is made, contested, or ruled. Add a theory
when its claims argue in words no existing theory coins.
