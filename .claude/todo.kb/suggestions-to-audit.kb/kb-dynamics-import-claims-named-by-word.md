# Import claims wear an `IMPORTED_` label and are named for their word

**Applied.** In `kb-dynamics/docs/dev/claims.kb/imported-terms.kb/`, each
claim's filename is the imported word (`load-event.md` imports "load
event") and its label is `IMPORTED_<WORD>`. The theory's schema stays a
one-line stub; the verify script holds the `ontology:` list equal to the
filenames.

**Why.** Two forced parts and one chosen. Forced: the labels had to
differ from the outer claims' labels, because the flatten tool renders
outer imports by label and reported five defined twice -- once the
paths are gone, labels are the only handle. Forced: reading the word
off the filename avoided a `term:` field, which a `#base` extender
could add but which the defining claim, validated under the same
schema, could never satisfy. Chosen: the prefix `IMPORTED_` rather than
a suffix or an unrelated coinage, so `grep IMPORTED_` lists every
import and a flattened line reads as a sentence, `IMPORTED_RULE+ <-
LAW+ RULE+`.

**What to check.** Whether a flattened render reads well to you, since
that is where the prefix is loudest. And whether an outer word ever
contains a hyphen: the filename-to-word mapping replaces every hyphen
with a space, so such a word would need the `term:` field after all.

**Reverse by.** Labels: one `sed` over the fourteen files, then re-run
`imported-terms.verify.py`, which checks label distinctness. Words: add
`term:` to a `#base`-extending `imported-terms.jsonschema.yaml`, and
change the one function `word()` in the verify script to read it.
