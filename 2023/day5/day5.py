import re, fileinput


data = "".join(fileinput.input())
seeds, *maps = data.strip().split("\n\n")
seeds = [int(n) for n in re.findall("\\d+", seeds)]
maps = [
    [list(map(int, line.split())) for line in part.splitlines()[1:]] 
    for part in maps
]

def solve(maps, seeds):
    for m in maps:
        new_seeds = []
        while seeds:
            start, end = seeds.pop()
            for dst, src, n in m:
                lower = max(start, src)
                upper = min(end, src + n)
                if lower < upper:
                    new_seeds.append((lower - src + dst, upper - src + dst))
                    if lower > start:
                        seeds.append((start, lower))
                    if end > upper:
                        seeds.append((upper, end))
                    break
            else:
                new_seeds.append((start, end))
        seeds = new_seeds
    return min(seeds)[0]

pt1 = [(seeds[i], seeds[i] + 1) for i in range(len(seeds))]
print(solve(maps, pt1))
pt2 = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
print(solve(maps, pt2))
