# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1100, 860)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 231, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 231, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 231, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 231, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(680, 10, 401, 101))
        self.label.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(690, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(690, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(690, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(840, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_name.setFont(font)
        self.label_name.setText("")
        self.label_name.setObjectName("label_name")
        self.label_surname = QtWidgets.QLabel(Form)
        self.label_surname.setGeometry(QtCore.QRect(840, 50, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_surname.setFont(font)
        self.label_surname.setText("")
        self.label_surname.setObjectName("label_surname")
        self.label_access_level = QtWidgets.QLabel(Form)
        self.label_access_level.setGeometry(QtCore.QRect(840, 80, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_access_level.setFont(font)
        self.label_access_level.setText("")
        self.label_access_level.setObjectName("label_access_level")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(180, 10, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(99999)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 131, 31))
        self.pushButton.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 230, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 50, 181, 31))
        self.pushButton_2.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 230, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 50, 141, 31))
        self.pushButton_3.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 230, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(20, 120, 1061, 661))
        self.tableView.setObjectName("tableView")
        self.label_error = QtWidgets.QLabel(Form)
        self.label_error.setGeometry(QtCore.QRect(20, 800, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.label_convert = QtWidgets.QLabel(Form)
        self.label_convert.setGeometry(QtCore.QRect(20, 800, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_convert.setFont(font)
        self.label_convert.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_convert.setText("")
        self.label_convert.setObjectName("label_convert")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 50, 141, 31))
        self.pushButton_4.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 230, 255);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Основное окно"))
        self.label_2.setText(_translate("Form", "Имя:"))
        self.label_3.setText(_translate("Form", "Фамилия:"))
        self.label_4.setText(_translate("Form", "Уровень доступа:"))
        self.label_5.setText(_translate("Form", "Введите ID файла:"))
        self.pushButton.setText(_translate("Form", "Открыть файл"))
        self.pushButton_2.setText(_translate("Form", "Конвертировать файл в аудио"))
        self.pushButton_3.setText(_translate("Form", "Далее"))
        self.pushButton_4.setText(_translate("Form", "Добавить файл"))
