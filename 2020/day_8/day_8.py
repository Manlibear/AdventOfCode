
class Line:
    def __init__(self, command, argument, visited = False):
        self.cmd = command
        self.arg = argument
        self.vstd = visited

    def copy(self):
        return Line(self.cmd, self.arg)

    cmd = ""
    arg = 0
    vstd = False

def part_one():
    print("---- Part One ----")
    print("Pre-loop ACC: " + str(preloop_acc))

def part_two():
    print("---- Part Two ----")
    print("Final ACC: " + str(acc))

def try_until_loop(version):
    global acc
    global preloop_acc
    i = 0

    while(not version[i].vstd):
        version[i].vstd = True
        if version[i].cmd == "jmp":
            i+= version[i].arg
        elif version[i].cmd == "acc":
            acc += version[i].arg
            i += 1
        elif version[i].cmd == "nop":
            i += 1
        elif version[i].cmd == "end":
            return True

    if preloop_acc == 0:
        preloop_acc = acc

    return False

def change_line(version, i):
    if version[i].cmd == "nop":
        version[i].cmd = "jmp"
    elif version[i].cmd == "jmp":
        version[i].cmd = "nop"


lines = open("days\\day_8\\input.txt", "r").read().splitlines()

acc = 0
preloop_acc = 0
program = []

for l in lines:
    l_parts = l.split(" ")
    program.append(Line(l_parts[0], int(l_parts[1])))
    
program.append(Line("end", 0))

i = 0

while(i < len(program)):
    acc = 0
    version = [line.copy() for line in program]
    change_line(version, i)
    if try_until_loop(version):
        break
    else:
        i += 1

part_one()
part_two()