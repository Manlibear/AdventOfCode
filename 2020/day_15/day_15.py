from collections import deque
from debug_helpers import log_test

DEBUG_MODE = False

def part_one():
    global numbers
    print("---- Part One ----") 
    
    last_number = numbers[-1]
    highest = {}

    for i in range(2020 - len(numbers)):
        indices = [index for index, x in enumerate(numbers) if x == last_number]

        if len(indices) < 2:
            numbers.append(0)
        else:
            new_number = indices[-1] - indices[-2]

            if new_number > max(numbers):
                highest[new_number] = len(numbers)

            numbers.append(new_number)
            # numbers = numbers[numbers.index(max(numbers)):]
            # numbers = numbers[-max(numbers):]


        last_number = numbers[-1]

    

    print("2020th number: " + str(last_number))
    if DEBUG_MODE:
        log_test(last_number == 436)



def part_two():
    print("---- Part Two ----")
    last_number = numbers[-1]

    numbers_lookup = {}

    for i in range(len(numbers)):
        numbers_lookup[numbers[i]] = [i]

    for i in range(len(numbers), 30000000):
        new_number = 0
        
        this_number = numbers_lookup[last_number]
        if len(this_number) >= 2:
            new_number = this_number[-1] - this_number[-2]
            if new_number in numbers_lookup:
                numbers_lookup[new_number] += [i]
            else:
                numbers_lookup[new_number] = [i]
        else:
            numbers_lookup[0] += [i]
        
        last_number = new_number

    print("30000000th: " + str(last_number))
    if DEBUG_MODE:
        log_test(last_number == 175594)

def find_first_two(the_list, target):
    count = 0

    if count == 2:
        raise StopIteration

    for i in range((len(the_list))):
        if the_list[i] == target:
            count += 1
            yield i

if DEBUG_MODE:
    lines = open("days\\day_15\\input_test.txt", "r").read().splitlines()
else:
    lines = open("days\\day_15\\input.txt", "r").read().splitlines() 

numbers = []
for d in lines[0].split(","):
    numbers.append(int(d))

part_one()

numbers = []
for d in lines[0].split(","):
    numbers.append(int(d))

part_two()
