import fileinput
from functools import cache


@cache
def solve(record, groups):
    if not groups:
        return int('#' not in record)

    if not record:
        return 0

    g, start = groups[0], record[0]
    need = '#' * g
    have = record[:g].replace("?", "#")

    if need == have:
        if len(record) == g:
            return int(len(groups) == 1)

        if start == '#':
            return 0 if record[g] == '#' else solve(record[g+1:], groups[1:])

        if start == '?' and record[g] != '#':
            return solve(record[g+1:], groups[1:]) + solve(record[1:], groups)

    return 0 if start == '#' else solve(record[1:], groups)


def parse(s, pt2=False):
    record, groups = s.split(" ")
    record = "?".join([record] * (5 if pt2 else 1))
    groups = ",".join([groups] * (5 if pt2 else 1))
    groups = tuple([int(n) for n in groups.split(",")])
    return solve(record, groups)


print(f"Part 1: {sum(parse(s) for s in fileinput.input())}")
print(f"Part 2: {sum(parse(s, True) for s in fileinput.input())}")
