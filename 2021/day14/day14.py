import fileinput
from collections import Counter

s, rules = "".join(fileinput.input()).split("\n\n")
rules = {k: v for line in rules.splitlines() for k, v in [line.split(" -> ")]}

def solve(rounds, s=s, rules=rules):
    pairs = Counter(["".join(t) for t in zip(s, s[1:])])
    counts = Counter(s)
    for _ in range(rounds):
        tmp = Counter()
        for k, v in pairs.items():
            ch = rules[k]
            counts[ch] += v
            tmp[k[0] + ch] += v
            tmp[ch + k[1]] += v
        pairs = tmp

    ans = counts.values()
    return max(ans) - min(ans)

print(solve(10))
print(solve(40))
