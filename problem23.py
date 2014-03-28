import datetime
start = datetime.datetime.now()

def get_divisors(n):
    divisors = []
    for i in reversed(xrange(1, n/2 + 1)):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_abundant(n):
    if sum(get_divisors(n)) > n:
        return True
    return False
# The naive approach takes 21 seconds to generate all abundants and find undecomposable numbers
# all_abundants = [] # All abundants in [1,28123), not [1, infinite)
# for i in range(1, 28123):
#     if is_abundant(i):
#         all_abundants.append(i)

# The better way to generate all amicable numbers
# Use sum of prime formula for a number's prime factors to determine the sum of a number's factors
# This approach to generate all abundants and sum undecomposables takes 15 seconds. Prime factorization is a 6 second improvement. Not all that much better w/ mathematical cleverness
def get_prime_factors(n):
    prime_factors = {}
    candidate_factor = 2
    while n > 1:
        if n % candidate_factor == 0:
            n /= candidate_factor
            if candidate_factor in prime_factors:
                prime_factors[candidate_factor] += 1
            else:
                prime_factors[candidate_factor] = 1
        else:
            candidate_factor += 1
    return prime_factors

def sum_divisors(n):
    prime_factors = get_prime_factors(n)
    sum_divisors = 1
    for prime_factor, exponent in prime_factors.iteritems():
        sum = (prime_factor ** (exponent + 1) - 1) / (prime_factor - 1)
        sum_divisors *= sum
    return sum_divisors - n

all_abundants = [i for i in range(1, 28123) if sum_divisors(i) > i]
current_abundants = set()
undecomposable = []
for i in range(1, 28123):
    if all_abundants[0] == i:
        current_abundants.add(all_abundants.pop(0))

    # test whether i is decomposable
    is_decomposable = False
    # n time search for decomposable number because current_abundants is a hash set
    for j in current_abundants:
        if i - j in current_abundants:
            is_decomposable = True
            break

    # current number is undecomposable if validation passed or, i is smaller than the smallest abundant number
    if not current_abundants or not is_decomposable:
        undecomposable.append(i)

print sum(undecomposable)


end = datetime.datetime.now()

print 'took ', end - start
