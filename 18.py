import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappush, heappop

# inc rec depth
sys.setrecursionlimit(10**6)

coords = [tuple(map(int, l.split(',')))[::-1] for l in sys.stdin.read().splitlines()]

N = 71
R = C = N

def shortest_path(grid):
    # shortest path from (0, 0) to (N, N)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Priority queue elements: (cost, row, col, direction, path
    pq = [(0, 0, 0, 0, [(0, 0)])]
    # State: (row, col, direction) -> cost
    seen = {}

    min_cost = float('inf')

    while pq:
        cost, row, col, dir_idx, path = heappop(pq)
        if cost > min_cost:
            continue

        state = (row, col, dir_idx)
        if state in seen and seen[state] <= cost:
            continue
        seen[state] = cost

        # check if end
        if row == N - 1 and col == N - 1:
            min_cost = min(min_cost, cost)
            continue

        for new_dir in range(4):
            nr = row + dirs[new_dir][0]
            nc = col + dirs[new_dir][1]

            if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] == '#':
                continue

            heappush(pq, (cost + 1, nr, nc, new_dir, path + [(nr, nc)]))

    return min_cost

def dfs(grid, r, c, visited=None):
    ''' check if there exists a path to (N-1, N-1) '''
    if visited is None:
        visited = set()
    if r == N - 1 and c == N - 1:
        return True
    if (r, c) in visited:
        return False
    visited.add((r, c))

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] == '#':
            continue
        if dfs(grid, nr, nc, visited):
            return True

    return False
    

grid = [['.' for _ in range(C)] for _ in range(R)]
for i, (r, c) in enumerate(coords):
    if i % 100 == 0: print(i)
    grid[r][c] = '#'
    if i > 1024 and not dfs(grid, 0, 0):
        print(f'{c},{r}')
        break
