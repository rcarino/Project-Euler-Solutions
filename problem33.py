__author__ = 'rcarino'

import fractions

def digit_canceling_fractions():
    # brute force
    fracs = []
    for n0 in range(10):
        for n1 in range(10):
            for d0 in range(10):
                for d1 in range(10):
                    num = str(n0) + str(n1)
                    denom = str(d0) + str(d1)
                    #   digit bounds                              remove trivial                       proper frac               more trivial elimination
                    if int(num) >= 10 and int(denom) >= 10 and num[1] != '0' and denom[1] != '0' and int(num) < int(denom) and n0 != n1 and d0 != d1:
                        frac = int(num) / float(denom)
                        cancel_num = set(num) - (set(num) & set(denom))
                        cancel_denom = set(denom) - (set(num) & set(denom))
                        if len(cancel_num) == 1:
                            cancel_num, cancel_denom = cancel_num.pop(), cancel_denom.pop()
                            if frac == int(cancel_num) / float(cancel_denom):
                                fracs.append((cancel_num, cancel_denom))
    return fracs

fracs = digit_canceling_fractions()
unsimple = reduce(lambda accum, cur: (accum[0] * int(cur[0]),accum[1] * int(cur[1])), fracs, (1, 1))
gcd = fractions.gcd(*unsimple)
print unsimple[1] / gcd