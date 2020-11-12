#爬取猫眼电影最受期待榜单
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    headers = {'User-Agent':'Mozllia 4.0 (compatible; MSIE 5.5, Windows NT'}
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(html, list):
    soup = BeautifulSoup(html, 'html.parser')
    movieList = soup.find(class_='main').find_all(class_='board-item-main')
    # print(movieList)
    count = 0
    for item in movieList:
        try:
            count += 1
            item_name = item.find(class_='name').find('a').get('title')
            item_actors = item.find(class_='star').string
            item_date = item.find(class_='releasetime').string
            print(count,' | ',item_name,' | ',item_actors,' | ',item_date)
        except:
            continue

def main():
    depth = 5
    start_url = 'https://maoyan.com/board/6?offset='
    titleList = []
    for i in range(depth):
        try:
            url = start_url + str(10 * i)
            # print(url)
            html = getHTMLText(url)
            parsePage(html, titleList)
        except:
            continue


main()