import requests
#https://www.baidu.com/baidu?isource=infinity&iname=baidu&itype=web&tn=02003390_42_hao_pg&ie=utf-8&wd=hello
payload={'isource': 'infinity', 'iname': 'baidu', 'itype': 'web', 'tn': '02003390_42_hao_pg', 'ie': 'utf-8', 'wd': 'hello'}
r = requests.get('http://www.baidu.com/baidu', params=payload)
print(r.url)
