import requests
from lxml import html
etree = html.etree


proxies = {'http': 'http://127.0.0.1:7777', 'https': 'http://127.0.0.1:7777'}
s = requests.Session()
r = s.get("http://hss3uro2hsxfogfq.onion/index.php?q=drug+sale&session=EcGhxn5bNOdnIeidxi8dvjwtbC%2FmPcUpIok62vawj9Y%3D&numRows=20&hostLimit=20&template=0", proxies=proxies)
print(r.text)
url = html.xpath('//span[@style="color:black;"].text()').get()
print(url)
f = open("onion1.html", "wb")
f.write(r.content)
f.close()