import sys
import re
sys.stdin = open('input2.txt', 'r')

grid = sys.stdin.read().splitlines()
R, C = len(grid), len(grid[0])


count = 0
word_len = 4

# rows
count += sum(row.count('XMAS') + row.count('SAMX') for row in grid)
# cols
for c in range(C):
    for r in range(R - word_len + 1):
        if all(grid[r+i][c] == 'XMAS'[i] for i in range(word_len)) or all(grid[r+i][c] == 'SAMX'[i] for i in range(word_len)):
            count += 1
    
# diag \
for r in range(R - word_len + 1):
    for c in range(C - word_len + 1):
        if all(grid[r+i][c+i] == 'XMAS'[i] for i in range(word_len)) or all(grid[r+i][c+i] == 'SAMX'[i] for i in range(word_len)):
            count += 1

# diag /
for r in range(R - word_len + 1):
    for c in range(C - word_len + 1):
        if all(grid[r+word_len-1-i][c+i] == 'XMAS'[i] for i in range(word_len)) or all(grid[r+word_len-1-i][c+i] == 'SAMX'[i] for i in range(word_len)):
            count += 1

print(count)



# part 2
# look for A's not along border, check all corners and make sure opposite corners are diff S/M
count = 0
for r in range(1, R - 1):
    for c in range(1, C - 1):
        if grid[r][c] == 'A' and set([grid[r-1][c-1], grid[r+1][c+1]]) == set([grid[r+1][c-1], grid[r-1][c+1]]) == set(['M', 'S']):
            count += 1

print(count)