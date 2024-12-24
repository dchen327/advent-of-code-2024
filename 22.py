import sys
sys.stdin = open('input2.txt', 'r')
from collections import defaultdict

nums = list(map(int, sys.stdin.read().splitlines()))

M = 16777216

# res = 0
best_seqs = defaultdict(int)  # maps 4 seqs to best prices
for num in nums:
    seq = [num % 10]
    curr = num
    for _ in range(2000):
        curr = ((curr * 64) ^ curr) % M
        curr = ((curr // 32) ^ curr) % M
        curr = ((curr * 2048) ^ curr) % M
        seq.append(curr % 10)
    diffs = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
    # res += curr

    # sliding window of 4
    seen = set()
    for i in range(len(diffs) - 3):
        tup = tuple(diffs[i:i + 4])
        if tup in seen:
            continue
        seen.add(tup)
        best_seqs[tup] += seq[i+4]

# print(res)
print(max(best_seqs.values()))