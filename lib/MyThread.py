#coding:utf-8
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow
from plug.chatroom.lib.server.server import Server as chat_server, Server


def init_server():
    server=Server()
    server.start()
