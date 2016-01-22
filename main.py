# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Jan 23 02:29:14 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(320, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.sta_lab_buy = QtGui.QLabel(self.centralwidget)
        self.sta_lab_buy.setGeometry(QtCore.QRect(10, 10, 45, 20))
        self.sta_lab_buy.setObjectName(_fromUtf8("sta_lab_buy"))
        self.sta_lab_sell = QtGui.QLabel(self.centralwidget)
        self.sta_lab_sell.setGeometry(QtCore.QRect(10, 30, 45, 20))
        self.sta_lab_sell.setObjectName(_fromUtf8("sta_lab_sell"))
        self.dina_num_buy = QtGui.QLabel(self.centralwidget)
        self.dina_num_buy.setGeometry(QtCore.QRect(90, 10, 80, 20))
        self.dina_num_buy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dina_num_buy.setObjectName(_fromUtf8("dina_num_buy"))
        self.dina_num_sell = QtGui.QLabel(self.centralwidget)
        self.dina_num_sell.setGeometry(QtCore.QRect(90, 30, 80, 20))
        self.dina_num_sell.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dina_num_sell.setObjectName(_fromUtf8("dina_num_sell"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.sta_lab_buy.setText(_translate("MainWindow", "ราคาซื้อ", None))
        self.sta_lab_sell.setText(_translate("MainWindow", "ราคาขาย", None))
        self.dina_num_buy.setText(_translate("MainWindow", "0", None))
        self.dina_num_sell.setText(_translate("MainWindow", "0", None))

