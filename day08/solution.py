digits = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}


def count_ones_fours_sevens_eights(numbers):
    count = 0
    unique = [2, 3, 4, 7]
    for n in numbers:
        if len(n) in unique:
            count += 1
    return count


def get_signals_to_segments(patterns):
    res = {}
    cf = ''
    bd = ''
    eg = ''

    for p in patterns:
        if len(p) == 2:  # 1
            cf = p

    for p in patterns:
        if len(p) == 3:  # 7
            for char in p:
                if char not in cf:
                    res[char] = 'a'

    for p in patterns:
        if len(p) == 6 and ((cf[0] in p) is not (cf[1] in p)):  # 6
            if cf[0] in p:
                res[cf[0]] = 'f'
                res[cf[1]] = 'c'
            elif cf[1] in p:
                res[cf[1]] = 'f'
                res[cf[0]] = 'c'

    for p in patterns:
        if len(p) == 4:  # 4
            for char in p:
                if char not in cf:
                    bd += char

    for p in patterns:
        if len(p) == 6 and ((bd[0] in p) is not (bd[1] in p)):  # 0
            if bd[0] in p:
                res[bd[0]] = 'b'
                res[bd[1]] = 'd'
            elif bd[1] in p:
                res[bd[1]] = 'b'
                res[bd[0]] = 'd'

    for char in 'abcdefg':
        if char not in res:
            eg += char

    for p in patterns:
        if len(p) == 6 and ((eg[0] in p) is not (eg[1] in p)):  # 9
            if eg[0] in p:
                res[eg[0]] = 'g'
                res[eg[1]] = 'e'
            elif eg[1] in p:
                res[eg[1]] = 'g'
                res[eg[0]] = 'e'

    return res


solution1 = 0
solution2 = 0
with open('input.txt') as f:
    for line in f.readlines():
        line_parts = line.split(' | ')
        patterns = line_parts[0].split()
        output = line_parts[1].split()
        solution1 += count_ones_fours_sevens_eights(output)
        decoded = get_signals_to_segments(patterns)
        num = ''
        for o in output:
            real_o = ''
            for char in o:
                real_o += decoded[char]
            real_o = ''.join(sorted(real_o))
            for k, v in digits.items():
                if real_o == v:
                    num += str(k)
        solution2 += int(num)

print(solution1)
print(solution2)
