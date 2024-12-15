import sys
sys.stdin = open('input2.txt', 'r')

grid = sys.stdin.read().splitlines()
grid = [list(row) for row in grid]
grid_c = [row.copy() for row in grid]

R, C = len(grid), len(grid[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_idx = 0

for r in range(R):
    for c in range(C):
        if grid[r][c] == '^':
            # start
            while True:
                grid[r][c] = 'X'
                r1, c1 = r + dirs[dir_idx][0], c + dirs[dir_idx][1]
                if not (0 <= r1 < R and 0 <= c1 < C):
                    break
                if grid[r1][c1] == '#':
                    dir_idx = (dir_idx + 1) % 4
                elif grid[r1][c1] == '.' or '^':
                    r, c = r1, c1

# print(sum(row.count('X') for row in grid))


# part 2
# loop is if we see the same (r, c, dir_idx) again
grid = grid_c

def check_loop(grid, start_r, start_c):
    R, C = len(grid), len(grid[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = 0

    r, c = start_r, start_c
    seen = set()
    while True:
        if (r, c, dir_idx) in seen:
            return True
        seen.add((r, c, dir_idx))

        r1, c1 = r + dirs[dir_idx][0], c + dirs[dir_idx][1]
        if not (0 <= r1 < R and 0 <= c1 < C):
            break
        if grid[r1][c1] == '#':
            dir_idx = (dir_idx + 1) % 4
        elif grid[r1][c1] == '.' or '^':
            r, c = r1, c1

    return False

start_r, start_c = None, None
for r in range(R):
    for c in range(C):
        if grid[r][c] == '^':
            start_r, start_c = r, c
            break

loops = 0
for r in range(R):
    for c in range(C):
        print(r, c)
        if grid[r][c] == '.':
            grid[r][c] = '#'
            if check_loop(grid, start_r, start_c):
                loops += 1
            grid[r][c] = '.'

print(loops)