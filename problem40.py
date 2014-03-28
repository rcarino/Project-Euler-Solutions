__author__ = 'rcarino'

def chamernownes_constant(n):
    # digits of chamernownes constant up to the nth digit in list form
    l = [-1] * n # favor creation of list because appending to list requires array resizes
    d = 1
    for i in range(n):
        # position smashed by a previous > 1 length digit
        if l[i] != -1:
            continue
        s = str(d)
        for j in range(len(s)):
            # array in bounds check
            if i+j < n:
                l[i + j] = int(s[j])
        d += 1
    return l

const = chamernownes_constant(1000000)
print const[0] * const[9] * const[99] * const[999] * const[9999] * const[99999] * const[999999]

