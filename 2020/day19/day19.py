import fileinput


def parse():
    data, msgs = "".join(line for line in fileinput.input()).split("\n\n")
    msgs = msgs.splitlines()
    rules = {k: [rs.split() for rs in rules.split("|")]
             for line in data.splitlines()
             for k, rules in [line.split(": ", 1)]
             }
    return msgs, rules


def apply_rules(message, rules, rule_num="0", pos=0):
    if pos >= len(message):
        return set()

    if rule_num.startswith('"'):
        if message[pos] == rule_num.strip('"'):
            return {pos + 1}
        return set()

    rule = rules[rule_num]
    valid_positions = set()
    for subrule in rule:
        curr_positions = {pos}

        for next_rule in subrule:
            new_positions = set()
            for p in curr_positions:
                new_positions |= apply_rules(message, rules, next_rule, p)
            curr_positions = new_positions
            if not curr_positions:
                break
        valid_positions |= curr_positions

    return valid_positions


def solve(msgs, rules, pt2=False):
    if pt2:
        rules["8"] = [["42"], ["42", "8"]]
        rules["11"] = [["42", "31"], ["42", "11", "31"]]
    return sum(len(msg) in apply_rules(msg, rules) for msg in msgs)


msgs, rules = parse()
print(solve(msgs, rules))
print(solve(msgs, rules, True))
