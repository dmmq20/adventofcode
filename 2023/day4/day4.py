from functools import cache
import fileinput

def parse_input():
    cards = []
    for line in fileinput.input():
        need, have = line.strip().split("|")
        _, need = need.split(":")
        need, have = tuple(need.split()), tuple(have.split())
        cards.append((need, have))
    return cards

@cache
def count_cards(cards, i):
    a, b = cards[i]
    wins = len(set(a) & set(b))
    return 1 + sum(count_cards(cards, j) for j in range(i + 1, i + wins + 1))
    
cards = parse_input()
winning_nums = [len(set(a) & set(b)) for a, b in cards]
pt1 = sum(2 ** (x - 1) for x in winning_nums if x != 0)
print(pt1)

cards = tuple(cards)
pt2 = sum(count_cards(cards, i) for i in range(len(cards)))
print(pt2)
