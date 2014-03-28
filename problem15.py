# Lattice paths


def count_paths(n):
    """ N is the size of an nxn grid. There are n+1 x n+1 points to visit """
    memo = {}
    # Initialize first row and col, only 1 way to get there from 0,0
    for i in xrange(n + 1):
        memo[(0, i)] = 1
        memo[(i, 0)] = 1
    for i in range(1, n + 1):  # Iterate across the diagonal
        memo[(i, i)] = memo[(i-1, i)] + memo[(i, i-1)]  # Current diagonal
        for col in range(i+1, n+1):
            memo[(i, col)] = memo[(i-1, col)] + memo[(i, col-1)]  # Fill remaining points in row
        for row in range(i+1, n+1):
            memo[row, i] = memo[(row, i-1)] + memo[(row-1, i)]  # Fill remaining points in column
    return memo[(n, n)]

print count_paths(20)