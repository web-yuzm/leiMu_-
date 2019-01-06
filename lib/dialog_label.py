from PyQt5 import Qt, QtCore

from PyQt5.QtWidgets import QLabel, QFrame


# from PyQt5.QtCore import QFrame


class dialog_label(QLabel):
    def __init__(self,centralwidget):
        super().__init__(centralwidget)
        # self.dialog_label.setGeometry(QtCore.QRect(30, 30, 251, 91))
        self.setFrameShape(QFrame.Box)
        self.setStyleSheet('border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);'+
                           'background-color: rgb(100,149,237);color:rgb(255,255,255);'+
                            'border-radius:15px; border-left:20px;padding-left:20px;'

                           )
        print('dialog_label')