import socket
class client():
    def __init__(self,host,name,port=12345):
        # 客户端Linux系统下：输入命令通过服务端返回
        # 声明协议类型,同事生成socket连接对象
        client = socket.socket()

        # 链接地址和端口,元组(本地，端口)
        client.connect((host, port))

        # 使用input循环向服务端发送请求
        while True:
            msg = input(">>:").strip()
            if len(msg) == 0: continue

            # 发送数据 b将字符串转为bys类型
            client.send(msg.encode('utf-8'))

            # 接收服务器端的返回，需要声明收多少，默认1024字节
            data = client.recv(1024)

            # 打印data是recv的data
            print("recv:", data)

        # 关闭接口
        client.close()
if __name__=='__main__':
    c=client('127.0.0.1','frank')
