from operator import xor

class Password:
    character = ""
    minimum = 0
    maximum = 0
    password = ""


def part_one():
    print("---- Part One ----")
    valid = 0
    for p in passwords:
        count = p.password.count(p.character)
        if count >= p.minimum and count <= p.maximum:
            valid += 1
    print("Valid passwords: " + str(valid))


def part_two():
    print("---- Part Two ----")
    valid = 0
    for p in passwords:
        if xor(p.password[p.minimum - 1] == p.character, p.password[p.maximum - 1] == p.character):
            valid += 1
    print("Valid passwords: " + str(valid))



lines = open("days\\day_2\\input.txt", "r").read().splitlines()
passwords = [None] * len(lines)

for i in range(len(passwords)):
    line = str(lines[i])
    parts = line.split()
    numbers = parts[0].split("-")

    p = Password()
    p.character = parts[1][0]
    p.minimum = int(numbers[0])
    p.maximum = int(numbers[1])
    p.password = parts[2]
    passwords[i] = p


part_one()
part_two()