import re
import fileinput


def calculate_determinant(a11, a12, a21, a22):
    return a11 * a22 - a12 * a21


def solve(buttonA, buttonB, target, pt2=False):

    ax, ay = buttonA
    bx, by = buttonB
    tx, ty = target

    if pt2:
        tx += 10000000000000
        ty += 10000000000000

    D = calculate_determinant(ax, bx, ay, by)
    if D == 0:
        return 0

    Dx = calculate_determinant(tx, bx, ty, by)
    Dy = calculate_determinant(ax, tx, ay, ty)

    presses_a = Dx / D
    presses_b = Dy / D

    if presses_a.is_integer() and presses_b.is_integer():
        return int(presses_a * 3 + presses_b)

    return 0


data = "".join(line for line in fileinput.input())
machines = []
for m in data.split("\n\n"):
    nums = [int(n) for n in re.findall("\\d+", m)]
    buttonA, buttonB, target = tuple(
        nums[:2]), tuple(nums[2:4]), tuple(nums[4:])
    machines.append([buttonA, buttonB, target])

pt1 = [solve(*m) for m in machines]
pt2 = [solve(*m, True) for m in machines]
print(sum(pt1), sum(pt2))
