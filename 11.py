from functools import cache
import sys
sys.stdin = open('input2.txt', 'r')

stones = list(map(int, input().split()))

# for _ in range(25):
#     print(_)
#     for i in range(len(stones) - 1, -1, -1):
#         if stones[i] == 0:
#             stones[i] = 1
#         elif len(str(stones[i])) % 2 == 0:
#             # split into two stones with each half of digits
#             half = len(str(stones[i])) // 2
#             s = str(stones[i])
#             stones[i] = int(s[half:])
#             stones.insert(i, int(s[:half]))
#         else:
#             stones[i] = 2024 * stones[i]
# print(len(stones))


# part 2: more optimal

@cache
def num_stones(stone, n):
    ''' for a given stone for n blinks '''
    if n == 0:
        return 1
    if stone == 0:
        return num_stones(1, n - 1)
    if len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        s = str(stone)
        return num_stones(int(s[:half]), n - 1) + num_stones(int(s[half:]), n - 1)
    return num_stones(stone * 2024, n - 1)

print(sum(num_stones(stone, 75) for stone in stones))