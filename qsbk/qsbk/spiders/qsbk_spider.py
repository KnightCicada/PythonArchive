# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['xiaohua.zol.com.cn']
    start_urls = ['http://xiaohua.zol.com.cn/lengxiaohua/1.html']
    base_domin = 'http://xiaohua.zol.com.cn'
    def parse(self, response):
        contents = response.xpath('//ul[@class= "article-list"]/li')
        print(contents)
        for content in contents:
            #提取的数据是selector或者selectorList对象，获取其中的字符串，应该使用get,或则getall方法
            source = content.xpath('.//span[2]/text()').get()
            if source is None:
                source = '本站原创'
            text = content.xpath('.//div[@class="summary-text"]//text()').getall()
            text = "".join(text).replace('\r', '').replace('\t', '').replace('\n', '')
            # print(source)
            item = QsbkItem(source=source, text=text)
            yield item
        next_url = response.xpath('//div[@class="page-box"]//a[@class="page-next"]/@href').get()
        # print(next_url)
        if next_url == '/lengxiaohua/6.html':
            return
        else:
            yield scrapy.Request(self.base_domin+next_url, callback=self.parse)