# session-model.claims.kb -- maintenance guide

A claim ledger (`Skill(llm-claims-kb)`): one claim per file, standing in
frontmatter, `why:` arrows to premises, cross-repo where the premise lives
in another ledger. `../session-model.claims.md` defines it.

## What belongs here

The defining claim of each simulation-side theory beside its `.kb/`: rules,
budgets, traces, the full game. Code, when it exists, sits beside this
directory, not inside it.

## What does NOT belong here

A claim about what the owner holds or how a ruling is recorded
(`design.claims.kb/commitment`), about asks (`design.claims.kb/ask`), or about
carriers and junctures (`strata.claims.kb/carriage`). Import them.

## When

Add a theory when its claims argue in words no existing theory coins. Add a
claim when a scenario, an oracle, or an exit is made, contested, or ruled.
