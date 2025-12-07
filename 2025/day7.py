from functools import cache

IN = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''

IN = [list(line) for line in IN.splitlines()]
S = [(r, c) for r in range(len(IN)) for c in range(len(IN[0])) if IN[r][c] == "S"][0]

def dfs(start):
    dfs, seen, splits = [start], set(), 0
    while dfs:
        r, c = dfs.pop()
        if (r, c) in seen or not (0<=r<len(IN) and 0<=c<len(IN)):
            continue
        seen.add((r, c))
        if IN[r][c] == "^":
            splits += 1
            dfs.append((r+1, c-1))
            dfs.append((r+1, c+1))
        else:
            dfs.append((r+1, c))
    return splits

@cache
def solve(row, col):
    if row == len(IN) and 0<=col<len(IN):
        return 1
    if not (0<=row<len(IN) and 0<=col<len(IN)):
        return 0
    if IN[row][col] == "^":
        return solve(row+1, col-1) + solve(row+1, col+1)
    else:
        return solve(row+1, col)

pt1, pt2 = dfs(S), solve(S[0], S[1])
print(pt1, pt2)
