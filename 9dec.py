
class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __hash__(self):
        return hash(self.__str__())

    def delta(self, other):
        return (self.x - other.x, self.y - other.y)

    def add(self, other):
        self.x += other.x
        self.y += other.y

def calculate_tail_move(head, tail):
    dx, dy = head.delta(tail)
    sign_dx = -1 if dx < 0 else 1
    sign_dy = -1 if dy < 0 else 1

    dx = abs(dx)
    dy = abs(dy)

    if dx + dy >= 3:
        return Point(sign_dx, sign_dy)
    if dx > 1 and dx + dy > 1:
        return Point(sign_dx, 0)
    if dy > 1 and dx + dy > 1:
        return Point(0, sign_dy)

    return Point(0, 0)

def step(knots, delta, visited):
    knots[0].add(delta)
    for i in range(1, len(knots)):
        head = knots[i-1]
        tail = knots[i]

        tail.add(calculate_tail_move(head, tail))
    visited.add(knots[-1])

def move(knots, x, y, visited):
    dx = -1 if x < 0 else 1 if x > 0 else 0
    dy = -1 if y < 0 else 1 if y > 0 else 0

    for x in range(abs(x)):
        step(knots, Point(dx, 0), visited)
    for y in range(abs(y)):
        step(knots, Point(0, dy), visited)


knots_part_1 = [Point(0,0) for i in range(2)]
visited_part_1 = set()

knots_part_2 = [Point(0,0) for i in range(10)]
visited_part_2 = set()

with open("input_9dec.txt", "r") as f:
    for line in f:
        direction, delta = line.strip('\n').split(' ')
        delta = int(delta)
        dx = 0
        dy = 0

        if direction == "U":
            dy = delta
        elif direction == "D":
            dy = -delta
        elif direction == "R":
            dx = delta
        elif direction == "L":
            dx = -delta

        move(knots_part_1, dx, dy, visited_part_1)
        move(knots_part_2, dx, dy, visited_part_2)

        knots = [str(knot) for knot in knots_part_2]

part_1 = len(visited_part_1)
part_2 = len(visited_part_2)
print("Part 1: %d" % part_1)
print("Part 2: %d" % part_2)

