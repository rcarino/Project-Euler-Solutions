import math

"""What is the 10 001st prime number?"""
def nthPrime(n):
    i = 2
    lastPrime = 1
    while lastPrime < n: # bootstrap primes enumeration from 2
        if isPrime(i):
            lastPrime += 1
        if lastPrime == n:
            break
        i += 1
    return i
        

def isPrime(n):
    if (n != 2 and n%2 == 0) or n == 1: # evens are not prime, 1 is not prime
        return False
    sqrt = int(math.ceil(math.sqrt(n)))
    for i in range(2, sqrt + 1):
        if n % i == 0: # divisibility test for [2, sqrt(n)]
            return False
    return True

print nthPrime(10001)

    
