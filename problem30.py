import math

def digit_fourth():
    rtn = []
    for i in range(10, 9**4 * 5 + 1):
        if i == sum([int(d)**4 for d in str(i)]):
            rtn.append(i)
    return rtn

# print digit_fourth()

def digit_fifth():
    # using math rather than str iterator takes solution from 2s to 1s
    rtn = []
    for i in range(10, 9**5 * 6 + 1):
        fifth_pows = 0
        for d in range(int(math.log10(i)) + 1):
            fifth_pows += (i/(10**d) % 10) ** 5
        if i == fifth_pows:
            rtn.append(i)
    return rtn

print sum(digit_fifth())
