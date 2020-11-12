import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url,headers):
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # print(r.text)
    return r.text

def parsePage(list, html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find(class_='J_ubt_module clearfix')

        for item in a.find_all(class_='price-num'):
            price = item.string
            # print(price)
            list.append(price)
        # print(list)
        for item in a.find_all('h4'):
            title = item.string
            # print(title)
            list.append(title)
        # print(list)

    except:
        print('爬取失败')


def printGoodlist(list):
    tplt = '{:4}\t{:6}\t\t{:32}'
    print(tplt.format('序号', '价格', '商品名称'))
    for i in range(16):
        print(tplt.format(i+1,list[i],list[i+16]))




def main():

    url = 'https://super.fanli.com/brand-85747/?lc=shouye_brand&spm=home.pc.bid-85747'
    headers = {'User-Agent': 'Mozilla 4.0 (compatible; MSIE 5.5; Windows NT'}
    infoList = []
    html = getHTMLText(url, headers)
    parsePage(infoList, html)
    printGoodlist(infoList)
main()
