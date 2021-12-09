def solution1(commands):
    horizontal_position = 0
    depth = 0
    for command in commands:
        direction, distance = command[0], int(command[1])
        if direction == 'forward':
            horizontal_position += distance
        elif direction == 'up':
            depth -= distance
        elif direction == 'down':
            depth += distance

    return horizontal_position * depth


def solution2(commands):
    horizontal_position = 0
    depth = 0
    aim = 0
    for command in commands:
        direction, distance = command[0], int(command[1])
        if direction == 'forward':
            horizontal_position += distance
            depth += aim * distance
        elif direction == 'up':
            aim -= distance
        elif direction == 'down':
            aim += distance

    return horizontal_position * depth


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
        commands = [line.split() for line in lines]
        print(solution1(commands))
        print(solution2(commands))
