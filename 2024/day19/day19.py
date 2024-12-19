import fileinput
from functools import lru_cache


@lru_cache
def solve(word):
    if not word:
        return 1
    return sum(solve(word[len(r):]) for r in rules if word.startswith(r))


data = "".join(line for line in fileinput.input())
rules, words = data.split("\n\n")
words = words.splitlines()
rules = rules.split(", ")
ans = [solve(w) for w in words]

print(f"Part 1: {sum(x > 0 for x in ans)}\nPart 2: {sum(ans)}")
