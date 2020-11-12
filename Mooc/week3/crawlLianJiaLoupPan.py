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
    goodsList = soup.find(class_='resblock-list-container clearfix').find_all('li')
    # print(goodsList)
    for item in goodsList:
        try:
            name = item.find('a').get('title')
            price = item.find(class_='main-price').find(class_='number').string
            location_block = item.find(class_='resblock-location').find('span').string
            location_detail = item.find(class_='resblock-location').find('a').string
            img = item.find(class_='lj-lazy').get('data-original')
            raw_tag = item.find(class_='resblock-tag').find_all('span')#
            print(raw_tag)
        except:
            continue
    return list

def main():
    depth = 1
    start_url = 'https://xa.fang.lianjia.com/loupan/pg'
    headers = {'User-Agent': 'Mozllia 4.0 (compatible; MSIE 5.5, Windows NT'}
    titleList = []
    for i in range(depth):
        try:
            i += 1
            url = start_url+str(i)
            # print(url)
            html = getHTMLText(url, headers)
            parsePage(html, titleList)
        except:
            continue
main()













