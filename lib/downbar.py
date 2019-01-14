#coding:utf-8
from PyQt5.QtWidgets import QDialog, QSystemTrayIcon, QMenu ,QAction,QApplication
from PyQt5.QtGui import QIcon
import sys
class main(QDialog):
    #托盘
    def __init__(self):
        super().__init__()
        self.loadMenu()
        self.initUI()

    def loadMenu(self):
        menuItems = []
        menuItems.append({"text": "启动", "icon": "./icon/launch.png", "event": self.show, "hot": "D"})
        menuItems.append({"text": "退出", "icon": "./icon/car.png", "event": self.close, "hot": "Q"})
        self.trayIconMenu = QMenu(self)
        for i in menuItems:
             tmp = QAction(QIcon(i["icon"]), i["text"],self, triggered=i["event"])
             tmp.setShortcut(self.tr(i["hot"]))
             self.trayIconMenu.addAction(tmp)

    def initUI(self):
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("./icon/car.png"))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()
        self.setWindowIcon(QIcon("./icon/car.png"))
        self.setGeometry(300, 300, 180, 300)
        self.setWindowTitle('窗体标题')
    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.trayIcon.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())