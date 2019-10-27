# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
"    border-image: url(:/login/images/a.jpg);\n"
"    \n"
"}")
        self.login_btn = QtWidgets.QPushButton(Form)
        self.login_btn.setEnabled(False)
        self.login_btn.setGeometry(QtCore.QRect(520, 360, 93, 28))
        self.login_btn.setStyleSheet("font: 16pt \"华文行楷\";")
        self.login_btn.setObjectName("login_btn")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 360, 93, 28))
        self.pushButton_2.setStyleSheet("font: 16pt \"华文行楷\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(460, 190, 54, 29))
        self.label.setStyleSheet("font: 16pt \"华文行楷\";")
        self.label.setObjectName("label")
        self.acount_le = QtWidgets.QLineEdit(Form)
        self.acount_le.setGeometry(QtCore.QRect(530, 190, 171, 24))
        self.acount_le.setClearButtonEnabled(True)
        self.acount_le.setObjectName("acount_le")
        self.password_le = QtWidgets.QLineEdit(Form)
        self.password_le.setGeometry(QtCore.QRect(530, 260, 171, 24))
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(460, 260, 54, 29))
        self.label_2.setStyleSheet("font: 16pt \"华文行楷\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.login_exit)
        self.login_btn.clicked.connect(Form.show_room)
        self.acount_le.textChanged['QString'].connect(Form.enable_login)
        self.password_le.textChanged['QString'].connect(Form.enable_login)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setProperty("bg", _translate("Form", "blue"))
        self.login_btn.setText(_translate("Form", "登入"))
        self.login_btn.setProperty("bg", _translate("Form", "blue"))
        self.pushButton_2.setText(_translate("Form", "返回"))
        self.pushButton_2.setProperty("bg", _translate("Form", "blue"))
        self.label.setText(_translate("Form", "账号"))
        self.label_2.setText(_translate("Form", "密码"))
import images_rc
