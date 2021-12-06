def solution1(data):
    """Count the number of increases from given list m."""
    res = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            res += 1
    return res


def solution2(data):
    """Count the number of increases from each sum of 3 number from give list"""
    new_list = [(data[i - 2] + data[i - 1] + data[i]) for i in range(2, len(data))]
    return solution1(new_list)


if __name__ == "__main__":
    with open("input.txt") as f:
        _input = [int(x) for x in f.read().splitlines()]

    print(solution1(_input))
    print(solution2(_input))