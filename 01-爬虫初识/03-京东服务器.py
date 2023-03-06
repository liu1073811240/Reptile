# -- coding: utf-8 --
# @Time : 2023/2/3 14:12
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 03-京东服务器.py
# @Software: PyCharm

import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8888))
sock.listen(3)

while True:
    print("京东服务器已经启动...")
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("data:", data)
    try:
        path = data.decode().split("\r\n")[0].split(" ")[1]
    except:
        print()
        path = ''

    # 请求data解析， 获取路径 path
    if path == "/login":
        conn.send(b"HTTP/1.1 200 ok\r\ncontent-type:text/plain\r\n\r\nlogin...")
    elif path == '/index':
        # conn.send(b"HTTP/1.1 200 ok\r\ncontent-type:text/plain\r\n\r\nindex..")
        conn.send(b"HTTP/1.1 200 ok\r\ncontent-type:text/html\r\n\r\n<h1>hello hei girl</h1><img src='https://img1.baidu.com/it/u=1147992555,4285883113&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500'>")

    else:
        conn.send(b"HTTP/1.1 404 Not Found\r\ncontent-type:text/plain\r\n\r\n404!")

    # conn.send(b"HTTP/1.1 200 ok\r\ncontent-type:text/html\r\n\r\n<h1>hello hei girl</h1><img src='https://img1.baidu.com/it/u=1147992555,4285883113&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500'>")
    # conn.send(b"HTTP/1.1 200 ok\r\ncontent-type:text/plain\r\n\r\n<h1>hello hei girl</h1><img src='https://img1.baidu.com/it/u=1147992555,4285883113&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500'>")

    conn.close()



