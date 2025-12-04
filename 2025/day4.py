IN = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

IN = [list(line.strip()) for line in IN.splitlines()]
R, C = len(IN), len(IN[0])
adj = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]

def solve(pt2=False):
    pts = {(r, c) for r in range(R) for c in range(C) if IN[r][c] == "@"}
    ans, removed = 0, set()
    while True:
        pts ^= removed
        removed.clear()
        for r, c in pts:
            nbrs = sum((r+dr, c+dc) in pts for dr, dc in adj)
            if nbrs < 4:
                removed.add((r, c))
        ans += len(removed)
        if pt2 and len(removed) > 0:
            continue
        break
    return ans
    
print(solve(), solve(True))
