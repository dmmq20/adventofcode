import heapq, fileinput
from collections import defaultdict

def min_heat_loss(grid, min_steps=0, max_steps=3):
    R, C = len(grid), len(grid[0])
    neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    distances = defaultdict(lambda: float('inf'))
    start_states = [(0, 0, 1, 0), (0, 0, 2, 0)]
    for state in start_states:
        distances[state] = 0
        
    pq = [(0, state) for state in start_states]
    heat_loss = None
    while pq:
        heat_loss, (r, c, dir, steps) = heapq.heappop(pq)

        if (r, c) == (R-1, C-1):
            return heat_loss
        
        for new_dir in range(4):
            if (new_dir + 2) % 4 == dir:
                continue
                
            if steps < min_steps and new_dir != dir and steps != 0:
                continue
                
            if new_dir == dir and steps >= max_steps:
                continue
                
            if new_dir != dir and 0 < steps < min_steps:
                continue
                
            new_steps = steps + 1 if new_dir == dir else 1
            dr, dc = neighbours[new_dir]
            new_r, new_c = r + dr, c + dc
            
            if not (0 <= new_r < R and 0 <= new_c < C):
                continue
                
            new_heat_loss = heat_loss + grid[new_r][new_c]
            new_state = (new_r, new_c, new_dir, new_steps)
            
            if new_heat_loss < distances[new_state]:
                distances[new_state] = new_heat_loss
                heapq.heappush(pq, (new_heat_loss, new_state))
    
    return heat_loss

grid = [[int(n) for n in row.strip()] for row in fileinput.input()]
pt1 = min_heat_loss(grid)
pt2 = min_heat_loss(grid, min_steps=4, max_steps=10)
print(f"Part 1: {pt1}")
print(f"Part 2: {pt2}")




