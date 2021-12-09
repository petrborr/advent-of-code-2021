from collections import defaultdict

with open('input.txt') as f:
    horizontal_vertical = defaultdict(int)
    horizontal_vertical_diagonal = defaultdict(int)
    for line in f:
        start, end = line.split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        dx = x2 - x1
        dy = y2 - y1
        for i in range(1 + max(abs(dx), abs(dy))):
            if dx > 0:
                x = x1 + 1 * i
            elif dx == 0:
                x = x1
            elif dx < 0:
                x = x1 - 1 * i

            if dy > 0:
                y = y1 + 1 * i
            elif dy == 0:
                y = y1
            elif dy < 0:
                y = y1 - 1 * i

            if x1 == x2 or y1 == y2:
                horizontal_vertical[x, y] += 1
            horizontal_vertical_diagonal[x, y] += 1

    solution1 = len([x for x in horizontal_vertical if horizontal_vertical[x] > 1])
    solution2 = len([x for x in horizontal_vertical_diagonal if horizontal_vertical_diagonal[x] > 1])
    print(solution1)
    print(solution2)
