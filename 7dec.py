from enum import Enum
from functools import reduce, total_ordering
import operator

@total_ordering
class Node:
    class NodeType(Enum):
        DIRECTORY = 1
        FILE = 2

    def __init__(self, nodetype : NodeType, name : str, size : int = 0):
        self._type = nodetype
        self._name = name
        self._size = size

    def size(self):
        return self._size

    def update_size(self, size):
        self._size = size

    def __lt__(self, other):
        return self._size < other.size()

class File(Node):
    def __init__(self, name, size):
        super().__init__(Node.NodeType.FILE, name, size)

class Directory(Node):
    def __init__(self, name):
        super().__init__(Node.NodeType.DIRECTORY, name)
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def size(self):
        size = 0
        for child in self._children:
            size += child.size()
        super().update_size(size)
        return size

def parse(line, parent_dir):
    sections = line.strip('\n').split(' ')

    if len(sections) == 3:
        if sections[1] == "cd":
            if sections[2] == "..":
                return parent_dir
            else:
                return Directory(sections[2])
    elif len(sections) == 2:
        try:
            size = int(sections[0])
            return File(sections[1], size)
        except ValueError as e:
            pass

    return None


path = []
filesystem = None

with open('input_7dec.txt', 'r') as f:
    for line in f:
        node = None
        if len(path) > 1:
            node = parse(line, path[-2])
        else:
            node = parse(line, None)

        if not node: # ls
            continue
        elif node._type == Node.NodeType.DIRECTORY:
            if len(path) == 0:
                path.append(node)
                filesystem = node
                continue
            elif len(path) > 1 and node._name == path[-2]._name:
                path.pop()
                continue

            if not node in path[-1]._children:
                path[-1].add_child(node)
            path.append(node)
        elif node._type == Node.NodeType.FILE:
            path[-1].add_child(node)


def get_filter_fun_for_size(size, op):
    def is_dir_with_correct_size(node):
        return node._type == Node.NodeType.DIRECTORY and op(node.size(), size)
    return is_dir_with_correct_size

def get_nodes(node, filter_fun):
    if filter_fun(node):
        yield node

    if node._type == Node.NodeType.DIRECTORY:
        for child in node._children:
            yield from get_nodes(child, filter_fun)

def nodesize(a):
    if isinstance(a, Node):
        return a.size()
    return a

part_1 = reduce(lambda x, y: nodesize(x) + nodesize(y), get_nodes(filesystem, get_filter_fun_for_size(100000, operator.lt)))
part_2 = sorted(get_nodes(filesystem, get_filter_fun_for_size(30000000 - (70000000 - filesystem.size()), operator.ge)))[0]

print("Part 1: %d" % part_1)
print("Part 2: %d" % part_2.size())
