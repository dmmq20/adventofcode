import re
import fileinput


def solve(data, pt2=False):
    total = 0
    can_mul = True
    for line in data:
        for i in range(len(line)):
            if pt2 and line[i:].startswith("don\'t()"):
                can_mul = False
            elif pt2 and line[i:].startswith("do()"):
                can_mul = True
            else:
                r = re.match(r'^mul\((\d+),(\d+)\)', line[i:])
                if r and can_mul:
                    a, b = (int(x) for x in r.groups())
                    total += a * b
    return total


data = [line for line in fileinput.input()]
print(solve(data))
print(solve(data, True))
