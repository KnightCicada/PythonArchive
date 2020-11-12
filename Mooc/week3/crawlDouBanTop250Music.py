#爬取豆瓣Top250音乐
#音乐名字存在副标题和空格换行
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(html, list):
    soup = BeautifulSoup(html, 'html.parser')
    MusicList = soup.find(class_='indent').find_all(class_='item')
    # print(BookList)
    for item in MusicList:
        item_name = item.find(class_='nbg').get('title')
        item_score = item.find(class_='rating_nums').string
        item_info = item.find('p').string
        print(item_name+' | '+item_score+' | '+item_info)

def printTitle(list):
    form = '{0:^4}{1:{3}^16}{2:^6}{:30}'
    print(form.format('排名', '影片名称', '评分', '介绍', chr(12288)))
    count = 0
    for i in range(250):
        count += 1
        print(form.format(count, list[i*2], list[i*2+1], chr(12288)))

def main():
    depth = 2
    start_url = 'https://music.douban.com/top250'
    titleList = []
    for i in range(depth):
        try:
            url = start_url + '?start=' + str(25 * i)
            html = getHTMLText(url)
            parsePage(html,titleList)
        except:
            continue
    # printTitle(titleList)

main()