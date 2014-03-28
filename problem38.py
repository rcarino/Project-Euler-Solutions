__author__ = 'rcarino'

def is_pandigital(n):
    s = set()
    i = 1
    while s != set(str(123456789)):
        cur = n * i
        new_s = set(str(cur))
        if len(new_s) != len(str(cur)) or s & new_s:
            return False
        i += 1
        s |= new_s
    return True

def get_prod(n):
    i = 1
    s = ''
    while set(s) != set(str(123456789)):
        cur = n*i
        s += str(cur)
        i += 1
    return int(s)

def largest_pandigital():
    max_prod = -1
    for i in reversed(range(9876+1)):
        if is_pandigital(i) and get_prod(i) > max_prod:
            max_prod = get_prod(i)
    return max_prod

print largest_pandigital()