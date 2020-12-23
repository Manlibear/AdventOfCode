from os import system
from time import sleep

def part_one():
    global seat_map
    print("---- Part One ----")
    
    seat_changed = True
    # update_screen(0)
    # sleep(2)
    # iteration = 1
    projected_seat_map = [row.copy() for row in seat_map]
    while seat_changed:
        seat_changed = False
        for y in range(len(seat_map)):
            for x in range(len(seat_map[y])):
                if seat_map[y][x] != ".":
                    this_seat_changed = update_seat(x, y, projected_seat_map)
                    if this_seat_changed:
                        seat_changed = True
        seat_map = [row.copy() for row in projected_seat_map]
        # update_screen(iteration)
        # sleep(2)
        # iteration += 1

    print("Number of occupied seats: " + str(sum(x.count('#') for x in seat_map)))

def part_two():
    global seat_map
    print("---- Part Two ----")
    seat_changed = True
    seat_map = [row.copy() for row in clean_seat_map] # reset the seat_map
    
    # update_screen(0)
    # sleep(2)
    # iteration = 1
    projected_seat_map = [row.copy() for row in seat_map]
    while seat_changed:
        seat_changed = False
        for y in range(len(seat_map)):
            for x in range(len(seat_map[y])):
                if seat_map[y][x] != ".":
                    this_seat_changed = update_seat(x, y, projected_seat_map, tolerance=5, raycast=True)
                    if this_seat_changed:
                        seat_changed = True
        seat_map = [row.copy() for row in projected_seat_map]
        
        # update_screen(iteration)
        # sleep(2)
        # iteration += 1

    print("Number of occupied seats: " + str(sum(x.count('#') for x in seat_map)))

def check_seat_avilable(x, y):
    if x < 0 or y < 0 or y > len(seat_map) - 1 or x > len(seat_map[0]) - 1:
        return True
    return seat_map[y][x] != "#"

def update_seat(x, y, target_map, tolerance = 4, raycast = False):
    seat_changed = False
    adjacent = [False] * 8

    if raycast:
        adjacent[0] = raycast_empty(x, y, 0, -1) # north
        adjacent[1] = raycast_empty(x, y, 1, 0) # east
        adjacent[2] = raycast_empty(x, y, 0, 1) # south
        adjacent[3] = raycast_empty(x, y, -1, 0) # west
        adjacent[4] = raycast_empty(x, y, 1, - 1) # north-east
        adjacent[5] = raycast_empty(x, y, 1, 1) # south-east
        adjacent[6] = raycast_empty(x, y, -1, -1) # north-west
        adjacent[7] = raycast_empty(x, y, -1, 1) # south-west

    else:
        adjacent[0] = check_seat_avilable(x, y - 1) # north
        adjacent[1] = check_seat_avilable(x + 1, y) # east
        adjacent[2] = check_seat_avilable(x, y + 1) # south
        adjacent[3] = check_seat_avilable(x - 1, y) # west
        adjacent[4] = check_seat_avilable(x + 1, y - 1) # north-east
        adjacent[5] = check_seat_avilable(x + 1, y + 1) # south-east
        adjacent[6] = check_seat_avilable(x - 1, y - 1) # north-west
        adjacent[7] = check_seat_avilable(x - 1, y + 1) # south-west


    if seat_map[y][x] == "L" and sum(adjacent) == 8:
        target_map[y][x] = "#"
        seat_changed = True
    elif seat_map[y][x] == "#" and sum(adjacent) <= (8 - tolerance):
        target_map[y][x] = "L"
        seat_changed = True

    return seat_changed

def update_screen(i):
    system('cls')
    screen = ""
    print("Iteration: " + str(i))
    for y in range(len(seat_map)):
        screen += "".join(seat_map[y]) + "\n"
    print(screen)
        
def raycast_empty(origin_x, origin_y, dir_x, dir_y):
    curr_x = origin_x
    curr_y = origin_y

    while True:
        curr_y += dir_y
        curr_x += dir_x

        if curr_x >= 0 and curr_y >= 0 and curr_y <= len(seat_map) - 1 and curr_x <= len(seat_map[0]) - 1:
            if seat_map[curr_y][curr_x] == "#":
                return False # line of sight obstructed by occupied chair
            elif seat_map[curr_y][curr_x] == "L":
                return True # line of sight obstructed, but by empty chair
        else:
            return True # line of sight clear, made it out of map



lines = open("days\\day_11\\input.txt", "r").read().splitlines()
seat_map = []

for l in lines:
    row = []
    for s in l:
        row.append(s)
    seat_map.append(row)

clean_seat_map = [row.copy() for row in seat_map]

part_one()
part_two()
