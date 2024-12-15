import sys
sys.stdin = open('input2.txt', 'r')

# total = 0
# for line in sys.stdin.read().splitlines():
#     res, vals = line.split(': ')
#     res = int(res)
#     vals = list(map(int, vals.split()))
#     # check if inserting + or * between vals will make res correct (eval l to r)
#     n = len(vals) 
#     for i in range(1 << (n - 1)):
#         curr = vals[0]
#         for j in range(1, n):
#             if i & (1 << (j - 1)):
#                 curr *= vals[j]
#             else:
#                 curr += vals[j]
#             if curr > res:
#                 break
#         if curr == res:
#             total += res
#             break

# print(total)

# part 2
total = 0
for line in sys.stdin.read().splitlines():
    print(line)
    res, vals = line.split(': ')
    res = int(res)
    vals = list(map(int, vals.split()))
    # check if inserting +, *, or || between vals will make res correct (eval l to r)
    n = len(vals)
    for i in range(3 ** (n - 1)):
        curr = vals[0]
        temp = i
        for j in range(1, n):
            op = temp % 3
            temp //= 3
            if op == 0:
                curr += vals[j]
            elif op == 1:
                curr *= vals[j]
            elif op == 2:
                curr = int(str(curr) + str(vals[j]))
            if curr > res:
                break
        if curr == res:
            total += res
            break

print(total)