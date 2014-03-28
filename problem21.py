# Amicable numbers

def get_divisors(n):
    divisors = set()
    for i in reversed(xrange(1, n/2 + 1)):
        if n % i == 0:
            divisors.add(i)
    return sorted(list(divisors))

def is_amicable(n):
    div_sum = sum(get_divisors(n))
    if n == sum(get_divisors(div_sum)) and n != div_sum:
        return True
    return False

amicable_numbers = [0]
iter = 2

while amicable_numbers[-1] < 10000:
    if is_amicable(iter):
        amicable_numbers.append(iter)
    iter += 1

# Amicable numbers contains the first amicable number that is greather than 10,000
print sum(amicable_numbers[1:-1])
print amicable_numbers

# I feel dirty checking in this brute force solution, but the given problem is pretty small.




