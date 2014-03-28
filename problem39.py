__author__ = 'rcarino'
import math

def num_rights(p):
    rtn = 0
    for a in range(1, p/2 + 1):
        for b in range(a, p/2 + 1):
            c = math.sqrt(a*a + b*b)
            if a + b + c > p:
                break
            if a + b + c == p:
                rtn += 1
    return rtn

def arg_max_rights(n):
    # 2 step approach takes 17 seconds, iterate thru interval, retrieving the number of triangles with that perimter
    max = 0
    val = -1
    for p in range(1, n+1):
        nr = num_rights(p)
        if nr > max:
            max = nr
            val = p
    return val

# print arg_max_rights(1000)

def one_step(p):
    # takes 9 seconds to iterate over the interval and write to a dictionary if a right triangle is found
    ps = {}
    for a in range(1, p+1):
        for b in range(a, p+1):
            for c in range(b, p+1):
                if a+b+c > p:
                    break
                if a*a + b*b == c*c:
                    ps[a+b+c] = ps[a+b+c] + 1 if a+b+c in ps else 1
    arg_max = 0
    max_val = 0
    for p in ps:
        if ps[p] > max_val:
            max_val = ps[p]
            arg_max = p
    return arg_max

print one_step(1000)