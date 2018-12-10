# -*- coding: utf-8 -*-
import scrapy
import os
from pic.items import PicItem

class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['haohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']

    def parse(self, response):
        # 获取所有图像的a标签
        allPics = response.xpath('//div[@class="img"]/a')
        for pic in allPics:
            # 分别处理每个图片取出名称及地址
            item = PicItem()
            name = pic.xpath('./img/@alt').extract()[0]
            addr = pic.xpath('./img/@src').extract()[0]
            addr = 'http://www.xiaohuar.com' + addr
            item['name'] = name
            item['addr'] = addr
            # 返回爬取数据
            yield item