# Rope Bridge

test_instructions = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")

input = open("adventofcode.com_2022_day_9_input.txt").read().strip().split("\n")

instructions = [tuple(line.split(" ")) for line in input]

head_pos = (0, 0)
tail_pos = (0, 0)
visited = [(0, 0)]

def touching(head_pos, tail_pos):
    h_x, h_y = head_pos
    t_x, t_y = tail_pos
    if abs(h_x - t_x) < 2 and abs(h_y - t_y) < 2:
        return True

def catchup(head_pos, tail_pos):
    if touching(head_pos, tail_pos):
        return tail_pos

    h_x, h_y = head_pos
    t_x, t_y = tail_pos

    # if head and tail are lined up we move the tail one space towards the head    
    if h_x == t_x:
        return (t_x, t_y + (1 if h_y > t_y else -1))
    if h_y == t_y:
        return (t_x + (1 if h_x > t_x else -1), h_y)

    # otherwise we always move the tail diagonally towards the head    
    return (t_x + (1 if h_x > t_x else -1), t_y + (1 if h_y > t_y else -1))


def move(d):
    current_x, current_y = head_pos
    h_new_x, h_new_y = head_pos
    if d == 'U':
        h_new_x = current_x + 1
    elif d == 'D':
        h_new_x = current_x - 1
    elif d == 'L':
        h_new_y = current_y - 1
    elif d == 'R':
        h_new_y = current_y + 1
    new_head_pos = (h_new_x, h_new_y)
    new_tail_pos = catchup(head_pos, tail_pos)
    if not tail_pos in visited:
        visited.append(tail_pos)
    return new_head_pos, new_tail_pos


for direction, distance in instructions:
    for i in range(int(distance)):
        head_pos, tail_pos = move(direction)

print(len(visited))

# part 2

visited = [(0,0)]
new_test_instructions = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split("\n")

new_test_instructions = [tuple(line.split(" ")) for line in new_test_instructions]

def move2(d):
    old_positions = [pos for pos in positions]
    new_positions = positions
    current_x, current_y = positions[0]
    h_new_x, h_new_y = positions[0]
    if d == 'U':
        h_new_x = current_x + 1
    elif d == 'D':
        h_new_x = current_x - 1
    elif d == 'L':
        h_new_y = current_y - 1
    elif d == 'R':
        h_new_y = current_y + 1
    new_positions[0] = (h_new_x, h_new_y)
    for i in range(1, 10):
        new_positions[i] = catchup(new_positions[i-1], new_positions[i])
    if not new_positions[9] in visited:
        visited.append(new_positions[9])
    return new_positions

positions = [(0, 0)] *10
for direction, distance in instructions:
    for i in range(int(distance)):
        positions = move2(direction)

print(len(visited))