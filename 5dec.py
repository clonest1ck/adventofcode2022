

class Stacks:
    def __init__(self, data):
        stacks_count = 9
        spacing = 4
        self._stacks = [[] for i in range(stacks_count)]
        for l in range(0, len(data) - 1):
            for i in range(0, stacks_count):
                s = 1 + (i * spacing)
                if len(data[l]) < s or data[l][s] == ' ':
                    continue

                container = data[l][s]
                self._stacks[i].insert(0, container)

    def move(self, src, dest, count, one_at_a_time = True):
        src -= 1
        dest -= 1

        assert src >= 0
        assert dest < len(self._stacks)
        assert count <= len(self._stacks[src])

        if one_at_a_time:
            for i in range(count):
                self._stacks[dest].append(self._stacks[src].pop())
        else:
            self._stacks[dest].extend(self._stacks[src][-count:])
            self._stacks[src] = self._stacks[src][:-count]

    def __str__(self):
        top_crates = [stack[-1] for stack in self._stacks]
        return "".join(top_crates)

stacks_input = []
parsing_stacks = True
moves = []

with open('input_5dec.txt', 'r') as f:
    for line in f:
        if line[0] == '\n':
            parsing_stacks = False
            continue

        if parsing_stacks:
            stacks_input.append(line)
        else:
            move_line = line.split(' ')
            moves.append((int(move_line[3]), int(move_line[5]), int(move_line[1])))

stacks = Stacks(stacks_input)

for move in moves:
    stacks.move(move[0], move[1], move[2])

print("Part 1: %s" % stacks)

stacks = Stacks(stacks_input)

for move in moves:
    stacks.move(move[0], move[1], move[2], False)

print("Part 2: %s" % stacks)
