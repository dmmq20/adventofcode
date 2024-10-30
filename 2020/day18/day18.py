import fileinput
from collections import deque

OPS = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b
}

def evaluate(operands, operators, pt2=False):
    while operands and operators:
        if pt2 and operators[0] == "*" and "+" in operators:
            operands.rotate(-1)
            operators.rotate(-1)
            continue
        op = operators.popleft()
        a, b = operands.popleft(), operands.popleft()
        operands.appendleft(OPS[op](a, b))
    return operands[0]

def solve(expr, pt2=False):
    operands, operators = deque([]), deque([])
    while expr:
        token = expr.popleft()
        match token:
            case ")": 
                break
            case "(":
                operands.append(solve(expr, pt2))
            case "*" | "+":
                operators.append(token)
            case _:
                operands.append(int(token))
    return evaluate(operands, operators, pt2)

data = [line.strip() for line in fileinput.input()]
for part in [False, True]:
    exprs = [deque(list(line.replace(" ", ""))) for line in data]
    print(f"Part {part + 1}: {sum([solve(expr, part) for expr in exprs])}")
