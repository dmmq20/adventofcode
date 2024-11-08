import fileinput

def solve(grid, start=(0, 0), init_dir=(0, 1)):
    
    R, C = len(grid), len(grid[0])
    Q = [(start, init_dir)]
    seen = set()
    
    while Q:
        (r, c), d = Q.pop()
        if (r, c, d) in seen or not (0 <= r < R and 0 <= c < C):
            continue
        
        seen.add((r, c, d))
        dr, dc = d
        match grid[r][c]:
            case "|" if d in {(0, 1), (0, -1)}:
                Q.append(((r+1, c), (1, 0)))
                Q.append(((r-1, c), (-1, 0)))
            case "-" if d in {(1, 0), (-1, 0)}:
                Q.append(((r, c+1), (0, 1)))
                Q.append(((r, c-1), (0, -1)))
            case "\\":
                dr, dc = dc, dr
                Q.append(((r+dr, c+dc), (dr, dc)))
            case "/":
                dr, dc = -dc, -dr
                Q.append(((r+dr, c+dc), (dr, dc)))
            case _:
                Q.append(((r+dr, c+dc), d))

    return len({(r, c) for r, c, _ in seen})

data = [row.strip() for row in fileinput.input()]
edge = len(data) - 1
pt2 = sum([[
    ((0, i), (1, 0)), 
    ((i, 0), (0, 1)), 
    ((edge, i), (0, -1)), 
    ((i, edge), (1, 0))] for i in range(len(data))], [])
    
print("Part 1: ", solve(data, (0, 0)))
print("Part 2: ", max(solve(data, *s) for s in pt2))
