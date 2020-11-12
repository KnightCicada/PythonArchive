import requests
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
cookies=dict(name='qiye', age='10')
r = requests.get('http://www.baidu.com', headers=headers, cookies=cookies)
print(r.text)
#遍历出所有的cookie字段的值


#for cookie in r.cookies.keys():
    #print(cookie+':'+r.cookies.get(cookie))
