# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_ready.ui'
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
"\n"
"    \n"
"    border-image: url(:/login/images/u0.png);\n"
"}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(450, 340, 93, 51))
        self.pushButton.setStyleSheet("background-color: transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 10, 61, 91))
        self.pushButton_2.setStyleSheet("background-color:transparent;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.ready)
        self.pushButton_2.clicked.connect(Form.game_exit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import images_rc
