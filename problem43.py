__author__ = 'rcarino'

def perms(s):
    if len(s) == 1 or not s:
        yield s
    else:
        for p in perms(s[1:]):
            for i in range(len(p) + 1):
                yield p[:i] + s[0] + p[i:]

def num_ss_divisible():
    # takes 8 seconds naively finding all permutations
    # pandigitals = [p for p in perms('0123456789')]

    # d5 can be fixed to 0 or 5, combine 2 smaller permutation sets
    # this approach brings running time down to 2 seconds
    # permutation calls combined, take .7 seconds
    pandigitals = [p[:5] + '0' + p[5:] for p in perms('123456789')] + [p[:5] + '5' + p[5:] for p in perms('012346789')]

    # filter violations in order
    filters = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        pandigitals = [p for p in pandigitals if int(p[i: i+3]) % filters[i-1] == 0]
    print pandigitals
    return sum(map(int, pandigitals))

print num_ss_divisible()