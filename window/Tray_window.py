from PyQt5 import QtGui

from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction


class MyTray(QSystemTrayIcon):
    def __init__(self,window):
        super().__init__()
        self.parent_window = window
        try:
            self.setIcon(QtGui.QIcon('icon/leimu.ico'))
            self.activated.connect(self.iconClicked)

            self.showMenu()
        except Exception as e:
            print(e)
    def test(self):
        try:
            self.parent_window.show()
            print('test')
        except Exception as e:
            print(e)

    def iconClicked(self,reason):
    #鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        print('click')
        if reason == 2 :#2是双击
            self.test()
    def hide(self):
        self.parent_window.hide()
    def showMenu(self):
        "设计托盘的菜单，这里我实现了一个二级菜单"
        self.menu = QMenu()
        self.menu1 = QMenu()
        self.showAction1 = QAction("显示", self, triggered=self.test)
        self.showAction2 = QAction("显示消息2", self,triggered=self.test)
        self.quitAction = QAction("退出", self, triggered=self.hide)
        self.menu1.addAction(self.showAction1)
        self.menu1.addAction(self.showAction2)
        self.menu.addMenu(self.menu1, )
        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.menu1.setTitle("设置")
        self.setContextMenu(self.menu)