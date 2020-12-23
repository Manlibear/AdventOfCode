from debug_helpers import log_test

DEBUG_MODE = False

def part_one():
    print("---- Part One ----")
    shortest = 9999
    selected_bus = 0
    for b in buses:
        count = 0
        while count < earliest_depart:
            count += b
        diff = count - earliest_depart
        if diff < shortest:
            selected_bus = b
            shortest = diff

    answer = shortest * selected_bus
    print("Our bus: " + str(answer))
    if DEBUG_MODE:
        log_test(answer == 295)



def part_two():
    print("---- Part Two ----")
    period = 1
    ts = 0
    buses = lines[1].split(",")
    for bus in buses:
        if bus != 'x':
            bus = int(bus)
            while (ts % bus) != 0:
                ts += period
            period *= bus
        ts += 1
    
    ts -= len(buses)
    print("First valid timestamp: " + str(ts))
    if DEBUG_MODE:
        log_test(ts == 1068781)

if DEBUG_MODE:
    lines = open("days\\day_13\\input_test.txt", "r").read().splitlines()
else:
    lines = open("days\\day_13\\input.txt", "r").read().splitlines() 

earliest_depart = int(lines[0])
buses = (int(bus) for bus in lines[1].split(",") if bus != "x")

bus_offsets = {}
bus_parts = lines[1].split(",")
for b in range(len(bus_parts)):
    if bus_parts[b] != "x":
        bus_offsets[b] = int(bus_parts[b])

part_one()
part_two()
