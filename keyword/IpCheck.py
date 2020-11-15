import csv
import socket
import urllib.request


def IPpool():
    socket.setdefaulttimeout(2)
    reader = csv.reader(open('ips.csv'))
    IPpool = []
    for row in reader:
        proxy = row[0] + ':' + row[1]
        proxy_handler = urllib.request.ProxyHandler({"http": proxy})
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)
        try:
            html = urllib.request.urlopen('https://www.bilibili.com/')
            IPpool.append([row[0], row[1]])
        except:
            continue
    print(IPpool)


if __name__ == '__main__':
    IPpool()
