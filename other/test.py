import requests
#下载百度的LOGO
response=requests.get("https://www.baidu.com/img/bd_logo1.png")
with open("1.jpg","wb") as f:
    f.write(response.content)
    f.close()