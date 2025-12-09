IN = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

tiles = [tuple(int(n) for n in line.split(",")) for line in IN.splitlines()]
pt1 = 0
for i, (x1, y1) in enumerate(tiles):
    for (x2, y2) in tiles[i+1:]:
        pt1 = max(pt1, (abs(x2-x1) + 1) * (abs(y2-y1) + 1))
        
print(pt1)
