# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(993, 516)
        Form.setMinimumSize(QtCore.QSize(993, 516))
        Form.setMaximumSize(QtCore.QSize(993, 516))
        Form.setStyleSheet("QWidget#Form{\n"
"border-image: url(:/login/images/a.jpg);\n"
"}")
        self.acount_le = QtWidgets.QLineEdit(Form)
        self.acount_le.setEnabled(True)
        self.acount_le.setGeometry(QtCore.QRect(540, 180, 171, 24))
        self.acount_le.setText("")
        self.acount_le.setClearButtonEnabled(True)
        self.acount_le.setObjectName("acount_le")
        self.password_le = QtWidgets.QLineEdit(Form)
        self.password_le.setEnabled(True)
        self.password_le.setGeometry(QtCore.QRect(540, 240, 171, 24))
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.count_le_3 = QtWidgets.QLineEdit(Form)
        self.count_le_3.setGeometry(QtCore.QRect(540, 300, 171, 24))
        self.count_le_3.setClearButtonEnabled(True)
        self.count_le_3.setObjectName("count_le_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(460, 180, 61, 24))
        self.label.setStyleSheet("font: 16pt \"华文行楷\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(459, 240, 61, 24))
        self.label_2.setStyleSheet("font: 16pt \"华文行楷\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 300, 111, 24))
        self.label_3.setStyleSheet("font: 16pt \"华文行楷\";")
        self.label_3.setObjectName("label_3")
        self.login_btn = QtWidgets.QPushButton(Form)
        self.login_btn.setEnabled(False)
        self.login_btn.setGeometry(QtCore.QRect(520, 370, 93, 28))
        self.login_btn.setStyleSheet("QPushButton{font: 16pt \"华文行楷\";\n"
"background-color: rgb(204, 204, 204);}\n"
"\n"
"QPushButton:disabled{font: 16pt \"华文行楷\";\n"
"background-color: color: rgb(85, 85, 255);}\n"
"")
        self.login_btn.setObjectName("login_btn")
        self.login_btn_2 = QtWidgets.QPushButton(Form)
        self.login_btn_2.setGeometry(QtCore.QRect(630, 370, 93, 28))
        self.login_btn_2.setStyleSheet("font: 16pt \"华文行楷\";")
        self.login_btn_2.setObjectName("login_btn_2")

        self.retranslateUi(Form)
        self.login_btn.clicked.connect(Form.login_show)
        self.login_btn_2.clicked.connect(Form.shouye_show)
        self.acount_le.textChanged['QString'].connect(Form.enable_register)
        self.password_le.textChanged['QString'].connect(Form.enable_register)
        self.count_le_3.textChanged['QString'].connect(Form.enable_register)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "账号"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label_3.setText(_translate("Form", "确认密码"))
        self.login_btn.setText(_translate("Form", "注册"))
        self.login_btn_2.setText(_translate("Form", "返回"))
import images_rc
