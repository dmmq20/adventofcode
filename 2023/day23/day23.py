import fileinput

def solve(grid, init_cost, start, end, done=set()):
    R, C = len(grid), len(grid[0])
    Q = [(init_cost, start)]
    nbrs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ans = [0]
    
    while Q:
        cost, (r, c) = Q.pop()
        if (r, c) == end:
            ans.append(cost)
        if (r, c) in done:
            continue
        done.add((r, c))
        adj = list(filter(lambda x: (0 <= x[0] < R and 0 <= x[1] < C) and grid[x[0]][x[1]] != '#', [(r+dr, c+dc) for dr,dc in nbrs]))
        for (rr, cc) in adj:
            match grid[rr][cc]:
                case '>' if c < cc:
                    if len(adj) > 1:
                        ans.append(solve(grid, cost+1, (rr, cc), end, done.copy()))
                        done.add((rr, cc))
                    else:
                        Q.append((cost+1, (rr, cc)))
                case 'v' if r < rr:
                    if len(adj) > 1:
                        ans.append(solve(grid, cost+1, (rr, cc), end, done.copy()))
                    else:
                        Q.append((cost+1, (rr, cc)))
                case '.':
                    Q.append((cost+1, (rr, cc)))
                case _:
                    pass
                
    return max(ans)
    
grid = [list(row.strip()) for row in fileinput.input()]
end = (len(grid)-1, len(grid[0]) - 2)
print(solve(grid, 0, (0, 1), end))
