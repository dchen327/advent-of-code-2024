import sys
sys.stdin = open('input2.txt', 'r')

# inc max rec depth
# sys.setrecursionlimit(10**6)

# grid = []
# while True:
#     i = input()
#     if i == '':
#         break
#     grid.append(list(i))

# moves = sys.stdin.read().replace('\n', '')

# dir_map = {
#     '>': (0, 1),
#     '<': (0, -1),
#     '^': (-1, 0),
#     'v': (1, 0)
# }

# R, C = len(grid), len(grid[0])
# pr, pc = None, None
# for r in range(R):
#     for c in range(C):
#         if grid[r][c] == '@':
#             pr, pc = r, c
#             break

# for move in moves:
#     dr, dc = dir_map[move]
#     nr, nc = pr + dr, pc + dc
#     if grid[nr][nc] == '.':
#         grid[pr][pc] = '.'
#         pr, pc = nr, nc
#         grid[pr][pc] = '@'
#     elif grid[nr][nc] == 'O':
#         # check if can move all the boxes
#         num_boxes = 0
#         while grid[nr + num_boxes * dr][nc + num_boxes * dc] == 'O':
#             num_boxes += 1
#         if grid[nr + num_boxes * dr][nc + num_boxes * dc] == '.':
#             grid[pr][pc] = '.'
#             pr, pc = nr, nc
#             grid[pr][pc] = '@'
#             grid[nr + num_boxes * dr][nc + num_boxes * dc] = 'O'
    

# sum_coords = 0
# for r in range(R):
#     for c in range(C):
#         if grid[r][c] == 'O':
#             sum_coords += 100 * r + c
# print(sum_coords)
            


# part 2
# need recursion: checking if can move, recursive, and same with actually moving the boxes

grid = []
while True:
    i = input()
    if i == '':
        break
    i = i.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    grid.append(list(i))

moves = sys.stdin.read().replace('\n', '')

dir_map = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

R, C = len(grid), len(grid[0])
pr, pc = None, None
for r in range(R):
    for c in range(C):
        if grid[r][c] == '@':
            pr, pc = r, c
            break

def can_move(pr, pc, dr, dc):
    ''' only for vertical '''
    nr, nc = pr + dr, pc + dc
    if grid[nr][nc] == '.':
        return True
    elif grid[nr][nc] == '[':
        return can_move(nr, nc, dr, dc) and can_move(nr, nc + 1, dr, dc)
    elif grid[nr][nc] == ']':
        return can_move(nr, nc, dr, dc) and can_move(nr, nc - 1, dr, dc)
    return False

made_moves = set()
def make_move(pr, pc, dr, dc):
    ''' only for vertical '''
    if (pr, pc, dr, dc) in made_moves:
        return
    made_moves.add((pr, pc, dr, dc))
    nr, nc = pr + dr, pc + dc
    if grid[nr][nc] != '.':
        if grid[nr][nc] == '[':
            make_move(nr, nc, dr, dc)
            make_move(nr, nc + 1, dr, dc)
        elif grid[nr][nc] == ']':
            make_move(nr, nc, dr, dc)
            make_move(nr, nc - 1, dr, dc)

    grid[nr][nc] = grid[pr][pc]
    grid[pr][pc] = '.'

# grid = '''
# ########
# #....@.#
# #...[].#
# #..[]..#
# #.[][].#
# ########
# '''
# grid = [list(i) for i in grid.split('\n') if i]
# pr, pc = 1, 5
# print(can_move(pr, pc, 1, 0))


for move in moves:
    dr, dc = dir_map[move]
    nr, nc = pr + dr, pc + dc
    if grid[nr][nc] == '.':
        grid[pr][pc] = '.'
        pr, pc = nr, nc
        grid[pr][pc] = '@'
    elif grid[nr][nc] in '[]':
        if dr == 0:  # only horiz, easier
            num_boxes = 0  # num box pieces, / 2 for boxes
            while grid[nr][nc + num_boxes * dc] in '[]':
                num_boxes += 1
            if grid[nr][nc + num_boxes * dc] == '.':
                # shift each over by 1
                for i in range(num_boxes, -1, -1):
                    grid[nr][nc + i * dc] = grid[nr][nc + (i - 1) * dc]
                grid[pr][pc] = '.'
                pr, pc = nr, nc
        else:
            if not can_move(pr, pc, dr, dc):
                continue
            made_moves = set()
            make_move(pr, pc, dr, dc)
            pr, pc = nr, nc
            grid[pr][pc] = '@'
    # print('move:', move)
    # for row in grid:
    #     print(''.join(row))

sum_coords = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == '[':
            sum_coords += 100 * r + c

print(sum_coords)