import copy
import math
from debug_helpers import log_test
from file_helpers import open_file

DEBUG_MODE = False

def part_one():
    global node_map
    print("---- Part One ----")
    active_node_count = 0

    for _ in range(6):
        grow_map()
        node_map_changes = copy.deepcopy(node_map)
        for z in range(len(node_map)):
            for y in range(len(node_map[z])):
                for x in range(len(node_map[z][y])):

                    active_neighbours = count_active_neighbours(z, y, x)
                                    
                    this_node = node_map[z][y][x]

                    if this_node == "#" and active_neighbours not in [2,3]:
                        node_map_changes[z][y][x] = "."
                    elif this_node == "." and active_neighbours == 3:
                        node_map_changes[z][y][x] = "#"

        node_map = node_map_changes

    for z in range(len(node_map)):
        for y in range(len(node_map[z])):
            for x in range(len(node_map[z][y])):
                active_node_count += node_map[z][y][x] == "#"

    print("Active nodes: " + str(active_node_count))
    if DEBUG_MODE:
        log_test(active_node_count == 112)

def part_two():
    global node_map_4d
    print("---- Part Two ----")
    active_node_count = 0

    for _ in range(6):
        grow_map_4d()
        node_map_4d_changes = copy.deepcopy(node_map_4d)
        for w in range(len(node_map_4d)):
            for z in range(len(node_map_4d[w])):
                for y in range(len(node_map_4d[w][z])):
                    for x in range(len(node_map_4d[w][z][y])):

                        active_neighbours = count_active_neighbours_4d(w, z, y, x)
                                        
                        this_node = node_map_4d[w][z][y][x]

                        if this_node == "#" and active_neighbours not in [2,3]:
                            node_map_4d_changes[w][z][y][x] = "."
                        elif this_node == "." and active_neighbours == 3:
                            node_map_4d_changes[w][z][y][x] = "#"

            node_map_4d = node_map_4d_changes

    for w in range(len(node_map_4d)):
        for z in range(len(node_map_4d[w])):
            for y in range(len(node_map_4d[w][z])):
                for x in range(len(node_map_4d[w][z][y])):
                    active_node_count += node_map_4d[w][z][y][x] == "#"

    print("Active Nodes: " + str(active_node_count))
    if DEBUG_MODE:
        log_test(active_node_count == 848)

def count_active_neighbours(z, y, x):
    active_neighbours = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:

                if i == 0 and j == 0 and k == 0:
                    continue

                active_neighbours += safe_check_node(z + i, y + j, x + k)
                
                if active_neighbours > 3:
                    return active_neighbours

    return active_neighbours

def count_active_neighbours_4d(w, z, y, x):
    active_neighbours = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:

                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue

                    active_neighbours += safe_check_node_4d(w + i, z + j, y + k, x + l)

                    if active_neighbours > 3:
                        return active_neighbours

    return active_neighbours
                    

def safe_check_node(z, y, x):
    if len(node_map) > z and len(node_map[z]) > y and len(node_map[z][y]) > x and x >= 0 and y >= 0 and z >= 0:
        return node_map[z][y][x] == "#"
    else:
        return False


def safe_check_node_4d(w,z,y,x):
    if len(node_map_4d) > w and len(node_map_4d[w]) > z and len(node_map_4d[w][z]) > y and len(node_map_4d[w][z][y]) > x and x >= 0 and y >= 0 and z >= 0 and w >= 0:
        return node_map_4d[w][z][y][x] == "#"
    else:
        return False


def grow_map():
    
    width = len(node_map)
    
    for z in range(width):
        
        for y in range(width):
            node_map[z][y].append(".")
            node_map[z][y].insert(0, ".")

        node_map[z].append(["." for i in range(width + 2)])
        node_map[z].insert(0, ["." for i in range(width  + 2)])
    
    node_map.append([["." for i in range(width + 2)] for j in range(width + 2)])
    node_map.insert(0, [["." for i in range(width + 2)] for j in range(width + 2)])

    
def grow_map_4d():
    
    width = len(node_map_4d)

    for w in range(width):
        for z in range(width):
            for y in range(width):

                node_map_4d[w][z][y].append(".")
                node_map_4d[w][z][y].insert(0, ".")

            node_map_4d[w][z].append(["." for i in range(width + 2)])
            node_map_4d[w][z].insert(0, ["." for i in range(width  + 2)])
        
        node_map_4d[w].append([["." for i in range(width + 2)] for j in range(width + 2)])
        node_map_4d[w].insert(0, [["." for i in range(width + 2)] for j in range(width + 2)])

    node_map_4d.append([[["." for i in range(width + 2)] for j in range(width + 2)] for k in range(width + 2)])
    node_map_4d.insert(0, [[["." for i in range(width + 2)] for j in range(width + 2)] for k in range(width + 2)])


lines = open_file(DEBUG_MODE).splitlines()

node_map = []

width = len(lines[0])
mid_point = math.floor(width / 2)

# floor(width/2) layers for ease
for _ in range(width):
    node_map.append([["." for i in range(width)] for j in range(width)])

for i in range(width):
    for j in range(width):
        node_map[mid_point][i][j] = lines[i][j]

node_map_4d = []

# floor(width/2) layers for ease
for _ in range(width):
    node_map_4d.append([[["." for i in range(width)] for j in range(width)] for k in range(width)])

for i in range(width):
    for j in range(width):
        node_map_4d[mid_point][mid_point][i][j] = lines[i][j]
        
part_one()
part_two()
