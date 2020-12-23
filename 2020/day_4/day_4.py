import re

class Passport:
    byr = ""
    iyr = ""
    eyr = ""
    hgt = ""
    hcl = ""
    ecl = ""
    pid = ""
    cid = ""

    def valid(self):
        return len(self.byr) > 0 and len(self.iyr) > 0 and len(self.eyr) > 0 and len(self.hgt) > 0 and len(self.hcl) > 0 and len(self.ecl) > 0 and len(self.pid) > 0

    def valid_2(self):
        return self.byr_valid() and self.iyr_valid() and self.eyr_valid() and self.hgt_valid() and self.hcl_valid() and self.ecl_valid() and self.pid_valid()

    def byr_valid(self):
        if self.byr == "":
            return False

        byr_int = int(self.byr)
        return len(self.byr) == 4 and byr_int >= 1920 and byr_int <= 2002

    def iyr_valid(self):
        if self.iyr == "":
            return False

        iyr_int = int(self.iyr)
        return len(self.iyr) == 4 and iyr_int >= 2010 and iyr_int <= 2020
    
    def eyr_valid(self):
        if self.eyr == "":
            return False

        eyr_int = int(self.eyr)
        return len(self.eyr) == 4 and eyr_int >= 2020 and eyr_int <= 2030

    def hgt_valid(self):
        if "cm" in self.hgt:
            hgt_val = int(self.hgt[:-2])
            return hgt_val >= 150 and hgt_val <= 193
        elif "in" in self.hgt:
            hgt_val = int(self.hgt[:-2])
            return hgt_val >= 59 and hgt_val <= 76
        else:
            return False

    def hcl_valid(self):
        return re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.hcl)

    def ecl_valid(self):
        return self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def pid_valid(self):
        if self.pid == "" or re.search(r'.*[a-zA-Z].*', self.pid):
            return False

        return int(self.pid) > 0 and len(self.pid) == 9


def part_one():
    print("---- Part One ----")
    valid = 0
    for p in passports:
        if p.valid():
            valid += 1
    print("Valid Passports: " + str(valid))

def part_two():
    print("---- Part Two ----")
    valid = 0
    for p in passports:
        if p.valid_2():
            valid += 1
    print("Valid Passports: " + str(valid))

groups = open("days\\day_4\\input.txt", "r").read().split("\n\n")
passports = [None] * len(groups)

for i in range(len(groups)):
    p = Passport()
    g_parts = re.split(" |\n", groups[i])
    for part in g_parts:
        part_parts = part.split(":")
        setattr(p, part_parts[0], part_parts[1])
    passports[i] = p

part_one()
part_two()