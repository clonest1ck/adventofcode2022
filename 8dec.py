
from functools import reduce

def visible_trees_from_outside(forrest):
    size_y = len(forrest)
    size_x = len(forrest[0])

    visible_x = []
    visible_y = []


    for y in range(size_y):
        max_x_l = -1
        max_x_r = -1

        visible_row = [False for x in range(size_x)]
        for x in range(size_x):
            if max_x_l < forrest[y][x]:
                max_x_l = forrest[y][x]
                visible_row[x] = True

            if max_x_r < forrest[y][-(x+1)]:
                max_x_r = forrest[y][-(x+1)]
                visible_row[-(x+1)] = True

            if max_x_l == 9 and max_x_r == 9:
                break

        visible_x.append(visible_row)

    for x in range(size_x):
        max_y_t = -1
        max_y_b = -1

        visible_col = [False for x in range(size_y)]
        for y in range(size_y):
            if max_y_t < forrest[y][x]:
                max_y_t = forrest[y][x]
                visible_col[y] = True

            if max_y_b < forrest[-(y+1)][x]:
                max_y_b = forrest[-(y+1)][x]
                visible_col[-(y+1)] = True

            if max_y_t == 9 and max_y_b == 9:
                break

        visible_y.append(visible_col)

    visible_trees = 0
    for x in range(size_x):
        for y in range(size_y):
            if visible_x[y][x] or visible_y[x][y]:
                visible_trees += 1

    return visible_trees

def scenic_score(x, y, forrest):
    size_x = len(forrest[0])
    size_y = len(forrest)

    treehouse_height = forrest[y][x]
    scores = [0, 0, 0, 0]
    done = [False, False, False, False]


    for dx in range(1, size_x):
        min_x = x - dx
        max_x = x + dx

        if min_x >= 0 and not done[0]:
            scores[0] += 1

            if forrest[y][min_x] >= treehouse_height:
                done[0] = True

        if max_x < size_x and not done[1]:
            scores[1] += 1

            if forrest[y][max_x] >= treehouse_height:
                done[1] = True


        if (min_x < 0 or done[0]) and (max_x >= size_x or done[1]):
            break


    for dy in range(1, size_y):
        min_y = y - dy
        max_y = y + dy

        if min_y >= 0 and not done[2]:
            scores[2] += 1

            if forrest[min_y][x] >= treehouse_height:
                done[2] = True

        if max_y < size_y and not done[3]:
            scores[3] += 1

            if forrest[max_y][x] >= treehouse_height:
                done[3] = True

        if (min_y < 0 or done[2]) and (max_y >= size_y or done[3]):
            break

    return reduce(lambda a, b: a * b, scores)

forrest = []
with open('input_8dec.txt', 'r') as f:
    for line in f:
        forrest.append(list(map(int, list(line.strip('\n')))))

part_1 = visible_trees_from_outside(forrest)

max_scenic_score = 0
for y in range(len(forrest)):
    for x in range(len(forrest[0])):
        score = scenic_score(x, y, forrest)
        if score > max_scenic_score:
            max_scenic_score = score

print("Part 1: %d" % part_1)
print("Part 2: %d" % max_scenic_score)
