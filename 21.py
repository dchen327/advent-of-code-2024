import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
from itertools import product

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

def shortest_paths(s):
    ''' s is a string of digits '''
    if len(s) < 2:
        return ['']
    sr, sc = numpad_to_rc[s[0]]
    er, ec = numpad_to_rc[s[1]]
    target_dist = abs(sr - er) + abs(sc - ec)

    R, C = 4, 3
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_to_symbol = {0: '>', 1: 'v', 2: '<', 3: '^'}

    # generate all symbol paths from s to e, can't go through ''
    paths = []
    # (r, c, dist, path)
    queue = deque([(sr, sc, 0, '')])
    while queue:
        r, c, dist, path = queue.popleft()
        if (r, c) == (er, ec) and dist == target_dist:
            paths.append(path + 'A')
            continue
    
        for dir_idx, (dr, dc) in enumerate(dirs):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and numpad[nr][nc] != '':
                if dist < target_dist:
                    queue.append((nr, nc, dist + 1, path + dir_to_symbol[dir_idx]))
    
    # take product with paths of s[1:]
    next_paths = shortest_paths(s[1:])
    return [p1 + p2 for p1, p2 in product(paths, next_paths)]

def shortest_paths(s, pad, pad_to_rc):
    ''' s is a string of digits '''
    if len(s) < 2:
        return ['']
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
        if (r, c) == (er, ec) and dist == target_dist:
            paths.append(path + 'A')
            continue
    
        for dir_idx, (dr, dc) in enumerate(dirs):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and numpad[nr][nc] != '':
                if dist < target_dist:
                    queue.append((nr, nc, dist + 1, path + dir_to_symbol[dir_idx]))
    
    # take product with paths of s[1:]
    next_paths = shortest_paths(s[1:], pad, pad_to_rc)
    return [p1 + p2 for p1, p2 in product(paths, next_paths)]

total_complexity = 0
for code in codes:
    num = int(code[:-1])
    p1 = shortest_paths(f'A{code}', numpad, numpad_to_rc)
    shortest_p1 = min(p1, key=len)
    p2 = shortest_paths(f'A{shortest_p1}', dpad, dpad_to_rc)
    shortest_p2 = min(p2, key=len)
    p3 = shortest_paths(f'A{shortest_p2}', dpad, dpad_to_rc)
    shortest_p3 = min(p3, key=len)
    print(code, len(p3[0]), num)
    total_complexity += num * len(p3[0])

print(total_complexity)