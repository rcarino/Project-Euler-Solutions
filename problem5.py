""" smallest multiple of [1,20] """

def dividesAll(n):
    """ is n divisible by all numbers in [1,20] """
    for i in xrange(20, 1, -1):
        if n % i != 0:
            return False
    return True

def nextNum(n):
    """ returns next number > n that is evenly divisible by [1,20] """
    while not(dividesAll(n)):
        n += 20
    return n

print nextNum(20)
