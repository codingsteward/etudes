# Implement common math algorithms

def is_prime(n):
    pass


def generate_primes(n):
    """Generate a list of primes up to and including n"""
    primes = [True] * (n+1)
    for i in range(2, n+1):
        if primes[i]:
            j = i
            while i*j <= n:
                primes[i*j] = False
                j += 1
    primes[0] = primes[1] = False
    return [index for index in range(n+1) if primes[index]]

def lg(n):
    pass

print(generate_primes(20))



# bc(n, k) = bc(n-1, k-1) + bc(n-1, k)
# n choose k = case 1: pick 1 bc(n-1, k-1) case 2: don't pick this bc(n-1, k)
# base case, bc(n, 0) = bc(n, n) = 1 
# given n, pick 0 => 1 way, given n pick n => 1 way
def binomial_coeff(N: int):
    """Generate a 2D array for binomial coefficients"""
    coeff = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N+1):
        coeff[i][0] = coeff[i][i] = 1
    for i in range(N+1):
        for k in range(1, i):
            coeff[i][k] = coeff[i-1][k-1] + coeff[i-1][k]
    return coeff


a = binomial_coeff(35)
print(a)
print(a[33][15])
print(sum(a[33]))

