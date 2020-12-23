def part_one():
    print("---- Part One ----")
    sum = 0
    for g in groups:
        sum += len(g)
    print("Total answers: " + str(sum))

def part_two():
    print("---- Part Two ----")
    sum = 0
    for g in agreed_groups:
        sum += len(g)
    print("Total agreed answers: " + str(sum))

groups_input = open("days\\day_6\\input.txt", "r").read().split("\n\n")
groups = [None] * len(groups_input)

for i in range(len(groups_input)):
    g = groups_input[i].replace("\n", "")
    answers = [""] * len(g)
    for j in range(len(g)):
        c = g[j]
        if c not in answers:
            answers[j] = c
        
    answers = list(filter(len, answers))
    groups[i] = answers

agreed_groups = [""] * len(groups_input)

for i in range(len(groups_input)):
    people = groups_input[i].splitlines()
    agreed_answers = ""
    for c in people[0]:
        agreed = True
        for k in range(1, len(people)):
            if c not in people[k]:
                agreed = False
        if agreed:
            agreed_groups[i] += c
            
    

part_one()
part_two()