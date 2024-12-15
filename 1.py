import sys
sys.stdin = open('input2.txt', 'r')

left, right = [], []
for line in sys.stdin.read().splitlines():
    l, r = map(int, line.split())
    left.append(l)
    right.append(r)

left.sort()
right.sort()

print(sum(abs(l - r) for l, r in zip(left, right)))

from collections import Counter
left_counts, right_counts = Counter(left), Counter(right)
total = 0
for x in left_counts:
    total += x * left_counts[x] * right_counts[x]

print(total)