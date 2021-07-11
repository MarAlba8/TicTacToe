class TicTacToe:
    def __init__(self):
        self.player = 1
        self.board = []
        self.init_board()

    def init_board(self):
        self.board = []
        for i in range(25):
            self.board.append(i)

    def check_win(self):
        """
        1 for winner
        -1 for tie
        0 for not finished
        """
        if self.board[0] == self.board[0] \
                and self.board[1] == self.board[2] \
                and self.board[2] == self.board[3] \
                and self.board[3] == self.board[4]:
            return 1
        elif self.board[5] == self.board[6] \
                and self.board[6] == self.board[7] \
                and self.board[7] == self.board[8] \
                and self.board[8] == self.board[9]:
            return 1
        elif self.board[10] == self.board[11] \
                and self.board[11] == self.board[12] \
                and self.board[12] == self.board[13] \
                and self.board[13] == self.board[14]:
            return 1
        elif self.board[15] == self.board[16] \
                and self.board[16] == self.board[17] \
                and self.board[17] == self.board[18] \
                and self.board[18] == self.board[19]:
            return 1
        elif self.board[20] == self.board[21] \
                and self.board[21] == self.board[22] \
                and self.board[22] == self.board[23] \
                and self.board[23] == self.board[24]:
            return 1
        elif self.board[0] == self.board[5] \
                and self.board[5] == self.board[10] \
                and self.board[10] == self.board[15] \
                and self.board[15] == self.board[20]:
            return 1
        elif self.board[1] == self.board[6] \
                and self.board[6] == self.board[11] \
                and self.board[11] == self.board[16] \
                and self.board[16] == self.board[21]:
            return 1
        elif self.board[2] == self.board[7] \
                and self.board[7] == self.board[12] \
                and self.board[12] == self.board[17] \
                and self.board[17] == self.board[22]:
            return 1
        elif self.board[3] == self.board[8] \
                and self.board[8] == self.board[13] \
                and self.board[13] == self.board[18] \
                and self.board[18] == self.board[23]:
            return 1
        elif self.board[4] == self.board[9] \
                and self.board[9] == self.board[14] \
                and self.board[14] == self.board[19] \
                and self.board[19] == self.board[24]:
            return 1
        elif self.board[0] == self.board[6] \
                and self.board[6] == self.board[12] \
                and self.board[12] == self.board[18] \
                and self.board[18] == self.board[24]:
            return 1
        elif self.board[4] == self.board[8] \
                and self.board[8] == self.board[12] \
                and self.board[12] == self.board[16] \
                and self.board[16] == self.board[20]:
            return 1
        else:
            for i in self.board:
                if i != 'X' and i != 'O':
                    return -1
        return 0

    def play(self, opt):
        mark = 'X' if self.player == 1 else 'O'
        if self.board[opt] != 'X' and self.board[opt] != 'O':
            self.board[opt] = mark

        status = self.check_win()
        return status



