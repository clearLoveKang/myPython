import scrapy

from onescrapy.items import OnescrapyItem

class DomzSpider(scrapy.Spider):
    name = 'domz'
    allowed_domains = ['domz.org']
    start_urls = [
        "http://www.baidu.com",
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = OnescrapyItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item