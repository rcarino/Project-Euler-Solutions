def pandigital_sum():
    # Find digit width of multipliers that may result in a pandigital equation
    arg_sizes = set()
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(min(a, b), a + b + 1):
                if a + b + c == 9:
                    # Sort multipliers to eliminate duplicates
                    arg_sizes.add((min(a, b), max(a, b)))
    # search the numbers within the found multipliers
    products = set()
    for a_len, b_len in arg_sizes:
        products |= try_multipliers(a_len, b_len)
    return sum([int(p) for p in products])

def choose_n(n, string, cur=''):
    # returns all n sized combinations of string
    if len(cur) == n:
        return {cur}
    else:
        substrings = []
        for c in string:
            substrings.append(choose_n(n, string.replace(c, ''), cur + c))
        rtn = set()
        for ss in substrings:
            rtn |= ss
        return rtn

def try_multipliers(a_len, b_len):
    rtn = set()
    # try all a's
    unused = '123456789'
    for a in choose_n(a_len, unused):
        str_cpy = ''.join([c for c in unused if c not in a])
        # try all compatible b's
        for b in choose_n(b_len, str_cpy):
            c = str(int(a) * int(b))
            if ''.join(sorted(a + b + c)) == unused:
                rtn.add(c)
    return rtn

print pandigital_sum()
