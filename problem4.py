""" largest palindrome from product of 2, 3 digit numbers """

def isPal(n):
    s = str(n)
    sLen = len(s)
    for i in range(sLen/2):
        if s[i] != s[sLen - 1 - i]:
            # NO I'M NACHO FRIEND
            return False
    return True

"""
# recursive version, but python kills it because depth is too high
def greatestPal(n1, n2):
    if isPal(n1 * n2):
        return n1 * n2
    else:
        return max(greatestPal(n1, n2-1), greatestPal(n1-1, n2-1))
"""

def greatestPal(n):
    """ brute force """
    pals = []
    maxPal = 0
    for i in xrange(n, 0, -1):
        for i2 in xrange(i, 0, -1):
            prod = i * i2
            if isPal(prod):
                if prod > maxPal:
                    maxPal = prod
    return maxPal

print greatestPal(999)

