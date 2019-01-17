#coding:utf-8
import json

from PyQt5 import Qt, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from lib.MainFrame import MyWindow
from lib.dialog_label import dialog_label

from ui.Ui_mywindow import Ui_mywindow
from window.ImageLabel import MyImageLabel
from window.float_window import FloatWindow


class main_window(Ui_mywindow):
    # 主窗口
    def __init__(self):
        super().__init__()
        window = MyWindow('main')
        # self.tray = MyTray(window)
        # window.tray=self.tray
        float=FloatWindow('dialog')
        self.centralwidget = QtWidgets.QWidget(window)
        self.widget2=QtWidgets.QWidget(float)
        self.dialog_label = dialog_label(self.widget2)
        self.dialog_label.setGeometry(QtCore.QRect(0, 80, 251, 91))
        self.dialog_label.hide()
        window.setObjectName("mywindow")
        window.resize(321, 558)
        window.setWindowFlags(Qt.Qt.FramelessWindowHint|Qt.Qt.WindowStaysOnTopHint|Qt.Qt.Tool)
        window.setAttribute(Qt.Qt.WA_TranslucentBackground)
        window.setCentralWidget(self.centralwidget)

        float.resize(321, 558)
        float.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.WindowStaysOnTopHint|Qt.Qt.Tool)
        float.setAttribute(Qt.Qt.WA_TranslucentBackground)
        float.setCentralWidget(self.widget2)
        self.float=float

        self.window = window

        self.image_label=MyImageLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(20, 120, 271, 391))
        self.image_label.dialog=self.dialog_label
        self.pic()
        self.talk_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.talk_edit.setGeometry(QtCore.QRect(20, 480, 201, 21))
        self.talk_edit.setObjectName("talk_edit")
        self.talk_edit.hide()
        self.image_label.ear=self.talk_edit
        self.window.show()
        self.float.show()
        self.talk_edit.returnPressed.connect(self.talk)


    def pic(self):#看板娘图片
        pix = QPixmap('icon/action1.png')
        scale = 1#暂时没用
        self.image_label.setPixmap(pix)

    def load_location(self):
        with open('window_location.txt', 'r') as f:
            txt = f.read()
            j = json.loads(txt)
            return j
    def talk(self):
        self.say(self.talk_edit.text().replace('吗','').replace('?','!').replace('你','我'))
    def say(self,content):
        self.image_label.say(content)