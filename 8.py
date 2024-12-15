import sys
sys.stdin = open('input2.txt', 'r')
from collections import defaultdict
from math import gcd

grid = sys.stdin.read().splitlines()
R, C = len(grid), len(grid[0])

freqs_to_pos = defaultdict(list)
for r in range(R):
    for c in range(C):
        if grid[r][c] != '.':
            freqs_to_pos[grid[r][c]].append((r, c))

antinodes = set()

for freq, positions in freqs_to_pos.items():
    # get all pairs of positions
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            r1, c1 = positions[i]
            r2, c2 = positions[j]

            dr, dc = r2 - r1, c2 - c1
            ar1, ac1 = r1 - dr, c1 - dc
            ar2, ac2 = r2 + dr, c2 + dc

            if 0 <= ar1 < R and 0 <= ac1 < C:
                antinodes.add((ar1, ac1))
            if 0 <= ar2 < R and 0 <= ac2 < C:
                antinodes.add((ar2, ac2))

print(len(antinodes))

# part 2
antinodes = set()
for freq, positions in freqs_to_pos.items():
    # get all pairs of positions
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            r1, c1 = positions[i]
            r2, c2 = positions[j]

            dr, dc = r2 - r1, c2 - c1
            g = gcd(dr, dc)
            dr //= g
            dc //= g

            # keep adding vector to r1, c1 until out of bounds, both ways
            r, c = r1, c1
            while 0 <= r < R and 0 <= c < C:
                antinodes.add((r, c))
                r += dr
                c += dc
            
            r, c = r1, c1
            while 0 <= r < R and 0 <= c < C:
                antinodes.add((r, c))
                r -= dr
                c -= dc

print(len(antinodes))