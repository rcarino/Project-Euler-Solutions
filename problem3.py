import math

""" largest prime factor of n """
def biggestPrimeFactor(n):
    sqrt = int(math.ceil(math.sqrt(n)))
    # get all primes lower than n
    primes = []
    for i in range(1, sqrt + 1):
        if isPrime(i):
            primes.append(i)
    # biggest prime that is divisible by n is the biggest prime factor
    for prime in reversed(primes):
        if n % prime == 0:
            return prime
    return -1

def isPrime(n):
    if n != 2 and n%2 == 0:
        return False
    sqrt = int(math.ceil(math.sqrt(n)))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True

print biggestPrimeFactor(600851475143)

