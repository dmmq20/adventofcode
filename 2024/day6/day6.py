import fileinput


data = [list(row) for row in fileinput.input()]
R, C = len(data), len(data[0])
start = [(r, c) for r in range(R) for c in range(C) if data[r][c] == "^"][0]
dirs = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}


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
            return False if pt2 else {(r, c) for (r, c), _ in visited}


path = solve(start, data)
pt2 = 0
for r, c in path:
    data[r][c] = "#"
    pt2 += int(solve(start, data, True))
    data[r][c] = "."

print(len(path), pt2)
