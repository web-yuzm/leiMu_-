import time
from PyQt5 import QtGui, QtCore, Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QFontMetrics
from PyQt5.QtWidgets import QLabel, QMenu, QAction, QApplication

# from lib.MyThread import init_server, wake_server
from plug.chatroom.lib.server.server import Server


class MyImageLabel(QLabel):
    #图片加载控件
    def __init__(self,centralwidget,dialog=0):
        #传入窗体
        super().__init__(centralwidget)
        self.stone = 1
        self.dialog=dialog
        self.window=centralwidget
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ear=''


        self.setAcceptDrops(True)
    def mouseDoubleClickEvent(self, *args, **kwargs):

        if self.ear!='':
            self.ear.show()


    def say(self,content,time=2000):
        print(content)
        if self.dialog:
            self.dialog.show()
            index=0
            temp=''
            for i in content:
                if index>5:
                    i+='\n'
                    index=0
                temp+=i
            self.dialog.setText(temp)
        try:
            self.myTimer(self.back,4000)
        except Exception as e:
            print(e)
    def back(self):
        self.dialog.hide()
        # self.dialog.setGeometry(QtCore.QRect(30, 190, 100, 40))#还原对话框
        # self.dialog.setText('等待指令')


    def myTimer(self,function,time=2000):
        self.t = QTimer()  # 初始化一个定时器
        self.t.timeout.connect(function)  # 计时结束调用operate()方法
        self.t.start(time)  # 设置计时间隔并启动
    def shy(self):
        pix = QPixmap('icon/action2.png')
        self.setPixmap(pix)
        self.myTimer(self.normal)
    def normal(self):
        pix = QPixmap('icon/action1.png')
        self.setPixmap(pix)
    def rightMenuShow(self, point):
            self.popMenu = QMenu()
            tj=QAction(u'聊天功能', self)
            sc=QAction(u'删除', self)
            xg = QAction(u'退出', self)
            self.popMenu.addAction(tj)
            self.popMenu.addAction(sc)
            self.popMenu.addAction(xg)
            tj.triggered.connect(lambda :self.chat_server())
            sc.triggered.connect(lambda :self.test('滚'))
            xg.triggered.connect(lambda :self.shut())
            self.showContextMenu(QtGui.QCursor.pos())
    def test(self,content):
        self.say(content)
    def chat_server(self):
        server = Server()
        server.start()
        server.trigger.connect(lambda :self.say('hello'))

    def shut(self):
        QApplication.quit()
    def showContextMenu(self, pos):
        '''''
        右键点击时调用的函数
        '''
        # 菜单显示前，将它移动到鼠标点击的位置

        self.popMenu.move( pos)
        self.popMenu.show()
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            try:
                event.setDropAction(Qt.Qt.CopyAction)
            except Exception as e:
                print(e)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        try:
            if event.mimeData().hasUrls:
                event.setDropAction(Qt.Qt.CopyAction)
                event.accept()
                links = []
                for url in event.mimeData().urls():
                    path=str(url.toLocalFile())
                    data={'filename':path.split(r'/')[-1],'path':path}
                    self.file_type_check(data)
                print(links)
            else:
                event.ignore()
        except Exception as e:
            print(e)
    def file_type_check(self,data):
        if data['filename'].split('.')[-1] == 'py':
            from plug.run_python.lib.run_py_script import run_that
            try:
                print(data['path'].replace('\\', '/'))
                res = run_that('python '+data['path'].replace('\\', '/'))  # 正在施工

                self.say(res,8000)
            except:
                self.say('脚本里有错误哦')
        else:
            from plug.run_python.lib.run_py_script import run_that
            res = run_that(data['path'].replace('\\', '/'))  # 正在施工
            # links.append(data)