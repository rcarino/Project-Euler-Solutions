__author__ = 'rcarino'
# solution: check all primes up to n for truncatable primes. That n happens to be < 1,000,000

import math

def prime_sieve(n):
    s = [True] * (n+1)
    s[0] = s[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        is_prime = s[i]
        if is_prime:
            for j in range(i*2, n+1, i):
                s[j] = False
    return [n for n, flag in enumerate(s) if flag]

primes = prime_sieve(1000000)

def is_truncatable(n):
    global primes
    if n < 10:
        return False
    size = int(math.log10(n)) + 1
    for i in range(size):
        left = n / 10**i
        right = n % 10**(i + 1)
        if left not in primes or right not in primes:
            return False
    return True

# left and right end filters. Left and right must be prime
primes_copy = [p for p in primes if int(str(p)[-1]) in [3, 7] and int(str(p)[0]) not in [4, 6, 8, 9]]
# middle must not contain any even non-primes
primes_copy = [p for p in primes_copy if not(str(p) > 2 and set(str(p)) & set('468'))]
truncatable = [p for p in primes_copy if is_truncatable(p)]
print truncatable
print sum(truncatable)