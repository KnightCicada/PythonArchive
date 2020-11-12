import urllib.request
from lxml import html
etree = html.etree
import requests

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('https://visualhunt.com/bedroom-sets'
                 , headers=headers)
html = etree.HTML(r.text)
# print(etree.tostring(html))

img_urls = html.xpath('.//div[@class="vh2-container"]//img/@src')
i = 0
for img_url in img_urls:
    print(img_url)
    urllib.request.urlretrieve(img_url, 'E:\Img\Arch\img' + str(i) + '.jpg')
    i += 1
