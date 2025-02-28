def abs(x):
    return -x if x < 0 else x

def square(x):
    return x * x


################### Newton's square root ##################

def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

def improve(guess, x):
    return average(guess, x/guess)

def average(x, y):
    return (x+y)/2

def good_enough(guess, x):
    return abs(square(guess)-x) < 0.0000000001

def sqrt(x):
    return sqrt_iter(1.0, x)

print(square(9))
print(sqrt(9))
print(sqrt(137))
print(sqrt(sqrt(2)+sqrt(3)))

print(square(0.000001))

"""Limitations of square root
Arithmetic operations performed with limited precision. Test inadequate for very small or very large numbers.
"""


################### Newton's cube root ####################

def cube(x):
    return x*x*x

def good_enough_cube(guess, x):
    return abs(cube(guess)-x) < 0.001

def improve_cube(guess, x):
    return (x/square(guess)+2*guess)/3

def cube_root_iter(guess, x):
    if good_enough_cube(guess, x):
        return guess
    else:
        return cube_root_iter(improve_cube(guess, x), x)


def cube_root(x):
    return cube_root_iter(1.0, x)

print(cube_root(8))
print(cube_root(27))


########## Localize subprocedures square root #############

def sqrt(x):
    def good_enough(guess):
        return abs(square(guess)-x) < 0.00001

    def improve(guess):
        return average(x/guess, guess)

    def sqrt_iter(guess):
        if good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))

    return sqrt_iter(1.0)


################### Factorial(n) ##########################

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fact(n):
    return fact_iter(1, 1, n)

def fact_iter(product, count, max_count):
    if count > max_count:
        return product
    else:
        return fact_iter(product*count, count+1, max_count)

print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))

def A(x, y):
    if y == 0: return 0
    if x == 0: return 2*y
    if y == 1: return 2
    return A(x-1, A(x, y-1))

print(A(2, 4)) # 65536


######################### fib(n) ##########################

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return fib(n-1) + fib(n-2)

def fib(n):
    return fib_iter(0, 1, n)

def fib_iter(a, b, count):
    if count == 0:
        return a
    else:
        return fib_iter(b, a+b, count-1)

print(fib(0))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))

################### Counting change #######################

def count_change(amount):
    return cc(amount, 5)

def cc(amount, kinds_of_coins):
    """EIther change amount without using current coin
    Or use current coin once
    """
    if amount == 0: return 1
    elif amount < 0 or kinds_of_coins == 0: return 0
    else:
        return cc(amount, kinds_of_coins-1) + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)

def first_denomination(kinds_of_coins):
    if kinds_of_coins == 1: return 1
    elif kinds_of_coins == 2: return 5
    elif kinds_of_coins == 3: return 10
    elif kinds_of_coins == 4: return 25
    elif kinds_of_coins == 5: return 50

print(count_change(100))



################### Exercises #############################

# Prove fib(n) closed form
# Computes elements of Pascal's triangle



################### Exponentiation ########################

def expt(b, n):
    # Linear recursive processs
    if n == 0: return 1
    else:
        return b * expt(b, n-1)

def expt_iter(b, counter, product):
    if counter == 0:
        return product
    else:
        return expt_iter(b, counter-1, product*b)

def expt(b, n):
    # O(N) time and O(1) space
    return expt_iter(b, n, 1)

def fast_expt(b, n):
    # O(lg N) time complexity and constant space
    # Use successive squaring
    # b**4 == b**2 * b**2
    # if n is odd, then do b**n = b*b**(n-1)
    if n == 0: return 1
    elif n % 2 == 1: return b * fast_expt(b, n-1)
    else:
        return fast_expt(b*b, n//2)

def fast_expt_iter(b, n, product):
    if n == 0: return product
    elif n  % 2 == 1:
        return fast_expt_iter(b, n-1, product*b)
    else:
        return fast_expt_iter(b*b, n//2, product)

print(fast_expt_iter(5, 10, 1))
print(5**10)

# Perform integer multiplication as repeated addition
# Perform Fibonacci numbers in log(n)




################### Euclid's GCD ##########################

def gcd(a, b):
    if b == 0: return a
    else:
        return gcd(b, a % b)

print(gcd(206, 40))

print(gcd(40, 6))
print(gcd(6, 4))
print(gcd(4, 2))
print(gcd(2, 0))

# O(log(n)) Lame's theorem: if euclid requires kth step to compute GCD of some pair, then the smaller number must be >= kth fib number

################### Testing for primality #################

def smallest_divisor(n):
    return find_divisor(n, 2)

def find_divisor(n, test_divisor):
    # If n is not a prime, must have a divisor <= sqrt(n)
    if square(test_divisor) > n:
        return n
    elif (n % test_divisor) == 0:
        return test_divisor
    else:
        find_divisor(n, test_divisor+1)

def is_prime(n):
    # O(sqrt(n))
    return n == smallest_divisor(n)


print(is_prime(18))
print(smallest_divisor(18))
print(18 % 2)

# Exercises
# Carmichael numbers do fool fermat test
# Miller-Rabin test variant of Fermat test


################### Higher order functions ################

def sum_integers(a, b):
    # Return sum of integers from a to b
    if a > b: return 0
    return a + sum_integers(a+1, b)

def sum_integers_iter(a, b):
    def helper(acc, a, b):
        if a > b: return acc
        return helper(acc+a, a+1, b)
    return helper(0, a, b)

print(sum_integers(5, 10) == sum_integers_iter(5, 10) == sum(range(5, 11)))

print(sum_integers(1, 10))

def sum_cubes(a, b):
    if a > b: return 0
    return cube(a) + sum_cubes(a+1, b)

print(sum_cubes(1, 10))
print(sum(a*a*a for a in range(1, 11)))


def sum_(term, a, next_, b):
    if a > b:
        return 0
    return term(a) + sum_(term, next_(a), next_, b)


def inc(n):
    return n + 1

def sum_cubes_(a, b):
    return sum_(cube, a, inc, b)

print(sum_cubes_(1, 10) == sum(a**3 for a in range(1, 11)))

def accumulate(combiner, null_value, term, a, next_, b):
    if a > b: return null_value
    return combiner(term(a), accumulate(combiner, null_value, term, next_(a), next_, b))

def add(a, b):
    return a + b

def sum_(term, a, next_, b):
    return accumulate(add, 0, term, a, next_, b)

print(sum_(lambda x: x, 1, lambda x: x+1, 10))


