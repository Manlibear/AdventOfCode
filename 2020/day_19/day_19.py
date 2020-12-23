import re
import copy
from debug_helpers import log_test

DEBUG_MODE = True

def part_one():
    print("---- Part One ----")
    answer = 0
    lookup = {}
    for i in rules:
        if rules[i].isalpha():
            lookup[i] = rules[i]

    while True:
        for i in rules:
            complete = True
            rule_parts = rules[i].split()
            for r_part in rule_parts:
                if r_part.isdigit():
                    complete = False
                    int_r_part = int(r_part)
                    if int_r_part in lookup:
                        rules[i] = re.sub(fr"\b{r_part}\b", f" (?:{lookup[int_r_part]}) ", rules[i])

            if complete and i not in lookup:
                rules[i] = rules[i].replace(" ", "")
                lookup[i] = rules[i]

        if 0 in lookup:
            break

    for d in data:
        answer += bool(re.match(f'^{lookup[0]}$', d))
                

    print("Lines matching rule[0]: " + str(answer))
    if DEBUG_MODE:
        log_test(answer == 2)


def part_two():
    print("---- Part Two ----")
    answer = 0
    lookup = {}
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"

    for i in rules:
        if rules[i].isalpha():
            lookup[i] = rules[i]

    while True:
        for i in rules:
            complete = True
            rule_parts = rules[i].split()
            for r_part in rule_parts:
                if r_part.isdigit():
                    complete = False
                    int_r_part = int(r_part)
                    if int_r_part in lookup:
                        rules[i] = re.sub(fr"\b{r_part}\b", f" (?:{lookup[int_r_part]}) ", rules[i])

            if complete and i not in lookup:
                rules[i] = rules[i].replace(" ", "")
                lookup[i] = rules[i]

        if 0 in lookup:
            break

    for d in data:
        answer += bool(re.match(f'^{lookup[0]}$', d))


    print("Lines matching rule[0]: " + str(answer))
    if DEBUG_MODE:
        log_test(answer == 12)

if DEBUG_MODE:
    parts = open("days\\day_19\\input_test.txt", "r").read().split("\n\n")
else:
    parts = open("days\\day_19\\input.txt", "r").read().split("\n\n")


rules = {}
for rule in parts[0].splitlines():
    rule_parts= rule.split(":")
    rule_index = int(rule_parts[0])
    rules[rule_index] = rule_parts[1].replace("\"", "").strip()

clean_rules = copy.deepcopy(rules)

data = []
for d in parts[1].splitlines():
    data.append(d)
        
part_one()

rules = clean_rules
part_two()
