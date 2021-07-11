class TicTacToe:
    def __init__(self):
        self.turn = 0
        self.mode = 0  #1.jugador vs jugador 2.jugador vs cpu

    def set_turn(self, turn):
        self.turn = turn

    def get_turn(self):
        return self.turn

    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode

    def set_board(self, board):
        for i, data in enumerate(board):
            self.board[i] = data

    def init_board(self):
        self.board = []
        for i in range(25):
            self.board.append(i)

    def get_board(self):
        return self.quare

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
        elif self.board[7] == self.board[8] \
                and self.board[8] == self.board[9] \
                and self.board[9] == self.board[10] \
                and self.board[10] == self.board[11]:
            return 1
        elif self.board[12] == self.board[13] \
                and self.board[13] == self.board[14] \
                and self.board[14] == self.board[15] \
                and self.board[15] == self.board[16]:
            return 1
        elif self.board[17] == self.board[18] \
                and self.board[18] == self.board[19] \
                and self.board[19] == self.board[20] \
                and self.board[20] == self.board[21]:
            return 1
        elif self.board[22] == self.board[23] \
                and self.board[23] == self.board[24] \
                and self.board[24] == self.board[25] \
                and self.board[25] == self.board[26]:
            return 1
        elif self.board[0] == self.board[5] \
                and self.board[5] == self.board[10] \
                and self.board[10] == self.board[15] \
                and self.board[15] == self.board[20]:
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
        elif self.board[5] == self.board[10] \
                and self.board[10] == self.board[15] \
                and self.board[15] == self.board[20] \
                and self.board[20] == self.board[25]:
            return 1
        elif self.board[1] == self.board[7] \
                and self.board[7] == self.board[13] \
                and self.board[13] == self.board[19] \
                and self.board[19] == self.board[25]:
            return 1
        elif self.board[5] == self.board[9] \
                and self.board[9] == self.board[13] \
                and self.board[13] == self.board[17] \
                and self.board[17] == self.board[21]:
            return 1
        else:
            for i in self.board:
                if i != 'X' and i != 'O':
                    return -1
        return 0

    def play(self, opt):
        self.player = 1 if self.player % 2 else 2
        mark = 'X' if self.player == 1 else 'O'
        if self.board[opt] != 'X' and self.board[opt] != 'O':
            self.board[opt] = mark

        actual_status = self.check_win()
        self.show_winner(actual_status)

        self.player += 1

    def show_winner(self, actual_status):
        if actual_status == 1:
            if (self.player - 1) % 2 == 1:
                self.show_o.setText("¡Ganador!")
                self.disable_buttons()
            else:
                self.show_x.setText("¡Ganador!")
                self.disable_buttons()
        elif actual_status == 0:
            self.show_x.setText("¡Empate!")
            self.show_o.setText("¡Empate!")
            self.disable_buttons()


