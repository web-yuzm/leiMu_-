# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mywindow(object):
    def setupUi(self, mywindow):
        mywindow.setObjectName("mywindow")
        mywindow.resize(321, 558)
        self.centralwidget = QtWidgets.QWidget(mywindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(20, 160, 271, 391))
        self.image_label.setObjectName("image_label")
        self.dialog_label = QtWidgets.QLabel(self.centralwidget)
        self.dialog_label.setGeometry(QtCore.QRect(30, 30, 251, 91))
        self.dialog_label.setObjectName("dialog_label")
        mywindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mywindow)
        QtCore.QMetaObject.connectSlotsByName(mywindow)

    def retranslateUi(self, mywindow):
        _translate = QtCore.QCoreApplication.translate
        mywindow.setWindowTitle(_translate("mywindow", "MainWindow"))
        self.image_label.setText(_translate("mywindow", "TextLabel"))
        self.dialog_label.setText(_translate("mywindow", "TextLabel"))

