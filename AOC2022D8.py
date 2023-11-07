# Treetop Tree House

test_input = """30373
25512
65332
33549
35390""".split("\n")

input = open("adventofcode.com_2022_day_8_input.txt").read().strip().split("\n")

rows = [[*row] for row in input]
cols = [[*row] for row in input]

for i in range(len(rows)):
    for j in range(len(rows[0])):
        cols[j][i] = rows[i][j]

def is_visible(r, c):

    w = rows[r][:c]
    e = rows[r][c+1:]
    n = cols[c][:r]
    s = cols[c][r+1:]

    if r in [0, len(rows)-1] or c in [0, len(cols)-1]:
        return True
    tree_height = rows[r][c]
    return any([tree_height > h for h in [max(w), max(e), max(n), max(s)]])

result = 0
for r in range(len(rows)):
    for c in range(len(cols)):
        if is_visible(r, c):
            result += 1

print(result)

# part 2

def look(from_height, trees):
    score = 0
    for tree in trees:
        score += 1
        if tree >= from_height:
            break
    return score

def scenic_score(r, c):
    from_tree = rows[r][c]

    west   = [t for t in rows[r][:c][::-1]]
    east   = [t for t in rows[r][c+1:]]
    north  = [t for t in cols[c][:r][::-1]]
    south  = [t for t in cols[c][r+1:]]
    
    w_score = look(from_tree, west)
    e_score = look(from_tree, east)
    n_score = look(from_tree, north)
    s_score = look(from_tree, south)

    return n_score * s_score * e_score * w_score

result = 0
for r in range(len(rows)):
    for c in range(len(cols)):
        ss = scenic_score(r, c)
        result = max(ss, result)

print(result)