import asyncore
import socket
from asyncore import dispatcher

from plug.chatroom.lib.rooms import ChatRoom

from plug.chatroom.lib.old.Session import ChatSession


class ChatServer(dispatcher):
    """
    聊天服务器
    """

    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('127.0.0.1', port))
        self.listen(5)
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)


if __name__=='__main__':
    port = 6666  # 设置服务器端口号
    server = ChatServer(port)  # 实例化聊天服务器
    try:
        asyncore.loop()  # 运行异步循环
    except KeyboardInterrupt:  # 捕获键盘中断异常
        print('服务器已被关闭！')
