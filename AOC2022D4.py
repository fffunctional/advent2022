# Camp Cleanup

input = open("adventofcode.com_2022_day_4_input.txt").read().strip()
lines = input.split("\n")

import re

start_ends = [re.match(r"(\d+)-(\d+),(\d+)-(\d+)", l) for l in lines]

def starts_and_ends(match):
	r1_start = int(match.group(1))
	r1_end   = int(match.group(2))
	r2_start = int(match.group(3))
	r2_end   = int(match.group(4))
	return r1_start, r1_end, r2_start, r2_end

def range_contains_range(match):
	r1_start, r1_end, r2_start, r2_end = starts_and_ends(match)
	return ((r1_start <= r2_start <= r2_end <= r1_end) or 
		    (r2_start <= r1_start <= r1_end <= r2_end))

def ranges_overlap(match):
	r1_start, r1_end, r2_start, r2_end = starts_and_ends(match)
	return min(r1_end, r2_end) - max(r1_start, r2_start) + 1 > 0


containments = [se for se in start_ends if range_contains_range(se)]

test_data = ["2-4,6-8","2-3,4-5","5-7,7-9","2-8,3-7","6-6,4-6","2-6,4-8"]
test_start_ends = [re.match(r"(\d+)-(\d+),(\d+)-(\d+)", l) for l in test_data]
test_containments = [se for se in test_start_ends if ranges_overlap(se)]

# part 2

overlaps = [se for se in start_ends if ranges_overlap(se)]

print(len(overlaps))