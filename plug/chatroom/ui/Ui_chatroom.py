# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatroom.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_chatroom(object):
    def setupUi(self, chatroom):
        chatroom.setObjectName("chatroom")
        chatroom.resize(974, 669)
        self.centralwidget = QtWidgets.QWidget(chatroom)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setMaximumSize(QtCore.QSize(400, 16777215))
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(16777214, 500))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        chatroom.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chatroom)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 26))
        self.menubar.setObjectName("menubar")
        chatroom.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(chatroom)
        self.statusbar.setObjectName("statusbar")
        chatroom.setStatusBar(self.statusbar)

        self.retranslateUi(chatroom)
        QtCore.QMetaObject.connectSlotsByName(chatroom)

    def retranslateUi(self, chatroom):
        _translate = QtCore.QCoreApplication.translate
        chatroom.setWindowTitle(_translate("chatroom", "MainWindow"))
        self.pushButton.setText(_translate("chatroom", "发送"))
        self.pushButton_2.setText(_translate("chatroom", "清空"))

