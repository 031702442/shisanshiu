# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_open.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(993, 516)
        Form.setStyleSheet("QWidget#Form{;\n"
"border-image: url(:/login/images/u1.jpg);}")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(290, 120, 421, 211))
        self.textEdit.setStyleSheet("background-color: transparent;\n"
"font: 18pt \"楷体\";")
        self.textEdit.setObjectName("textEdit")
        self.play_lab = QtWidgets.QLabel(Form)
        self.play_lab.setGeometry(QtCore.QRect(460, 340, 91, 51))
        self.play_lab.setStyleSheet("\n"
"font: 20pt \"华文行楷\";")
        self.play_lab.setObjectName("play_lab")
        self.jiesuan_lab = QtWidgets.QLabel(Form)
        self.jiesuan_lab.setGeometry(QtCore.QRect(840, 410, 101, 51))
        self.jiesuan_lab.setStyleSheet("font: 20pt \"华文行楷\";")
        self.jiesuan_lab.setText("")
        self.jiesuan_lab.setObjectName("jiesuan_lab")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(810, 40, 72, 31))
        self.label.setStyleSheet("font: 18pt \"华文行楷\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(810, 70, 72, 31))
        self.label_2.setStyleSheet("font: 18pt \"华文行楷\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(810, 30, 71, 81))
        self.pushButton_3.setStyleSheet("background-color:transparent;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(460, 330, 93, 61))
        self.pushButton.setStyleSheet("background-color: transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(850, 390, 101, 61))
        self.label_3.setStyleSheet("font: 18pt \"华文行楷\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 380, 101, 71))
        self.pushButton_2.setStyleSheet("background-color: transparent;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.open_game_exit)
        self.pushButton.clicked.connect(Form.play)
        self.pushButton_2.clicked.connect(Form.jiesuan)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.play_lab.setText(_translate("Form", "出牌"))
        self.label.setText(_translate("Form", "返回"))
        self.label_2.setText(_translate("Form", "房间"))
        self.label_3.setText(_translate("Form", "结算"))
import images_rc
