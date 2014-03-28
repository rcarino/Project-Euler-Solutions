__author__ = 'rcarino'
import math

def prime_sieve(n):
    s = [True] * (n+1)
    s[0] = s[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if i:
            for j in range(i*2, n+1, i):
                s[j] = False
    return [i for i, bool in enumerate(s) if bool]


def longest_consec1(primes):
    # takes ~6 seconds
    # iterate over all primes, searching if they have compatible subintervals
    sums = [0] * len(primes)
    sums[0] = primes[0]
    for i in range(1, len(primes)):
        sums[i] = sums[i-1] + primes[i]
    max_prime = -1
    max_consec = 0
    sums = {sum:i for i, sum in enumerate(sums) if sum <= primes[-1]}
    for p in primes:
        for s in sums:
            if s < p:
                continue
            if s == p or s-p in sums:
                run = sums[s] if s == p else sums[s] - sums[s-p] - 1
                if run > max_consec:
                    max_consec = run
                    max_prime = p
    return max_prime

def longest_consec2(primes):
    # takes ~.86 seconds
    # iterate over all subintervals, checking if they're prime
    sums = [0] * len(primes)
    sums[0] = primes[0]
    for i in range(1, len(primes)):
        sums[i] = sums[i-1] + primes[i]
    sums = [s for s in sums if s <= primes[-1]] # Narrow search space from ~78k to 500
    primes = set(primes)
    max_prime = -1
    max_consec = 0
    for l in range(len(sums)):
        for r in range(l+1, len(sums)):
            full = sums[r]
            partial = sums[r] - sums[l]
            if full in primes or partial in primes:
                run = r if full in primes else r-l - 1
                if run > max_consec:
                    max_consec = run
                    max_prime = full if full in primes else partial
    return max_prime

primes = prime_sieve(1000000)
print longest_consec2(primes)