# Monkey in the Middle

class Monkey:
    def __init__(self, operation, test, items, t, f):
        self.operation = operation
        self.test = test
        self.items = items
        self.t = t
        self.f = f
        self.inspected = 0

monkey0 = Monkey(lambda n: n * 19, lambda n: n % 23 == 0, [79, 98, 2, 3])
monkey1 = Monkey(lambda n: n + 6,  lambda n: n % 19 == 0, [54, 65, 75, 74], 2, 0)
monkey2 = Monkey(lambda n: n * n,  lambda n: n % 13 == 0, [79, 60, 97], 1, 3)
monkey3 = Monkey(lambda n: n + 3,  lambda n: n % 17 == 0, [74], 0, 1)

monkeys = [monkey0, monkey1, monkey2, monkey3]

input = open("adventofcode.com_2022_day_11_input.txt").read().strip().split("\n\n")
monkeys = {}
for i in range(len(input)):
    monkey_data = input[i].split("\n")
    starting_items = [int(n) for n in monkey_data[1].split(":")[1].split(",")]
    operation = monkey_data[2].split(" ")[-2:]
    operator, v = operation
    if v == "old":
        op = lambda n: n * n
    elif operator == "*":
        op = lambda n, v=int(v): n * v
    elif operator == "+":
        op = lambda n, v=int(v): n + v
    divisor = int(monkey_data[3].split(" ")[-1])
    test = lambda n, divisor=divisor: n % divisor == 0
    t = int(monkey_data[4].split(" ")[-1])
    f = int(monkey_data[5].split(" ")[-1])
    monkeys[i] = Monkey(op, test, starting_items, t, f)

for round in range(10000):
    for monkey in monkeys.values():
        while monkey.items:
            item = monkey.items.pop(0)
            monkey.inspected += 1
            new_worry_level = monkey.operation(item) % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
            if monkey.test(new_worry_level):
                monkeys[monkey.t].items.append(new_worry_level)
            else:
                monkeys[monkey.f].items.append(new_worry_level)
        for i in monkeys:
            print(i, monkeys[i].items)    

a, b = sorted([monkey.inspected for monkey in monkeys.values()])[-2:]
print(a*b)
