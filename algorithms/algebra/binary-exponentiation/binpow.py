# Practice code to implement exponentiation
# a^n => O(n)

def linear_exp(a, n):
    total = 1
    for i in range(n):
        total *= a
    return total


assert(linear_exp(3, 1) == 3)
assert(linear_exp(3, 8) == 6561)



# a^n = (a^2)^(n/2) if n is even
# a^n = (a^2)^((n-1)/2) * a if n is odd
def binpow(a, n):
    if n == 0: return 1
    if n % 2 == 0:
        return binpow(a*a, n//2)
    else:
        return a * binpow(a*a, n//2)

print(binpow(3, 8))


# bottom up binpow
def binpow1(a, n):
    # break 13 into power of 2
    pow = a
    ans = 1
    while n > 0:
        if n & 1: # last bit is set
            print(n, pow)
            ans *= pow
        n = n >> 1 # move down one bit
        pow = pow * pow
    return ans

print(binpow1(3, 13))


# Computation of large exponents modulo m
def binpow2(a, b, m):
    a %= m
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b = b >> 1
    return res

print(binpow2(3, 13, 100))
