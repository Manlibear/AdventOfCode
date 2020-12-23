def part_one():
    print("---- Part One ----")
    print("Highest Seat Position: " + str(max(seat_ids)))

def part_two():
    print("---- Part Two ----")
    seat_ids.sort()
    
    for i in range(len(seat_ids)):
       
        if i > 0:
            prev = seat_ids[i - 1]
            cur = seat_ids[i]
            
            if cur - prev > 1:
                print("My seat: " + str(seat_ids[i] - 1))

lines = open("days\\day_5\\input.txt", "r").read().splitlines()
seat_ids = [0] * len(lines)

for i in range(len(seat_ids)):
    row = 0
    chunk = [0, 127]
    for j in range(7):
        c = lines[i][j]
        if c == "F":
            chunk = [chunk[0], chunk[1] - ((chunk[1] - chunk[0]) + 1)  / 2]
        else:
            chunk = [chunk[0] + ((chunk[1] - chunk[0]) + 1) / 2 , chunk[1]]

    row = chunk[0]

    seat = 0
    chunk = [0, 7]
    for c in lines[i][7:]:
        if c == "L":
            chunk = [chunk[0], chunk[1] - ((chunk[1] - chunk[0]) + 1)  / 2]
        else:
            chunk = [chunk[0] + ((chunk[1] - chunk[0]) + 1) / 2 , chunk[1]]
    
    seat = chunk[0]
            
    seat_ids[i] = int((row * 8) + seat)

part_one()
part_two()