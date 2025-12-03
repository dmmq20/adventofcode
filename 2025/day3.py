IN = '''987654321111111
811111111111119
234234234234278
818181911112111'''
IN = [list(line.strip()) for line in IN.splitlines()]

def solve(i, length, max_len):
    if length == max_len:
        return ""

    if i == len(bank):
        return None

    if (i, length) in DP:
        return DP[(i, length)]

    skip = solve(i+1, length, max_len)
    take = solve(i+1, length+1, max_len)
    if take is not None:
        take = bank[i] + take

    if skip is None:
        best = take
    elif take is None:
        best = skip
    else:
        best = max(skip, take)

    DP[(i, length)] = best
    return best

pt1 = pt2 = 0
for bank in IN:
    DP = {}
    pt1 += int(solve(0, 0, 2))
    DP = {}
    pt2 += int(solve(0, 0, 12))

print(pt1, pt2)
