"""Find the sum of all the primes below two million."""
import math

def isPrime(n):
    if (n != 2 and n%2 == 0) or n == 1: # evens are not prime, 1 is not prime
        return False
    sqrt = int(math.ceil(math.sqrt(n)))
    for i in range(2, sqrt + 1):
        if n % i == 0 and i != n: # divisibility test for [2, sqrt(n)]
            return False
    return True

def primesUpTo(n):
    rtn = []
    for i in xrange(2, n+1):
        if isPrime(i):
            rtn.append(i)
    return rtn

print sum(primesUpTo(2000000))
