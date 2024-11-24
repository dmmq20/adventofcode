import fileinput
from collections import deque

maze = [list(row.strip()) for row in fileinput.input()]
R, C = len(maze), len(maze[0])
start = (0, maze[0].index("."))
end = (R - 1, maze[-1].index("."))
poi = {start, end}

dirs = {
    "^": [(-1, 0)],
    "v": [(1, 0)],
    ">": [(0, 1)],
    "<": [(0, -1)],
    ".": [(0, 1), (0, -1), (1, 0), (-1, 0)]
}

for r in range(R):
    for c in range(C):
        if maze[r][c] == "#": continue
        nbrs = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = dr+r, dc+c
            if 0<=rr<R and 0<=cc<C and maze[rr][cc] != "#":
                nbrs += 1
        if nbrs > 2:
            poi.add((r, c))

def bfs(start, poi, pt2=False):

    dists = dict()
    Q = deque([(0, start)])
    seen = set()
    nbrs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while Q:
        dist, (r, c) = Q.popleft()
        if ((r, c)) in seen:
            continue
        seen.add((r, c))

        if (r, c) in poi and (r, c) != start:
            dists[(r, c)] = dist
            continue

        d = nbrs if pt2 else dirs[maze[r][c]]
        for dr, dc in d:
            rr, cc = dr+r, dc+c
            if 0<=rr<R and 0<=cc<C and maze[rr][cc] != "#":
                Q.append((dist + 1, (rr, cc)))

    return dists

def solve(start, pt2=False):
    G = {(r, c): bfs((r, c), poi, pt2) for r,c in poi - {end}}
    def dfs(start, path):
        if start == end:
            return 0
        ans = -float('inf')
        for pos, dist in G[start].items():
            if pos not in path:
                path.add(start)
                ans = max(ans, dist + dfs(pos, path))
                path.remove(start)
        return ans
    return dfs(start, set())

print(solve(start))
print(solve(start, True))
