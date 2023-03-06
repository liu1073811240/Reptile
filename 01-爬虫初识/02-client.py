# -- coding: utf-8 --
# @Time : 2023/2/2 15:43
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-client.py
# @Software: PyCharm

import socket

sock = socket.socket()

sock.connect(("127.0.0.1", 5501))

sock.send(b"hello world")

res = sock.recv(1024)

print("服务端相应数据：", res.decode())
