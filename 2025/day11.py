import re, functools

IN = '''svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out'''

@functools.cache
def solve(node, pt2=False, fft=False, dac=False):
    if node == "out":
        return fft and dac if pt2 else 1
    return sum(solve(child, pt2, child=="fft" or fft, child=="dac" or dac) for child in D[node])

IN = [re.findall('\\w+', line) for line in IN.splitlines()]
D = {parent: children for parent, *children in IN}
# print(solve(IN, "you")) -> pt1 has different sample input
print(solve("svr", True))
