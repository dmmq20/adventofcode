import fileinput
from collections import defaultdict

data = [row.strip() for row in fileinput.input()]

D = defaultdict(list)
for i, row in enumerate(data):
    for j, ch in enumerate(row):
        if ch != ".":
            D[ch].append((i, j))


def solve(pt2=False):
    pts = set()
    for value in D.values():
        for i in range(len(value)):
            for j in range(i + 1, len(value)):
                x, y = value[i]
                w, z = value[j]
                if pt2:
                    pts.add((x, y))
                    pts.add((w, z))
                dx, dy = w-x,  z-y
                while 0 <= x-dx < len(data) and 0 <= y-dy < len(data[0]):
                    pts.add((x-dx, y-dy))
                    x -= dx
                    y -= dy
                    if not pt2:
                        break
                while 0 <= w+dx < len(data) and 0 <= z+dy < len(data[0]):
                    pts.add((w+dx, z+dy))
                    w += dx
                    z += dy
                    if not pt2:
                        break
    return pts


print(len(solve()))
print(len(solve(True)))
