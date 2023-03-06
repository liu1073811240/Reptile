import re

s = "666.chinaz.com|888;china"

# ret = re.findall("\d+", s)  # 取所有的数字出来
# ret = re.findall("\w+", s)  # 取所有的单词出来
ret = re.findall("[a-z]+", s)  # 取所有的英文词组出来

# re.sub()  # 替换
print(ret)


