import sys
sys.stdin = open('input.txt', 'r')
from functools import cache

towels = input().split(', ')
input()
possible = 0

@cache
def check(design):
    if design == '':
        return 1
    res = 0
    for towel in towels:
        if design.startswith(towel):
            res += check(design[len(towel):])
    return res

for designs in sys.stdin.read().splitlines():
    possible += check(designs)

print(possible)