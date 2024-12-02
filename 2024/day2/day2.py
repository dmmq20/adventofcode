import fileinput

def solve(row):
    pairs = list(zip(row, row[1:]))
    asc = pairs[0] < pairs[1]
    for a, b in pairs:
        if not (0 < abs(a-b) <= 3):
            return False
        if a > b and asc or b > a and not asc:
            return False
    return True

def pt2(row):
    return any(solve(row[:i] + row[i+1:]) for i in range(len(row)))

data = [[int(n) for n in line.split()] for line in fileinput.input()]
print(sum(solve(row) for row in data))
print(sum(pt2(row) for row in data))
