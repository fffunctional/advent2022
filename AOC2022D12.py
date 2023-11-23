# # Hill-Climbing Algorithm

rows = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split("\n")

rows = open("adventofcode.com_2022_day_12_input.txt").read().strip().split("\n")
m = [list(row) for row in rows]



# maxy = len(rows[0]) - 1
# maxx = len(rows) - 1

# from string import ascii_lowercase

# from queue import PriorityQueue
# p = PriorityQueue()

# distances = {}
# unvisited = []
# for x in range(len(m)):
#     for y in range(len(m[0])):
#         distances[(x, y)] = float('inf')
#         unvisited.append((x, y))


# distances[(20, 0)] = 0
# unvisited.remove((20, 0))
# p.put((20, 0))

# found = False
# while not found:
#     x, y = p.get()
#     if m[x][y] == 'S':
#         height = ord('a')
#     else:
#         height = ord(m[x][y])
#     next_steps = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
#     for a, b in next_steps:
#         if a < 0 or b < 0 or a > maxx or b > maxy:
#             continue
#         if m[a][b] == 'E':
#             to_height = ord('z')
#         else:
#             to_height = ord(m[a][b])
#         if (a, b) not in unvisited:
#             continue
#         if to_height - height > 1:
#             continue
#         if m[a][b] == 'E':
#             found = True
#             print("found", distances[(x, y)])
#             break
#         p.put((a, b))
#         distances[(a,b)] = distances[(x, y)] + 1
#         unvisited.remove((a, b))

# for x in range(len(m)):
#     row = ""
#     for y in range(len(m[0])):
#         row += str(distances[(x, y)]) + " "
#     print(row + "\n")

# found = False
# while not found:
#     best = min(distances, key=distances.get)
#     x, y = best
#     next_steps = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
#     for a, b in next_steps:
#         if a < 0 or b < 0 or a > maxx or b > maxy:
#             continue
#         if visited[(a,b)]:
#             continue
#         if heights.index(m[a][b]) - heights.index(m[x][y]) > 1:
#             continue
#         if m[a][b] == 'E':
#             found = True
#             print(distances[(x, y)] + 1)
#             break
#         visited[(a, b)] = True
#         distances[(a, b)] = distances[(x, y)] + 1
#         distances[(x, y)] = float('inf')


# def find_the_path(x, y):
#     next_steps = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
#     for a, b in next_steps:
#         if a < 0 or b < 0 or a > maxx or b > maxy:
#             continue
#         if visited[(a,b)]:
#             continue
#         if heights.index(m[a][b]) - heights.index(m[x][y]) > 1:
#             continue
#         if m[a][b] == 'E':
#             found = True
#             return 1
#         else:
#             return find_the_path(a, b) + 1

# print(find_the_path(20, 0))

# found = False
# while paths and not found:
#     p = paths.pop(0)
#     x, y = p[-1]
#     current_at = real_map[x][y]
#     next_steps = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
#     valid = [(a, b) for a, b in next_steps if a >= 0 and b >= 0 and a <= maxx and b <= maxy]
#     for (a, b) in valid:
#         new_at = real_map[a][b]
#         if new_at == 'E' and current_at >= 'y':
#             print("FOUND", p, len(p))
#             found = True
#             break
#         if not (a, b) in p and ((ord(new_at) <= ord(current_at) + 1) or current_at == 'S'):
#             new_path = p.copy()
#             new_path.append((a, b))
#             paths.append(new_path)
#             print(paths)

# breadth-first search

# from queue import PriorityQueue

# q = PriorityQueue()

# visited = {}
# for x in range(len(m)):
#     for y in range(len(m[0])):
#         visited[(x, y)] = False

# distances = {}
# for x in range(len(m)):
#     for y in range(len(m[0])):
#         distances[(x, y)] = float('inf')

# from string import ascii_lowercase
# heights = 'S' + ascii_lowercase + 'E'

# assert m[20][0] == 'S'
# q.put((20, 0), 0)
# visited[(20, 0)] = True
# distances[(20, 0)] = 0
# found = False
# while not found:
#     best_dist = float('inf')
#     candidate = None
#     next_steps = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
#     for a, b in next_steps:
#         if a < 0 or b < 0 or a > maxx or b > maxy:
#             continue
#         if visited[(a,b)]:
#             continue
#         if heights.index(m[a][b]) - heights.index(m[x][y]) > 1:
#             continue
#         if m[a][b] == 'E':
#             found = True
#             print(distances[(x, y)] + 1)
#             break
#         queue.append((a, b))
#         distances[(a,b)] = min(distances[(a, b)], distances[(x, y)] + 1)
#         visited[(a, b)] = True
#     for q in queue:
#         if distances[q] < best_dist:
#             best_dist = distances[q]
#             candidate = q
#     (x, y) = candidate
# while q and not found:
#     x, y = q.get()
#     next_steps = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
#     for a, b in next_steps:
#         if a < 0 or b < 0 or a > maxx or b > maxy:
#             continue
#         if visited[(a,b)]:
#             continue
#         if heights.index(m[a][b]) - heights.index(m[x][y]) > 1:
#             continue
#         if m[a][b] == 'E':
#             found = True
#             print(distances[(x,y)])
#             break
#         alt = 1 + distances[(x, y)]
#         if alt < distances[(a, b)]:
#             distances[(a, b)] = alt
#             q.put((a, b), alt)
#             visited[(a,b)] = True

# pseudocode it

# found = False
# distance = 0
# q = [(20, 0)]
# deadend = True
# while not found:
#     x, y = q.pop(0)
#     print(x, y)
#     visited[(x, y)] = True
#     next_steps = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
#     if not deadend:
#         distance += 1
#         deadend = True
#     for a, b in next_steps:
#         print("a, b", a, b)
#         if a < 0 or b < 0 or a > maxx or b > maxy:
#             continue
#         if visited[(a,b)]:
#             continue
#         if heights.index(m[a][b]) - heights.index(m[x][y]) > 1:
#             continue
#         if m[a][b] == 'E':
#             found = True
#             print(distance)
#             break
#         q.append((a, b))
#         visited[(a, b)] = True
#         deadend = False


# I am at S (distance = 0)
# there are 1 - 4 reachable squares from where I am
# for each reachable square, the distance is 1
# I have visited S

# for each reachable square
# there are 1 - 4 reachable squares from where I am, but not anything visited
# for each reachable square, the distance += 1
# I have visited here

# BFS

def getHeight(char):
    if char == 'S':
        return ord('a')
    if char == 'E':
        return ord('z')
    return ord(char)

def reachable(m, v, cx, cy, nx, ny, reversed = False):
    if nx < 0 or ny < 0:
        return False
    if nx >= len(m) or ny >= len(m[0]):
        return False
    if (nx, ny) in v:
        return False
    f = m[cx][cy]
    t = m[nx][ny]
    fromH = getHeight(f)
    toH = getHeight(t)
    if not reversed:
        inaccessible = toH - fromH > 1
    else:
        inaccessible = fromH - toH > 1
    return not inaccessible

def countSteps(start, goal, reversed = False):
    visited = []
    queue = []
    distances = {}

    queue.append(start)
    visited.append(start)
    distances[start] = 0

    found = False
    while not found and queue:
        cx, cy = queue.pop(0)
        adj = [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]

        nexts = [(a, b) for (a, b) in adj if reachable(m, visited, cx, cy, a, b, reversed)]

        while nexts:
            n = nexts.pop(0)
            nx, ny = n
            if m[nx][ny] == goal:
                return distances[(cx, cy)] + 1
                found = True
            distances[(nx, ny)] = distances[(cx, cy)] + 1
            queue.append(n)
            visited.append(n)

# part 1
print(countSteps((20,0), 'E'))

# part 2
print(countSteps((20,139), 'a', True))
