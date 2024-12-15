import sys
sys.stdin = open('input2.txt', 'r')

grid = sys.stdin.read().splitlines()
R, C = len(grid), len(grid[0])

def dfs(r, c, elev, reached):
    if grid[r][c] != str(elev):
        return
    if elev == 9:
        reached.add((r, c))
        return

    for r1, c1 in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if 0 <= r1 < R and 0 <= c1 < C:
            dfs(r1, c1, elev + 1, reached)

scores = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == '0':
            reached = set()
            dfs(r, c, 0, reached)
            scores += len(reached)

print(scores)

# part 1 vs part 2: no set for reached, track all reaches

def dfs(r, c, elev):
    if grid[r][c] != str(elev):
        return 0
    if elev == 9:
        return 1

    score = 0
    for r1, c1 in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if 0 <= r1 < R and 0 <= c1 < C:
            score += dfs(r1, c1, elev + 1)
    return score

scores = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == '0':
            scores += dfs(r, c, 0)

print(scores)