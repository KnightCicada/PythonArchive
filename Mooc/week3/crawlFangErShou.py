import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url,headers):
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(html):
    soup = BeautifulSoup(html, 'html.parser')
    goodsList = soup.find(class_='shop_list shop_list_4').find_all(dataflag='bg')
    # print(goodsList)
    # form = '{:^10}{:^50}{:<8}{:<8}{:4}{:10}{:20}{:20}'
    # print(form.format('序号','名字','价格','单价','城区','详细地址','信息','关注信息',chr(12288)))
    count = 0
    for item in goodsList:
        try:
            count += 1
            title = item.find(class_='tit_shop').string
            price = item.find(class_='price_right').find('span').text
            name = item.find(class_='add_shop').find('a').get('title')
            address = item.find(class_='add_shop').find('span').string
            print(name)
            # print(form.format(count,name,price,ave_price,location_rough,location_detail,info,info_more,chr(12288)))
        except:
            continue


def main():
    url = 'https://xian.esf.fang.com/'
    headers = {'User-Agent': 'Mozllia 4.0 (compatible; MSIE 5.5, Windows NT'}
    html = getHTMLText(url, headers)
    parsePage(html)
main()













