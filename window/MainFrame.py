from PyQt5 import Qt
from PyQt5.QtGui import QCursor

from window.float_window import FloatWindow


class MyWindow(FloatWindow):
    #
    def __init__(self,name):
        super().__init__(name)
        self.tray=0

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
