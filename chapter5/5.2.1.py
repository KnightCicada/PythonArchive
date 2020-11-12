#http://www.ivsky.com/tupian/ziranfengguang/
#coding:utf-8

'''
导入etree的方法
from lxml import html
etree = html.etree
'''

import urllib.request
import requests
import ssl
from lxml import html


def Schedule(blocknum,blocksize,totalsize):


    '''''
    blocknum:已经下载的数据块
    blocksize:数据块的大小
    totalsize:远程文件的大小
    '''

    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100 :
        per = 100
    print('当前下载进度：%d'%per)


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('https://www.ivsky.com/tupian/ziranfengguang/', headers=headers)
#使用lxml解析网页
etree = html.etree
html = etree.HTML(r.text)

img_urls = html.xpath('.//img/@src')#先找到所有的img
i = 0
for img_url in img_urls:
    print(img_url)
    urllib.request.urlretrieve('https:'+img_url, 'E:\Img\img'+str(i)+'.jpg')
    i += 1
