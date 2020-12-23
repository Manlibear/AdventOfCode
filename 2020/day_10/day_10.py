import numpy as np

def part_one():
    print("---- Part One ----")
    i = 0
    curr_jolt = 0

    while curr_jolt < max(jolt_lines):
        ups = jolt_lines[(jolt_lines > curr_jolt) & (jolt_lines <= (curr_jolt + 3.0))]
        min_up = min(ups)
        diff = int(min_up) - int(curr_jolt)
        jolt_diffs[diff - 1] += 1
        curr_jolt = min_up
        i += 1

    print("1-jolts + 3-jolts = " + str(jolt_diffs[0] * jolt_diffs[2]))

def part_two():
    print("---- Part Two ----")
    ways = [0] * len(jolt_lines)
    
    for i in range(len(jolt_lines)):
        if i == 0:
            ways[0] = 1
        else:
            ways[i] = 0
            for j in range(i, -1, -1):
                if jolt_lines[i] - jolt_lines[j] <= 3:
                    ways[i] += ways[j]
                else:
                    break


    print("Total combinations: " + str(ways[-1]))


jolt_diffs= [0] * 3

lines = open("days\\day_10\\input.txt", "r").read().splitlines()
jolt_lines = np.array([0])

for l in lines:
     jolt_lines = np.append(jolt_lines, int(l))

jolt_lines.sort()
jolt_lines = np.append(jolt_lines, jolt_lines[-1] + 3)

part_one()
part_two()
