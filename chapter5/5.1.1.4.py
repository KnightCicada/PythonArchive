#https://www.17k.com/
import requests
from bs4 import BeautifulSoup
import chardet

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {'User-Agent':user_agent}
r = requests.get('https://www.17k.com/list/493239.html', header)
print(chardet.detect(r.content))
r.encoding = r.apparent_encoding
#print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
for i in soup.find_all(class_='Main List'):
    h1 = i.find('h1')
    if h1!=None:
        for a in i.find_all('Volume'):
            # print(a)
            target = a.get('target')
            href = a.get('href')
            title = a.get('title')
            print(target, href, title)