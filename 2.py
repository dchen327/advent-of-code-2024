import sys
sys.stdin = open('input2.txt', 'r')

# num_safe = 0
# for line in sys.stdin.read().splitlines():
#     vals = list(map(int, line.split()))
#     # ensure adj vals diff by 1 <= and <= 3
#     if not all(1 <= abs(vals[i] - vals[i - 1]) <= 3 for i in range(1, len(vals))):
#         continue

#     num_safe += vals == sorted(vals) or vals == sorted(vals, reverse=True)

# print(num_safe)
            

# part 2
def is_safe(vals):
    if not all(1 <= abs(vals[i] - vals[i - 1]) <= 3 for i in range(1, len(vals))):
        return False
    return vals == sorted(vals) or vals == sorted(vals, reverse=True)

num_safe = 0
for line in sys.stdin.read().splitlines():
    vals = list(map(int, line.split()))
    # check if vals is safe or if removing 1 element makes it safe
    for i in range(len(vals)):
        if is_safe(vals[:i] + vals[i + 1:]):
            num_safe += 1
            break

print(num_safe)