IN = '''987654321111111
811111111111119
234234234234278
818181911112111'''

def solve(bank, max_len):
    DP = {}
    def _solve(idx=0, curr_len=0, max_len=0):
        if curr_len == max_len or idx >= len(bank):
            return ""
        take = bank[idx] + _solve(idx+1, curr_len+1, max_len)
        skip = _solve(idx+1, curr_len, max_len)
        if skip:
            DP[(idx, curr_len)] = str(max(int(take), int(skip)))
            return DP[(idx, curr_len)]
        DP[(idx, curr_len)] = take
        return DP[(idx, curr_len)]  
        
    return _solve(0, 0, max_len)

banks = IN.splitlines()
pt1 = sum(int(solve(bank, 2)) for bank in banks)
pt2 = sum(int(solve(bank, 12)) for bank in banks)
print(pt1, pt2)
