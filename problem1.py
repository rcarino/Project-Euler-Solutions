""" Find sum of all multiples of 3 and 5 below 1000"""
def allMultiples(n):
    rtn = []
    for i in range(0, n):
        if (((i % 3) == 0) or ((i % 5) == 0)):
            rtn.append(i)
    return rtn

nums = allMultiples(1000)
print reduce(lambda l,r: l + r, nums, 0)
