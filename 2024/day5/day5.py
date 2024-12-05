import fileinput
from collections import defaultdict
from functools import cmp_to_key


def parse():

    data = "".join(fileinput.input())
    rules, updates = data.strip().split("\n\n")
    updates = [[int(n) for n in line.split(",")]
               for line in updates.splitlines()]

    D = defaultdict(list)
    for rule in rules.splitlines():
        x, y = rule.split("|")
        D[int(x)].append(int(y))

    return D, updates


def solve(rules, updates):

    def sort(x, y):
        if y in rules[x]:
            return 1
        return -1

    pt1 = pt2 = 0
    for update in updates:
        correct = sorted(update, key=cmp_to_key(sort), reverse=True)
        if update == correct:
            pt1 += update[len(update)//2]
        else:
            pt2 += correct[len(correct)//2]

    return pt1, pt2


print(solve(*parse()))
