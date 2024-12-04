import fileinput


def check_ws(coords, word, data):
    if all(0 <= dr < len(data) and 0 <= dc < len(data[0]) for dr, dc in coords):
        found = "".join(data[dr][dc] for dr, dc in coords)
        return found in [word, word[::-1]]
    return False


def solve1(data):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)]
    xs = [
        [(r + dr * i, c + dc * i) for i in range(4)]
        for r in range(len(data))
        for c in range(len(data[0]))
        for dr, dc in dirs
        if data[r][c] == "X"
    ]

    return sum(check_ws(coords, "XMAS", data) for coords in xs)


def solve2(data):
    xs = [
        [((r-1, c-1), (r, c), (r+1, c+1)),
         ((r-1, c+1), (r, c), (r+1, c-1))]
        for r in range(len(data))
        for c in range(len(data[0]))
        if data[r][c] == "A"
    ]

    return sum(
        all(check_ws(c, "MAS", data) for c in coords) for coords in xs
    )


data = [row for row in fileinput.input()]
print(solve1(data), solve2(data))
