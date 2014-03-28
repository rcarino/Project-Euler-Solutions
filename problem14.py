# Longest Collatz sequence


def generate_collatz_sequence(start, cache):
    sequence = [start]
    while sequence[-1] != 1:
        n = sequence[-1]
        if n in cache:
            new_seq = sequence + cache[n][1:]
            cache[start] = new_seq
            return new_seq
        if n % 2 == 0:
            sequence.append(n/2)
        else:
            sequence.append(n*3 + 1)
    cache[start] = sequence
    return sequence

biggest_seq = []
biggest_seed = 0
cache = {}
for i in range(1, 1000000 + 1):
    current_seq = generate_collatz_sequence(i, cache)
    if len(current_seq) > len(biggest_seq):
        biggest_seed = i
        biggest_seq = current_seq

print biggest_seed

#time python problem14.py
#real	0m24.843s
#user	0m18.846s
#sys	0m1.294s