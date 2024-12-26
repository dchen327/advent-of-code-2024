import sys
from collections import defaultdict

def bron_kerbosch_pivot(graph, r, p, x, max_clique):
    if len(p) == 0 and len(x) == 0:
        if len(r) > max_clique[0]:
            max_clique[0] = len(r)
            max_clique[1] = r
        return
    
    pivot = max(p.union(x), key=lambda u: len(p.intersection(graph[u])), default=None)
    
    for v in p.difference(graph[pivot] if pivot else set()):
        new_r = r.union({v})
        new_p = p.intersection(graph[v])
        new_x = x.intersection(graph[v])
        bron_kerbosch_pivot(graph, new_r, new_p, new_x, max_clique)
        p = p.difference({v})
        x = x.union({v})

# Read input and build graph
graph = defaultdict(set)
with open('input2.txt') as f:
    for line in f:
        a, b = line.strip().split('-')
        graph[a].add(b)
        graph[b].add(a)

# Find max clique
max_clique = [0, None]  # Using list to modify value in recursive calls
vertices = set(graph.keys())
bron_kerbosch_pivot(graph, set(), vertices, set(), max_clique)
print(','.join(sorted(max_clique[1])))