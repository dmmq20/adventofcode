import fileinput
from collections import defaultdict

ans = defaultdict(int)
def solve(containers, eggnog, used=0):
    
    if (not containers and eggnog) or eggnog < 0:
        return 0
        
    if eggnog == 0:
        ans[used] += 1
        return 1

    return solve(containers[1:], eggnog-containers[0], used+1) + solve(containers[1:], eggnog, used)

data = [int(n) for n in fileinput.input()]
print(solve(tuple(data), 150))
print(ans[min(ans.keys())])
