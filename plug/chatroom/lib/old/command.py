
class CommandHandler:
    """
    命令处理类
    """

    def unknown(self, session, cmd):
        '响应未知命令'
        session.push('Unknown command: %s\n' % cmd)

    def handle(self, session, line):
        '命令处理'
        if not line.strip():
            return
        parts = line.split(' ', 1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
        except IndexError:
            line = ''
        meth = getattr(self, 'do_' + cmd, None)
        try:
            meth(session, line)
        except TypeError:
            self.unknown(session, cmd)