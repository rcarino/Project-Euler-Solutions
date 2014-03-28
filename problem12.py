# What is the value of the first triangle number to have over five hundred divisors?

def num_divisors(n):
    divisors = set([1, n])
    for i in xrange(2, n/2 + 1):  # The largest factor != n is <= n/2
        # Add factors to divisors in pairs
        if n % i == 0:
            if i in divisors:  # Set lookup is constant time
                break  # Terminate because factor was previously added as a pair of a smaller or equal factor
            divisors.add(i)
            divisors.add(n/i)
    return len(divisors)

triangle_index = 1  # From 1
triangle_num = 0
while num_divisors(triangle_num) < 500:
    triangle_num += triangle_index
    triangle_index += 1

print(triangle_num)

#time python problem12.py
#76576500
#
#real	0m7.046s
#user	0m7.036s
#sys	0m0.009s