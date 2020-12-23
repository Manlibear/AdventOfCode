import math
import os
import copy
from rich.console import Console
from rich.table import Table
from rich import box
from rich.columns import Columns
from rich.panel import Panel
from rich import print
from debug_helpers import log_test

DEBUG_MODE = True

def part_one():
    print("---- Part One ----")
    answer = 0
    tile_pos[list(tile_map.keys())[0]] = (1, 1)

    # print_tiles()
    while (-1, -1) in tile_pos.values():
        for t in [x for x in tile_pos if tile_pos[x] == (-1, -1)]:
            search = True
            for m in [tile for tile in tile_pos if tile_pos[tile] != (1, 1)]:
                
                for i in range(width):
                    if not search:
                        break
                    for j in range(width):
                        if not search:
                            break
                        if check_neighbours(tile_map[t], i, j):
                            tile_pos[t] = (i, j)
                            search =False


        

    print("Answer: " + str(answer))
    if DEBUG_MODE:
        log_test(answer == 2)


def part_two():
    print("---- Part Two ----")
    answer = 0

    print("Answer: " + str(answer))
    if DEBUG_MODE:
        log_test(answer == 12)


def print_tiles():
    os.system('cls')
    console = Console()
    table = Table()
    
    for i in range(width):
        print(Columns([Panel(render_tile(tile_map[x]), box=box.SIMPLE,padding=(0,0), expand=True) for x in list(tile_map.keys())[i:i+(width)]], padding=(0,0)))

    # for y in range(width):
    #     for x in range(width):
    #         if (y, x) in tile_map.value():

    #         else:

def check_neighbours(tile, x, y):
    print(f"Checking neighbours of {(x, y)}")
    if (x, y) in tile_pos.values():
        return False

    for i in [-1, 1, 0]:
        for j in [-1, 1, 0]:
            if (i in [1, -1] and j == 0) or (j in [1, -1] and i == 0):
                if not safe_check_tile_match(tile, x, y, i, j):
                    return False
    return True    

def safe_check_tile_match(tile, x, y, i, j):
    if (x + i, y + j) in tile_pos.values():
        rotated = copy.deepcopy(tile)
        for r in range(4):
            if r > 0:
                rotated = list(zip(*rotated[::-1]))
            match_tile = tile_map[list([k for k,v in tile_pos.items() if v == (x + i, y + j)])[0]]
            match = False
            if j == -1 and i ==0:
                match = tile[0] == match_tile[-1]
            elif j == 1 and i ==0:
                match = tile[-1] == match_tile[0]
            elif i == 1 and j == 0:
                match = [t[-1] for t in tile] == [t[0] for t in match_tile]
            elif i == -1 and j == 0:
                match = [t[0] for t in tile] == [t[-1] for t in match_tile]
            
            if match:
                tile = rotated
                return True
        return False
    else:
        return True
                
def render_tile(tile):
    tile_str = ""
    for r in tile:
        tile_str += "".join(r) + "\n"
    return tile_str

if DEBUG_MODE:
    parts = open("days\\day_20\\input_test.txt", "r").read().split("\n\n")
else:
    parts = open("days\\day_20\\input.txt", "r").read().split("\n\n")

tile_map = {}
tile_pos = {}
for p in parts:
    tile_parts = p.split("\n")
    tile_name = tile_parts[0][5:-1]
    rows = []
    for r in range(1, len(tile_parts) - 1):
        rows.append(list(tile_parts[r]))
    tile_map[tile_name] = rows
    tile_pos[tile_name] = (-1,-1)


width = int(math.sqrt(len(tile_map)))

part_one()
part_two()
