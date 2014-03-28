

def sum_spiral_diagonals(n):
    # n must be odd
    spiral = []

    # init spiral to proper size matrix of 0's
    for i in xrange(n):
        spiral.append([0 for j in xrange(n)])

    # fill spiral and count diagonals
    start, end = (0, n - 1) # Begin filling from top-right corner
    val = n ** 2
    sum = 0
    while start != end:
        # right to left
        sum += val # add top right corner
        for top in reversed(xrange(start, end+1)):
            spiral[start][top] = val
            val -= 1
        # top to bottom
        sum += val + 1 # add top left corner
        for left in xrange(start+1, end+1):
            spiral[left][start] = val
            val -= 1
        # left to right
        sum += val + 1 # add bottom left corner
        for bottom in xrange(start+1, end+1):
            spiral[end][bottom] = val
            val -= 1
        # fill bottom to top
        sum += val + 1 # add bottom right corner
        for right in reversed(xrange(start+1, end)):
            spiral[right][end] = val
            val -= 1
        start, end = (start+1, end-1)
    return sum + 1 # Add 1 because we omitted the center. Print spiral list to verify this

print sum_spiral_diagonals(1001)

