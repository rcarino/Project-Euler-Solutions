__author__ = 'rcarino'

import math

def sum_factorials():
    for i in range(10, 1000000):
        if i == sum([math.factorial(int(c)) for c in str(i)]):
            print i, 'with factorials: ', [math.factorial(int(c)) for c in str(i)]

sum_factorials()