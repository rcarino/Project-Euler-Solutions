import math
def find_triple(n):
    for a in xrange(1, n+1):
        for b in xrange(a+1, n+1):
            c = a*a + b*b
            if math.sqrt(c).is_integer() and a+b+c == 1000:
                return a*b*c


print find_triple(1000)
