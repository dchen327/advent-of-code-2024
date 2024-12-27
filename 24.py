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

# dict to map from right side to parts
get_parts = {}

part_to_rule = defaultdict(list)
for line in sys.stdin.read().splitlines():
    left, right = line.split(' -> ')
    a, x, b = left.split()
    part_to_rule[a].append((a, b, gate_map[x], right))
    part_to_rule[b].append((a, b, gate_map[x], right))
    if right in get_parts:
        print("should not get here")
    get_parts[right] = (a, x, b)

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

x, y, z = 0, 0, 0
for wire, val in vals.items():
    if wire[0] == 'x':
        x |= val << int(wire[1:])
    elif wire[0] == 'y':
        y |= val << int(wire[1:])
    if wire[0] == 'z':
        z |= val << int(wire[1:])

# print(bin(x)[2:].zfill(46))
# print(bin(y)[2:].zfill(46))
# print(bin(z)[2:].zfill(46))
carries = {}
for i in range(1, 45):
    z = f'z{str(i).zfill(2)}'
    parts = get_parts[z]
    a, x, b = parts
    # check if either a or b is made with an OR
    try:
        carry = None
        if get_parts[a][1] == 'OR':
            carry = a
        if get_parts[b][1] == 'OR':
            carry = b
        # print(z, carry)
        if carry is not None:
            carries[carry] = str(i - 1)
    except KeyError:
        print("KEY ERROR", z)
        pass
# print(carries)
carries['qvs'] = '23'

# recursively calc expression for z in terms of x and y
def calc(part):
    if part[0] in 'xy':
        return part
    if part in carries:
        return f'c{carries[part].zfill(2)}'
    a, x, b = get_parts[part]
    a = calc(a)
    b = calc(b)
    return f'({a} {gate_map[x]} {b})'



print('*', calc('mjb'))
print('*', calc('bbc'))

for i in range(1, 45):
    z = f'z{str(i).zfill(2)}'
    print(z, calc(z))
    
wrong = 'z11,vkq,z24,mmk,qdq,pvb,z38,hqh'
print(','.join(sorted(wrong.split(','))))
    



'''
wrong: 
z11 + vkq
z24 + mmk
qdq + pvb
z38 + hqh
qvs (c23)
sbs (c10)

vsb AND c37 -> z38 should be XOR
c37 XOR vsb -> hqh

'''