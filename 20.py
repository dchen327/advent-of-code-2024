import sys
import pickle
sys.stdin = open('input2.txt', 'r')
from heapq import heappop, heappush
from collections import deque, defaultdict, Counter
from copy import deepcopy
from time import time

start_time = time()

grid = [list(l) for l in sys.stdin.read().splitlines()]
R, C = len(grid), len(grid[0])

graph = defaultdict(list)
for r in range(R):
    for c in range(C):
        if grid[r][c] == '#':
            continue
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
                graph[(r, c)].append(((nr, nc), 1))

sr, sc = None, None
er, ec = None, None
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            sr, sc = r, c
            grid[r][c] = '.'
        if grid[r][c] == 'E':
            er, ec = r, c
            grid[r][c] = '.'


def shortest_path(grid):
    ''' shortest path from (sr, sc) to (er, ec) '''
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Priority queue elements: (cost, row, col, path)
    pq = [(0, sr, sc, [(sr, sc)])]
    # State: (row, col) -> cost
    seen = {}

    min_cost = float('inf')

    while pq:
        cost, row, col, path = heappop(pq)
        if cost > min_cost:
            continue

        state = (row, col)
        if state in seen and seen[state] <= cost:
            continue
        seen[state] = cost

        # check if end
        if row == er and col == ec:
            min_cost = min(min_cost, cost)
            continue
    
        for new_dir in range(4):
            nr = row + dirs[new_dir][0]
            nc = col + dirs[new_dir][1]

            if grid[nr][nc] == '#':
                continue

            heappush(pq, (cost + 1, nr, nc, path + [(nr, nc)]))
    
    return min_cost

def shortest_path_bfs(grid, max_len):
    ''' bfs shortest path, if > max_len return inf '''
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(sr, sc, 0)])
    visited = set([(sr, sc)])

    while queue:
        r, c, dist = queue.popleft()
        if dist > max_len:
            return float('inf')
        if r == er and c == ec:
            return dist
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and grid[nr][nc] != '#':
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return float('inf')

def shortest_path_graph_bfs(graph, max_len):
    ''' bfs shortest path in graph '''
    queue = deque([((sr, sc), 0)])
    visited = set([(sr, sc)])

    while queue:
        node, dist = queue.popleft()
        if dist > max_len:
            return float('inf')
        if node == (er, ec):
            return dist
        
        for neighbor, edge_dist in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + edge_dist))
    
    return float('inf')

def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def shortest_path_graph_djikstra(graph, start):
    ''' shortest path from start to all nodes '''
    # filter graph to only keep nodes 

    pq = [(0, start)]
    dists = {node: float('inf') for node in graph}
    dists[start] = 0

    while pq:
        dist, node = heappop(pq)
        if dist > dists[node]:
            continue
        
        for neighbor, edge_dist in graph[node]:
            new_dist = dist + edge_dist
            if new_dist < dists[neighbor]:
                dists[neighbor] = new_dist
                heappush(pq, (new_dist, neighbor))
    
    return {node: dist for node, dist in dists.items() if node > start}
    



# calc shortest path between all nodes in graph
# shortest_dist = {}
# for start in graph:
#     shortest = shortest_path_graph_djikstra(graph, start)
#     for node in shortest:
#         if manhattan_dist(start, node) <= 20:
#             shortest_dist[(start, node)] = shortest[node]

# with open('shortest_dist.pkl', 'wb') as f:
#     pickle.dump(shortest_dist, f)
# quit()

with open('shortest_dist.pkl', 'rb') as f:
    shortest_dist = pickle.load(f)

no_cheat_time = shortest_path(grid)
print('no_cheat_time:', no_cheat_time)
# print(shortest_dists)

# allow cheating: can replace .#. with ... once
# num_checks = 0
# S = 100
# total = 0
# for r in range(1, R - 1):
#     print(r, R)
#     for c in range(1, C - 1):
#         if grid[r][c] == '#':
#             if (grid[r - 1][c] == '.' and grid[r + 1][c] == '.') or (grid[r][c - 1] == '.' and grid[r][c + 1] == '.'):
#                 num_checks += 1
#                 grid[r][c] = '.'
#                 time = shortest_path_bfs(grid, no_cheat_time - S)
#                 if no_cheat_time - time >= S:
#                     total += 1
#                 grid[r][c] = '#'
            
# print('Num checks:', num_checks)
# print(total)

'''
part 2: can add an edge of len <= 20 between any two . cells (manhattan distance)

we can precalc dist between all . points <= 20 manh dist
and if maze dist > manh dist, can consider adding an edge there
'''

num_checks = 0
S = 100
total = 0
counts = Counter()
for r in range(R):
    for c in range(C):
        if grid[r][c] == '.':
            for r1 in range(r, R):
                for c1 in range(C):
                    if not (r < r1 or (r == r1 and c < c1)):  # avoid dups
                        continue
                    if (r1 == r and c1 == c) or grid[r1][c1] == '#':
                        continue
                    dist = abs(r1 - r) + abs(c1 - c)
                    if dist <= 20 and shortest_dist[((r, c), (r1, c1))] - dist >= S:
                        num_checks += 1
                        if num_checks % 10000 == 0:
                            print(num_checks)
                        graph[(r, c)].append(((r1, c1), dist))
                        graph[(r1, c1)].append(((r, c), dist))
                        time = shortest_path_graph_bfs(graph, no_cheat_time - S)
                        if no_cheat_time - time >= S:
                            counts[no_cheat_time - time] += 1
                            total += 1
                        graph[(r, c)].pop()
                        graph[(r1, c1)].pop()
 
print('Num checks:', num_checks)
print(total)

print(counts)

print(time() - start_time)


'''
opt: need to cache dist from every point to start/end
for all these pairs, if manh dist <= 20, can add edge
'''