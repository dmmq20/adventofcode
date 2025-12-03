IN = '''987654321111111
811111111111119
234234234234278
818181911112111'''

IN = [list(line.strip()) for line in IN.splitlines()]

def solve(bank, max_len):
    DP = {}
    def _solve(i, length, max_len):
        if length == max_len:
            return ""
    
        if i == len(bank):
            return None
    
        if (i, length) in DP:
            return DP[(i, length)]
    
        skip = _solve(i+1, length, max_len)
        take = _solve(i+1, length+1, max_len)
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
    return _solve(0, 0, max_len)


pt1 = sum(int(solve(bank, 2)) for bank in IN)
pt2 = sum(int(solve(bank, 12)) for bank in IN)
print(pt1, pt2)
