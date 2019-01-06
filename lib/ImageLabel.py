import time
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMenu, QAction


class MyImageLabel(QLabel):
    #图片label
    def __init__(self,centralwidget,dialog=0):
        #传入窗体
        super().__init__(centralwidget)
        self.stone = 1
        self.dialog=dialog
        self.window=centralwidget
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)

    def focusInEvent(self, QFocusEvent):
        try:
            self.shy()
        except Exception as e:
            print(e)

    def say(self,content):
        if self.dialog:
            self.dialog.setText(content)
    def myTimer(self,function):
        self.t = QTimer()  # 初始化一个定时器
        self.t.timeout.connect(function)  # 计时结束调用operate()方法
        self.t.start(2000)  # 设置计时间隔并启动
    def shy(self):
        pix = QPixmap('icon/action2.png')
        self.setPixmap(pix)
        self.myTimer(self.normal)
    def normal(self):
        pix = QPixmap('icon/action1.png')
        self.setPixmap(pix)
    def rightMenuShow(self, point):
            self.popMenu = QMenu()
            tj=QAction(u'添加', self)
            sc=QAction(u'删除', self)
            xg = QAction(u'修改', self)
            self.popMenu.addAction(tj)
            self.popMenu.addAction(sc)
            self.popMenu.addAction(xg)
            tj.triggered.connect(lambda :self.test('走开'))
            sc.triggered.connect(lambda :self.test('滚'))
            xg.triggered.connect(lambda :self.test('一边去'))
            self.showContextMenu(QtGui.QCursor.pos())
    def test(self,content):
        self.say(content)
    def showContextMenu(self, pos):
        '''''
        右键点击时调用的函数
        '''
        # 菜单显示前，将它移动到鼠标点击的位置

        self.popMenu.move( pos)
        self.popMenu.show()