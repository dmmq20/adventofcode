import fileinput

nums = [[int(n) for n in row.split()] for row in fileinput.input()]
nums = [sorted(nums) for nums in zip(*nums)]
pt1 = sum([abs(a-b) for a, b in zip(*nums)])
pt2 = sum([nums[1].count(n) * n for n in nums[0]])

print(pt1, pt2)
