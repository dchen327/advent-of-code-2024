import sys
sys.stdin = open('input2.txt', 'r')
from collections import deque, defaultdict

vals = {}
while True:
    i = input()
    if i == '':
        break
    wire, val = i.split(': ')
    vals[wire] = int(val)

gate_map = {
    'AND': '&',
    'OR': '|',
    'XOR': '^',
}

part_to_rule = defaultdict(list)
for line in sys.stdin.read().splitlines():
    left, right = line.split(' -> ')
    a, x, b = left.split()
    part_to_rule[a].append((a, b, gate_map[x], right))
    part_to_rule[b].append((a, b, gate_map[x], right))

q = deque()
for wire, val in vals.items():
    for rule in part_to_rule[wire]:
        q.append(rule)

while q:
    rule = q.popleft()
    a, b, x, right = rule
    if a in vals and b in vals:
        vals[right] = eval(f'{vals[a]} {x} {vals[b]}')
        for rule in part_to_rule[right]:
            q.append(rule)
    else:
        q.append(rule)

res = 0
for wire, val in vals.items():
    if wire[0] == 'z':
        res |= val << int(wire[1:])
# print(res)