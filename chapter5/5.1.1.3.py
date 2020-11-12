#爬取https://b.faloo.com/
import requests
from bs4 import BeautifulSoup
import chardet

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {'User-Agent': user_agent}
r = requests.get('https://b.faloo.com/f/652488.html', header)
# print(chardet.detect(r.content))
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
for i in soup.find_all(class_='ni_list'):
    h1 = i.find('h1')

    if h1!=None:
        for a in i.find_all('a'):
            href = a.get('href')
            title = a.get('title')
            print(href, title)
