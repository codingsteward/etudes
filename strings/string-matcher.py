# Implement string matching algorithms here


# Naive -- For all possible shifting, check pattern is a suffix of haystack
def naive_string_match(T, p):
    """Naive string matcher tries all possible shifts of pattern and check if string is equal after a shift
    Time complexity: O((n-m+1)*m) as there are n-m+1 possible shifts and m to check each pattern length
    O(N^2) if m = n/2
    """
    # try all possible shifts
    n, m = len(T), len(p)
    for s in range(n-m+1):
        if p == T[s:s+m]:
            print(f"pattern occurs with shift {s}")

def naive_string_with_distinct_pattern(T, p):
    """Naive string matcher optimised if p has distinct characters, this means we can skip ahead instead of increment by 1
    """
    n, m = len(T), len(p)
    s = 0
    while s < n-m+1:
        i = 1
        if T[s] == p[0]: # found initial match, try checking
            k, i = s, 0
            while i < m and T[k+i] == p[i]:
                i += 1
                if i == m:
                    print(f"Pattern found with shift {s}")
        s += i

def rabin_karp(T, p):
    """Rabin-karp string matching algorithm computes the rolling hash for each substring of T and compares it with the hash of p
    If the hash are equal, we check for equality of two strings as two strings might hash to same value but have a conflict
    Worst case: O((n-m+1)*m) each substring has same hash and we need redo a check
    On average: we don't expect a lot of matches and spurious hits given a good hash function and modulo q
    Then O(n) + O(m(v + n/q)), where v = valid shifts i.e substring matches and n/q as expected number of spurious hits
    If v == 1 and n/q == 1 where q >= m, that is if expected matches is small and prime q is larger than length of pattern, we can expect O(n + m) matching time. Since m <= n, the expected matching time is O(n)
    """
text = "acaabcaaabcdaedabcdaedabcdadabcabc"
pattern = "abc"
naive_string_match(text, pattern)
naive_string_with_distinct_pattern(text, pattern)
