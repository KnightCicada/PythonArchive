#爬取豆瓣Top250电影
#219，250 由于没有introduction故发生问题

import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(html, list):
    soup = BeautifulSoup(html, 'html.parser')
    movieList = soup.find(class_='grid_view').find_all('li')
    count = 0
    for item in movieList:
        try:
            count += 1

            item_intr = item.find(class_='inq').string
            # print(count,item_name+'  |  '+item_img+'  |  '+item_score+'  |  '+item_intr)

            print(item_intr)
        except:
            continue

def printTitle(list):
    form = '{0:^4}{1:{3}^16}{2:^6}{:30}'
    print(form.format('排名', '影片名称', '评分', '介绍', chr(12288)))
    count = 0
    for i in range(250):
        count += 1
        print(form.format(count, list[i*2], list[i*2+1], chr(12288)))

def main():
    depth = 10
    url = 'https://movie.douban.com/top250?start=200'
    titleList = []



    html = getHTMLText(url)
    parsePage(html,titleList)

    # printTitle(titleList)

main()