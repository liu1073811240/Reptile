with open("豆瓣top250.html", 'r', encoding='utf-8') as f:
    s = f.read()
# print(s)

import re

ret = re.findall('<li>.*?class="item">.*?<div class="info">.*?<div class="hd">.*?<span class="title">(.*?)</span>.*?<div class="bd">.*?<p class="">(.*?)<span class="rating_num".*?>(.+?)</span>', s, re.S)
print(ret)
print(len(ret))


