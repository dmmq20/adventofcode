IN = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''

IN = [line.strip().split("-") for line in IN.split(",")]

def invalid_id(id, pt2=False):
    id = str(id)
    k = len(id) // 2
    if not pt2:
        return len(id) % 2 == 0 and id[:k] == id[k:]
        
    for i in range(1, k+1):
        chunk = id[:i]
        chunk_len = len(chunk)
        if all(chunk == id[j:j+chunk_len] for j in range(i, len(id), chunk_len)):
            return True
    return False

pt1, pt2 = 0, 0
for low, high in IN:
    for i in range(int(low), int(high) + 1):
        pt1 += i if invalid_id(i) else 0
        pt2 += i if invalid_id(i, pt2=True) else 0

print(pt1, pt2)
