# find the two entries that sum to 2020 and then multiply those two numbers together.

import time

def part_one():
    print("---- Part One ----")
    iterations = 0
    success = False
    startTime = time.perf_counter()
    for x in numbers:

        if success:
            break

        for y in reversed(numbers):        
            iterations += 1
            if x + y == 2020:
                print("Found: " + str(x) + " x " + str(y) + " = " + str(x * y))
                print("Total iterations: " + str(iterations) + ", Total time: " + str(time.perf_counter() - startTime))
                success = True
                break
            elif x+y < 2020:
                #this is always going to be too low, abort
                break

    if not success:
        print("Unable to find solution")

def part_one_b():

    print("---- Part One(b) ----")
    iterations = 0
    startTime = time.perf_counter()
    for num in numbers:
        iterations+=1
        if 2020-num in numbers:
            print("Found: " + str(num) + " x " + str(2020-num) + " = " + str(num * (2020-num)))
            print("Total iterations: " + str(iterations) + ", Total time: " + str(time.perf_counter() - startTime))
            return



def part_two():
    print("---- Part Two ----")
    maxZ = numbers[-1]
    iterations = 0
    success = False
    for x in numbers:
        if success:
            break

        for y in numbers:
            if success:
                break
            elif x + y + maxZ < 2020:
                # never gonna be big enough
                break
            
            for z in reversed(numbers):
                iterations += 1
                if x + y + z == 2020:
                    print("Found: " + str(x) + " x " + str(y) + " x " + str(z) + " = " + str(x * y * z))
                    success = True
                    break
                elif x + y + z < 2020:
                    # never gonna be big enough
                    break

    if success:
        print("Total iterations: " + str(iterations))
    else:
        print("Unable to find solution")



lines = open("days\\day_1\\input.txt", "r").read().splitlines()

numbers = [0] * len(lines)
i=0
for l in lines:
    numbers[i] = int(l)
    i+=1
numbers.sort()

part_one()
# part_one_b()
part_two()