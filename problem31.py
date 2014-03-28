def count_change(denoms, val):
    memo = {}
    # Trivially only 1 way to make 0 pence, using i kinds of coins
    for i in range(len(denoms)):
        memo[(0, i)] = 1
    for cur_val in range(1, val+1):
        for di, denom in enumerate(denoms):
            if di == 0:
                # Val w/ all pennies is count_change(val - 1, w/ just pennies)
                memo[(cur_val, di)] = memo[(cur_val - 1, di)]
            elif cur_val - denom < 0:
                memo[(cur_val, di)] = memo[(cur_val, di - 1)]
            else:
                memo[(cur_val, di)] = memo[(cur_val - denom, di)] + memo[(cur_val, di - 1)]
    return memo[(val, len(denoms) - 1)]

denoms = [1, 2, 5, 10, 20, 50, 100, 200]
print count_change(denoms, 200)