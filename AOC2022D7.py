# No Space Left on Device

test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split("\n")

input = open("adventofcode.com_2022_day_7_input.txt").read().strip().split("\n")

import re

current_node = None
# a node is [the current name, the parent, the children, and the non-directory files]
for command in input:
    m = re.match(r"\$ cd (.+)", command)
    if m:
        d = m.groups(1)[0]
        if d == "/":
            current_node = ["/", None, [], []]
        elif d == "..":
            current_node = current_node[1]
        else:
            existing_node = next((n for n in current_node[2] if n[0] == d), None)
            if not existing_node:
                new_node = [d, current_node, [], []]
                current_node[2].append(new_node)
            current_node = existing_node or new_node
    m = re.match(r"dir (.+)", command)
    if m:
        d = m.groups(1)[0]
        existing_node = next((n for n in current_node[2] if n[0] == d), None)
        if not existing_node:
            new_node = [d, current_node, [], []]
            current_node[2].append(new_node)
    m = re.match(r"(\d+) (.+)", command)
    if m:
        filesize = int(m.groups(1)[0])
        filename = m.groups(1)[1]
        if (filename, filesize) not in current_node[3]:
            current_node[3].append((filename, filesize))

head = current_node[1]

def filesize(node):
    return sum([v for k, v in node[3]]) + sum([filesize(n) for n in node[2]])

result = {}
def traverse_tree(node, indent = ""):
    # print(indent + node[0] + " (" + str(filesize(node)) + ")")
    result[indent + node[0]] = filesize(node)
    for d in node[2]:
        traverse_tree(d, indent + (node[0] if node[0] != '/' else '') + '/')

traverse_tree(head)

print(sum([v for v in result.values() if v <= 100000]))

# part 2

total_disk_space  = 70000000
needed_disk_space = 30000000
used_space = filesize(head)
current_disk_space = total_disk_space - used_space
extra_room_needed = needed_disk_space - current_disk_space

print(sorted([v for v in result.values() if v >= extra_room_needed])[0])

