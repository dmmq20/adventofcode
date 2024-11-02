from functools import cache
from collections import Counter

f = open("day10.in").read()
data = [0] + [int(x) for x in f.splitlines()]
data.append(max(data) + 3)
data.sort()
ans = Counter(data[i+1] - data[i] for i in range(len(data)-1))

@cache
def solve_recursive(arr, adapter):
    
    if len(arr) == 1:
        return 1
    
    return sum(solve_recursive(arr[i+1:], arr[i]) if arr[i] - adapter <= 3 else 0 
                    for i in range(min(len(arr), 3)))
        
    # return statement equiv of below:
    # total = 0
    # for i in range(len(arr)):
    #     if arr[i] - adapter > 3:
    #         break
    #     total += solve(arr[i+1:], arr[i])
    # return total

def solve_dp(data):
    ans = [0] * (max(data)+1)
    ans[0] = 1

    for i, a1 in enumerate(data):
        a1 = data[i]
        for a2 in data[i+1:]:
            if a2 - a1 > 3:
                break
            ans[a2] += ans[a1]

    return ans[-1]

print(ans[1] * ans[3])
print(solve_recursive(tuple(data[1:]), data[0]))
