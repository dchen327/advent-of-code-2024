import sys
sys.stdin = open('input2.txt', 'r')
from math import gcd, ceil
from sympy import symbols, Eq, solve


# # split stdin.readlines() by blank line
data = sys.stdin.read().split('\n\n')

# token_count = 0

# for machine in data:
#     lines = machine.splitlines()
#     coords = []
#     for i, line in enumerate(lines):
#         x, y = map(int, line.replace('X', '').replace('Y', '').replace('+', '').replace('=', '').split(': ')[1].split(', '))
#         coords.append((x, y))
#     ax, ay = coords[0]
#     bx, by = coords[1]
#     px, py = coords[2]

#     # check if soln exists (diophantine)
#     if (px % gcd(ax, bx) != 0) or (py % gcd(ay, by) != 0):
#         continue

#     min_tokens = float('inf')
#     # iterate through all solutions and find cheapest
    
    
#     token_count += min_tokens if min_tokens != float('inf') else 0

# print(token_count)

def extended_gcd(a, b):
    """
    Extended Euclidean algorithm to find GCD and Bézout's identity coefficients.
    Returns (gcd, x, y) where gcd = ax + by
    """
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

def solve_diophantine(ax, ay, bx, by, px, py):
    """
    Solve the Diophantine equation:
    a*ax + b*bx = px
    a*ay + b*by = py
    
    Returns the cheapest solution (lowest 3*a + b)
    """
    # First, check if a solution exists
    gcd_x = gcd(ax, bx)
    gcd_y = gcd(ay, by)
    
    if (px % gcd_x != 0) or (py % gcd_y != 0):
        return None
        
    # Solve for x first
    _, x1, y1 = extended_gcd(ax, bx)
    # we have ax * x + bx * y = gcd_ax_bx
    x1, y1 = x1 * (px // gcd_x), y1 * (px // gcd_x)
    u1, v1 = ax // gcd_x, bx // gcd_x
    # all solns are of the form (x + kv, y - ku)
    # Solve for y
    _, x2, y2 = extended_gcd(ay, by)
    # we have ay * x + by * y = gcd_ay_by
    x2, y2 = x2 * (py // gcd_y), y2 * (py // gcd_y)
    u2, v2 = ay // gcd_y, by // gcd_y
    # all solns are of the form (x + kv, y - ku)


    # print(f'{x1} + {v1}k1, {y1} - {u1}k1')
    # print(f'{x2} + {v2}k2, {y2} - {u2}k2')
    # # print out eqn:
    # print(f'{ax} * {x1} + {bx} * {y1} = {px}')
    # print(f'{ay} * {x2} + {by} * {y2} = {py}')
    # print('-' * 50)

    k1, k2 = symbols('k1 k2', integer=True)
    eq1 = Eq(x1 + k1 * v1, x2 + k2 * v2)
    eq2 = Eq(y1 - k1 * u1, y2 - k2 * u2)

    sol = solve((eq1, eq2), (k1, k2))
    if sol:
        a, b = x1 + sol[k1] * v1, y1 - sol[k1] * u1
        print(a, b)
        min_tokens = 3*a + b
        return min_tokens
    return 0

def solve_machines(data):
    token_count = 0
    
    for machine in data:
        lines = machine.splitlines()
        coords = []
        for i, line in enumerate(lines):
            x, y = map(int, line.replace('X', '').replace('Y', '').replace('+', '').replace('=', '').split(': ')[1].split(', '))
            coords.append((x, y))
        ax, ay = coords[0]
        bx, by = coords[1]
        px, py = coords[2]
        px, py = (px + 10000000000000, py + 10000000000000)
        
        # Solve and add to token count
        solution = solve_diophantine(ax, ay, bx, by, px, py)
        if solution:
            min_tokens = solution
            token_count += min_tokens
    
    return token_count

print(solve_machines(data))