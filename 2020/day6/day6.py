import fileinput

IN = "".join(fileinput.input())
data = [[set(g) for g in groups.splitlines()] for groups in IN.split("\n\n")]
pt1 = sum(len(first.union(*rest)) for first, *rest in data)
pt2 = sum(len(first.intersection(*rest)) for first, *rest in data)

print(pt1, pt2)
