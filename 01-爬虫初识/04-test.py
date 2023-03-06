# -- coding: utf-8 --
# @Time : 2023/2/9 16:10
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 04-test.py
# @Software: PyCharm

import requests


# res = requests.get('https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=')
res = requests.get('https://paddlenlp.bj.bcebos.com/data/automobile_mrc_train.json')


print(res.text)
# print(res.json())
# print(res.json().get("cityid"))

with open('file.txt', 'w', encoding='utf-8') as f:
    f.write(res.text)

