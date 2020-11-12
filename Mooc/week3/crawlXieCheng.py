#爬取携程周边一日游信息
import requests
import xlwt
from bs4 import BeautifulSoup


def getHTMLText(url):
    headers = {'User-Agent':'Mozllia 4.0 (compatible; MSIE 5.5, Windows NT'}
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # print(r.text)
    return r.text
book=xlwt.Workbook(encoding='utf-8',style_compression=0)

sheet=book.add_sheet('携程一日游',cell_overwrite_ok=True)
sheet.write(0, 0, '项目名称')
sheet.write(0, 1, '特色')
sheet.write(0, 2, '价格')
sheet.write(0, 3, '评分')
sheet.write(0, 4, '点评数字')
sheet.write(0, 5, '月销量')

n=1


def parsePageAndSave(soup):
    tourList = soup.find(class_='product_wrap').find_all('a')
    # print(tourList)
    for item in tourList:
        title = item.find('h2').get('title')
        feature = item.find(class_='product_feature').get('title')
        price = item.find(class_='base_price').text
        score = item.find(class_='product_info').find(class_='blue').text.replace('\n', '').replace(' ', '')
        dp = item.find(class_='product_info').find(class_='product_db').text.replace('\n', '').replace(' ', '')
        sale = item.find(class_='product_info').find(class_='black').string
        global n

        sheet.write(n, 0, title)
        sheet.write(n, 1, feature)
        sheet.write(n, 2, price)
        sheet.write(n, 3, score)
        sheet.write(n, 4, dp)
        sheet.write(n, 5, sale)
        n = n + 1


def main():
    depth = 2
    start_url = 'https://huodong.ctrip.com/dailytour/search/?keyword=%E5%91%A8%E8%BE%B9&filters='
    for i in range(depth):
        try:
            i += 1
            url = start_url + 'p'+str(i)
            # print(url)
            html = getHTMLText(url)
            soup = BeautifulSoup(html, 'html.parser')
            parsePageAndSave(soup)
        except:
            continue

book.save(u'携程一日游.xlsx')
main()