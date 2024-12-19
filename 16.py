import sys
from heapq import heappush, heappop

# Read input
sys.stdin = open('input2.txt', 'r')
maze = sys.stdin.read().splitlines()

def solve():
    # Find starting position
    start_r, start_c = next((i, j) for i in range(len(maze)) 
                for j in range(len(maze[i])) if maze[i][j] == 'S')
    
    # Direction vectors: east, south, west, north
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Priority queue elements: (cost, row, col, direction)
    pq = [(0, start_r, start_c, 0, [(start_r, start_c)])]  # Start facing east
    # State: (row, col, direction) -> cost
    seen = {}

    opt_paths = []
    min_cost = float('inf')
    
    while pq:
        cost, r, c, dir_idx, path = heappop(pq)

        if cost > min_cost:
            continue
        
        # Skip if we've seen this state with a lower cost
        state = (r, c, dir_idx)
        # if state in seen and seen[state] <= cost:
        #     continue
        seen[state] = cost
        
        # Check if we reached the end
        if maze[r][c] == 'E':
            if cost < min_cost:
                min_cost = cost
                opt_paths = [path]
            elif cost == min_cost:
                opt_paths.append(path)
            continue
            
        # Try all directions
        for new_dir in range(4):
            nr = r + dirs[new_dir][0]
            nc = c + dirs[new_dir][1]
            
            # Skip if out of bounds or wall
            if maze[nr][nc] == '#':
                continue
                
            # Calculate new cost
            turn_cost = min(abs(new_dir - dir_idx), 4 - abs(new_dir - dir_idx)) * 1000
            new_cost = cost + turn_cost + 1

            # if new_cost > min_cost:
            #     continue
            
            # Add new state to queue if it's better than what we've seen
            new_state = (nr, nc, new_dir)
            if new_state not in seen or new_cost <= seen[new_state]:
                heappush(pq, (new_cost, nr, nc, new_dir, path + [(nr, nc)]))
    
    if opt_paths:
        # Draw an O for every point on the path
        for opt_path in opt_paths:
            for r, c in opt_path:
                maze[r] = maze[r][:c] + 'O' + maze[r][c + 1:]
        # for row in maze:
        #     print(row)
        print(sum(row.count('O') for row in maze))

        return min_cost
    
    return float('inf')

print(solve())