import re
from debug_helpers import log_test

DEBUG_MODE = False

def part_one():
    print("---- Part One ----")
    line_sum = 0

    for l in lines:
        l = solve_parenthesis(l, solve_line)
        line_sum += solve_line(l)


    print("Sum of all lines: " + str(line_sum))
    if DEBUG_MODE:
        log_test(line_sum == 26335)


def part_two():
    print("---- Part Two ----")
    line_sum = 0

    for l in lines:
        l = solve_parenthesis(l, solve_addition)
        l = solve_addition(l)
        line_sum += solve_line(l)

    print("Sum of all lines: " + str(line_sum))
    if DEBUG_MODE:
        log_test(line_sum == 693942)


def solve_line(line: str) -> int:
    parts = line.split()
    index = 2
    total = int(parts[0])

    while index < len(parts):
        operator = parts[index - 1]

        if operator == "+":
            total += int(parts[index])
        else:
            total *= int(parts[index])

        index += 2

    return total

def solve_addition(line: str) -> str:
    return solve_order(line, "+")

def solve_multiplication(line: str) -> str:
    return solve_order(line, "*")

def solve_order(line: str, operator: str) -> str:
    parts = line.split()
    total = int(parts[0])
    index = 2

    while index < len(parts):
        opr = parts[index - 1]
        
        if opr == operator:
            segment = f"{parts[index - 2]} {opr} {parts[index]}"
            
            value = int(parts[index - 2]) 

            if operator == "+":
                value += int(parts[index])
            else:
                value *= int(parts[index])

            line = line.replace(segment, str(value))
            parts = line.split()
        else:
            index += 2

    if len(line.split()) > 1:
        # more work to do
        return solve_order(line, "+" if operator == "*" else "*")
    else:
        # all done
        return line

        


def solve_parenthesis(line: str, solve_function):
    
    matches = re.findall("\([^()]*\)", line)

    while len(matches) > 0:

        for m in matches:
            value = solve_function(m[1:-1])
            line = line.replace(m, str(value))

        matches = re.findall("\([^()]*\)", line)

    return line





if DEBUG_MODE:
    lines = open("days\\day_18\\input_test.txt", "r").read().splitlines()
else:
    lines = open("days\\day_18\\input.txt", "r").read().splitlines()
        
part_one()
part_two()
