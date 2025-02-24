# String matching
T refers to text, P refers to pattern

## Test

Finding all shifts s in the range of 0 to n-m s.t Pattern is a suffix of T[:s+m], m is length of pattern

Equal length string between x and y comparison will take O(t) where t is the length of longest string that is a prefix of both x and y 

## Naive string matcher

Finds all valid shifts and check if pattern matches T

The naive is inefficient as it ignores information gained about the text for one value of shift. if P = aaab and s = 0 is valid, then none of the shifts are valid since T[4] = b 

1. Distinct characters in pattern means we can skip ahead by how many characters were matched, we skip by this amount

2. To support pattern with "gaps" i.e can match 0 or more than characters, we can find first occurrence of a1, then first occurrence of a2 after a1.


## Rabin-Karp algorithm
Performs well in practice, generalises to 2D pattern matching
The Rabin-Karp algorithm uses O(m) preprocessing time and worst-case running time is O((n-m+1)m). Based on certain assumptions, average case is better.

The idea of Rabin-Karp is we can treat the characters as digits and compute a rolling hash for each substring to be checked. As we increase the shift, we can compute the next rolling hash in O(1) since we can subtract the previous digit, shift the rest and add the new digit. The previous digit value would be 10^m-1 so if we can compute this in constant time, next substring rolling hash can be computed faster. Hence the pre-computation work to compute all 10^m


Spurious hits: hash(pattern) == hash(substring) but pattern != substring e.g. hash(aal) == hash(abb)

To hash the substring, this might lead to overflow. Hence we use modulo q. By using a large prime q, we reduce the spurious hits.

Expected number of spurious hits is O(n/q), the chance that substring of t equals to pattern is 1/q. There's q possible hashes and substring matches 1 of them. There's n possible substrings so n/q


