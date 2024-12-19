import fileinput
from functools import lru_cache


@lru_cache(None)
def solve(n, rounds=25):
    if rounds == 0:
        return 1
    elif n == 0:
        return solve(1, rounds-1)
    elif len(str(n)) % 2 == 0:
        n = str(n)
        a, b = n[:len(n)//2], n[len(n)//2:]
        return solve(int(a), rounds-1) + solve(int(b), rounds-1)
    else:
        return solve(n*2024, rounds-1)


nums = [int(n) for n in "".join(line for line in fileinput.input()).split()]
print(sum(solve(n) for n in nums))
print(sum(solve(n, 75) for n in nums))
