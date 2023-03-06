# -- coding: utf-8 --
# @Time : 2023/2/2 15:24
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-server.py
# @Software: PyCharm

import socket

# 网络三要素： IP PORT 协议（TCP, UDP）
sock = socket.socket()

sock.bind(("127.0.0.1", 5501))
sock.listen(5)

# 等待客户端来连接
print('Server is waiting...')
conn, addr = sock.accept()

print("conn:", conn)
print("addr:", addr)

data = conn.recv(1024)

print("data:", data)

conn.send(b"message has received")

