import fileinput


def dfs(start, pt2=False):

    Q = [(start, start)]
    seen = set()
    ans = 0
    while Q:
        (r, c), prev = Q.pop()
        if not pt2 and (r, c) in seen:
            continue
        seen.add((r, c))
        if trails[(r, c)] == 9:
            ans += 1
            continue

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rr, cc = r+dr, c+dc
            if (rr, cc) not in trails or (rr, cc) == prev:
                continue
            if trails[(rr, cc)] - trails[(r, c)] != 1:
                continue
            Q.append(((rr, cc), (r, c)))

    return ans


data = [line.strip() for line in fileinput.input()]
R, C = len(data), len(data[0])
trails = {(r, c): int(data[r][c]) for r in range(R)
          for c in range(C) if data[r][c] != "."}
trailheads = [k for k, v in trails.items() if v == 0]

print(sum(dfs(s) for s in trailheads))
print(sum(dfs(s, True) for s in trailheads))
