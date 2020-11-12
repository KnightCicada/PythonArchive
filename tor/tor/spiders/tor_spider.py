# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TorSpiderSpider(CrawlSpider):
    name = 'tor_spider'
    allowed_domains = ['hss3uro2hsxfogfq.onion']
    start_urls = ['http://hss3uro2hsxfogfq.onion/index.php?q=drug+sale&session=iux%2BRMzLSpS26g1D3C7H4vUFdq9SDdny8N6KXpt5%2Bx8%3D&hostLimit=20&start=0&numRows=20&template=0']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
