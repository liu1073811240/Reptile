# -- coding: utf-8 --
# @Time : 2023/2/13 15:03
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : server.py
# @Software: PyCharm

from flask import Flask


app = Flask(__name__)

@app.route('/index')
def index():
    return

@app.route('/login')
def index():
    return




