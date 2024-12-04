import fileinput
from collections import defaultdict

data = [line for line in fileinput.input()]
R, C = len(data), len(data[0])
D = defaultdict(str) | {(r, c): data[r][c] for r in range(R) for c in range(C)}


def search(pos, _dir, word, D=D):
    (r, c), (dr, dc) = pos, _dir
    letters = [D[(r+dr*i, c+dc*i)] for i in range(len(word))]
    return "".join(letters) in [word, word[::-1]]


xs = [(r, c) for r in range(R) for c in range(C) if data[r][c] == "X"]
ys = [(r, c) for r in range(R) for c in range(C) if data[r][c] == "A"]

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
        (0, 1), (1, -1), (1, 0), (1, 1)]

pt1 = sum(search(x, d, "XMAS") for x in xs for d in dirs)
pt2 = sum(all(search((r-dr, c-dc), (dr, dc), "MAS")
              for dr, dc in [(1, 1), (1, -1)]) for r, c in ys)

print(pt1, pt2)
