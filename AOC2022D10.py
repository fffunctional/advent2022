# Cathode-Ray Tube

small_program = """noop
addx 3
addx -5""".split("\n")

larger_program = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".split("\n")

input = open("adventofcode.com_2022_day_10_input.txt").read().strip().split("\n")

def get_signal_strengths(program):
    x = 1
    signal_strengths = []
    cycle = 0
    for instruction in program:
        if instruction == "noop":
            cycle += 1
            signal_strengths.append(x * cycle)
        else:
            addx, n = instruction.split(" ")
            cycle += 1
            signal_strengths.append(x * cycle)
            cycle += 1
            signal_strengths.append(x * cycle)
            x += int(n)
    return signal_strengths

test_signals = get_signal_strengths(larger_program)
assert sum(test_signals[19::40]) == 13140

signals = get_signal_strengths(input)
print(sum(signals[19::40]))

def add_pixel(x, cycle, readout):
    cycle += 1
    if cycle % 40 == 0:
        cycle = 0
        readout += "\n"
    if abs(cycle - x) <= 1:
        readout += "#"
    else:
        readout += " "
    return cycle, readout

def draw(program):
    x = 1 # x is the (centre of the) sprite position
    cycle = -1
    readout = ""
    for instruction in program:
        cycle, readout = add_pixel(x, cycle, readout)
        if instruction != "noop":
            cycle, readout = add_pixel(x, cycle, readout)
            addx, n = instruction.split(" ")
            x += int(n)
    print(readout)

draw(input)

###  ###    ##  ##  ####  ##   ##  ###  
#  # #  #    # #  #    # #  # #  # #  # 
###  #  #    # #  #   #  #    #  # #  # 
#  # ###     # ####  #   # ## #### ###  
#  # #    #  # #  # #    #  # #  # #    
###  #     ##  #  # ####  ### #  # #  