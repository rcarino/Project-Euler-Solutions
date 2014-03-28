__author__ = 'rcarino'
import math

def permute(s):
    if not s or len(s) == 1:
        yield s
    else:
        for p in permute(s[1:]):
            for i in range(len(p) + 1):
                 yield p[:i] + s[0] + p[i:]

def is_prime(n):
    if n <= 1 or n > 2 and n%2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n != i and n % i == 0:
            return False
    return True

def pandigital_primes():
    digits = '123456789'
    max_primes = 0
    for i in reversed(range(1, len(digits) + 1)):
        # filter evens and divisible by 3
        perms = [p for p in permute(digits[:i]) if int(p[-1]) % 2 != 0]
        perms = [p for p in perms if sum([int(d) for d in p]) % 3 != 0]
        for p in perms:
            if is_prime(int(p)) and int(p) > max_primes:
                max_primes = int(p)
        if max_primes != 0:
            return max_primes

print pandigital_primes()