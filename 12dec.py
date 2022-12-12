from queue import PriorityQueue
from functools import total_ordering

@total_ordering
class Node:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = ord(height)

    def __str__(self):
        return "(%d, %d) @ %d" % (self.x, self.y, self.height)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x + self.y < other.x + other.y

def trace(world, is_goal, neighbours, queue, visited = []):
    assert queue.qsize() > 0

    steps, current = queue.get()
    while current in visited:
        assert queue.qsize() > 0
        steps, current = queue.get()

    visited.append(current)

    if is_goal(current):
        return steps

    for neighbour in neighbours(current, world):
        queue.put((steps + 1, neighbour))

    return -1

def goal_part_1(goal):
    return lambda node: node == goal

def goal_part_2(node):
    return node.height == ord('a')

def neighbour_coords(node):
    return [(node.x-1, node.y), (node.x+1, node.y), (node.x, node.y-1), (node.x, node.y+1)]

def neighbours_part_1(node, world):
    ok_moves = [world[coord] for coord in neighbour_coords(node) if coord in world and world[coord].height <= node.height + 1]
    return ok_moves

def neighbours_part_2(node, world):
    ok_moves = [world[coord] for coord in neighbour_coords(node) if coord in world and world[coord].height + 1 >= node.height]
    return ok_moves

world = {}
start = None
goal = None

with open('input_12dec.txt', 'r') as f:
    y = 0
    for line in f:
        x = 0
        for c in line.strip('\n'):
            if c == 'S':
                start = Node(x, y, 'a')
                world[(x, y)] = start
            elif c == 'E':
                goal = Node(x, y, 'z')
                world[(x, y)] = goal
            else:
                world[(x, y)] = Node(x, y, c)

            x += 1
        y += 1

assert start is not None and goal is not None

queue = PriorityQueue()
queue.put((0, start))
visited = []
part_1 = -1
while part_1 < 0:
    part_1 = trace(world, goal_part_1(goal), neighbours_part_1, queue, visited)

visited = []
queue = PriorityQueue()
queue.put((0, goal))
part_2 = -1
while part_2 < 0:
    part_2 = trace(world, goal_part_2, neighbours_part_2, queue, visited)

print("Part 1: %d" % part_1)
print("Part 2: %d" % part_2)
