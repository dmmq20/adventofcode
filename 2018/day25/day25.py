import heapq, fileinput

stars = {tuple(int(n) for n in line.split(",")) for line in fileinput.input()}

def prims(stars, max_dist=None):
    pq = [(0, stars.pop())]
    seen = set()
    ans = 0
    while pq:
        dist, s = heapq.heappop(pq)
        if s in seen:
            continue
        seen.add(s)
        ans += dist
        for ns in stars:
            if ns in seen:
                continue
            dist = sum(abs(ds[0] - ds[1]) for ds in zip(s, ns))
            if not max_dist or dist < max_dist:
                heapq.heappush(pq, (dist, ns))
    stars -= seen
    return ans + len(seen)

constellations = []
while stars:
    constellations.append(prims(stars, 4))
    
print(len(constellations))
