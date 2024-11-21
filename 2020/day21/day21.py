import re, fileinput
from collections import Counter

D = dict()
C = Counter()
for line in fileinput.input():
    ingredients, allergens = re.findall("(.*?)(?: \\((?:contains )(.+?)\\))", line)[0]
    ingredients = set(ingredients.split(" "))
    C += Counter(ingredients)
    for allergen in allergens.split(", "):
        if allergen in D:
            D[allergen] &= ingredients
        else:
            D[allergen] = ingredients.copy()
            
bad = set().union(*D.values())
pt1 = sum(v for k, v in C.items() if k not in bad)

pt2 = []
while D:
    k, v = [(k, v) for k, v in D.items() if len(v) == 1][0]
    del D[k]
    for K, V in D.items():
        D[K] = V - v
    pt2.append((k, v.pop()))
pt2.sort(key=lambda x: x[0])

print(pt1, ",".join(x[1] for x in pt2))
