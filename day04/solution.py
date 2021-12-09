def parse_data(txt):
    numbers = txt.pop(0).split(',')
    matrices = []
    matrix = []
    for line in txt:
        if line != '':
            matrix.append(line.split())
        else:
            if matrix:
                matrices.append(matrix)
                matrix = []
    matrices.append(matrix)

    return numbers, matrices


def is_winner(board):
    for r in board:
        if all(r):
            return True
    for c in range(len(board[0])):
        if all([board[r][c] for r in range(len(board[c]))]):
            return True
    return False


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
        numbers, boards = parse_data(data)
        marked = [[[False for _ in r] for r in b] for b in boards]
        won = [False for _ in range(len(boards))]
        for number in numbers:
            for i in range(len(boards)):
                for r in range(len(boards[0])):
                    for c in range(len(boards[0][0])):
                        num = boards[i][r][c]
                        if number == num:
                            marked[i][r][c] = True
                if is_winner(marked[i]) and not won[i]:
                    won[i] = True
                    n_of_winners = len([x for x in range(len(boards)) if won[x]])
                    if n_of_winners == 1 or n_of_winners == len(boards):
                        unmarked = 0
                        for row in range(5):
                            for col in range(5):
                                if not marked[i][row][col]:
                                    unmarked += int(boards[i][row][col])
                        print(unmarked * int(number))
