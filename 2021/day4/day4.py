import re

f = open("day4.txt").read()

nums, *cards = f.split("\n\n")
nums = re.findall("\\d+", nums)
cards = [[re.findall("\\d+", row) for row in card.splitlines()] for card in cards]

def sum_card(card, nums):
    return sum(sum(int(x) for x in row if x not in nums) for row in card) * int(nums[-1])

def check_win(card, nums):
    rows = any(all(n in nums for n in row) for row in card)
    return rows or any(all(n in nums for n in col) for col in zip(*card))

def solve():
    done = set()
    for i in range(6, len(nums)):
        for j, card in enumerate(cards):
            if j not in done and check_win(card, nums[:i]):
                done.add(j)
                if len(done) in [1, len(cards)]: 
                    print(sum_card(card, nums[:i]))

solve()
