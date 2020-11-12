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
    goodsList = soup.find(class_='sellListContent').find_all('li')
    # print(goodsList)
    form = '{:^10}{:^50}{:<8}{:<8}{:4}{:10}{:20}{:20}'
    print(form.format('序号','名字','价格','单价','城区','详细地址','信息','关注信息',chr(12288)))
    count = 0
    for item in goodsList:
        try:
            count += 1
            name = item.find(class_='title').find('a').string
            price = item.find(class_='totalPrice').find('span').string
            ave_price = item.find(class_='unitPrice').find('span').string
            location_detail = item.find(class_='positionInfo').find('a').string
            location_rough = item.find(class_='positionInfo').find(target='_blank').string
            info = item.find(class_='houseInfo').text
            info_more = item.find(class_='followInfo').text
            print(form.format(count,name,price,ave_price,location_rough,location_detail,info,info_more,chr(12288)))
        except:
            continue


def main():
    depth = 1
    start_url = 'https://xa.lianjia.com/ershoufang/pg'
    headers = {'User-Agent': 'Mozllia 4.0 (compatible; MSIE 5.5, Windows NT'}
    for i in range(depth):
        try:
            i += 1
            url = start_url+str(i)
            # print(url)
            html = getHTMLText(url, headers)
            parsePage(html)
        except:
            continue
main()













