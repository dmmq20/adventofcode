import re, heapq

IN = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''

def solve(line):
    lights, *btns, _ = line.split(" ")
    lights = lights[1:-1]
    goal = set(i for i in range(len(lights)) if lights[i] == "#")
    btns = [frozenset({int(n) for n in re.findall('\\d+', btn)}) for btn in btns]
    
    Q = [(0, frozenset())]
    heapq.heapify(Q)
    explored = dict()
    while Q:
        curr_cost, curr_set = heapq.heappop(Q)
        if curr_set == goal:
            return curr_cost
        if curr_set in explored and explored[curr_set] <= curr_cost:
            continue
        explored[curr_set] = curr_cost
        for btn in btns:
            new_set = frozenset(curr_set ^ btn)
            heapq.heappush(Q, (curr_cost+1, new_set))
    return None

print(sum(solve(line) for line in IN.splitlines()))
