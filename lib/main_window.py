#coding:utf-8
import json
from PyQt5.QtGui import QPixmap, QCursor
from lib.ImageLabel import MyImageLabel
from lib.MainFrame import MyWindow
from lib.Tray_window import MyTray
from lib.dialog_label import dialog_label
from lib.float_window import FloatWindow
from ui.Ui_mywindow import Ui_mywindow
from PyQt5 import Qt, QtGui, QtCore, QtWidgets

class main_window(Ui_mywindow):
    # 主窗口
    def __init__(self):
        super().__init__()
        window = MyWindow('main')
        self.tray = MyTray(window)
        window.tray=self.tray
        float=FloatWindow('dialog')
        self.centralwidget = QtWidgets.QWidget(window)
        self.widget2=QtWidgets.QWidget(float)
        self.dialog_label = dialog_label(self.widget2)
        self.dialog_label.setGeometry(QtCore.QRect(30, 190, 100, 41))
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
        self.image_label.setGeometry(QtCore.QRect(20, 160, 271, 391))
        self.image_label.dialog=self.dialog_label
        self.pic()

        self.window.show()
        self.float.show()


    def pic(self):#看板娘图片
        pix = QPixmap('icon/action1.png')
        scale = 1#暂时没用
        self.image_label.setPixmap(pix)

    def load_location(self):
        with open('window_location.txt', 'r') as f:
            txt = f.read()
            j = json.loads(txt)
            return j
