# Calorie Counting

# Part 1

input = open("adventofcode.com_2022_day_1_input.txt").read().strip()

elves     = input.split("\n\n")
food      = [elf.split("\n") for elf in elves]
calories  = [list(map(int, item)) for item in food]
totals    = [sum(c) for c in calories]

print(max(totals))

# Part 2

ordered = sorted(totals, reverse=True)
top3 = ordered[:3]

print(sum(top3))