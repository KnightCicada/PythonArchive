import re
import requests


def getHTMLText(url, header):
    try:
        r = requests.get(url, headers=header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(list, html):
    try:
        plt = re.findall(r'"view_price":"[\d\.]*"', html)
        print(plt)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            list.append([price, title])

    except:
        print("爬取失败")


def printGoodsList(list):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in list:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = "书包"
    depth = 1
    start_url = "https://s.taobao.com/search?q=" + goods
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Cookie":'thw=cn; enc=KyuATCtpEE%2BuwpR1iPg9xPP6c3ZrBykd3bXlDosLqINASUSC0WcMWyb5kI8bi%2FIGvZzMzPD%2FCi%2Fu0ZohzWc8NA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; t=945b29317afe445e55694f5b81471d55; cookie2=70b4c24fd69d7e3b20f724c67a18b6c3; _tb_token_=7eab8b35b81d5; alitrackid=www.taobao.com; swfstore=246985; cna=6SSNFYhZpDgCAXxz3pTnYsgA; v=0; unb=2151831255; uc3=lg2=Vq8l%2BKCLz3%2F65A%3D%3D&id2=UUkLViKikAeaFw%3D%3D&vt3=F8dByuDjO77Xcbmksmc%3D&nk2=BJfi8CoopVS3; csg=3eb3ce52; lgc=galaxyysr; cookie17=UUkLViKikAeaFw%3D%3D; dnk=galaxyysr; skt=99068a696faa9859; existShop=MTU3MTE5ODc1Mw%3D%3D; uc4=id4=0%40U2uHfr0VKXId7osIzvsi38a8BmNb&nk4=0%40BpMrtlSRAw%2BtRrjEJ5HsgNIsedc%3D; tracknick=galaxyysr; _cc_=UtASsssmfA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=r57; _nk_=galaxyysr; cookie1=ACu%2Ft9mPGIvVR6hLtRy52IUY0GwtZvsoTh7DvoqV7RA%3D; mt=ci=3_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; lastalitrackid=www.taobao.com; JSESSIONID=A6C0188B8E7AEF598521AE04A0EFFD3C; whl=-1%260%260%261571199596363; l=dBQ2XRw4qjZBi9L9BOCwhurza77thIRAguPzaNbMi_5BW68_KaQOkguKpFJ6cjWftVTB4tm2-g29-etkiG4pJA--g3fyDxDc.; isg=BMzMmJcc_bm4COnkWNCarIktnSo-rW_bnBhY5yaNvncasWy7ThRRPQ0DUfks-agH; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=V32FPkk%2FgihF%2FS5nr3O5&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTbnKISUxFOvA%3D%3D&tag=8&lng=zh_CN'

    }
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44 * i)
            html = getHTMLText(url, header)
            # print(html)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()