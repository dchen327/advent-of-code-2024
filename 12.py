import sys
sys.stdin = open('input2.txt', 'r')

garden = sys.stdin.read().splitlines()
garden = [list(row) for row in garden]
R, C = len(garden), len(garden[0])

def calc_cost(r, c):
    type_ = garden[r][c]
    # dfs and find connected island, mark as ., calc perimeter and area
    perim, area = 0, 0
    def dfs(r, c):
        nonlocal perim, area
        
        garden[r][c] = garden[r][c].lower()
        area += 1
        
        for r1, c1 in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= r1 < R and 0 <= c1 < C:
                if garden[r1][c1].upper() != type_:
                    perim += 1
                elif garden[r1][c1] == type_ and garden[r1][c1].isupper():
                    dfs(r1, c1)
            else:
                perim += 1

    dfs(r, c)
    return perim * area

def calc_cost2(r, c):
    ''' no perim, calc # of sides by listing all sides and merging '''
    type_ = garden[r][c]
    # dfs and find connected island, mark as ., calc perimeter and area
    sides, area = [], 0
    def dfs(r, c):
        nonlocal sides, area
        
        garden[r][c] = garden[r][c].lower()
        area += 1
        
        for r1, c1 in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if not (0 <= r1 < R and 0 <= c1 < C) or garden[r1][c1].upper() != type_:
                if (r1, c1) == (r - 1, c):
                    sides.append(((r, c), (r, c + 1), 'ED'))
                elif (r1, c1) == (r + 1, c):
                    sides.append(((r + 1, c), (r + 1, c + 1), 'EU'))
                elif (r1, c1) == (r, c - 1):
                    sides.append(((r, c), (r + 1, c), 'SR'))
                elif (r1, c1) == (r, c + 1):
                    sides.append(((r, c + 1), (r + 1, c + 1), 'SL'))
            elif garden[r1][c1] == type_ and garden[r1][c1].isupper():
                dfs(r1, c1)

    dfs(r, c)

    # merge sides while possible
    merged = True
    while merged:
        merged = False
        for i in range(len(sides)):
            for j in range(i + 1, len(sides)):
                if sides[i][2] == sides[j][2] and sides[i][1] == sides[j][0]:
                    sides[i] = (sides[i][0], sides[j][1], sides[i][2])
                    sides.pop(j)
                    merged = True
                    break
                elif sides[i][2] == sides[j][2] and sides[i][0] == sides[j][1]:
                    sides[i] = (sides[j][0], sides[i][1], sides[i][2])
                    sides.pop(j)
                    merged = True
                    break
            if merged:
                break

    return len(sides) * area

total_cost = 0
for r in range(R):
    for c in range(C):
        if garden[r][c] == garden[r][c].upper():
            total_cost += calc_cost2(r, c)

print(total_cost)

