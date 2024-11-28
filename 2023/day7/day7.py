from collections import Counter
import functools, fileinput

def apply_joker(ctr):
    if "J" not in ctr or ctr["J"] == 5:
        return

    js = ctr["J"]
    del ctr["J"]
    best = max(ctr.values())
    for k, v in ctr.items():
        if v == best:
            ctr[k] += js
            return

def tie_break(h1, h2):
    for c1, c2 in zip(h1[0], h2[0]):
        if RANKS[c1] > RANKS[c2]:
            return 1
        if RANKS[c1] < RANKS[c2]:
            return -1
    return 0

def rank_hands(h1, h2, pt2=False):
    c1 = Counter(h1[0])
    c2 = Counter(h2[0])
    if pt2:
        apply_joker(c1)
        apply_joker(c2)
    c1_vals = sorted(c1.values(), reverse=True)
    c2_vals = sorted(c2.values(), reverse=True)

    if c1_vals == c2_vals:
        return tie_break(h1, h2)

    for v1, v2 in zip(c1_vals, c2_vals):
        if v1 > v2:
            return 1
        if v2 > v1:
            return -1

    return 0

data = [row.split(" ") for row in fileinput.input()]
RANKS = {k: v for k, v in zip(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"], list(range(13, -1, -1)))}

ranked = sorted(data, key=functools.cmp_to_key(rank_hands))
pt1 = sum([(i+1) * int(n) for i, (_, n) in enumerate(ranked)])
RANKS["J"] = -1
ranked = sorted(data, key=functools.cmp_to_key(lambda x, y: rank_hands(x, y, True)))
pt2 = sum([(i+1) * int(n) for i, (_, n) in enumerate(ranked)])
print(pt1, pt2)
