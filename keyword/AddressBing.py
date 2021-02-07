import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent


def crawlProcess(page, startUrl, keyword, addressSet, browser):
    # browser = webdriver.Firefox()
    for j in range(page):
        try:
            url = startUrl + keyword + '&first=' + str(15 * j)
            print('爬取  ' + url)
            browser.get(url)
            # js = "var q=document.documentElement.scrollTop=10000"
            # browser.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至最底端。
            # time.sleep(1)
            body = browser.page_source
            getAddress(body, addressSet)
            # 已隐藏相似结果，停止爬取
            if judge(body) == True:
                break
            else:
                continue
        except:
            continue


# 判断是否存在相似结果
def judge(body):
    text = BeautifulSoup(body, 'html.parser').find(class_='sb_count').text
    pattern = re.compile(r'[\d,]*')
    first = re.search(pattern, text).group(0).replace(' ', '').replace(',', '')
    pattern = re.compile('(?<=\\().*(?=\\))')
    tmp = re.search(pattern, text).group(0)

    patternNum = re.compile(r'[\d,]+')
    target = re.search(patternNum, tmp).group(0).replace(',', '')
    return first == target


def getAddress(body, addressSet):
    list = BeautifulSoup(body, 'html.parser').find(id='b_results').find_all(class_='b_attribution')
    # print(list)
    for i in list:
        # href = regexOnion(i.find('cite').text)
        # href = regexTor2web(i.find('cite').text)
        href = regexHiddenService(i.find('cite').text)
        # href = regexTorstorm(i.find('cite').text)
        href = str(href).replace("['", '').replace("']", '')
        addressSet.add(href)


# 正则提取洋葱地址
def regexOnion(href):
    pattern = re.compile(r'https*://\w+\.onion')
    res = re.findall(pattern, href)
    # print(res)
    return res


def regexTor2web(href):
    pattern = re.compile(r'https*://\w+\.tor2web')
    res = re.findall(pattern, href)
    res = str(res).replace('tor2web', 'onion')
    # print(res)
    return res


def regexHiddenService(href):
    pattern = re.compile(r'https*://\w+\.hiddenservice')
    res = re.findall(pattern, href)
    res = str(res).replace('hiddenservice', 'onion')
    # print(res)
    return res


def regexTorstorm(href):
    pattern = re.compile(r'https*://\w+\.torstorm')
    res = re.findall(pattern, href)
    res = str(res).replace('torstorm', 'onion')
    # print(res)
    return res


def WriteFile(addressSet):
    for item in addressSet:
        f = open("addressB.txt", 'a')
        f.write(item + '\n')
        f.close()
        print(item)


if __name__ == '__main__':
    keyWordsList = (
        # 'site:onion.sh',
        # 'site:onion.to',
        # 'site:onion.guide',
        # 'site:onion.rip',
        # 'site:onion.city',
        # 'site:onion.top',
        # 'site:onion.cab',
        # 'site:onion.rent',
        # 'site:onion.lt',
        # 'site:onion.lu',
        # 'site:onion.plus',
        # 'site:onion.cafe',

        # 'site:tor2web.io',
        # 'site:tor2web.fi',
        # 'site:tor2web.ch',

        'site:hiddenservice.net',

        # 'site:torstorm.org'
    )

    addressSet = set()

    ua = UserAgent()
    # headers = {'User-Agent': ua.random}
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent=%s' % ua.random)
    options.add_argument('disable-infobars')
    options.add_argument("--no-sandbox")
    options.add_argument("--lang=zh-CN")
    options.add_argument("--proxy-server=http://127.0.0.1:7890")

    # print(options.arguments)

    browser = webdriver.Chrome(options=options)

    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
    })

    # https: // www.bing.com / search?hl = en & q = site % 3 aonion.sh & start = 30 & first = 15 & FORM = PERE
    for keyword in keyWordsList:
        start_url = 'https://www.bing.com/search?hl=en&q='
        url = start_url + keyword
        try:
            # 获取总结果数
            browser.get(url)
            # js = "var q=document.documentElement.scrollTop=10000"
            # browser.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至最底端。
            # time.sleep(1)
            body = browser.page_source
            # pageInfo = BeautifulSoup(body, 'html.parser').find(class_='sb_count').text
            # # print(pageInfo)
            # pattern = re.compile(r'[\d,]*')
            # res = re.search(pattern, pageInfo).group(0).replace(' ', '')
            # print(res)
            # totalAmount = res.replace(',', '')
            # page = math.ceil(int(totalAmount, 15) / 15)
            # print('结果共计 ' + str(page) + ' 页')
        except:
            continue
        crawlProcess(2, start_url, keyword, addressSet, browser)
        time.sleep(3)

    WriteFile(addressSet)
    print('得到 ' + str(len(addressSet)) + ' 个洋葱地址')
    browser.quit()
    browser.close()
