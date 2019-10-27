# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(993, 516)
        Form.setMinimumSize(QtCore.QSize(993, 516))
        Form.setMaximumSize(QtCore.QSize(993, 516))
        Form.setStyleSheet("QWidget#Form{\n"
"border-image: url(:/login/images/room.png);\n"
"}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 100, 171, 51))
        self.pushButton.setStyleSheet("background-color:transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 170, 171, 51))
        self.pushButton_2.setStyleSheet("background-color:transparent;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 270, 171, 51))
        self.pushButton_3.setStyleSheet("background-color:transparent;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 340, 171, 51))
        self.pushButton_4.setStyleSheet("background-color:transparent;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(780, 20, 61, 81))
        self.pushButton_5.setStyleSheet("background-color:transparent;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(880, 30, 61, 81))
        self.pushButton_6.setStyleSheet("background-color:transparent;")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 100, 171, 121))
        self.pushButton_7.setStyleSheet("background-color: transparent;")
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Form)
        self.pushButton_6.clicked.connect(Form.room_exit)
        self.pushButton_3.clicked.connect(Form.history)
        self.pushButton_4.clicked.connect(Form.rank)
        self.pushButton_7.clicked.connect(Form.game)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_7.setText(_translate("Form", "PushButton"))
import images_rc
