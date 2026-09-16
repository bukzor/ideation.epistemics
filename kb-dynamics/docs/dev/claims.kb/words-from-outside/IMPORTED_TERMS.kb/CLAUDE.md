# IMPORTED_TERMS.kb -- maintenance guide

`../IMPORTED_TERMS.md` defines this theory and stipulates its words.

## What belongs here

One claim per imported word, its slug the word (`load-event/IMPORTED_LOAD_EVENT.md`
imports "load event"), signed `+`, with `why:` pointing at the outer claim that
coins it and a body saying how this project reads and uses it.

## What does NOT belong here

A word this project coins itself: that belongs to the theory that coins it.
A claim about the outer project beyond the word's sense.

## When

Add a claim before a working theory first says an outer word. Add the word
to `../IMPORTED_TERMS.md`'s `ontology:` in the same change; the verify
script holds the two equal.
