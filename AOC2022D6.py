# Tuning Trouble

input = open("adventofcode.com_2022_day_6_input.txt").read().strip()

def detect_marker(str, length=4):
    i = length
    while len(set(list(str[i-length:i]))) != length:
        i += 1
    return i   

assert(detect_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb")) == 7
assert(detect_marker("bvwbjplbgvbhsrlpgdmjqwftvncz")) == 5
assert(detect_marker("nppdvjthqldpwncqszvftbrmjlhg")) == 6
assert(detect_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")) == 10
assert(detect_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")) == 11

print(detect_marker(input))

# part 2

assert(detect_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14)) == 19
assert(detect_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)) == 23
assert(detect_marker("nppdvjthqldpwncqszvftbrmjlhg", 14)) == 23
assert(detect_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14)) == 29
assert(detect_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14)) == 26

print(detect_marker(input, 14))
