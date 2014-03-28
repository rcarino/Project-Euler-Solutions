__author__ = 'rcarino'
import math

def primes_upto(n):
    # sieve of eras-something
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i, is_prime in enumerate(sieve):
        if is_prime:
            for j in range(i*i, len(sieve), i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def is_circular_prime(n):
    # true if n and all of its rotations are prime
    global primes
    n_len = int(math.log10(n)) + 1
    for i in range(n_len):
        if n not in primes:
            return False
        n = (n % 10 ** (n_len - 1) * 10) + n / 10 ** (n_len - 1)
    return True

def contains_even_d_or_5(n):
    if n == 5 or n == 2:
        return True
    for d in str(n):
        if int(d) % 2 == 0 or int(d) == 5:
            return False
    return True

def circular_primes(n):
    circs = []
    for p in [n for n in primes if contains_even_d_or_5(n)]:
        if is_circular_prime(p):
            circs.append(p)
    return circs

n = 1000000
primes = primes_upto(n)

print len(circular_primes(n))