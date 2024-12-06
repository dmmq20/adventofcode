import fileinput


def solve(pos, data, pt2=False):

    d = (-1, 0)
    visited = set()
    while True:
        if (pos, d) in visited:
            return True
        visited.add((pos, d))
        r, c = pos
        dr, dc = d
        if 0 <= r+dr < R and 0 <= c+dc < C:
            if data[r+dr][c+dc] == "#":
                d = dirs[d]
            else:
                pos = (r+dr, c+dc)
        else:
            return False if pt2 else len({(r, c) for (r, c), _ in visited})


data = [list(row) for row in fileinput.input()]
R, C = len(data), len(data[0])
start = [(r, c) for r in range(R) for c in range(C) if data[r][c] == "^"][0]
dirs = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

ans = 0
for r in range(R):
    for c in range(C):
        if (r, c) != start and data[r][c] != "#":
            data[r][c] = "#"
            ans += int(solve(start, data, True))
            data[r][c] = "."


print(solve(start, data))
print(ans)
