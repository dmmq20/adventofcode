import re, fileinput

IN = "".join(fileinput.input())
fields, mine, others = IN.split("\n\n")
mine = [int(n) for n in mine.splitlines()[1].split(",")]
F = {}
for line in fields.splitlines():
    f, a, b, c, d = re.findall("(\\w+ ?\\w+?): (\\d+)-(\\d+) or (\\d+)-(\\d+)", line)[0]
    F[f] = [int(a), int(b), int(c), int(d)]

pt1, valid = 0, []
for line in others.splitlines()[1:]:
    line = [int(n) for n in line.split(",")]
    is_valid = True
    for k in line:
        if not any(a <= k <= b or c <= k <= d for a, b, c, d in F.values()):
            pt1 += k
            is_valid = False
    if is_valid:
        valid.append(line)

pt2 = 1
while F:
    for i in range(len(valid[0])):
        possible = set()
        for k, (a, b, c, d) in F.items():
            if all(a <= valid[j][i] <= b or c <= valid[j][i] <= d for j in range(len(valid))):
                possible.add(k)
        if len(possible) == 1:
            f = possible.pop()
            if f.startswith("departure"):
                pt2 *= mine[i]
            del F[f]
            
print(pt1, pt2)
