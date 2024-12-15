import sys
import re
sys.stdin = open('input2.txt', 'r')

# grab all lines and put into one string
s = sys.stdin.read()
s1 = s

# match "mul(x,y)" with regex, multiply x and y
pattern = r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)'

sum_ = 0
for match in re.finditer(pattern, s):
    sum_ += int(match.group(1)) * int(match.group(2))


print(sum_)

# part 2
s = s1

# remove anything between a don't() and a do()
do_idx = len(s) - 1
for i in range(len(s) - 1, -1, -1):
    if s[i:i+4] == 'do()':
        do_idx = i
    elif do_idx is not None and s[i:i+7] == 'don\'t()':
        s = s[:i] + s[do_idx+4:]
        do_idx = None


pattern = r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)'
sum_ = 0
for match in re.finditer(pattern, s):
    sum_ += int(match.group(1)) * int(match.group(2))
print(sum_)




# not 139389154