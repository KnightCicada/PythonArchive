import requests
from fake_useragent import UserAgent

proxies = {
    'http': 'socks5h://127.0.0.1:7891',
    'https': 'socks5h://127.0.0.1:7891'
}

ua = UserAgent()
headers = {'User-Agent': ua.random}
res = requests.get("http://www.baidu.com", headers=headers, proxies=proxies)
print(res.text)
