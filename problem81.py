__author__ = 'rcarino'
# dijkstra to find shortest path in matrix

import sys
from heapq import heappush, heappop

small_m = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]

def shortest_path(m, goal_x,goal_y):
    heap = []
    heappush(heap, (m[0][0], 0,0)) # heap nodes are (path, x, y)
    visited = set()
    while heap:
        path, x, y = heappop(heap)
        visited.add((x,y))
        if goal_x == x and goal_y == y:
            return path
        for child in [(0, 1), (1, 0)]:
            new_x, new_y = child
            new_x += x
            new_y += y
            if 0 <= new_x <len(m) and 0 <= new_y < len(m[0]) and (new_x, new_y) not in visited:
                heappush(heap, (path+ m[new_x][new_y], new_x, new_y))
    return None

with open(sys.argv[1]) as f :
    content = f.readlines()
    m = []
    for line in content:
        row = [int(num) for num in line.strip().split(',')]
        m.append(row)
    print shortest_path(m, 79, 79)