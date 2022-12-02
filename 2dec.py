
from enum import IntEnum

class Result(IntEnum):
    LOOSE = -1
    DRAW = 0
    WIN = 1

    @staticmethod
    def fromString(s):
        if s == 'X':
            return Result.LOOSE
        if s == 'Y':
            return Result.DRAW
        if s == 'Z':
            return Result.WIN

        raise ValueError("Unkown string: %s" % s)

class RPS(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def cmp(lhs, rhs):
        if lhs == RPS.ROCK:
            if rhs == RPS.SCISSORS:
                return -1
            elif rhs == RPS.PAPER:
                return 1
            else:
                return 0

        elif lhs == RPS.PAPER:
            if rhs == RPS.ROCK:
                return -1
            elif rhs == RPS.SCISSORS:
                return 1
            else:
                return 0

        elif lhs == RPS.SCISSORS:
            if rhs == RPS.PAPER:
                return -1
            elif rhs == RPS.ROCK:
                return 1
            else:
                return 0

        raise ValueError("Unkown lhs: %d" % lhs)

    @staticmethod
    def fromString(s):
        if s == 'A' or s == 'X':
            return RPS.ROCK
        if s == 'B' or s == 'Y':
            return RPS.PAPER
        if s == 'C' or s == 'Z':
            return RPS.SCISSORS

        raise ValueError("Unkown string: %s" % s)


    @staticmethod
    def round(opponent, me):
        result = RPS.cmp(opponent, me)
        score = 3 + (3 * result) + int(me)
        return score

    @staticmethod
    def calculateChoice(opponent, result):
        for choice in [RPS.ROCK, RPS.PAPER, RPS.SCISSORS]:
            if int(result) == RPS.cmp(opponent, choice):
                return choice

        raise ValueError("Failed to choose: %s" % result)

f = open('input_2dec.txt')

total_score_part_1 = 0
total_score_part_2 = 0

for line in f:
    opponent, me = list(map(RPS.fromString, line[:-1].split(' ')))
    total_score_part_1 += RPS.round(opponent, me)

    opponent_s, result_s = line[:-1].split(' ')
    opponent = RPS.fromString(opponent_s)
    result = Result.fromString(result_s)
    me = RPS.calculateChoice(opponent, result)
    total_score_part_2 += RPS.round(opponent, me)

print("Part 1: %d" % total_score_part_1)
print("Part 2: %d" % total_score_part_2)
