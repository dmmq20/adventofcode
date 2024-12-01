import re, fileinput
from collections import defaultdict

D = defaultdict(list)
for line in fileinput.input():
    outer, *inner = re.findall("((\\d*)?\\s?(\\w+ \\w+) bag|bags)", line)
    outer = outer[2]
    for bag in inner:
        _, n, colour = bag
        n = int(n) if n else 0
        D[outer].append((n, colour))

def solve_pt1(bag):
    if bag == "shiny gold":
        return True
    return any(solve_pt1(inner_bag) for _, inner_bag in D[bag])
    
def solve_pt2(bag):
    if not D[bag]:
        return 0
    return sum((solve_pt2(inner_bag) + 1) * n for n, inner_bag in D[bag])

pt1 = sum(solve_pt1(bag) for bag in list(D.keys())) - 1
print(pt1)
print(solve_pt2("shiny gold"))
