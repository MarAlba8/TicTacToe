from cpu import CPU
from vsplayer_view import ViewPlayerVsPlayer


class ViewPlayerVsCPU(ViewPlayerVsPlayer):
    def __init__(self, parent=None):
        super(ViewPlayerVsCPU, self).__init__(parent)
        self.cpu = CPU()

    def button_clicked(self):
        name = self.sender().objectName()
        position = int(name.replace("button", ""))
        self.board[position] = self.cpu.human_mark
        self.sender().setEnabled(False)
        self.sender().setText("X")

        self.play_cpu()

    def play_cpu(self):
        position = self.cpu.play(self.board)
        if position:
            self.board[position] = self.cpu.cpu_mark
            self.board_buttons[position].setText('O')
            self.board_buttons[position].setEnabled(False)