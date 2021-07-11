import sys
from qtpy import QtWidgets
from views.main_view import MainView

app = QtWidgets.QApplication(sys.argv)
app.main_view = MainView()
app.main_view.setWindowTitle("TicTacToe")
app.main_view.show()
sys.exit(app.exec_())

