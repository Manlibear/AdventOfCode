import re

def part_one():
    print("---- Part One ----")
    outer_bags = []
    count_parents("shiny gold", outer_bags)
    print("Total outer bags: " + str(len(outer_bags)))

def part_two():
    print("---- Part Two ----")
    total_bags = count_children(bag_rules["shiny gold"], 1)
    print("Total inner bags: " + str(total_bags - 1))


def count_parents(bag, outer_bags):
    bags = [outer for outer, inners in bag_rules.items() if bag in [x[1] for x in inners]]
    for b in bags:
        if b not in outer_bags:
            outer_bags.append(b)
            count_parents(b, outer_bags)

def count_children(bag, count):
    level_count = count
    for b in bag:
        count += count_children(bag_rules[b[1]], int(b[0]) * level_count)
    
    return count

lines = open("days\\day_7\\input.txt", "r").read().splitlines()

bag_rules = {}

for l in lines:
    l_parts = l.split(" contain ")
    bags = l_parts[1].split(",")
    bags = re.findall(r'(\d) ([a-zA-Z]+\s[a-zA-Z]+)', l_parts[1])
    outer_bag = l_parts[0][:-5]
    bag_rules[outer_bag] = bags

part_one()
part_two()