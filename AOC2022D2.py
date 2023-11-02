# Rock Paper Scissors

input = open("adventofcode.com_2022_day_2_input.txt").read().strip()
lines = input.split("\n")
moves = [tuple(l.split(" ")) for l in lines]

def result(they, you, part=1):
	shape_value = {
		'X': 1, 'Y': 2, 'Z': 3
	}
	win_value = {
		'AX': 3, 'BY': 3, 'CZ': 3,
		'AY': 6, 'BZ': 6, 'CX': 6,
		'AZ': 0, 'BX': 0, 'CY': 0
	}

	if part == 1:
		return shape_value[you] + win_value[they+you]

	if part == 2:
		your_move = calculate_your_move(they+you)
		return shape_value[your_move] + win_value[they+your_move]

def calculate_your_move(input):
	your_moves = {
		'AX': 'Z', 'BX': 'X', 'CX': 'Y',
		'AY': 'X', 'BY': 'Y', 'CY': 'Z',
		'AZ': 'Y', 'BZ': 'Z', 'CZ': 'X'
	}
	return your_moves[input]

def get_score(moves, part=1):
	score = 0
	for they, you in moves:
	    score += result(they, you, part)
	return score

test_moves = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
assert get_score(test_moves) == 15	
assert get_score(test_moves, part=2) == 12

print(get_score(moves, part=2))