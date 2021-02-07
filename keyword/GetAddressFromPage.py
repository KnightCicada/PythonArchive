import os
import re
from itertools import chain


def fun(list):
    path = "/Users/Eureka/personal/python/keyword/test/"
    filelist = [path + i for i in os.listdir(path)]
    for file in filelist:
        if file.endswith(".txt"):
            getContent(file, list)


def getContent(name, list):
    f = open(name, "r")  # 设置文件对象
    str = f.read()  # 将txt文件的所有内容读入到字符串str中

    pattern = re.compile(r'https*://\w+\.onion')
    res = re.findall(pattern, str)

    if len(res) != 0:
        list.append(res)
    f.close()  # 将文件关闭


if __name__ == '__main__':
    addressList = []
    fun(addressList)
    print(addressList)
    uniqueList = list(chain(*addressList))
    addressSet = set(uniqueList)
    print(len(addressSet))
