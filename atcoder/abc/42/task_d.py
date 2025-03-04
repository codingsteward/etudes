MOD = 10**9 + 7

H, W, A, B  = (int(i) for i in input().split())

from functools import lru_cache
# compute n choose r for the first H-A rows to W cols 

@lru_cache
def fast_comb(n, r):
    dividend = 1
    if r > n-r:
        a = r
        b = (n-r)
    else:
        a = n-r
        b = r

    for i in range(n, a, -1):
        dividend = dividend * i

    return dividend // factorial(b)

@lru_cache(None)
def multiplicity(n, p):
    """Return the power of the prime number p in the
    factorization of n!"""
    if p > n: return 0
    if p > n//2: return 1
    q, m = n, 0
    while q >= p:
        q //= p
        m += q
    return m

@lru_cache(None)
def primes(n):
    """Generate a list of the prime numbers [2, 3, ... m] where
    m is the largest prime <= n."""
    n = n + 1
    sieve = list(range(n))
    sieve[:2] = [0, 0]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i**2, n, i):
                sieve[j] = 0
    # Filter out the composites, which have been replaced by 0's
    return [p for p in sieve if p]

all_primes = primes(max(W, H))


def powproduct(ns):
    """Compute the explicit value of a factored integer
    given as a list of (base, exponent) pairs."""
    if not ns:
        return 1
    units = 1
    multi = []
    for base, exp in ns:
        if exp == 0:
            continue
        elif exp == 1:
            units *= base
        else:
            if exp % 2:
                units *= base
            multi.append((base, exp//2))
    return units * powproduct(multi)**2

@lru_cache(None)
def factorial(n):
    print(n)
    return powproduct((p, multiplicity(n, p)) for p in all_primes)


total = 0
for b in range(B, W):
    total += fast_comb(H-A-1+b, b) * fast_comb(A-1+W-b-1, A-1) % MOD

print(total)
# matrix = [[0 for _ in range(W)] for _ in range(H)]

# matrix[0][0] = 1

# dp = [1 for _ in range(W)] # For top row, always 1 
# 
# for r in range(1, H):
#     # handle forbidden rows with new start
#     col_start = B if r >= H-A else 0
#     for c in range(col_start, W):
#         in_forbidden = r >= H-A and c < B
#         if in_forbidden:
#             continue
#         if c > 0 and (r < H-A or c-1 >= B):
#             dp[c] += dp[c-1] % MOD
# print(dp[-1])
