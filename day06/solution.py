from collections import defaultdict

with open('input.txt') as f:
    lanternfish = [int(x) for x in f.read().split(',')]
    days = 256

    fish_types = defaultdict(int)
    for f in lanternfish:
        fish_types[f] += 1

    for d in range(days):
        y = defaultdict(int)
        for t, c in fish_types.items():
            if t == 0:
                y[6] += c
                y[8] += c
            else:
                y[t-1] += c
        fish_types = y
print(sum(fish_types.values()))

