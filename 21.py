import sys
sys.stdin = open('input2.txt', 'r')
from collections import deque, Counter
from itertools import product
from functools import cache

codes = sys.stdin.read().splitlines()

numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['',  '0', 'A']
]

dpad = [
    ['',  '^', 'A'],
    ['<', 'v', '>'],
]

# map button to (r, c)
numpad_to_rc = {}
for r in range(4):
    for c in range(3):
        numpad_to_rc[numpad[r][c]] = (r, c)

dpad_to_rc = {}
for r in range(2):
    for c in range(3):
        dpad_to_rc[dpad[r][c]] = (r, c)

# store best paths for a given pair of buttons
best_paths_numpad = {}
best_paths_dpad = {}
best_paths2_dpad = {}


def shortest_paths(s, is_numpad):
    ''' s is a string of digits '''
    if is_numpad:
        pad = numpad
        pad_to_rc = numpad_to_rc
    else:
        pad = dpad
        pad_to_rc = dpad_to_rc
    sr, sc = pad_to_rc[s[0]]
    er, ec = pad_to_rc[s[1]]
    target_dist = abs(sr - er) + abs(sc - ec)

    R, C = len(pad), len(pad[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_to_symbol = {0: '>', 1: 'v', 2: '<', 3: '^'}

    # generate all symbol paths from s to e, can't go through ''
    paths = []
    # (r, c, dist, path)
    queue = deque([(sr, sc, 0, '')])
    while queue:
        r, c, dist, path = queue.popleft()
        if (r, c) == (er, ec):
            paths.append(path + 'A')
            continue
    
        for dir_idx, (dr, dc) in enumerate(dirs):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and numpad[nr][nc] != '' and dist < target_dist:
                queue.append((nr, nc, dist + 1, path + dir_to_symbol[dir_idx]))
    
    return paths

for r in range(4):
    for c in range(3):
        for r2 in range(4):
            for c2 in range(3):
                if numpad[r][c] == '' or numpad[r2][c2] == '':
                    continue
                s = numpad[r][c] + numpad[r2][c2]
                best_paths_numpad[s] = shortest_paths(s, True)

for r in range(2):
    for c in range(3):
        for r2 in range(2):
            for c2 in range(3):
                if dpad[r][c] == '' or dpad[r2][c2] == '':
                    continue
                s = dpad[r][c] + dpad[r2][c2]
                best_paths_dpad[s] = shortest_paths(s, False)

# best_paths2_dpad maps a pair of buttons to length of shortest possible 2 deep path
for r in range(2):
    for c in range(3):
        for r2 in range(2):
            for c2 in range(3):
                if dpad[r][c] == '' or dpad[r2][c2] == '':
                    continue
                s = dpad[r][c] + dpad[r2][c2]
                shortest_path = float('inf')
                for path in best_paths_dpad[s]:
                    path_len = 0
                    path = 'A' + path
                    for i in range(len(path) - 1):
                        s2 = path[i:i+2]
                        path_len += min(map(len, best_paths_dpad[s2]))
                    shortest_path = min(shortest_path, path_len)
                    best_paths2_dpad[s] = shortest_path

@cache
def get_next_codes(code, is_numpad=False):
    res = ['']
    for i in range(len(code) - 1):
        s = code[i:i+2]
        p1 = best_paths_numpad[s] if is_numpad else best_paths_dpad[s]
        new_res = []
        for x in res:
            for y in p1:
                new_res.append(x + y)
        res = new_res
    return res

total_complexity = 0
for code in codes:
    num = int(code[:-1])
    code = f'A{code}'

    next_codes = get_next_codes(code, True)
    min_sum = float('inf')
    for x in next_codes:
        sum_ = 0
        x = 'A' + x
        for i in range(len(x) - 1):
            s = x[i:i+2]
            sum_ += best_paths2_dpad[s]
        min_sum = min(min_sum, sum_)
    print(min_sum, num)
    total_complexity += num * min_sum
    # y = sum([get_next_codes(code, False) for code in x], [])
    # # remove non min len seqs
    # y = [x for x in y if len(x) == min(map(len, y))]
    # # print(y)
    # z = sum([get_next_codes(code, False) for code in y], [])
    # # print counter of lens
    # print(len(min(z, key=len)), num)
    # total_complexity += num * len(min(z, key=len))
    # break
print(total_complexity)

# print(shortest_paths('A4', True))
# print(shortest_paths('A^A', False))

# total_complexity = 0
# for code in codes:
#     num = int(code[:-1])
#     p1 = shortest_paths(f'A{code}', True)
#     p1 = [x for x in p1 if len(x) <= min(map(len, p1))]
#     p2 = sum([shortest_paths(f'A{x}', False) for x in p1], [])
#     p2 = [x for x in p2 if len(x) <= min(map(len, p2))]
#     p3 = sum([shortest_paths(f'A{x}', False) for x in p2], [])
#     shortest_p3 = min(p3, key=len)
#     print(code, len(p3[0]), num)
#     total_complexity += num * len(p3[0])

# print(total_complexity)

'''
456A is wrong (66 instead of 64)
'''