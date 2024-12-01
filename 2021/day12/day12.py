import fileinput
from collections import defaultdict

D = defaultdict(list)
for line in fileinput.input():
    src, dst = line.strip().split("-")
    D[src].append(dst)
    D[dst].append(src)

def solve(src, path, visit_twice=False):
    if src == "end":
        return 1
    path.add(src)
    total = 0
    for dst in D[src]:
        if dst.isupper():
            total += solve(dst, path, visit_twice)
        elif dst not in path:
            total += solve(dst, path.copy(), visit_twice)
        else:
            if visit_twice and dst != "start":
                total += solve(dst, path.copy(), False)
    return total
    
print(solve("start", set()))
print(solve("start", set(), True))
