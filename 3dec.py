import math

def priority(c):
    raw = ord(c)
    if raw - ord('a') < 0:
        return 27 + raw - ord('A')

    return 1 + raw - ord('a')

def parse_compartments(line):
    size = math.floor(len(line) / 2)
    return line[:size], line[size:]

def common_item(groups):
    intersection = set(groups[0])
    for i in range(1, len(groups)):
        intersection = intersection.intersection(set(groups[i]))

    assert len(intersection) == 1

    return list(intersection)[0]


f = open('input_3dec.txt', 'r')

backpacks = list(map(lambda s: s.strip('\n'), f.readlines()))
part_1 = sum(map(priority, map(common_item, map(parse_compartments, backpacks))))

groups = [backpacks[i:i+3] for i in range(0, len(backpacks), 3)]
badges = map(common_item, groups)
part_2 = sum(map(priority, badges))

print("Part 1: %d" % part_1)
print("Part 2: %d" % part_2)
