import fileinput

def smudge(r1, r2):
    return sum(a != b for a, b in zip(r1, r2))

def find_reflection(mirror, pt2):
    for i in range(1, len(mirror)):
        if sum(smudge(r1, r2) for r1, r2 in zip(reversed(mirror[:i]), mirror[i:])) == int(pt2):
            return i
    return 0

def solve(mirror, pt2=False):
    if x := find_reflection(mirror, pt2):
        return x * 100
    return find_reflection(list(zip(*mirror)), pt2)

mirrors = "".join(fileinput.input()).strip().split("\n\n")
mirrors = [[list(row) for row in m.splitlines()] for m in mirrors]

print(sum(solve(mirror) for mirror in mirrors))
print(sum(solve(mirror, True) for mirror in mirrors))
