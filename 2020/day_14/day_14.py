import re
from debug_helpers import log_test
from itertools import product


DEBUG_MODE = False

def part_one():
    print("---- Part One ----") 
    curr_mask = ""
    for l in lines:
        line_value = l.split(" = ")[1]

        if l.startswith("mask"):
            curr_mask = line_value
        else:
            addr = re.findall("\[(\d*)\]", l)[0]
            value = mask_value(curr_mask, line_value)
            mem[addr] = value

    answer = 0
    for m in mem.values():
        answer += int(m, 2)

    print("Sum in memory: " + str(answer))
    if DEBUG_MODE:
        log_test(answer == 165)



def part_two():
    print("---- Part Two ----")
    mem.clear()

    for l in lines:
        line_value = l.split(" = ")[1]

        if l.startswith("mask"):
            curr_mask = line_value
        else:
            addr = re.findall("\[(\d*)\]", l)[0]

            for a in mask_addr(curr_mask, addr):
                mem[int(a, 2)] = int(line_value)

    
    answer = 0
    for m in mem.values():
        answer += m

    print("Sum in memory V2: " + str(answer))
    if DEBUG_MODE:
        log_test(answer == 208)


def mask_value(mask: str, value: str) -> int:
    value = "{0:b}".format(int(value)).zfill(36)
    for i in range(len(mask)):
        if mask[i].isdigit():
            value = replace_str_index(value, i, mask[i])
    return value

def mask_addr(mask: str, addr: str) -> list:
    addrs = []
    addr = "{0:b}".format(int(addr)).zfill(36)

    for i in range(len(mask)):
        if mask[i] in ["1", "X"]:
            addr = replace_str_index(addr, i, mask[i])

    for f in filler(addr):
        unique_append(addrs, f)
    
    return addrs

def unique_append(col: list, value: str):
    if value not in col:
        col.append(value)


def filler(word):    
    options = {'X': ['0', '1']}
    combos = [(c,) if c not in options else options[c] for c in word]
    return (''.join(o) for o in product(*combos))


if DEBUG_MODE:
    lines = open("days\\day_14\\input_test.txt", "r").read().splitlines()
else:
    lines = open("days\\day_14\\input.txt", "r").read().splitlines() 

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

mem = {}

part_one()

if DEBUG_MODE:
    lines = open("days\\day_14\\input_test_part_two.txt", "r").read().splitlines()

part_two()
