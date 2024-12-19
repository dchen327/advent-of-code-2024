import sys
sys.stdin = open('input2.txt', 'r')
from collections import Counter
import math

# input is a  bunch of lines like p=2,4 v=2,-3
# parse these lines into a list of tuples (p, v)
data = []
for line in sys.stdin.read().splitlines():
    parts = line.split(' ')  # Split into `p=2,4` and `v=2,-3`
    p_values = list(map(int, parts[0][2:].split(',')))  # Extract and convert `p=2,4`
    v_values = list(map(int, parts[1][2:].split(',')))  # Extract and convert `v=2,-3`
    data.append((p_values, v_values))

# X, Y = 11, 7
X, Y = 101, 103

quadrants = [0] * 4
N = 100
for (px, py), (vx, vy) in data:
    px = (px + N * vx) % X
    py = (py + N * vy) % Y

    # Determine which quadrant the point is in
    if px < X // 2:
        if py < Y // 2:
            # print(px, py)
            quadrants[0] += 1
        elif py > Y // 2:
            quadrants[1] += 1
    elif px > X // 2:
        if py < Y // 2:
            quadrants[2] += 1
        elif py > Y // 2:
            quadrants[3] += 1

# print prod of quadrants
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

def calculate_entropy(grid):
    flat_grid = [cell for row in grid for cell in row if cell > 0]
    total_cells = len(flat_grid)
    if total_cells == 0:  # No points in the grid
        return 0

    frequencies = Counter(flat_grid)
    entropy = -sum((freq / total_cells) * math.log2(freq / total_cells) for freq in frequencies.values())
    return entropy

# Modify print_points to return the grid
def create_grid(points):
    grid = [[0] * X for _ in range(Y)]
    for px, py in points:
        grid[py][px] += 1
    return grid

def display_grid(grid):
    for row in grid:
        print(''.join(' ' if x == 0 else str(x) for x in row))

# Collect all grids and their entropies
grids = []
points = [(px, py) for (px, py), _ in data]
for t in range(1, 10000):
    if t % 1000 == 0:
        print(t)
    for i, (px, py) in enumerate(points):
        vx, vy = data[i][1]
        points[i] = ((px + vx) % X, (py + vy) % Y)
    
    grid = create_grid(points)
    entropy = calculate_entropy(grid)
    grids.append((entropy, grid, t))

# Sort grids by entropy
grids.sort(key=lambda x: x[0])

# Display sorted grids
for i, (entropy, grid, t) in enumerate(grids):
    print(f"Grid {i + 1} - Entropy: {entropy}, t: {t}")
    display_grid(grid)
    print('-' * 105)
    if i > 3:
        break


# 2397 is too low