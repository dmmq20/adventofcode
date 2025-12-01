pt1, pt2, pos = 0, 0, 50
for line in IN.strip().splitlines():
    d, n = line[0], int(line[1:])
    dir = 1 if d == "R" else -1
    if dir == 1:
        rot = (100 - pos) % 100
    else:
        rot = pos % 100
    if rot != 0 and rot <= n:
        pt2 += 1 + (n - rot) // 100
    elif rot == 0:
        pt2 += n // 100
    pos = (pos + dir * n) % 100
    pt1 += pos == 0

print(pt1, pt2)
