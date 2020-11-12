#爬取豆瓣Top250电影的名字
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(html, list):
    soup = BeautifulSoup(html, 'html.parser')
    movieList = soup.find(id='nowplaying').find_all(class_='list-item')
    # print(movieList)
    for i in movieList.find('li'):
        print(i)
        # for item in i:
    #         item_name = item.get('data-title')
    #         item_score = item.get('data-score')
    #         item_release = item.get('data-release')
    #         item_duration = item.get('data-data-duration')
    #         item_director = item.get('data-director')
    #         item_actors = item.get('data-actors')
    # print(item)

    # print(movieList)
        

def printTitle(list):
    form = '{0:^4}{1:{3}^16}{2:^6}{:30}'
    print(form.format('排名', '影片名称', '评分', '介绍', chr(12288)))
    count = 0
    for i in range(250):
        count += 1
        print(form.format(count, list[i*2], list[i*2+1], chr(12288)))

def main():
    depth = 2
    url = 'https://movie.douban.com/cinema/nowplaying/xian/'
    titleList = []

    try:
        html = getHTMLText(url)
        parsePage(html,titleList)
    except:
        print('')
    # printTitle(titleList)

main()