# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow
from functools import partial

from src.interface import HelpWindow, LicenseWindow
from os import walk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk
import webbrowser

class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
        #Define Bold Font
        self.font = QtGui.QFont()
        self.font.setPointSize(14)
        self.font.setBold(True)
        self.font.setWeight(75)

        #Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1200)


        #Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 750))
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        #Define VTK Layouts:
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("centralGridLayout")

        self.panelVerticalLayout = QtWidgets.QVBoxLayout()
        self.panelVerticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.panelVerticalLayout.setObjectName("panelVerticalLayout")

        ################  Load Grid  ################
        self.createLoadLayout()

        ################  Registration Grid  ################
        self.createRegistrationLayout()

        ################  View Grid  ################
        self.createViewLayout()

        ################  Save Grid  ################
        self.createSaveLayout()

        #vtk grid
        self.vtkGridWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.vtkGridWidget.sizePolicy().hasHeightForWidth())
        self.vtkGridWidget.setSizePolicy(sizePolicy)
        self.vtkGridWidget.setMinimumSize(QtCore.QSize(700, 700))
        self.vtkGridWidget.setObjectName("vtkGridWidget")
        self.gridLayout.addWidget(self.vtkGridWidget, 0, 1, 1, 1)


        self.vtkGrid = QtWidgets.QGridLayout(self.vtkGridWidget)
        # self.vtkGrid.setContentsMargins(0, 0, 0, 0)
        self.vtkGrid.setObjectName("vtkGrid")

        #Create VTK window widget
        self.vtkWidget = QVTKRenderWindowInteractor(self.vtkGridWidget)
        # set size policy
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        self.vtkWidget.setSizePolicy(sizePolicy)
        self.vtkWidget.setObjectName("vtkWidget")

        # Create Renderer
        self.ren = vtk.vtkRenderer()

        # Render Window
        self.renWin = self.vtkWidget.GetRenderWindow()
        # Add Renderer to Render Window
        self.renWin.AddRenderer(self.ren)
        # Interactor
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        InteractorStyle = vtk.vtkInteractorStyleTrackballCamera()
        # InteractorStyle = vtk.vtkInteractorStyleTrackball()
        self.iren.SetInteractorStyle(InteractorStyle)

        self.iren.Initialize()
        self.iren.Start()
        #add vtk widget to vtk grid
        self.vtkGrid.addWidget(self.vtkWidget, 0, 0, 1, 1)

        horizontalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        verticalSpacer = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.panelVerticalLayout.addItem(verticalSpacer)
        self.panelVerticalLayout.addItem(horizontalSpacer)
        self.gridLayout.addLayout(self.panelVerticalLayout, 0, 0, 1, 1)


        MainWindow.setCentralWidget(self.centralwidget)

        self.createNewMenu(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Add text to all objects
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3DSpineVizualization"))
        self.loadXRayButton.setText(_translate("MainWindow", "Load X-Ray"))
        self.loadXRaylandmarksButton.setText(_translate("MainWindow", "Load X-Ray Landmarks"))
        self.loadMRIButton.setText(_translate("MainWindow", "Load MRI"))
        self.loadMRILandmarksButton.setText(_translate("MainWindow", "Load MRI Landmarks"))
        self.loadSTButton.setText(_translate("MainWindow", "Load Surface Topography"))
        self.loadSTLandmarksButton.setText(_translate("MainWindow", "Load Surface Landmarks"))
        self.loadQuestionnaireButton.setText(_translate("MainWindow", "Load Questionnaire"))
        self.loadLabel.setText(_translate("MainWindow", "Load"))
        self.rigidRegistrationButton.setText(_translate("MainWindow", "Rigid Registration"))
        self.articulatedRegistrationButton.setText(_translate("MainWindow", "Articulated Registration"))
        self.reloadButton.setText(_translate("MainWindow", "Reload modalities"))
        self.regitsrationLabel.setText(_translate("MainWindow", "Registration"))
        self.xRayCheckBox.setText(_translate("MainWindow", "X-Ray"))
        self.mriLMCheckBox.setText(_translate("MainWindow", "MRI Landmarks"))
        self.sliceLabel.setText(_translate("MainWindow", "View registered slice"))
        self.stCheckBox.setText(_translate("MainWindow", "Surface"))
        self.viewLabel.setText(_translate("MainWindow", "View"))
        self.xRayExtLMCheckBox.setText(_translate("MainWindow", "External XRay Landmarks"))
        self.xRayVertLMCheckBox.setText(_translate("MainWindow", "Vertebrae XRay Landmarks"))
        self.mriCheckBox.setText(_translate("MainWindow", "MRI"))
        self.surfaceExtLMCheckBox.setText(_translate("MainWindow", "External Surface Landmarks"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.saveLabel.setText(_translate("MainWindow", "Save Registered File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation", None))
        self.actionSourceCode.setText(_translate("MainWindow", "Go to Source Code", None))
        self.actionLicense.setText(_translate("MainWindow", "License", None))

    def createLoadLayout(self):

        self.gridLoadLayout = QtWidgets.QGridLayout()
        self.gridLoadLayout.setVerticalSpacing(10)
        self.gridLoadLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLoadLayout.setObjectName("gridloadLayout")

        loadFont = QtGui.QFont()
        loadFont.setPointSize(10)
        loadFont.setItalic(True)

        ########################################################################### Row 0

        #Load Label
        self.loadLabel = QtWidgets.QLabel(self.centralwidget)
        self.loadLabel.setFont(self.font)
        self.loadLabel.setObjectName("loadLabel")
        self.gridLoadLayout.addWidget(self.loadLabel, 0, 0)

        ########################################################################### Row 1

        #Load MRI Button
        self.loadMRIButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadMRIButton.setEnabled(True)
        self.loadMRIButton.setObjectName("loadMRIButton")
        self.loadMRIButton.clicked.connect(self.selectMRIDirectory)
        self.gridLoadLayout.addWidget(self.loadMRIButton, 1, 0)

        # MRI Text
        self.mriLoadText = QtWidgets.QLabel(self.centralwidget)
        self.mriLoadText.setFont(loadFont)
        self.mriLoadText.setObjectName("mriLoadText")
        self.mriLoadText.setText("No MRI directory selected...")
        self.gridLoadLayout.addWidget(self.mriLoadText, 1, 1)

        ########################################################################### Row 2

        #Load XRay Button
        self.loadXRayButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadXRayButton.setEnabled(True)
        self.loadXRayButton.setObjectName("loadXRayButton")
        self.loadXRayButton.clicked.connect(self.selectXRayFile)
        self.gridLoadLayout.addWidget(self.loadXRayButton, 2, 0)

        #XRay Text
        self.xrayLoadText = QtWidgets.QLabel(self.centralwidget)
        self.xrayLoadText.setFont(loadFont)
        self.xrayLoadText.setObjectName("xrayLoadText")
        self.xrayLoadText.setText("No X-ray file selected...")
        self.gridLoadLayout.addWidget(self.xrayLoadText, 2, 1)

        ########################################################################### Row 3

        #Load Surface Topography Button
        self.loadSTButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadSTButton.setEnabled(True)
        self.loadSTButton.setObjectName("loadSTButton")
        self.loadSTButton.clicked.connect(self.selectSurfaceTopography)
        self.gridLoadLayout.addWidget(self.loadSTButton, 3, 0)

        # ST Text
        self.stLoadText = QtWidgets.QLabel(self.centralwidget)
        self.stLoadText.setFont(loadFont)
        self.stLoadText.setObjectName("stLoadText")
        self.stLoadText.setText("No ST file selected...")
        self.gridLoadLayout.addWidget(self.stLoadText, 3, 1)

        ########################################################################### Row 4

        # First Spacer
        self.gridLoadLayout.addWidget(QtWidgets.QLabel(self.centralwidget), 4, 0)

        ########################################################################### Row 5

        # Load MRI Landmark Button
        self.loadMRILandmarksButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadMRILandmarksButton.setEnabled(True)
        self.loadMRILandmarksButton.setObjectName("loadMRILandmarksButton")
        self.loadMRILandmarksButton.clicked.connect(self.selectMRILandmarks)
        self.gridLoadLayout.addWidget(self.loadMRILandmarksButton, 5, 0)

        # MRI Landmarks Text
        self.mriLMLoadText = QtWidgets.QLabel(self.centralwidget)
        self.mriLMLoadText.setFont(loadFont)
        self.mriLMLoadText.setObjectName("mriLMLoadText")
        self.mriLMLoadText.setText("No MRI landmarks selected...")
        self.gridLoadLayout.addWidget(self.mriLMLoadText, 5, 1)

        ########################################################################### Row 6

        #Load XRay landmarks Button
        self.loadXRaylandmarksButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadXRaylandmarksButton.setEnabled(True)
        self.loadXRaylandmarksButton.setObjectName("loadXRayButton")
        self.loadXRaylandmarksButton.clicked.connect(self.selectXRayLandmarks)
        self.gridLoadLayout.addWidget(self.loadXRaylandmarksButton, 6, 0)

        # XRay Landmarks Text
        self.xrayLMLoadText = QtWidgets.QLabel(self.centralwidget)
        self.xrayLMLoadText.setFont(loadFont)
        self.xrayLMLoadText.setObjectName("xrayLoadText")
        self.xrayLMLoadText.setText("No X-ray landmarks selected...")
        self.gridLoadLayout.addWidget(self.xrayLMLoadText, 6, 1)

        ########################################################################### Row 7

        # Load Surface Topography Landmarks Button
        self.loadSTLandmarksButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadSTLandmarksButton.setEnabled(True)
        self.loadSTLandmarksButton.setObjectName("loadSTButton")
        self.loadSTLandmarksButton.clicked.connect(self.selectSurfaceTopographyLandmark)
        self.gridLoadLayout.addWidget(self.loadSTLandmarksButton, 7, 0)

        # ST Landmarks Text
        self.stLMLoadText = QtWidgets.QLabel(self.centralwidget)
        self.stLMLoadText.setFont(loadFont)
        self.stLMLoadText.setObjectName("stLoadText")
        self.stLMLoadText.setText("No ST landmarks selected...")
        self.gridLoadLayout.addWidget(self.stLMLoadText, 7, 1)

        ########################################################################### Row 8

        # Second Spacer
        self.gridLoadLayout.addWidget(QtWidgets.QLabel(self.centralwidget), 8, 0)

        ########################################################################### Row 9

        # Load Questionnaire Button
        self.loadQuestionnaireButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadQuestionnaireButton.setEnabled(True)
        self.loadQuestionnaireButton.setObjectName("loadSTButton")
        self.loadQuestionnaireButton.clicked.connect(self.selectQuestionnaire)
        self.gridLoadLayout.addWidget(self.loadQuestionnaireButton, 9, 0)

        # Questionnaire Text
        self.questionnaireLoadText = QtWidgets.QLabel(self.centralwidget)
        self.questionnaireLoadText.setFont(loadFont)
        self.questionnaireLoadText.setObjectName("qtLoadText")
        self.questionnaireLoadText.setText("No Questionnaire selected...")
        self.gridLoadLayout.addWidget(self.questionnaireLoadText, 9, 1)

        ########################################################################### Row 10

        self.reloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.reloadButton.setEnabled(False)
        self.reloadButton.setObjectName("reloadButton")
        self.reloadButton.clicked.connect(self.reload)
        self.gridLoadLayout.addWidget(self.reloadButton, 10, 0, 1, 2)

        ########################################################################### Row 11

        self.panelVerticalLayout.addLayout(self.gridLoadLayout)

    def createRegistrationLayout(self):
        self.registrationLayout = QtWidgets.QVBoxLayout()
        self.registrationLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.registrationLayout.setObjectName("registrationLayout")

        #Registration Label
        self.regitsrationLabel = QtWidgets.QLabel(self.centralwidget)
        self.regitsrationLabel.setFont(self.font)
        self.regitsrationLabel.setObjectName("regitsrationLabel")
        self.registrationLayout.addWidget(self.regitsrationLabel)

        #Rigid Registration Button
        self.rigidRegistrationButton = QtWidgets.QPushButton(self.centralwidget)
        self.rigidRegistrationButton.setEnabled(False)
        self.rigidRegistrationButton.setObjectName("rigidRegistrationButton")
        self.registrationLayout.addWidget(self.rigidRegistrationButton)
        self.rigidRegistrationButton.clicked.connect(self.selectRigidRegister)

        #Articulated Registration Button
        self.articulatedRegistrationButton = QtWidgets.QPushButton(self.centralwidget)
        self.articulatedRegistrationButton.setEnabled(False)
        self.articulatedRegistrationButton.setObjectName("articulatedRegistrationButton")
        self.registrationLayout.addWidget(self.articulatedRegistrationButton)
        self.articulatedRegistrationButton.clicked.connect(self.selectArticulatedRegister)


        self.panelVerticalLayout.addLayout(self.registrationLayout)

    def createViewLayout(self):

        loadFont = QtGui.QFont()
        loadFont.setPointSize(10)
        loadFont.setItalic(True)

        self.viewLayout = QtWidgets.QVBoxLayout()
        self.viewLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.viewLayout.setObjectName("viewLayout")

        # View Label
        self.viewLabel = QtWidgets.QLabel(self.centralwidget)
        self.viewLabel.setFont(self.font)
        self.viewLabel.setObjectName("viewLabel")
        self.viewLayout.addWidget(self.viewLabel)

        # Checkboxes
        # MRI Checkbox

        self.mriCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.mriCheckBox.setObjectName("mriCheckBox")
        self.mriCheckBox.setEnabled(False)
        self.mriCheckBox.stateChanged.connect(lambda: self.checkType("MRI", self.mriCheckBox.isChecked()))
        self.viewLayout.addWidget(self.mriCheckBox)

        # X-Ray Checkbox
        self.xRayCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.xRayCheckBox.setObjectName("xRayCheckBox")
        self.xRayCheckBox.setEnabled(False)
        self.xRayCheckBox.stateChanged.connect(lambda: self.checkType("XRay", self.xRayCheckBox.isChecked()))
        self.viewLayout.addWidget(self.xRayCheckBox)

        # Surface Topography Checkbox
        self.stCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.stCheckBox.setObjectName("stCheckBox")
        self.stCheckBox.setEnabled(False)
        self.stCheckBox.stateChanged.connect(lambda: self.checkType("Surface", self.stCheckBox.isChecked()))
        self.viewLayout.addWidget(self.stCheckBox)

        # First Spacer
        self.spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.viewLayout.addItem(self.spacerItem1)

        # MRI Landmarks Checkbox
        self.mriLMCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.mriLMCheckBox.setObjectName("mriLMCheckBox")
        self.mriLMCheckBox.setEnabled(False)
        self.mriLMCheckBox.stateChanged.connect(lambda: self.checkType("MRI_LM", self.mriLMCheckBox.isChecked()))
        self.viewLayout.addWidget(self.mriLMCheckBox)

        # XRay Landmarks Checkbox
        self.xRayExtLMCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.xRayExtLMCheckBox.setObjectName("xRayExtLMCheckBox")
        self.xRayExtLMCheckBox.setEnabled(False)
        self.xRayExtLMCheckBox.stateChanged.connect(lambda: self.checkType("XRay_LM", self.xRayExtLMCheckBox.isChecked()))
        self.viewLayout.addWidget(self.xRayExtLMCheckBox)

        # XRay Vertebrae Landmarks Checkbox
        self.xRayVertLMCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.xRayVertLMCheckBox.setObjectName("xRayVertLMCheckBox")
        self.xRayVertLMCheckBox.setEnabled(False)
        self.xRayVertLMCheckBox.stateChanged.connect(lambda: self.checkType("Vertebrae_XRay_LM", self.xRayVertLMCheckBox.isChecked()))
        self.viewLayout.addWidget(self.xRayVertLMCheckBox)

        # Surface Landmarks Checkbox
        self.surfaceExtLMCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.surfaceExtLMCheckBox.setObjectName("surfaceExtLMCheckBox")
        self.surfaceExtLMCheckBox.setEnabled(False)
        self.surfaceExtLMCheckBox.stateChanged.connect(lambda: self.checkType("Surface_LM", self.surfaceExtLMCheckBox.isChecked()))
        self.viewLayout.addWidget(self.surfaceExtLMCheckBox)

        # Second Spacer
        self.spacerItem2 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.viewLayout.addItem(self.spacerItem2)

        # Slice Label
        self.sliceLabel = QtWidgets.QLabel(self.centralwidget)
        self.sliceLabel.setObjectName("sliceLabel")
        self.viewLayout.addWidget(self.sliceLabel)

        # SpinBox
        self.sliceSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.sliceSpinBox.setObjectName("sliceSpinBox")
        self.sliceSpinBox.setEnabled(False)
        self.sliceSpinBox.valueChanged.connect(self.changeSlice)
        self.viewLayout.addWidget(self.sliceSpinBox)

        self.panelVerticalLayout.addLayout(self.viewLayout)

    def createSaveLayout(self):
        self.saveLayout = QtWidgets.QVBoxLayout()
        self.saveLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.saveLayout.setObjectName("saveLayout")

        # Save Label
        self.saveLabel = QtWidgets.QLabel(self.centralwidget)
        self.saveLabel.setFont(self.font)
        self.saveLabel.setObjectName("saveLabel")
        self.saveLayout.addWidget(self.saveLabel)

        # Save Button
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(True)
        self.saveButton.setObjectName("saveButton")
        self.saveLayout.addWidget(self.saveButton)
        self.saveButton.clicked.connect(self.save)

        self.panelVerticalLayout.addLayout(self.saveLayout)

    def createNewMenu(self, MainWindow):
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 25))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.showMessage("Copyright Rola Harmouche, Luan Tran, Abdullah Sumbal")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionSourceCode = QtWidgets.QAction(MainWindow)
        self.actionSourceCode.setObjectName("actionSourceCode")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")

        self.menuHelp.addAction(self.actionDocumentation)
        self.actionDocumentation.triggered.connect(self.openDocumentationWindow)
        self.menuHelp.addAction(self.actionSourceCode)
        self.actionSourceCode.triggered.connect(self.goToSourceCode)
        self.menuHelp.addAction(self.actionLicense)
        self.actionLicense.triggered.connect(self.openLicenseWindow)
        self.menubar.addAction(self.menuHelp.menuAction())

    def setController(self, controller):
        self.controller = controller

    def selectMRIDirectory(self, dirName=None):
        if not dirName:
            dirName = QFileDialog.getExistingDirectory(self, 'Open MRI Directory', "")
        if dirName:
            errorStatus = False
            for root, dirs, files in walk(dirName):
                if dirs:
                    errorStatus = True
                for file in files:
                    if file.rsplit('.', 1)[1].lower() != "dcm" and file.rsplit('.', 1)[1].lower() != "ima":
                        errorStatus = True
                        break

            if errorStatus:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Error: The selected directory contains non-MRI files")
                msgBox.exec()
            else:
                self.mriLoadText.setText(self.processFilename(dirName))
                self.controller.setMRIDirectory(dirName)
                self.sliceSpinBox.setEnabled(True)
                self.sliceSpinBox.setProperty("value", 0)
                self.currentSliceValue = self.sliceSpinBox.value()
                self.controller.setMRIDirectory(dirName)
                self.controller.executeReader("MRI")
                self.mriCheckBox.setEnabled(True)
                self.mriCheckBox.setChecked(True)
                self.controller.check['MRI'] = True
        else:
            self.mriCheckBox.setEnabled(False)
            self.mriCheckBox.setChecked(False)
            self.controller.check['MRI'] = False
            self.mriLoadText.setText("No MRI directory selected...")
        self.checkRegistration()

    def selectMRILandmarks(self, filename=None):
        if not filename:
            filename = QFileDialog.getOpenFileName(self, 'Open Landmark file', "", ".scp  file (*.scp)")
        if filename[0]:
            self.mriLMLoadText.setText(self.processFilename(filename[0]))
            self.controller.setMRILandmarks(filename[0])
            self.controller.loadLandmarks("MRI_LM")
            self.mriLMCheckBox.setEnabled(True)
            self.mriLMCheckBox.setChecked(True)
            self.controller.check['MRI_LM'] = True
        else:
            self.mriLMCheckBox.setEnabled(False)
            self.mriLMCheckBox.setChecked(False)
            self.controller.check['MRI_LM'] = False
        self.checkRegistration()

    def selectXRayLandmarks(self, filename=None):
        if not filename:
            filename = QFileDialog.getOpenFileName(self, 'Open XRay Landmarks file', "", "o3 file (*.o3)")
        if filename[0]:
            self.xrayLMLoadText.setText(self.processFilename(filename[0]))
            self.controller.setXRayLandmarks(filename[0])
            self.controller.loadLandmarks("XRay_LM")
            self.xRayExtLMCheckBox.setEnabled(True)
            self.xRayExtLMCheckBox.setChecked(True)
            self.xRayVertLMCheckBox.setEnabled(True)
            self.xRayVertLMCheckBox.setChecked(True)
            self.controller.check['XRay_LM'] = True
        else:
            self.surfaceExtLMCheckBox.setEnabled(False)
            self.surfaceExtLMCheckBox.setChecked(False)
            self.xRayVertLMCheckBox.setEnabled(False)
            self.xRayVertLMCheckBox.setChecked(False)
            self.controller.check['XRay_LM'] = False
        self.checkRegistration()

    def selectXRayFile(self, filename=None):
        if not filename:
            filename = QFileDialog.getOpenFileName(self, 'Open XRay File', "", "WRL files (*.wrl)")
        if filename[0]:
            self.xrayLoadText.setText(self.processFilename(filename[0]))
            self.controller.setXRay(filename[0])
            self.controller.executeReader("XRay")
            self.xRayCheckBox.setEnabled(True)
            self.xRayCheckBox.setChecked(True)
            self.controller.check['XRay'] = True
        else:
            self.xRayCheckBox.setEnabled(False)
            self.xRayCheckBox.setChecked(False)
            self.controller.check['XRay'] = False
            self.xrayLoadText.setText("No X-ray file selected...")
        self.checkRegistration()

    def selectSurfaceTopographyLandmark(self, filename=None):
        if not filename:
            filename = QFileDialog.getOpenFileName(self, 'Open Surface Topography Landamrk', "", ".ext files (*.ext)")
        if filename[0]:
            self.stLMLoadText.setText(self.processFilename(filename[0]))
            self.controller.setSurfaceLandmarks(filename[0])
            self.controller.loadLandmarks("Surface_LM")
            self.surfaceExtLMCheckBox.setEnabled(True)
            self.surfaceExtLMCheckBox.setChecked(True)
            self.controller.check['ST_LM'] = True
        else:
            self.surfaceExtLMCheckBox.setEnabled(False)
            self.surfaceExtLMCheckBox.setChecked(False)
            self.controller.check['ST_LM'] = False
        self.checkRegistration()

    def selectSurfaceTopography(self, filename=None):
        if not filename:
            filename = QFileDialog.getOpenFileName(self, 'Open Surface Topography', "", "SZE files (*.sze)")
        if filename[0]:
            self.stLoadText.setText(self.processFilename(filename[0]))
            self.controller.setSurface(filename[0])
            self.controller.executeReader("Surface")
            self.stCheckBox.setEnabled(True)
            self.stCheckBox.setChecked(True)
            self.controller.check['ST'] = True
        else:
            self.stCheckBox.setEnabled(False)
            self.stCheckBox.setChecked(False)
            self.controller.check['ST'] = False
            self.stLoadText.setText("No ST file selected...")
        self.checkRegistration()


    def selectQuestionnaire(self):
        filename = QFileDialog.getOpenFileName(self, 'Open Questionnaire', "", "CSV files (*.csv)")
        if filename[0]:
            self.questionnaireLoadText.setText(self.processFilename(filename[0]))
            with open(filename[0]) as csvFile:
                filePaths = csv.reader(csvFile, delimiter=',')
                for fileData in filePaths:
                    if fileData[0] == "Surface Topography":
                        self.selectSurfaceTopography([fileData[1]])
                    elif fileData[0] == "X-Ray":
                        self.selectXRayFile([fileData[1]])
                    elif fileData[0] == "MRI":
                        self.selectMRIDirectory(fileData[1])
                    elif fileData[0] == "MRI Landmarks":
                        self.selectMRILandmarks([fileData[1]])
                    elif fileData[0] == "X-Ray Landmarks":
                        self.selectXRayLandmarks([fileData[1]])
                    elif fileData[0] == "Surface Topography Landmarks":
                        self.selectSurfaceTopographyLandmark([fileData[1]])

        else:
            self.questionnaireLoadText.setText("No Questionnaire file selected...")
        self.checkRegistration()

    def checkType(self, type, isChecked):
        self.controller.checkboxUpdate(type, isChecked)

    def checkRegistration(self):
        if self.controller.checkRequirementsForRegistration():
            self.rigidRegistrationButton.setEnabled(True)
            self.articulatedRegistrationButton.setEnabled(True)
            self.reloadButton.setEnabled(True)

    def openDocumentationWindow(self):
        dialog = QtWidgets.QDialog()
        ui = HelpWindow.Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def openLicenseWindow(self):
        dialog = QtWidgets.QDialog()
        ui = LicenseWindow.Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def changeSlice(self):
        self.controller.changeSlice(self.sliceSpinBox.value())


    def selectRigidRegister(self):
        self.controller.performRegistration("rigid")
        self.articulatedRegistrationButton.setEnabled(False)
        self.rigidRegistrationButton.setEnabled(False)
        self.saveButton.setEnabled(True)

    def selectArticulatedRegister(self):
        self.controller.performRegistration("articulated")
        self.articulatedRegistrationButton.setEnabled(False)
        self.rigidRegistrationButton.setEnabled(False)
        self.saveButton.setEnabled(True)

    def reload(self):
        self.controller.reload()
        self.saveButton.setEnabled(False)
        self.checkRegistration()

    def save(self):
        dirName = QFileDialog.getExistingDirectory(self, 'Directory Location', "")
        self.controller.executeWriter(dirName)


    def changeStatusMessage(self, message):
        self.statusbar.showMessage(message)

    def processFilename(self, text):
        if len(text) < 30:
            return text
        else:
            return text.rsplit('/', 1)[1]

    def goToSourceCode(self):
        webbrowser.open_new('https://github.com/luantran/CapstoneProject/')