# imported-terms.kb -- maintenance guide

`../imported-terms.md` defines this theory and stipulates its words.

## What belongs here

One claim per imported word, named for the word (`load-event.md` imports
"load event"), signed `+`, with `why:` pointing at the outer claim that
coins it and a body saying how this project reads and uses it.

## What does NOT belong here

A word this project coins itself: that belongs to the theory that coins it.
A claim about the outer project beyond the word's sense.

## When

Add a claim before a working theory first says an outer word. Add the word
to `../imported-terms.md`'s `ontology:` in the same change; the verify
script holds the two equal.
