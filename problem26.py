def long_divide_unit(d):
    # use grade-school long division algorithm to find cycles if any. Cycles are tracked by which remainders are seen again
    solution = []
    numerator = 10
    numerators = set()
    while d > numerator:
        numerator *= 10
        solution.append('0')
    while numerator % d != 0:
        solution.append(str(numerator/d))
        numerators.add(numerator)
        numerator = (numerator % d) * 10
        if numerator in numerators:
            return ('repeating', '.' + ''.join(solution))
    solution.append(str(numerator/d))
    return ('non-repeating', '.' + str(''.join(solution)))

biggest_repeating = 0
biggest_d = 0
for i in range(2,1000):
    repeat_stat, decimal = long_divide_unit(i)
    if repeat_stat == 'repeating' and len(decimal[1:]) > biggest_repeating:
        biggest_repeating = len(decimal[1:])
        biggest_d = i

print biggest_d