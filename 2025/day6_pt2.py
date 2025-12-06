IN = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

IN = [line.replace(" ", ".") for line in IN.splitlines()]
cols = list(zip(*IN))

OPS = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}
ptr, pt2, total, op = 0, 0, None, None
while ptr < len(cols):
    k = cols[ptr]
    ptr += 1
    if all(ch == "." for ch in k):
        pt2 += total
        total = op = None
        continue
    if not op:
        op = k[-1]
    x = int("".join(ch for ch in k if ch not in [".", "+", "*"]))
    if not total:
        total = x
    else:
        total = OPS[op](total, x)
print(pt2 + total)
