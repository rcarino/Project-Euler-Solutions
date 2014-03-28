# Quadratic primes
import math

def max_primes():
    max_chain = 0
    # The a and b of the max_chain
    max_coefficients = (-999, -999)
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            chain = len_primes(a, b)
            if chain > max_chain:
                max_chain = chain
                max_coefficients = (a, b)
    return max_coefficients

def is_prime(n):
    # Naive
    if n < 2:
        return False
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if n % i == 0 and n != i:
            return False
    return True


def len_primes(a, b):
    # Number of primes in given quadratic equation
    rtn = 0
    n = 0
    while is_prime(n ** 2 + a*n + b):
        n += 1
        rtn += 1
    return rtn

# COMMENTS: ran in 6 seconds, using naive prime checker. Not much incentive to improve
a, b = max_primes()
print a * b

# Primes test code
# check_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# primes = []
# for i in range(2, 100):
#     if is_prime(i):
#         primes.append(i)
