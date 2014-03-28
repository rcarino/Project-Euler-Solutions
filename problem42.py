__author__ = 'rcarino'

import sys

def is_triangular(s):
    global triangles, last_n
    last_t = ((last_n + 1) * last_n) / 2
    v = sum([ord(c) - 64 for c in s])
    while v >= (last_t):
        triangles.add(last_t)
        last_n += 1
        last_t = ((last_n + 1) * last_n) / 2
    return v in triangles

triangles = {1}
last_n = 1

def num_tri(f):
    with open(f) as file:
        words = [w[1:-1] for w in file.read().strip().split(',')]
        cnt = 0
        for word in words:
            if is_triangular(word):
                cnt += 1
        return cnt

print num_tri(sys.argv[1])