
def part_one():
    print("---- Part One ----")

    for l in lines:
        instr = l[0]
        param = int(l[1:])
        process_input(instr, param)

    print("Manhattan Dist: " + str(abs(north_pos) + abs(east_pos)))


def part_two():
    global waypoint_east_pos
    global waypoint_north_pos
    print("---- Part Two ----")

    waypoint_east_pos = 10
    waypoint_north_pos = 1

    for l in lines:
        instr = l[0]
        param = int(l[1:])
        process_input_waypoint(instr, param)

    print("Manhattan Dist: " + str(abs(north_pos) + abs(east_pos)))

def process_input(i, p):
    
    # pylint: disable=E0602

    global north_pos
    global east_pos
    global facing

    if i == "N":
        north_pos += p
    elif i == "S":
        north_pos -= p
    elif i == "E":
        east_pos += p
    elif i == "W":
        east_pos -= p
    elif i == "L":
        facing -= p 
    elif i == "R":
        facing += p
    elif i == "F":
        if facing == 0:
            north_pos += p
        elif facing == 90:
            east_pos += p
        elif facing == 180:
            north_pos -= p
        elif facing == 270:
            east_pos -= p

    if facing < 0:
        facing += 360

    facing = facing % 360

def process_input_waypoint(i, p):
    global facing
    global north_pos
    global east_pos
    global waypoint_east_pos
    global waypoint_north_pos

    if i == "N":
        waypoint_north_pos += p
    elif i == "S":
        waypoint_north_pos -= p
    elif i == "E":
        waypoint_east_pos += p
    elif i == "W":
        waypoint_east_pos -= p
    elif i in ["L", "R"]:
        # for R
        #N10 E4
        #N-4 E10
        #N-10 E-4
        #N4 E-10
        for _ in range(int(p / 90)):
            waypoint_east_pos, waypoint_north_pos = waypoint_north_pos, waypoint_east_pos 
            if i == "L":
                waypoint_east_pos *= -1
            else:
                waypoint_north_pos *= -1
        

    elif i == "F":
        north_pos += waypoint_north_pos * p
        east_pos += waypoint_east_pos * p


lines = open("days\\day_12\\input.txt", "r").read().splitlines()


east_pos = 0
north_pos = 0
facing = 90
waypoint_east_pos = 0
waypoint_north_pos = 0

part_one()

# reset the values between runs
east_pos = 0
north_pos = 0
facing = 90

part_two()
