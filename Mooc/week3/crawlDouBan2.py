#爬取豆瓣Top250电影的名字和评分
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(html, list):
    soup = BeautifulSoup(html, 'html.parser')
    for titles in soup.find(class_='article').find_all(class_='info'):
        for title in titles.find(class_='title'):
            # print(title)
            list.append(title)
        for rate in titles.find(class_='rating_num'):
            # print(rate)
            list.append(rate)
    return list

def printTitle(list):
    form = '{0:^4}{1:{3}^16}{2:^6}'
    print(form.format('排名', '影片名称', '评分', chr(12288)))
    count = 0
    for i in range(250):
        count += 1
        print(form.format(count, list[i*2], list[i*2+1], chr(12288)))

def main():
    depth = 10
    start_url = 'https://movie.douban.com/top250'
    titleList = []
    for i in range(depth):
        try:
            url = start_url+'?start='+str(25*i)
            # print(url)
            html = getHTMLText(url)
            parsePage(html,titleList)
        except:
            continue
    printTitle(titleList)
main()