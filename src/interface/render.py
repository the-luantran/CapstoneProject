from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
import sys
import vtk
from QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.vtk_widget = None
        self.ui = None
        self.setup()

    def setup(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vtk_widget = QTorsoViewer(self.ui.render_frame)

  # def initialize(self):
        # self.vtk_widget.start()


class QTorsoViewer(QtWidgets.QFrame):
    def __init__(self, parent):
        super(QTorsoViewer,self).__init__(parent)

        # VTK part
        # create the widget
        widget = QVTKRenderWindowInteractor(self)
        widget.Initialize()
        widget.Start()
      
 
        ren = vtk.vtkRenderer()
        widget.GetRenderWindow().AddRenderer(ren)

        cone = vtk.vtkConeSource()
        cone.SetResolution(8)

        coneMapper = vtk.vtkPolyDataMapper()
        coneMapper.SetInputConnection(cone.GetOutputPort())

        coneActor = vtk.vtkActor()
        coneActor.SetMapper(coneMapper)

        ren.AddActor(coneActor)


        self.interactor = widget

    # def start(self):
    #     self.interactor.Initialize()
    #     self.interactor.Start()


        

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()