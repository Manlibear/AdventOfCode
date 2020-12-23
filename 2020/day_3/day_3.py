from functools import reduce

def part_1():
    print("---- Part One ---")
    x = 0
    y = 0
    found_trees = 0
    line_length = len(map[0])
    while y < len(map) - 1:
        x += 3
        y += 1

        if x >= line_length:
            x -= line_length

        if map[y][x]:
            found_trees += 1
    
    print("Found Trees: " + str(found_trees))


def part_2():
    print("---- Part Two ---")
    line_length = len(map[0])
    movement = [[1, 1], [3, 1], [5, 1],[7, 1], [1,2]]
    results = [0] * len(movement)

    for m in range(len(movement)):
        x = 0
        y = 0
        found_trees = 0

        while y < len(map) - movement[m][1]:
            x += movement[m][0]
            y += movement[m][1]
            
            if x >= line_length:
                x -= line_length

            if map[y][x]:
                found_trees += 1

        results[m] = found_trees
    
    print("Product of Found Trees: " + str(reduce((lambda x, y: x * y), results)))


lines = open("days\\day_3\\input.txt", "r").read().splitlines()
map = [False] * len(lines)

for y in range(len(lines)):
    line = [False] * len(lines[y])
    for x in range(len(line)):
        line[x] = (lines[y][x] == "#")
    map[y] = line

part_1()
part_2()