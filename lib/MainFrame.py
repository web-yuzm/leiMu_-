import json

from PyQt5 import Qt
from PyQt5.QtGui import QCursor

from PyQt5.QtWidgets import QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tray=0

    def closeEvent(self, *args, **kwargs):
        if self.tray:
            try:
                self.tray.deleteLater()
            except Exception as e:
                print(e)
            print("delete")
        # self.
    def mousePressEvent(self, event):
        if event.button() == Qt.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.Qt.ArrowCursor))
        self.save_location()
    def save_location(self):
        with open('window_location.txt', 'w') as f:
            data = {'x': self.x(), 'y': self.y()}
            print(data)
            f.write(json.dumps(data))


