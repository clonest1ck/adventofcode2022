from functools import total_ordering

@total_ordering
class Range:
    def __init__(self, start, end):
        self._start = int(start)
        self._end = int(end)

    def covers(self, other):
        return self._start <= other._start and other._end <= self._end

    def overlap(self, other):
        return self._start <= other._start and other._start <= self._end

    def __lt__(self, other):
        if self._start == other._start:
            return self._end > other._end

        return self._start < other._start

class Section:
    def __init__(self, line):
        self._ranges = sorted(list(map(lambda r: Range(r[0], r[1]), map(lambda l: l.split('-'), line.strip('\n').split(',')))))

    def is_one_range(self):
        return self._ranges[0].covers(self._ranges[1])

    def has_overlap(self):
        return self._ranges[0].overlap(self._ranges[1])

sections = []

with open('input_4dec.txt', 'r') as f:
    sections = list(map(lambda l: Section(l), f.readlines()))

part_1 = sum(map(lambda section: section.is_one_range(), sections))
part_2 = sum(map(lambda section: section.has_overlap(), sections))

print("Part 1: %d" % part_1)
print("Part 2: %s" % part_2)
