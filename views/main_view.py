from qtpy.QtWidgets import QWidget, QPushButton, QApplication
from qtpy.QtGui import QPainter, QPixmap
from qtpy.QtCore import QRect

from views.mode_view import ModeView


class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, 750, 575)

        self.newgame_button = QPushButton(self)
        self.newgame_button.setFlat(True)
        self.newgame_button.setGeometry(290, 190, 221, 41)
        self.newgame_button.clicked.connect(self.new_game_clicked)

        self.exit_button = QPushButton(self)
        self.exit_button.setFlat(True)
        self.exit_button.setGeometry(300, 270, 121, 41)
        self.exit_button.clicked.connect(self.exit_clicked)

    def new_game_clicked(self):
        mode_view = ModeView(self)
        mode_view.show()

    def exit_clicked(self):
        app = QApplication.instance()
        app.quit()

    def paintEvent(self, event):
        image_path = "./images/Principal.jpg"
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        pixmap = QPixmap(image_path)
        painter.drawPixmap(QRect(0, 0, 750, 575), pixmap)


