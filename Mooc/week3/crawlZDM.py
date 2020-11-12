import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url,headers):
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(html, list):
    soup = BeautifulSoup(html, 'html.parser')
    goodsList = soup.find(class_='feed-list-hits').find_all(class_='feed-block z-hor-feed')
    for item in goodsList:
        try:
            title = item.find('img').get('alt')
            raw_price = item.find(class_='z-highlight').find('a').string
            price = raw_price.replace('\n', '').replace(' ', '')#替换结果中的换行和空格
            print(title + '  |  ' + price)

        except:
            continue
    return list

def printTitle(list):
    form = '{0:^4}{1:{3}^16}{2:^6}'
    print(form.format('序号', '商品信息', '价格', chr(12288)))
    count = 0
    for i in range(250):
        count += 1
        print(form.format(count, list[i*2], list[i*2+1], chr(12288)))

def main():
    depth = 2
    start_url = 'https://www.smzdm.com/fenlei/jiulei/'
    headers = {'User-Agent': 'Mozllia 4.0 (compatible; MSIE 5.5, Windows NT'}
    titleList = []
    for i in range(depth):
        try:
            i += 1
            url = start_url+'p'+str(i)
            # print(url)
            html = getHTMLText(url, headers)
            parsePage(html, titleList)
        except:
            continue
    # printTitle(titleList)
main()













