# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bangding.ui'
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
"border-image: url(:/login/images/a.jpg);\n"
"}")
        self.jw_acount_le = QtWidgets.QLineEdit(Form)
        self.jw_acount_le.setEnabled(True)
        self.jw_acount_le.setGeometry(QtCore.QRect(550, 180, 171, 24))
        self.jw_acount_le.setText("")
        self.jw_acount_le.setClearButtonEnabled(True)
        self.jw_acount_le.setObjectName("jw_acount_le")
        self.jw_pwd_le = QtWidgets.QLineEdit(Form)
        self.jw_pwd_le.setEnabled(True)
        self.jw_pwd_le.setGeometry(QtCore.QRect(550, 260, 171, 24))
        self.jw_pwd_le.setText("")
        self.jw_pwd_le.setClearButtonEnabled(True)
        self.jw_pwd_le.setObjectName("jw_pwd_le")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 180, 111, 24))
        self.label_3.setStyleSheet("font: 14pt \"华文行楷\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(420, 260, 131, 24))
        self.label_4.setStyleSheet("font: 14pt \"华文行楷\";")
        self.label_4.setObjectName("label_4")
        self.login_btn_2 = QtWidgets.QPushButton(Form)
        self.login_btn_2.setGeometry(QtCore.QRect(520, 360, 93, 28))
        self.login_btn_2.setStyleSheet("font: 15pt \"华文行楷\";")
        self.login_btn_2.setObjectName("login_btn_2")
        self.login_btn_3 = QtWidgets.QPushButton(Form)
        self.login_btn_3.setGeometry(QtCore.QRect(630, 360, 93, 28))
        self.login_btn_3.setStyleSheet("font: 16pt \"华文行楷\";")
        self.login_btn_3.setObjectName("login_btn_3")

        self.retranslateUi(Form)
        self.login_btn_2.clicked.connect(Form.bangding)
        self.login_btn_3.clicked.connect(Form.bd_exit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "教务处账号"))
        self.label_4.setText(_translate("Form", "教务处密码"))
        self.login_btn_2.setText(_translate("Form", "绑定"))
        self.login_btn_3.setText(_translate("Form", "返回"))
import images_rc
