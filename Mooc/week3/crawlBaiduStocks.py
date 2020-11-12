import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append((re.findall(r"[s][hz]\d{6}", href)[0])[2:])
        except:
            continue
    return ""


def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-quote-wrap'})

            name = stockInfo.find_all('p', attrs={'class': "title"})[0]
            infoDict.update({'股票名称': name.text.split()[1]})

            for ch in infoDict['股票名称']:
                if u'\u4e00' <= ch <= u'\u9fff':
                    contentList = stockInfo.find_all('td')
                    for i in range(len(contentList)):
                        key = contentList[i].text.split(':')[0]
                        value = contentList[i].text.split(':')[1]
                        infoDict[key] = value

                    with open(fpath, 'a', encoding='GB2312') as f:
                        f.write(str(infoDict) + '\n')
                        f.close()
                    break
        except:
            traceback.print_exc()
            continue

    return ""


def main():
    stock_list_url = "http://quote.eastmoney.com/stock_list.html"
    stock_info_url = "https://www.laohu8.com/hq/s/"
    output_file = 'e:/stockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist[:100], stock_info_url, output_file)


if __name__ == '__main__':
    main()