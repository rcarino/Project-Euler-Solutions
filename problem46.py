__author__ = 'rcarino'
import math

def prime_sieve(n):
    s = [True] * (n+1)
    s[0] = s[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if s[i]:
            for j in range(2*i, n+1, i):
                s[j] = False
    return [i for i, bool in enumerate(s) if bool]

def is_two_times_square(n):
    m = n/2
    m = int(math.sqrt(m))
    return m*m*2 == n

def unverify(n):
    # unverify goldbach's other conjecture for every odd number up to n
    primes = prime_sieve(n)
    pset = set(primes)
    for i in range(5, n+1, 2):
        if i not in pset:
            for p in primes:
                if p >= i:
                    return i # no valid r to complete conjecture
                r = i - p
                if is_two_times_square(r):
                    break
    return 'Not found'

print unverify(10000)