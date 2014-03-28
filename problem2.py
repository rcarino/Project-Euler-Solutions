""" Even fib sum < 4000000 """
def fibs(n):
    fibs = [1, 2]
    ptr1 = 0
    ptr2 = 1
    while fibs[ptr2] < n:
        fibs.append(fibs[ptr1] + fibs[ptr2])
        ptr1 += 1
        ptr2 += 1
    return fibs

evens = filter(lambda elt: elt % 2 == 0, fibs(4000000))
print reduce(lambda l,r: l+r, evens, 0)
