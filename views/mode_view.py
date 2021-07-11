from qtpy.QtWidgets import QWidget, QPushButton, QApplication
from qtpy.QtGui import QPainter, QPixmap
from qtpy.QtCore import QRect

from views.vscpu_view import ViewPlayerVsCPU
from views.vsplayer_view import ViewPlayerVsPlayer


class ModeView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, 750, 575)
        self.init_menu_buttons()
        self.init_mode_buttons()

    def init_menu_buttons(self):
        self.back_button = QPushButton(self)
        self.back_button.setFlat(True)
        self.back_button.setGeometry(40, 10, 99, 27)
        self.back_button.clicked.connect(self.back_clicked)

        self.exit_button = QPushButton(self)
        self.exit_button.setFlat(True)
        self.exit_button.setGeometry(610, 10, 101, 31)
        self.exit_button.clicked.connect(self.exit_clicked)

    def init_mode_buttons(self):
        self.vsplayer_button = QPushButton(self)
        self.vsplayer_button.setFlat(True)
        self.vsplayer_button.setGeometry(330, 180, 211, 51)
        self.vsplayer_button.clicked.connect(self.vs_player_clicked)

        self.vscpu_button = QPushButton(self)
        self.vscpu_button.setFlat(True)
        self.vscpu_button.setGeometry(210, 250, 211, 41)
        self.vscpu_button.clicked.connect(self.vs_cpu_clicked)

    def exit_clicked(self):
        app = QApplication.instance()
        app.quit()

    def back_clicked(self):
        self.deleteLater()

    def vs_player_clicked(self):
        game_window = ViewPlayerVsPlayer(self)
        game_window.show()

    def vs_cpu_clicked(self):
        game_window = ViewPlayerVsCPU(self)
        game_window.show()

    def paintEvent(self, event):
        image_path = "./images/ModeMenu.jpg"
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        pixmap = QPixmap(image_path)
        painter.drawPixmap(QRect(0, 0, 750, 575), pixmap)
