# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 557)
        MainWindow.setMinimumSize(QtCore.QSize(988, 557))
        MainWindow.setMaximumSize(QtCore.QSize(988, 557))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 640, 480))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.hsv_upper = QtWidgets.QWidget(self.centralwidget)
        self.hsv_upper.setGeometry(QtCore.QRect(670, 170, 311, 141))
        self.hsv_upper.setObjectName("hsv_upper")
        self.v_upper = QtWidgets.QSlider(self.hsv_upper)
        self.v_upper.setGeometry(QtCore.QRect(70, 100, 171, 22))
        self.v_upper.setMaximum(255)
        self.v_upper.setOrientation(QtCore.Qt.Horizontal)
        self.v_upper.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.v_upper.setObjectName("v_upper")
        self.label_5 = QtWidgets.QLabel(self.hsv_upper)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 41, 21))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.h_upper = QtWidgets.QSlider(self.hsv_upper)
        self.h_upper.setGeometry(QtCore.QRect(69, 20, 171, 22))
        self.h_upper.setMaximum(255)
        self.h_upper.setPageStep(10)
        self.h_upper.setProperty("value", 0)
        self.h_upper.setOrientation(QtCore.Qt.Horizontal)
        self.h_upper.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.h_upper.setObjectName("h_upper")
        self.label_7 = QtWidgets.QLabel(self.hsv_upper)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.hsv_upper)
        self.label_6.setGeometry(QtCore.QRect(19, 100, 41, 21))
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.s_upper = QtWidgets.QSlider(self.hsv_upper)
        self.s_upper.setGeometry(QtCore.QRect(69, 60, 171, 22))
        self.s_upper.setMaximum(255)
        self.s_upper.setOrientation(QtCore.Qt.Horizontal)
        self.s_upper.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.s_upper.setObjectName("s_upper")
        self.value_v_upper = QtWidgets.QLabel(self.hsv_upper)
        self.value_v_upper.setGeometry(QtCore.QRect(250, 100, 41, 21))
        self.value_v_upper.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.value_v_upper.setText("")
        self.value_v_upper.setObjectName("value_v_upper")
        self.value_s_upper = QtWidgets.QLabel(self.hsv_upper)
        self.value_s_upper.setGeometry(QtCore.QRect(250, 60, 41, 21))
        self.value_s_upper.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.value_s_upper.setText("")
        self.value_s_upper.setObjectName("value_s_upper")
        self.value_h_upper = QtWidgets.QLabel(self.hsv_upper)
        self.value_h_upper.setGeometry(QtCore.QRect(250, 20, 41, 21))
        self.value_h_upper.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.value_h_upper.setText("")
        self.value_h_upper.setObjectName("value_h_upper")
        self.hsv_lower = QtWidgets.QWidget(self.centralwidget)
        self.hsv_lower.setGeometry(QtCore.QRect(670, 20, 311, 141))
        self.hsv_lower.setObjectName("hsv_lower")
        self.v_lower = QtWidgets.QSlider(self.hsv_lower)
        self.v_lower.setGeometry(QtCore.QRect(70, 100, 171, 22))
        self.v_lower.setMaximum(255)
        self.v_lower.setOrientation(QtCore.Qt.Horizontal)
        self.v_lower.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.v_lower.setObjectName("v_lower")
        self.label_8 = QtWidgets.QLabel(self.hsv_lower)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 41, 21))
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setObjectName("label_8")
        self.h_lower = QtWidgets.QSlider(self.hsv_lower)
        self.h_lower.setGeometry(QtCore.QRect(69, 20, 171, 22))
        self.h_lower.setMaximum(255)
        self.h_lower.setPageStep(10)
        self.h_lower.setProperty("value", 0)
        self.h_lower.setOrientation(QtCore.Qt.Horizontal)
        self.h_lower.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.h_lower.setTickInterval(0)
        self.h_lower.setObjectName("h_lower")
        self.label_9 = QtWidgets.QLabel(self.hsv_lower)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.hsv_lower)
        self.label_10.setGeometry(QtCore.QRect(19, 100, 41, 21))
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setObjectName("label_10")
        self.s_lower = QtWidgets.QSlider(self.hsv_lower)
        self.s_lower.setGeometry(QtCore.QRect(69, 60, 171, 22))
        self.s_lower.setMaximum(255)
        self.s_lower.setOrientation(QtCore.Qt.Horizontal)
        self.s_lower.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.s_lower.setObjectName("s_lower")
        self.value_h_lower = QtWidgets.QLabel(self.hsv_lower)
        self.value_h_lower.setGeometry(QtCore.QRect(250, 20, 41, 21))
        self.value_h_lower.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.value_h_lower.setText("")
        self.value_h_lower.setObjectName("value_h_lower")
        self.value_s_lower = QtWidgets.QLabel(self.hsv_lower)
        self.value_s_lower.setGeometry(QtCore.QRect(250, 60, 41, 21))
        self.value_s_lower.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.value_s_lower.setText("")
        self.value_s_lower.setObjectName("value_s_lower")
        self.value_v_lower = QtWidgets.QLabel(self.hsv_lower)
        self.value_v_lower.setGeometry(QtCore.QRect(250, 100, 41, 21))
        self.value_v_lower.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.value_v_lower.setText("")
        self.value_v_lower.setObjectName("value_v_lower")
        self.buttons = QtWidgets.QWidget(self.centralwidget)
        self.buttons.setGeometry(QtCore.QRect(670, 320, 311, 181))
        self.buttons.setObjectName("buttons")
        self.confirm = QtWidgets.QPushButton(self.buttons)
        self.confirm.setGeometry(QtCore.QRect(10, 110, 291, 51))
        self.confirm.setObjectName("confirm")
        self.yellow = QtWidgets.QPushButton(self.buttons)
        self.yellow.setGeometry(QtCore.QRect(110, 20, 91, 71))
        self.yellow.setObjectName("yellow")
        self.red = QtWidgets.QPushButton(self.buttons)
        self.red.setGeometry(QtCore.QRect(10, 20, 91, 71))
        self.red.setObjectName("red")
        self.blue = QtWidgets.QPushButton(self.buttons)
        self.blue.setGeometry(QtCore.QRect(210, 20, 91, 71))
        self.blue.setObjectName("blue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "S upper"))
        self.label_7.setText(_translate("MainWindow", "H upper"))
        self.label_6.setText(_translate("MainWindow", "V upper"))
        self.label_8.setText(_translate("MainWindow", "S lower"))
        self.label_9.setText(_translate("MainWindow", "H lower"))
        self.label_10.setText(_translate("MainWindow", "V lower"))
        self.confirm.setText(_translate("MainWindow", "Confirm"))
        self.yellow.setText(_translate("MainWindow", "Yellow"))
        self.red.setText(_translate("MainWindow", "Red"))
        self.blue.setText(_translate("MainWindow", "Blue"))