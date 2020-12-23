def part_one():
    print("---- Part One ----")
    global first_invalid
    for d in data:
        int_d = int(d)
        if int_d not in valid_data:
            first_invalid = int_d
            break
        else:
            preamble.pop(0)
            preamble.append(int_d)
            process_valid_data()
    print("First Invalid: " + d)

def part_two():
    print("---- Part Two ----")
    global first_invalid
    weakness_test = []
    for d in lines:
        int_d = int(d)

        if int_d > first_invalid:
            print("Failed to find weakness")
            break 

        weakness_test.append(int_d)
        weakness_sum = sum(weakness_test)
        success = weakness_sum == first_invalid

        if weakness_sum > first_invalid:
            while weakness_sum > first_invalid:
                weakness_test.pop(0)
                weakness_sum = sum(weakness_test)
            success = weakness_sum == first_invalid

        if success:
            print("Weakness: " + str(min(weakness_test) + max(weakness_test)))
            break


lines = open("days\\day_9\\input.txt", "r").read().splitlines()

preamble = lines[:25]
data = lines[25:]
valid_data = []
first_invalid = 0

def list_sums(L):
    if len(L) == 0:return []
    return L+list((L[index] + rest) for index in range(len(L)) for rest in list_sums(L[:index])+L[index+1:])

def process_valid_data():
    valid_data.clear()
    for i in range(len(preamble)):
        for j in range(len(preamble)):
            if i != j :
                s = int(preamble[i]) + int(preamble[j])
                if s not in valid_data:
                    valid_data.append(s)
    

process_valid_data()


part_one()
part_two()