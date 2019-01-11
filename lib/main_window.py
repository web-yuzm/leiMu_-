#coding:utf-8
import json
from PyQt5.QtGui import QPixmap, QCursor
from lib.ImageLabel import MyImageLabel
from lib.MainFrame import MyWindow
from lib.Tray_window import MyTray
from lib.dialog_label import dialog_label
from ui.Ui_mywindow import Ui_mywindow
from PyQt5 import Qt, QtGui, QtCore, QtWidgets

class main_window(Ui_mywindow):
    # window.setWindowOpacity(0.5)
    def __init__(self):
        super().__init__()
        window = MyWindow()
        self.tray = MyTray(window)
        window.tray=self.tray
        self.centralwidget = QtWidgets.QWidget(window)
        self.dialog_label = dialog_label(self.centralwidget)
        # self.dialog_label.setText('test')
        self.dialog_label.setGeometry(QtCore.QRect(30, 190, 100, 41))
        window.setObjectName("mywindow")
        window.resize(321, 558)
        window.setWindowFlags(Qt.Qt.FramelessWindowHint|Qt.Qt.WindowStaysOnTopHint)
        window.setAttribute(Qt.Qt.WA_TranslucentBackground)
        window.setCentralWidget(self.centralwidget)
        # super().setupUi(window)
        self.window = window

        self.image_label=MyImageLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(20, 160, 271, 391))
        self.image_label.dialog=self.dialog_label
        # super().retranslateUi(window)
        try:
            j = self.load_location()
            self.window.move(j['x'], j['y'])
        except Exception as e:
            print(e)
            self.window.save_location()
            j=self.load_location()
            self.window.move(j['x'],j['y'])
        self.pic()
        self.window.show()
    def pic(self):#看板娘图片
        pix = QPixmap('icon/action1.png')
        scale = 1#暂时没用
        self.image_label.setPixmap(pix)

    def load_location(self):
        with open('window_location.txt', 'r') as f:
            txt = f.read()
            j = json.loads(txt)
            return j
    # def setRightClickMenu(self,window):
    #     self.window.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    #     self.window.customContextMenuRequested.connect(self.rightMenuShow)
    #     QtCore.QMetaObject.connectSlotsByName(window)

    # def rightMenuShow(self):
    #     try:
    #         self.contextMenu = QMenu()
    #         self.actionA = self.contextMenu.addAction(u'动作')
    #         self.contextMenu.popup(QCursor.pos(self))  # 2菜单显示的位置
    #         self.actionA.triggered.connect(self.actionHandler)
    #         self.contextMenu.show()
    #     except Exception as e:
    #         print(e)
    # def actionHandler(self):
    #     print('action')
    #     self.window.close()

