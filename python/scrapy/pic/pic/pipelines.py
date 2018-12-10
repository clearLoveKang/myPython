# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from urllib import request
import os
import requests

class PicPipeline(object):
    def process_item(self, item, spider):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }
        # req = request.Request(url=item['addr'], headers=headers)
        # res = request.urlopen(req)
        file_name = os.path.join(r'/Users/yimihaodi/md/python/python/scrapy/down_pic', item['name']+'.jpg')
        # with open(file_name, 'wb') as f:
        #     f.write(res.read())
        # with open('xiaohua5.txt','a') as f:
        #     f.write(item['name']+'--'+item['addr'] + '\n')
        rsp = requests.get(url=item['addr'], headers=headers)
        with open(file_name, 'wb') as file:
            file.write(rsp.content)

