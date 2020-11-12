import requests
r = requests.get('http://bilibili.com')
print(r.url)
print(r.status_code)
print(r.history)

