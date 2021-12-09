def solution1(data):
    zeroes = {}
    ones = {}
    for line in data:
        for k, v in enumerate(line):
            if v == '0':
                if k not in zeroes:
                    zeroes[k] = 1
                else:
                    zeroes[k] += 1
            elif v == '1':
                if k not in ones:
                    ones[k] = 1
                else:
                    ones[k] += 1
    gamma_rate = {}
    epsilon_rate = {}
    for k in zeroes:
        if zeroes[k] > ones[k]:
            gamma_rate[k] = '0'
            epsilon_rate[k] = '1'
        else:
            gamma_rate[k] = '1'
            epsilon_rate[k] = '0'
    gamma_rate = [v for k, v in sorted(gamma_rate.items(), key=lambda x: x[0])]
    epsilon_rate = [v for k, v in sorted(epsilon_rate.items(), key=lambda x: x[0])]
    gamma_rate = ''.join(gamma_rate)
    epsilon_rate = ''.join(epsilon_rate)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def solution1_version2(data):
    zeroes = {}
    ones = {}
    for line in data:
        for k, v in enumerate(line):
            if k not in zeroes:
                zeroes[k] = 0
            if k not in ones:
                ones[k] = 0
            if v == '0':
                zeroes[k] += 1
            elif v == '1':
                ones[k] += 1
    gamma_rate = ''
    epsilon_rate = ''
    for k in zeroes:
        if zeroes[k] > ones[k]:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def find_most_common(data):
    zeroes = {}
    ones = {}
    for line in data:
        for k, v in enumerate(line):
            if k not in zeroes:
                zeroes[k] = 0
            if k not in ones:
                ones[k] = 0
            if v == '0':
                zeroes[k] += 1
            elif v == '1':
                ones[k] += 1

    most_common = ''
    for k in zeroes:
        if ones[k] >= zeroes[k]:
            most_common += '1'
        else:
            most_common += '0'
    return most_common


def find_least_common(data):
    zeroes = {}
    ones = {}
    for line in data:
        for k, v in enumerate(line):
            if k not in zeroes:
                zeroes[k] = 0
            if k not in ones:
                ones[k] = 0
            if v == '0':
                zeroes[k] += 1
            elif v == '1':
                ones[k] += 1

    least_common = ''
    for k in zeroes:
        if ones[k] >= zeroes[k]:
            least_common += '0'
        else:
            least_common += '1'
    return least_common


def solution2(data):
    data1 = data.copy()
    data2 = data.copy()
    oxygen_rating = ''
    co2_rating = ''
    most_common = find_most_common(data1)
    for i in range(len(most_common)):
        data1 = [x for x in data1 if x[i] == most_common[i]]
        most_common = find_most_common(data1)
        if len(data1) == 1:
            oxygen_rating = data1[0]
            break

    least_common = find_least_common(data2)
    for i in range(len(least_common)):
        data2 = [x for x in data2 if x[i] == least_common[i]]
        least_common = find_least_common(data2)
        if len(data2) == 1:
            co2_rating = data2[0]
            break

    return int(oxygen_rating, 2) * int(co2_rating, 2)


if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = f.read().splitlines()
        print(solution1(numbers))
        print(solution2(numbers))
