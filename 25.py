import sys
sys.stdin = open('input2.txt', 'r')

chunks = sys.stdin.read().split('\n\n')
locks, keys = [], []

for chunk in chunks:
    if chunk.startswith('#####'):
        # convert to array of 5 nums where each num is how many # is in that column
        counts = [-1] * 5
        for line in chunk.splitlines():
            for i, c in enumerate(line):
                if c == '#':
                    counts[i] += 1
        locks.append(counts)
    else:
        counts = [-1] * 5
        for line in chunk.splitlines():
            for i, c in enumerate(line):
                if c == '#':
                    counts[i] += 1
        keys.append(counts)

num_no_overlap = 0
for key in keys:
    for lock in locks:
        if all(k + l <= 5 for k, l in zip(key, lock)):
            num_no_overlap += 1
    
print(num_no_overlap)