import fileinput
from collections import defaultdict

G = defaultdict(list)
for line in fileinput.input():
    src, _, dst, _, k = line.split()
    G[src].append((dst, int(k)))
    G[dst].append((src, int(k)))

def solve(src, seen, depth=3, pt2=False):
    
    if len(seen) == depth:
        return 0
    
    total = -1 if pt2 else float('inf')
    for dst, cost in G[src]:
        if dst in seen:
            continue
        seen.add(dst)
        fn = max if pt2 else min
        total = fn(total, solve(dst, seen, depth, pt2) + cost)
        seen.remove(dst)
        
    return total
    
cities = G.keys()
print(min([solve(city, {city}, len(cities)) for city in cities]))
print(max([solve(city, {city}, len(cities), True) for city in cities]))
