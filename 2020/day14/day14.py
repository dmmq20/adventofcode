import re, fileinput

def f(s):
    if "X" not in s:
        return [s]
    return f(s.replace("X", "1", 1)) + f(s.replace("X", "0", 1))

def parse(value, mask, pt2=False):
    for i in range(len(value)):
        match mask[i]:
            case "0" | "1" if not pt2: value[i] = mask[i]
            case "1" if pt2: value[i] = "1"
            case "X" if pt2: value[i] = mask[i]
            case _: continue
    return "".join(value)

def pt1(mask, vals, M):
    addr, val = vals
    val = list(bin(val)[2:].zfill(36))
    M[addr] = int(parse(val, mask), 2)

def pt2(mask, vals, M):
    addr, val = vals
    addr = list(bin(addr)[2:].zfill(36))
    addr = parse(addr, mask, True)
    for a in f(addr):
        M[int(a, 2)] = val 

mem1, mem2 = {}, {}
mask = None
for line in fileinput.input():
    if line.startswith("mask"):
        mask = line.split()[2]
    else:
        vals = [int(n) for n in re.findall("\\[(\\d+)\\] = (\\d+)", line)[0]]
        pt1(mask, vals, mem1)
        pt2(mask, vals, mem2)

print(sum(mem1.values()))
print(sum(mem2.values()))
