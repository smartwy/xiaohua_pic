# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import os

class XiaohuaPicPipeline(object):
    def process_item(self, item, spider):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        req = urllib.request.Request(url=item['addr'], headers=headers)
        # Python3.3之后urllib与urllib2合并，只能使用urllib.request/response代替urllib2
        res = urllib.request.urlopen(req)
        file_name = os.path.join(r'E:\python_project_dir\xiaohua_pic\pic_dir', item['name'] + '.jpg')
        with open(file_name, 'wb') as fp:
            fp.write(res.read())
