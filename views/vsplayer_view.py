from qtpy.QtCore import QRect
from qtpy.QtGui import QPainter, QPixmap
from qtpy.QtWidgets import QWidget, QPushButton, QLabel, QApplication

from TicTacToe.TicTacToe import TicTacToe


class ViewPlayerVsPlayer(QWidget, TicTacToe):
    def __init__(self, parent=None):
        super(ViewPlayerVsPlayer, self).__init__(parent)
        self.setGeometry(0, 0, 750, 575)
        self.board_buttons = [] * 25
        self.init_board_buttons()
        self.init_menu_buttons()
        self.init_results_labels()
        self.init_board()
        self.player = 1
        #TODO: style files
        self.setStyleSheet("QWidget {"
                           "font-size: 40px;"
                           "border-style: outset;"
                           "border-width: 0px;"
                           "}")

    def init_results_labels(self):
        self.show_x = QLabel(self)
        self.show_x.setGeometry(50, 420, 91, 51)
        self.show_x.setStyleSheet("QWidget {"
                                  "font-size: 20px;}")
        self.show_o = QLabel(self)
        self.show_o.setGeometry(555, 420, 91, 51)
        self.show_o.setStyleSheet("QWidget {"
                                  "font-size: 20px;}")

    def init_menu_buttons(self):
        self.back_button = QPushButton(self)
        self.back_button.setFlat(True)
        self.back_button.setGeometry(630, 210, 99, 27)
        self.back_button.clicked.connect(self.back_clicked)

        self.exit_button = QPushButton(self)
        self.exit_button.setFlat(True)
        self.exit_button.setGeometry(620, 260, 99, 27)
        self.exit_button.clicked.connect(self.exit_clicked)

    def back_clicked(self):
        self.deleteLater()

    def exit_clicked(self):
        app = QApplication.instance()
        app.quit()

    def init_board_buttons(self):
        pos_x = 188
        pos_y = 140
        for _ in range(5):
            for _ in range(5):
                button = self.create_button_at(pos_x, pos_y)
                self.add_button_to_board(button)
                pos_x = pos_x + 68
            pos_x = 188
            pos_y = pos_y + 70

    def create_button_at(self, pos_x, pos_y):
        button = QPushButton(self)
        button.setGeometry(pos_x, pos_y, 51, 51)
        return button

    def add_button_to_board(self, button):
        self.board_buttons.append(button)
        list_index = len(self.board_buttons) - 1
        button.setObjectName("button" + str(list_index))
        self.board_buttons[list_index].clicked.connect(self.button_clicked)

    def button_clicked(self):
        name = self.sender().objectName()
        option = int(name.replace("button", ""))

        self.sender().setEnabled(False)
        if (self.player % 2) != 0:
            self.sender().setText("X")
        else:
            self.sender().setText("O")

        status = self.play(option)
        if status != -1:
            self.show_winner(status)
        else:
            self.change_player()

    def show_winner(self, status):
        if status == 1:
            if (self.player - 1) % 2 == 1:
                self.show_o.setText("??Ganador!")
                self.disable_buttons()
            else:
                self.show_x.setText("??Ganador!")
                self.disable_buttons()
        elif status == 0:
            self.show_x.setText("??Empate!")
            self.show_o.setText("??Empate!")
            self.disable_buttons()

    def change_player(self):
        self.player = (self.player % 2) + 1

    def disable_buttons(self):
        for button in self.board_buttons:
            button.setEnabled(False)

    def paintEvent(self, event):
        #TODO: Change path
        image_path = "./images/Table.jpg"
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        pixmap = QPixmap(image_path)
        painter.drawPixmap(QRect(0, 0, 750, 575), pixmap)
