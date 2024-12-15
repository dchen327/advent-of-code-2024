import sys
from collections import defaultdict, deque
sys.stdin = open('input2.txt', 'r')

# rules = []
# while True:
#     i = input()
#     if '|' not in i:
#         break
#     rules.append(i.split('|'))

# updates = [line.split(',') for line in sys.stdin.read().splitlines()]

# sum_middles = 0  # sum of middles of correct
# for update in updates:
#     for a, b in rules:
#         if a in update and b in update:
#             if len(update) - 1 - update[::-1].index(a) > update.index(b):
#                 break
#     else:
#         sum_middles += int(update[len(update) // 2])

# print(sum_middles)


# part 2 topo sort
def topo_sort(rules, vals):
    sorted_vals = [] 

    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for a, b in rules:
        if a in vals and b in vals:
            graph[a].append(b)
            in_degree[b] += 1
    
    sources = deque() 
    for val in vals:
        if in_degree[val] == 0:
            sources.append(val)
    
    while sources:
        val = sources.popleft()
        sorted_vals.append(val)
        # decrement child nodes
        for child in graph[val]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    
    return sorted_vals

rules = []
while True:
    i = input()
    if '|' not in i:
        break
    rules.append(i.split('|'))

updates = [line.split(',') for line in sys.stdin.read().splitlines()]

sum_middles = 0  # sum of middles of correct
for update in updates:
    for a, b in rules:
        if a in update and b in update:
            if len(update) - 1 - update[::-1].index(a) > update.index(b):
                # incorrect, topo sort
                sorted_update = topo_sort(rules, update)
                sum_middles += int(sorted_update[len(sorted_update) // 2])
                break

print(sum_middles)