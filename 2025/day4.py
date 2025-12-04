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

def solve(pt2=False):
    adj = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]
    ans, changed = 0, True
    while changed:
        changed = False
        for r in range(len(IN)):
            for c in range(len(IN[0])):
                if IN[r][c] != "@":
                    continue
                cnt = 0
                for dr, dc in adj:
                    if dr+r < 0 or dc+c < 0:
                        continue
                    if dr+r >= len(IN) or dc+c >= len(IN[0]):
                        continue
                    cnt += IN[r+dr][c+dc] == "@"
                ans += cnt < 4
                if pt2 and cnt < 4:
                    IN[r][c] = "."
                    changed = True and pt2
    
    return ans
    
print(solve(), solve(True))
