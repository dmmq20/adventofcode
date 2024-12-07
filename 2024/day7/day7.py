import fileinput


def solve(target, k, nums, pt2=False):

    if not nums:
        return int(target) == int(k)
    n, *nums = nums
    add = solve(target, int(k) + n, nums, pt2)
    times = solve(target, int(k) * n, nums, pt2)
    cat = pt2 and solve(target, str(k) + str(n), nums, pt2)

    return add or times or cat


data = [
    (int(t), [int(n) for n in nums.split()])
    for line in fileinput.input()
    for t, nums in [line.split(":")]
]

print(sum(t for t, [n, *nums] in data if solve(t, n, nums)))
print(sum(t for t, [n, *nums] in data if solve(t, n, nums, True)))
