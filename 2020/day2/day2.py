import re, fileinput

pt1 = pt2 = 0
for line in fileinput.input():
    a, b, ch, pw = re.findall("(\\d+)-(\\d+) (\\w+): (\\w+)", line)[0]
    a, b = int(a), int(b)
    pt1 += a <= pw.count(ch) <= b
    pt2 += (pw[a-1] == ch) ^ (pw[b-1] == ch)
print(pt1, pt2)
