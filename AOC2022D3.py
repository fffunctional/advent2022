# Rucksack Reorg

input = open("adventofcode.com_2022_day_3_input.txt").read().strip()
lines = input.split("\n")

from itertools import chain
from string import ascii_lowercase, ascii_uppercase

def bisect(line):
	halfway_point = len(line)//2
	return line[:halfway_point], line[halfway_point:]

rucksacks = map(bisect, lines)
shared = list(chain(*[set(c1)&set(c2) for c1, c2 in rucksacks]))

priorities = '0' + ascii_lowercase + ascii_uppercase

p_values = [priorities.index(char)for char in shared]

print(sum(p_values))

# part 2

def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
groups = list(divide_chunks(lines, 3)) 
shared = list(chain(*[set(g[0])&set(g[1])&set(g[2]) for g in groups]))
p_values = [priorities.index(char)for char in shared]
print(sum(p_values))