import heapq, fileinput
from collections import defaultdict

def extend_grid(grid):
    extended_grid = []
    for j in range(5):
        for row in grid:
            new_row = []
            for i in range(5):
                new_row += [(x + i + j - 1) % 9 + 1 for x in row]
            extended_grid.append(new_row)
    return extended_grid

def solve(grid, start=(0, 0)):
    
    R, C = len(grid), len(grid[0])
    distances = defaultdict(lambda: None)
    pq = [(0, (0, 0), start)]
    neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while pq:
        cost, last_dir, (r, c) = heapq.heappop(pq)
        for dr, dc in neighbours:
            if (dr, dc) == tuple(x * -1 for x in last_dir):
                continue
            
            new_r, new_c = r+dr, c+dc
            if not (0 <= new_r < R and 0 <= new_c < C):
                continue
            
            new_cost = cost + grid[new_r][new_c]
            old_cost = distances[(new_r, new_c)]
            if not old_cost or old_cost > new_cost:
                distances[(new_r, new_c)] = new_cost
                heapq.heappush(pq, (new_cost, (dr, dc), (new_r, new_c)))
                
    return distances[(R-1, C-1)]

grid = [[int(n) for n in list(row.strip())] for row in fileinput.input()]

print(solve(grid))
print(solve(extend_grid(grid)))
