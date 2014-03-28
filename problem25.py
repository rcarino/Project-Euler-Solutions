def nth_digit_fib(n):
    f1 = 1
    f2 = 1
    nth = 2
    while len(str(f2)) < n:
        tmp = f2
        f2 = f1 + f2
        f1 = tmp
        nth += 1
    return nth

print nth_digit_fib(1000)
