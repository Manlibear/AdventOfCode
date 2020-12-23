from debug_helpers import log_test, log_answer
from file_helpers import open_file
import os
from art import tprint

DEBUG_MODE = True

def part_one():
    print("---- Part One ----")
    answer = 0

    log_answer("Answer: ", answer, 123, DEBUG_MODE)

def part_two():
    print("---- Part Two ----")
    answer = 0

    log_answer("Answer: ", answer, 123, DEBUG_MODE)


lines = open_file(DEBUG_MODE).splitlines()

os.system("cls")
day_number = __file__.split("_")[2].split(".")[0]
tprint("Day    " + day_number)

part_one()
print()
part_two()
print()

