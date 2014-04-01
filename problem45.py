__author__ = 'rcarino'

def tph(n):
    # brute force trial the triangle, pentagonal, and hexagonal numbers for the intersection after 40755
    t = [0] * n
    p = [0] * n
    h = [0] * n
    for i in range(n):
        t[i] = ((i+1)*(i+1+1))/ 2
        p[i] = ((i+1)*(3*(i+1) - 1))/2
        h[i] = (i+1)*(2*(i+1) -1)
    return sorted(set(t) & set(p) & set(h))

print tph(100000)