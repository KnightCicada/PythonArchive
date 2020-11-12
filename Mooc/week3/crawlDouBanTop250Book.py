#爬取豆瓣Top250书籍
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(html, list):
    soup = BeautifulSoup(html, 'html.parser')
    BookList = soup.find(class_='indent').find_all(class_='item')
    # print(BookList)
    for item in BookList:
        item_name = item.find(class_='pl2').find('a').get('title')
        item_score = item.find(class_='rating_nums').string
        item_info = item.find('p').string
        item_intro = item.find(class_='inq').string
        list.append([item_name, item_score, item_intro, item_info])
    print(list)


def printTitle(list):
    form = '{:^4}{:^16}{:^6}{:^18}{:^40}'
    print(form.format('排名', '图书名称', '评分', '介绍', '出版信息', chr(12288)))
    count = 0
    for g in list:
        count += 1
        print(form.format(count, g[0], g[1], g[2], g[3], chr(12288)))

def main():
    depth = 3
    start_url = 'https://book.douban.com/top250'
    titleList = []
    for i in range(depth):
        try:
            url = start_url + '?start=' + str(25 * i)
            print(url)
            html = getHTMLText(url)
            # parsePage(html, titleList)
        except:
            continue
    # printTitle(titleList)

main()