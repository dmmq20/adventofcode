import fileinput

def solve(s, pt2=False):
    ans = ptr = 0
    while ptr < len(s):
        if s[ptr] == "(":
            marker, s = s[ptr+1:].split(")", 1)
            a, b = [int(n) for n in marker.split("x")]
            ptr = a
            ans += solve(s[:ptr], pt2) * b if pt2 else a * b
        else:
            ans += 1
            ptr += 1
    
    return ans

#recursive with no loops
def solve2(seq, pt2=False):
    if ")" not in seq:
        return len(seq)
        
    lhs, rhs = seq.split("(", 1)
    marker, rhs = rhs.split(")", 1)
    a, b = [int(n) for n in marker.split("x")]
    
    return len(lhs) + solve2(rhs[a:], pt2) + solve2(rhs[:a], pt2) * b if pt2 else a * b

s = next(fileinput.input()).strip()
print(solve(s, True))
