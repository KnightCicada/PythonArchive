import requests
from bs4 import BeautifulSoup


url = 'https://huodong.ctrip.com/dailytour/search/?keyword=%E5%91%A8%E8%BE%B9'
headers = {'User-Agent':'Mozllia 4.0 (compatible; MSIE 5.5, Windows NT'}
r = requests.get(url, headers=headers, timeout=30)
r.raise_for_status()
r.encoding = r.apparent_encoding
# print(r.text)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
print(soup.find(class_='product_wrap'))




