import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QApplication, QMainWindow

from src.interface import MainWindow
from src.registration import registration
from src.registration import wrlReader
from src.registration import szeReader
from src.controller import controller

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.controller = controller.Controller(self.ui)
        self.window.show()

app = QApplication(sys.argv)
w = AppWindow()
sys.exit(app.exec_())