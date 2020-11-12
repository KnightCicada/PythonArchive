import requests
import json
from lxml import html
etree = html.etree


def getHTMLText(url):
    proxies = {'http': 'http://127.0.0.1:7777', 'https': 'http://127.0.0.1:7777'}
    s = requests.Session()
    r = s.get(url, proxies=proxies)
    # print(r.text)
    html = etree.HTML(r.text)
    return html

def parsePage(html):
    url = html.xpath('//span[@style="color:black;"]/text()')
    title = html.xpath('//p/a[1]/text()')
    print(title)
    print(url)

    # for item in title:
    #     print(item)
    # f = open("onion1.html", "wb")
    # f.write(r.content)
    # f.close()


def main():
    #爬取深度
    depth = 20
    start_url = 'http://hss3uro2hsxfogfq.onion/index.php?q=drug+sale&session=ikddVrLSBZswt15MQXIJbbPzmX0X9slAgPKCIvds0W8%3D&hostLimit=20&start='
    for i in range(depth):
        try:
            url = start_url + str(20 * i)
            # print(url)
            html = getHTMLText(url)
            parsePage(html)
        except:
            continue

main()