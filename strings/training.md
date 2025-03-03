# Last min work...


A border is a prefix and suffix


lcs = lcs(i-1, j-1) + 1 // if matchin
    = max(lcs(i, j-1), lcs(i-1, j)) otherwise

lcs(i, j) = length of common subsequences of the prefixes x[0...i] and y[0...j]

base case: ? 


Edit distance/levenshtein distance is min edit operations to transform first string to second string
1. insert, remove, modify

edit(a, b) = edit distance between prefixes x[0...a] and y[0...b]

edit(a, b) = min(edit(a, b-1) + 1 // insert at x
                 edit(a-1, b) + 1 // remove last x
                 edit(a-1, b-1) + cost(a, b) // matching or modify x


## String hashing

Check equal by hash values

Polynomial hashing A and B are chosen constants

A = 3, mod B (some prime)

By precomputing the hash[k] of prefixes from 0 to k, we can then compute the hash of any substring in O(1).. same concept as prefix array range queries

## Suffix arrays

Lexicopgrahic order of suffixes, values of it is starting position of suffix:wq!
:

