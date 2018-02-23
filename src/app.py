import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QApplication, QMainWindow

from src.interface import MainWindow
from src.interface.render import QTorsoViewer, WRLTest


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self.window)

        # Set up VTK render in UI

        # Render Sphere in the window
        #QTorsoViewer(self.ui.render_frame)
        # Render wrl files
        WRLTest(self.ui.render_frame)
        self.window.show()

app = QApplication(sys.argv)
# window = QMainWindow()
# ui = MainWindow.Ui_MainWindow()
# ui.setupUi(window)

w = AppWindow()
sys.exit(app.exec_())