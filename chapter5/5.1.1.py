import requests
import chardet
import re
import csv
import json
from bs4 import BeautifulSoup

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com', headers=headers)
#print(r.text)
#查看网页编码格式
# print(chardet.detect(r.content))

soup = BeautifulSoup(r.text, 'html.parser')
rows = []

for mulu in soup.find_all(class_='mulu'):
    h2 = mulu.find('h2')
    if h2!=None:
        h2_title = h2.string
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            # print(href, box_title)

            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            if match!=None:
                date = match.group(1)
                real_title = match.group(2)
                content = (h2_title, real_title, href, date)
                # print(content)
                rows.append(content)

headers = ['title', 'real_title', 'href', 'date']
with open('qiye.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)



