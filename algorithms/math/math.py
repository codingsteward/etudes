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
