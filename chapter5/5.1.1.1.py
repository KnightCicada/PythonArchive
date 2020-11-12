#自己爬取http://www.tadu.com/
import requests
import chardet
from bs4 import BeautifulSoup

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('http://www.tadu.com/book/catalogue/381247', headers=headers)
r.encoding = r.apparent_encoding
# print(chardet.detect(r.content))
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
for i in soup.find_all(class_='chapter clearfix'):
    h2 = i.find('h2')
    if h2!= None:
        for a in i.find_all('a'):
            href = a.get('href')
            title = a.get('title')
            target = a.get('target')
            print(href, title, target)
for i in soup.find_all(class_='chapter chapterVip clearfix'):
        h2 = i.find('h2')
        if h2!= None:
            for a in i.find_all('a'):
                href = a.get('href')
                target = a.get('target')
                print(href, target)

for i in soup.find_all(class_='boxCenter directory'):
    h1 = i.find('h1')
    if h1!= None:
        for a in i.find_all('a'):
            href = a.get('href')
            title = a.get('title')
            target = a.get('target')
            print(href, title, target)





