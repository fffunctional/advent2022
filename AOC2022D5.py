# Supply Stacks

test_data = [
	['Z', 'N'],
	['M', 'C', 'D'],
	['P']
]

test_instructions = [
	'move 1 from 2 to 1',
	'move 3 from 1 to 3',
	'move 2 from 2 to 1',
	'move 1 from 1 to 2'
]

data = [
	['D','L','V','T','M','H','F'],
	['H','Q','G','J','C','T','N','P'],
	['R','S','D','M','P','H'],
	['L','B','V','F'],
	['N','H','G','L','Q'],
	['W','B','D','G','R','M','P'],
	['G','M','N','R','C','H','L','Q'],
	['C','L','W'],
	['R','D','L','Q','J','Z','M','T']
]

input = open("adventofcode.com_2022_day_5_input.txt").read().strip()
lines = input.split("\n")

import re
import copy

parsed = [re.match(r"move (\d+) from (\d+) to (\d+)", i) for i in lines if i.startswith('move')]

def get_info(p):
	move_n = int(p.group(1))
	from_n = int(p.group(2)) - 1
	to_n   = int(p.group(3)) - 1
	return move_n, from_n, to_n

d5_data = copy.deepcopy(data)
for p in parsed:
	move_n, from_n, to_n = get_info(p)
	for i in range(move_n):
	    d5_data[to_n].append(d5_data[from_n].pop())

result = [d.pop() for d in d5_data]

# part2

pt2_data = copy.deepcopy(data)

for p in parsed:
    move_n, from_n, to_n = get_info(p)
    pt2_data[to_n] = pt2_data[to_n] + pt2_data[from_n][-move_n:]
    del pt2_data[from_n][-move_n:]

result = [d.pop() for d in pt2_data if d]

print(''.join(result))