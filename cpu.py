import math
import random


class CPU:
    def __init__(self):
        self.cpu_mark = 'O'
        self.human_mark = 'X'
        self.counter = 0

    def play(self, board):
        return self.best_move(board.copy())

    def best_move(self, board):
        depth = 0
        best_score = -math.inf
        move = None
        for index, value in enumerate(board):
            if value != 'X' and value != 'O':
                board[index] = self.cpu_mark
                score = self.minimax(board.copy(), depth, False)
                board[index] = value
                if score > best_score:
                    best_score = score
                    move = index

        return move

    def minimax(self, board, depth, is_maximizing):
        random_number = random.random() / random.randrange(32000, 100000)
        if depth == 2:
            return check(board)*random_number

        winner = check_winner(board)
        if winner == 'X':
            return -10
        elif winner == 'O':
            return 10
        elif winner == 0:
            return winner

        if is_maximizing:
            best_score = -math.inf
            for index, value in enumerate(board):
                if value != 'X' and value != 'O':
                    board[index] = self.cpu_mark
                    score = self.minimax(board, depth + 1, False)
                    board[index] = value
                    best_score = max(score, best_score)
        else:
            best_score = math.inf
            for index, value in enumerate(board):
                if value != 'X' and value != 'O':
                    board[index] = self.human_mark
                    score = self.minimax(board, depth + 1, True)
                    board[index] = value
                    best_score = min(score, best_score)
        return best_score


def check(board):
    count = 0
    i = 0

    for _ in range(5):
        count_x = 0
        count_o = 0
        count_empty = 0
        for _ in range(5):
            if board[i] == 'X':
                count_x += 1
            elif board[i] == 'O':
                count_o += 1
            else:
                count_empty += 1
            i += 1
        count += check_counters(count_x, count_o, count_empty)

    for j in range(5):
        i = j
        count_x = 0
        count_o = 0
        count_empty = 0
        for _ in range(5):
            if board[i] == 'X':
                count_x += 1
            elif board[i] == 'O':
                count_o += 1
            else:
                count_empty += 1
            i += 5
        count += check_counters(count_x, count_o, count_empty)

    # diagonal
    i = 0
    count_x = 0
    count_o = 0
    count_empty = 0
    for _ in range(5):
        if board[i] == 'X':
            count_x += 1
        elif board[i] == 'O':
            count_o += 1
        else:
            count_empty += 1
        i += 6
        count += check_counters(count_x, count_o, count_empty)

    # diagonal
    i = 4
    count_x = 0
    count_o = 0
    count_empty = 0

    for _ in range(5):
        if board[i] == 'X':
            count_x += 1
        elif board[i] == 'O':
            count_o += 1
        else:
            count_empty += 1
        i += 4
        count += check_counters(count_x, count_o, count_empty)

    return count


def check_counters(count_x, count_o, count_empty):
    count = 0
    if count_empty != 0:
        if count_x == 0:
            if count_o > 0:
                count += count_x * 80 + (1000 / count_empty)
            count += (count_o * 20 + (1000 / count_empty))

        if count_o == 0:
            count -= count_x * (-20) - 1000 / count_empty

    if count_x == 4 and count_empty == 1:
        count += count_o * 60 + 1000 / count_empty

    if count_o == 4 and count_empty == 1:
        count += count_x * 70 + 1000 / count_empty

    return count


def check_winner(board):
    """
    1 for winner
    -1 for tie
    0 for not finished
    """
    if board[0] == board[0] \
            and board[1] == board[2] \
            and board[2] == board[3] \
            and board[3] == board[4]:
        return board[0]
    elif board[5] == board[6] \
            and board[6] == board[7] \
            and board[7] == board[8] \
            and board[8] == board[9]:
        return board[5]
    elif board[10] == board[11] \
            and board[11] == board[12] \
            and board[12] == board[13] \
            and board[13] == board[14]:
        return board[10]
    elif board[15] == board[16] \
            and board[16] == board[17] \
            and board[17] == board[18] \
            and board[18] == board[19]:
        return board[15]
    elif board[20] == board[21] \
            and board[21] == board[22] \
            and board[22] == board[23] \
            and board[23] == board[24]:
        return board[20]
    elif board[0] == board[5] \
            and board[5] == board[10] \
            and board[10] == board[15] \
            and board[15] == board[20]:
        return board[0]
    elif board[1] == board[6] \
            and board[6] == board[11] \
            and board[11] == board[16] \
            and board[16] == board[21]:
        return board[1]
    elif board[2] == board[7] \
            and board[7] == board[12] \
            and board[12] == board[17] \
            and board[17] == board[22]:
        return board[2]
    elif board[3] == board[8] \
            and board[8] == board[13] \
            and board[13] == board[18] \
            and board[18] == board[23]:
        return board[3]
    elif board[4] == board[9] \
            and board[9] == board[14] \
            and board[14] == board[19] \
            and board[19] == board[24]:
        return board[4]
    elif board[0] == board[6] \
            and board[6] == board[12] \
            and board[12] == board[18] \
            and board[18] == board[24]:
        return board[0]
    elif board[4] == board[8] \
            and board[8] == board[12] \
            and board[12] == board[16] \
            and board[16] == board[20]:
        return board[4]
    else:
        for i in board:
            if i != 'X' and i != 'O':
                return -1
    return 0
