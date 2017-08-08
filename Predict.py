# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Predict.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_predictDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(700, 419)
        self.tableWidget_1 = QtGui.QTableWidget(Dialog)
        self.tableWidget_1.setGeometry(QtCore.QRect(10, 50, 291, 351))
        self.tableWidget_1.setRowCount(10)
        self.tableWidget_1.setColumnCount(2)
        self.tableWidget_1.setObjectName(_fromUtf8("tableWidget_1"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, item)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(360, 180, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_1 = QtGui.QLineEdit(Dialog)
        self.lineEdit_1.setGeometry(QtCore.QRect(440, 180, 181, 21))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.predictResultLabel = QtGui.QLabel(Dialog)
        self.predictResultLabel.setGeometry(QtCore.QRect(440, 260, 181, 21))
        self.predictResultLabel.setFrameShape(QtGui.QFrame.Box)
        self.predictResultLabel.setText(_fromUtf8(""))
        self.predictResultLabel.setObjectName(_fromUtf8("predictResultLabel"))
        self.predictButton_1 = QtGui.QPushButton(Dialog)
        self.predictButton_1.setGeometry(QtCore.QRect(440, 220, 75, 23))
        self.predictButton_1.setObjectName(_fromUtf8("predictButton_1"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(350, 260, 91, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.linearModelButton = QtGui.QPushButton(Dialog)
        self.linearModelButton.setGeometry(QtCore.QRect(440, 300, 101, 23))
        self.linearModelButton.setObjectName(_fromUtf8("linearModelButton"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 40, 151, 121))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("house-prices-up.jpg")))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Square_Feet", None))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Price", None))
        self.label.setText(_translate("Dialog", "House Price Prediction", None))
        self.label_2.setText(_translate("Dialog", "Square Feet :", None))
        self.predictButton_1.setText(_translate("Dialog", "Predict Price", None))
        self.label_4.setText(_translate("Dialog", "Predicted Price :", None))
        self.linearModelButton.setText(_translate("Dialog", "Show Linear Model", None))

