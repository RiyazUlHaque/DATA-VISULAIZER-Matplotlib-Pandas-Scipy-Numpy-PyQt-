# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(995, 720)
        
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -20, 1001, 251))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("BigData.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.databaseButton = QtGui.QPushButton(Dialog)
        self.databaseButton.setGeometry(QtCore.QRect(560, 660, 101, 21))
        
        self.databaseButton.setObjectName(_fromUtf8("databaseButton"))
        self.comboCountry = QtGui.QComboBox(Dialog)
        self.comboCountry.setGeometry(QtCore.QRect(120, 290, 271, 22))
        
        self.comboCountry.setObjectName(_fromUtf8("comboCountry"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 290, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(120, 330, 271, 192))
        
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.addButton = QtGui.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(30, 340, 75, 23))
        
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.deleteButton = QtGui.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(30, 410, 75, 23))
        
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.clearAllButton = QtGui.QPushButton(Dialog)
        self.clearAllButton.setGeometry(QtCore.QRect(30, 490, 75, 23))
        
        self.clearAllButton.setObjectName(_fromUtf8("clearAllButton"))
        self.comboParameter = QtGui.QComboBox(Dialog)
        self.comboParameter.setGeometry(QtCore.QRect(120, 540, 271, 22))
        
        self.comboParameter.setObjectName(_fromUtf8("comboParameter"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 540, 91, 20))
        
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.showGraphButton = QtGui.QPushButton(Dialog)
        self.showGraphButton.setGeometry(QtCore.QRect(200, 680, 101, 31))
        
        self.showGraphButton.setObjectName(_fromUtf8("showGraphButton"))
        self.showGraphButton_2 = QtGui.QPushButton(Dialog)
        self.showGraphButton_2.setGeometry(QtCore.QRect(770, 610, 101, 31))
        
        self.showGraphButton_2.setObjectName(_fromUtf8("showGraphButton_2"))
        self.listWidget_2 = QtGui.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(670, 330, 291, 192))
        
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.comboCountry_2 = QtGui.QComboBox(Dialog)
        self.comboCountry_2.setGeometry(QtCore.QRect(670, 540, 291, 22))
        
        self.comboCountry_2.setObjectName(_fromUtf8("comboCountry_2"))
        self.comboParameter_2 = QtGui.QComboBox(Dialog)
        self.comboParameter_2.setGeometry(QtCore.QRect(670, 290, 291, 22))
        
        self.comboParameter_2.setObjectName(_fromUtf8("comboParameter_2"))
        self.deleteButton_2 = QtGui.QPushButton(Dialog)
        self.deleteButton_2.setGeometry(QtCore.QRect(580, 410, 75, 23))
        
        self.deleteButton_2.setObjectName(_fromUtf8("deleteButton_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(570, 290, 101, 20))
        
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(580, 540, 91, 20))
        
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.clearAllButton_2 = QtGui.QPushButton(Dialog)
        self.clearAllButton_2.setGeometry(QtCore.QRect(580, 490, 75, 23))
        
        self.clearAllButton_2.setObjectName(_fromUtf8("clearAllButton_2"))
        self.addButton_2 = QtGui.QPushButton(Dialog)
        self.addButton_2.setGeometry(QtCore.QRect(580, 340, 75, 23))
        
        self.addButton_2.setObjectName(_fromUtf8("addButton_2"))
        self.radioButtonEnergy = QtGui.QRadioButton(Dialog)
        self.radioButtonEnergy.setGeometry(QtCore.QRect(400, 540, 131, 17))
        
        self.radioButtonEnergy.setObjectName(_fromUtf8("radioButtonEnergy"))
        self.radioButtonHealth = QtGui.QRadioButton(Dialog)
        self.radioButtonHealth.setGeometry(QtCore.QRect(400, 590, 131, 17))
        
        self.radioButtonHealth.setObjectName(_fromUtf8("radioButtonHealth"))
        self.radioButtonPop = QtGui.QRadioButton(Dialog)
        self.radioButtonPop.setGeometry(QtCore.QRect(400, 640, 131, 17))
        
        self.radioButtonPop.setObjectName(_fromUtf8("radioButtonPop"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 590, 91, 20))
        
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboParameterHealth = QtGui.QComboBox(Dialog)
        self.comboParameterHealth.setGeometry(QtCore.QRect(120, 590, 271, 22))
        
        self.comboParameterHealth.setObjectName(_fromUtf8("comboParameterHealth"))
        self.comboParameterPop = QtGui.QComboBox(Dialog)
        self.comboParameterPop.setGeometry(QtCore.QRect(120, 640, 271, 22))
        
        self.comboParameterPop.setObjectName(_fromUtf8("comboParameterPop"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 640, 91, 20))
        
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.radioButtonBar = QtGui.QRadioButton(Dialog)
        self.radioButtonBar.setGeometry(QtCore.QRect(740, 580, 82, 17))
        
        self.radioButtonBar.setObjectName(_fromUtf8("radioButtonBar"))
        self.radioButtonPie = QtGui.QRadioButton(Dialog)
        self.radioButtonPie.setGeometry(QtCore.QRect(840, 580, 82, 17))
        
        self.radioButtonPie.setObjectName(_fromUtf8("radioButtonPie"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(510, 230, 16, 491))
        self.label_8.setFrameShape(QtGui.QFrame.VLine)
        self.label_8.setText(_fromUtf8(""))
        
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.aboutButton = QtGui.QPushButton(Dialog)
        self.aboutButton.setGeometry(QtCore.QRect(560, 690, 101, 21))
        
        self.aboutButton.setObjectName(_fromUtf8("aboutButton"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(50, 250, 341, 21))
        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtGui.QFrame.Box)
        
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(620, 250, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtGui.QFrame.Box)
        
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.predictButon = QtGui.QPushButton(Dialog)
        self.predictButon.setGeometry(QtCore.QRect(560, 630, 101, 20))
        
        self.predictButon.setObjectName(_fromUtf8("predictButon"))
        self.retranslateUi(Dialog)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.databaseButton.setText(_translate("Dialog", "Database", None))
        self.label_2.setText(_translate("Dialog", "Select Countries :", None))
        self.addButton.setText(_translate("Dialog", "Add", None))
        self.deleteButton.setText(_translate("Dialog", "Delete", None))
        self.clearAllButton.setText(_translate("Dialog", "Clear All", None))
        self.label_3.setText(_translate("Dialog", "Select Parameter :", None))
        self.showGraphButton.setText(_translate("Dialog", "SHOW GRAPH", None))
        self.showGraphButton_2.setText(_translate("Dialog", "SHOW GRAPH", None))
        self.deleteButton_2.setText(_translate("Dialog", "Delete", None))
        self.label_4.setText(_translate("Dialog", "Select Parameters :", None))
        self.label_5.setText(_translate("Dialog", "Select Country :", None))
        self.clearAllButton_2.setText(_translate("Dialog", "Clear All", None))
        self.addButton_2.setText(_translate("Dialog", "Add", None))
        self.radioButtonEnergy.setText(_translate("Dialog", "Energy Reports", None))
        self.radioButtonHealth.setText(_translate("Dialog", "Health Reports", None))
        self.radioButtonPop.setText(_translate("Dialog", "Population Reports", None))
        self.label_6.setText(_translate("Dialog", "Select Parameter :", None))
        self.label_7.setText(_translate("Dialog", "Select Parameter :", None))
        self.radioButtonBar.setText(_translate("Dialog", "Bar Chart", None))
        self.radioButtonPie.setText(_translate("Dialog", "Pie Chart", None))
        self.aboutButton.setText(_translate("Dialog", "About", None))
        self.label_9.setText(_translate("Dialog", "VISUALIZATION AMONG MULTIPLE COUNTRIES", None))
        self.label_10.setText(_translate("Dialog", "VISUALIZATION AMONG MULTIPLE PARAMETERS", None))
        self.predictButon.setText(_translate("Dialog", "Prediction", None))
        print("DONE")

