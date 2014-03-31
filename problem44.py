__author__ = 'rcarino'

def pentagonals(n):
    pents = [0] * n
    for i in range(n):
        pents[i] = ((i+1)*(3*(i+1) -1)) / 2
    return pents

def pent_pairs(l):
    # returns the only solution with l being 2500 in 420ms. Reached this limit thru trial and error
    pairs = set()
    pset = set(l)
    for i in range(len(l)):
        for j in range(0, i):
            if l[i] - l[j] in pset and l[j] + l[i] in pset and (l[i], l[j]) not in pairs:
                pairs.add((l[i], l[j]))
    return pairs

pents = pentagonals(2500)
pairs = pent_pairs(pents)
l, r = list(pairs).pop()
print max(l,r) - min(l, r)

