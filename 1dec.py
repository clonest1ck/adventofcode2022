

f = open('input_1dec.txt', 'r')

elves = []

current = []
for line in f:
    if line == '\n':
        elves.append(current)
        current = []
        continue

    current.append(int(line))

by_calorie_count = list(reversed(sorted(map(lambda elf: sum(elf), elves))))
max_calories = by_calorie_count[0]
top_three = sum(by_calorie_count[0:3])
print("Part 1: %d" % max_calories)
print("Part 2: %d" % top_three)
