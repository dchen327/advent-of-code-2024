import sys
sys.stdin = open('input2.txt', 'r')
line = input()

disk_map = list(line)
expanded = []

id_ = 0
for i, d in enumerate(disk_map):
    d = int(d)
    if i % 2 == 0:  # file len
        expanded += [str(id_)] * d
        id_ += 1
    else:  # free space
        expanded += ['.'] * d 

expanded_c = expanded.copy()

# swap all ends with periods at the beginning
l = 0
for r in range(len(expanded) - 1, -1, -1):
    if expanded[r] != '.':
        while expanded[l] != '.':
            l += 1
        if l >= r:
            break
        expanded[l], expanded[r] = expanded[r], expanded[l]

# remove all periods (all at end)
expanded = expanded[:l]

print(sum(int(d) * i for i, d in enumerate(expanded)))

# part 2
expanded = []
id_ = 0
for i, d in enumerate(disk_map):
    d = int(d)
    if i % 2 == 0:  # file len
        expanded.append([str(id_)] * d)
        id_ += 1
    else:  # free space
        expanded.append(['.'] * d)

for i in range(len(expanded) - 1, -1, -1):
    if i % 1000 == 0:
        print(i)
    if not len(expanded[i]):
        continue
    for j in range(i):
        if len(expanded[j]) >= len(expanded[i]) and expanded[j][-1] == '.' and expanded[j].count('.') >= len(expanded[i]):
            # replace with expanded[i] starting at index of first period
            p_idx = expanded[j].index('.')
            expanded[j][p_idx:p_idx + len(expanded[i])] = expanded[i]
            expanded[i] = ['.'] * len(expanded[i])
            break

expanded = sum(expanded, [])
print(sum(int(d) * i for i, d in enumerate(expanded) if d != '.'))