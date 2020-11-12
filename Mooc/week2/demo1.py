import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r =requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find(class_='hidden_zhpm'):
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist,num):
    #{1:{3}^10}表示使用chr(12288)进行填充
    #1表示format函数的第二个变量，学校
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    #chr(12288)表示中文不够时，使用中文空格进行填充，而不使用西文空格
    print(tplt.format("排名", "学校", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
        # print("Suc" + str(num))



def main():
   uinfo = []
   url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
   html = getHTMLText(url)
   fillUnivList(uinfo, html)
   printUnivList(uinfo, 25)
main()