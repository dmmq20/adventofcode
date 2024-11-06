import re, fileinput
from collections import defaultdict

top, bottom = "".join(fileinput.input()).strip().split("\n\n")

OPS = {">": lambda x, y: x > y, "<": lambda x, y: x < y}

workflows = defaultdict(list)
for line in top.splitlines():
    k, rest = line.split("{")
    *rules, default = rest[:-1].split(",")
    rs = []
    for rule in rules:
        cond, dest = rule.split(":")
        var, op, n = re.match("(.+)(>|<)(\\d+)", cond).groups()
        workflows[k].append((var, op, int(n), dest))
    workflows[k].append(default)

parts = [part[1:-1].split(",") for part in bottom.splitlines()]
parts = [{k: int(v) for k, v in (p.split("=") for p in part)} for part in parts]

def pt1(part, rule, workflows):
    if rule in ['A', 'R']:
        return rule == 'A'
        
    *rules, default = workflows[rule]
    for var, op, n, dest in rules:
        if var in part:
            k = part[var]
            if OPS[op](k, n):
                return pt1(part, dest, workflows)
                
    return pt1(part, default, workflows)

accepted = list(filter(lambda x: pt1(x, "in", workflows), parts))
print(sum(sum(part.values()) for part in accepted))
