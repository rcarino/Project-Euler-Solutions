def distinct_terms(a, b):
    distinct = set()
    for i in range(2, a+1):
        for j in range(2, b+1):
            distinct.add(i ** j)
    return len(distinct)

print distinct_terms(100, 100)