from asynchat import async_chat

from plug.chatroom.lib.old.rooms import LogoutRoom, LoginRoom


class ChatSession(async_chat):
    """
    负责和单用户通信
    """

    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator('\n')
        self.data = []
        self.name = None
        self.enter(LoginRoom(server))

    def enter(self, room):
        '从当前房间移除自身，然后添加到指定房间'
        try:
            cur = self.room
        except AttributeError:
            pass
        else:
            cur.remove(self)
        self.room = room
        room.add(self)

    def collect_incoming_data(self, data):
        '接受客户端的数据'
        self.data.append(data)

    def found_terminator(self):
        '当客户端的一条数据结束时的处理'
        line = ''.join(self.data)
        self.data = []
        try:
            self.room.handle(self, line)
        except EndSession:
            self.handle_close()

    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(conn))
class EndSession(Exception):
    """
    自定义会话结束时的异常
    """
    pass