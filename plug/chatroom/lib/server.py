import socket
from asyncore import dispatcher
from plug.chatroom.lib.Session import ChatSession
from plug.chatroom.lib.rooms import ChatRoom


class ChatServer(dispatcher):
    """
    聊天服务器
    """

    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)


# if __name__=='__main__':
#     start()