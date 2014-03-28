__author__ = 'rcarino'
__author__ = 'rcarino'
import heapq
import pprint
pp = pprint.PrettyPrinter(indent=4)

m = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]

def single_source_mp(m, src, dst):
    x, y = src
    size = len(m)
    paths = [[0 for col in range(size)] for row in range(size)]
    h = [(m[x][y], src)]
    visited = set()
    while h:
        cost, prev = heapq.heappop(h)
        if prev not in visited:
            visited.add(prev)
            x, y = prev
            paths[x][y] = cost
            if x == dst[0] and y == dst[1]:
                return paths[x][y]
            for child in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newx, newy = x+child[0], y+child[1]
                if 0 <= newx < size and 0 <= newy < size:
                    heapq.heappush(h, (cost+m[newx][newy], (newx, newy)))
        else:
            continue
    # pp.pprint(paths)
    return -1

with open('matrix.txt') as f:
    content = f.readlines()
    m = []
    for line in content:
        m.append([int(c) for c in line.split(',')])
    print single_source_mp(m, (0,0), (79,79))