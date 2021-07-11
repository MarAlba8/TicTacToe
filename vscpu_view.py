from cpu import CPU
from vsplayer_view import ViewPlayerVsPlayer


class ViewPlayerVsCPU(ViewPlayerVsPlayer):
    def __init__(self, parent=None):
        super(ViewPlayerVsCPU, self).__init__(parent)
        self.cpu = CPU()
        self.player = 1

    def button_clicked(self):
        name = self.sender().objectName()
        position = int(name.replace("button", ""))
        self.sender().setEnabled(False)
        self.sender().setText("X")

        status = self.play(position)
        if status != -1:
            self.show_winner(status)
        else:
            self.change_player()
            self.play_cpu()

    def play_cpu(self):
        position = self.cpu.play(self.board)
        if position:
            status = self.play(position)
            self.board_buttons[position].setText('O')
            self.board_buttons[position].setEnabled(False)
            if status != -1:
                self.show_winner(status)
            else:
                self.change_player()


