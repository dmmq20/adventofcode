IN = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

ranges, ids = IN.split("\n\n")
ranges = [tuple(map(int, line.split("-"))) for line in ranges.splitlines()]
ids = [int(n) for n in ids.splitlines()]
ranges.sort()

merged = [ranges[0]]
for a, b in ranges[1:]:
    da, db = merged[-1]
    if a <= db:
        merged[-1] = (da, max(db, b))
    else:
        merged.append((a, b))

pt1 = sum(any(a <= id <= b for a, b in ranges) for id in ids)
pt2 = sum(b - a + 1 for a, b in merged)
print(pt1, pt2)
