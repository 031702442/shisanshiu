# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shouye.ui'
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
"border-image: url(:/login/images/首页.jpg);\n"
"}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 140, 401, 41))
        self.pushButton.setStyleSheet("font: 18pt \"华文行楷\";\n"
"background-color: transparent;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 260, 401, 41))
        self.pushButton_2.setStyleSheet("font: 18pt \"华文行楷\";\n"
"background-color: transparent;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.login_show)
        self.pushButton_2.clicked.connect(Form.register_show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "登入"))
        self.pushButton_2.setText(_translate("Form", "注册"))
import images_rc
