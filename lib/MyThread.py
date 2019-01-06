#coding:utf-8
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow,QDialog
from ui.Ui_progress_bar import Ui_Form as progress_bar
from windows.filesave import filesave
from windows.mwin import mwin
from windows.setting import setting


def init_mwin(parent):
    m = wake_mwin()
    m.run()
    parent.son = m
    if not m.p.window.isVisible():
        m.p.window.show()

def init_setting(parent):

    m = wake_setting()
    m.run()
    parent.son = m
    if not m.p.window.isVisible():
        m.p.window.show()
def init_file(parent):
    m = wake_file()
    m.run()
    parent.son = m
    if not m.p.window.isVisible():
        m.p.window.show()
def init_progress(parent):
    m = wake_progress()
    parent.progress = m
    m.run()
    if not m.window.isVisible():
        m.window.show()
class wake_file(QThread):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
    def run(self):
        self.p=filesave(self.window)

class wake_mwin(QThread):
    def __init__(self):

        super().__init__()
        self.window = QMainWindow()
    def run(self):
        self.p=mwin(self.window)

class wake_setting(QThread):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
    def run(self):
        self.p =setting(self.window)


class wake_progress(QThread):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()

        self.p=''
    def run(self):
        self.p =file_upload_statu_bar(self.window)

class file_upload_statu_bar(progress_bar):
    #进度条类
    def setupUi(self, Form):
        super().setupUi(Form)
        self.comfire_btn.clicked.connect(self.submit)
    def __init__(self,Form):
        print('progress bar')
        self.window=Form
        super().__init__()
        self.setupUi(Form)
        self.window.show()
    def change(self,name):
        self.label.setText(name)
    def submit(self):
        self.window.close()
