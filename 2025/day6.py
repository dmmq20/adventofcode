import math

IN = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

IN = zip(*[line.split() for line in IN.strip().splitlines()])

pt1 = 0
for line in IN:
    *nums, op = [int(n) if n not in ["+", "*"] else n for n in line]
    pt1 += sum(nums) if op == "+" else math.prod(nums)
  
print(pt1)
