from debug_helpers import log_test

DEBUG_MODE = False

def part_one():
    global other_tickets
    print("---- Part One ----") 
    error_rate = 0
    to_remove = []

    for t in other_tickets:
        for v in t:
            if not any(v in x for x in rules.values()):
                error_rate += v
                to_remove.append(t)
    
    other_tickets = [t for t in other_tickets if t not in to_remove]

    print("Error rate: " + str(error_rate))
    if DEBUG_MODE:
        log_test(error_rate == 71)



def part_two():
    print("---- Part Two ----")
    answer = 1
    pos_rule = {}
    rule_names = list(rules.keys())
    key_count = len(rules.keys())
    failed_rules = []

    for k in rules.keys():
        pos_rule[k] = [True] * key_count

    for i in range(key_count):
        rule_name = rule_names[i]
        rule_values = rules[rule_name]

        for j in range(key_count):
            for t in other_tickets:
                value = t[j]

                if value not in rule_values:
                    pos_rule[rule_name][j] = False
                    if rule_name not in failed_rules:
                        failed_rules.append(rule_name)
                    break

    valid_rules = {}
    for r in pos_rule.keys():
        valid_rules[r] = [i for i, x in enumerate(pos_rule[r]) if x]

    while True:
        one_valids = [(i, valid_rules[i][0]) for i in valid_rules if len(valid_rules[i]) == 1]

        if len(one_valids) == len(valid_rules):
            break

        for ov in one_valids:
            for r in valid_rules:
                if r != ov[0]:
                    valid_rules[r] = [vr for vr in valid_rules[r] if vr != ov[1]]


    for rule_index in [value[0] for key, value in valid_rules.items() if 'departure' in key.lower()]:
        answer *= my_ticket[rule_index]

    print("Answer: " + str(answer))
    if DEBUG_MODE:
        log_test(valid_rules["row"][0] == 0 and valid_rules["class"][0] == 1 and valid_rules["seat"][0] == 2)


if DEBUG_MODE:
    parts = open("days\\day_16\\input_test.txt", "r").read().split("\n\n")
else:
    parts = open("days\\day_16\\input.txt", "r").read().split("\n\n") 

rules = {}
for rule_line in parts[0].splitlines():
    rule_parts = rule_line.split(":")
    rule_values = []
    
    for rp in rule_parts[1].split(" or "):
        bracket = rp.split("-")
        for i in range(int(bracket[0]), int(bracket[1]) + 1):
            rule_values.append(i)
    rules[rule_parts[0]] = rule_values

my_ticket = [int(value) for value in parts[1].splitlines()[1].split(",")]

other_tickets = []
first_line = True
for ticket_line in parts[2].splitlines():

    # skip the first line, it's a heading
    if first_line:
        first_line = False
        continue

    other_tickets.append([int(value) for value in ticket_line.split(",")])



part_one()
part_two()
