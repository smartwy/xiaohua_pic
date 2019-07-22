# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.http import Request
from xiaohua_pic.items import XiaohuaPicItem

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua/']

    url_set = set()
    def parse(self, response):
        # 获取所有图片的a标签
        if response.url.startswith("http://www.xiaohuar.com/list-"):
            allPics = response.xpath('//div[@class="img"]/a')
            for pic in allPics:
                # 分别处理每个图片，取出名称及地址
                item = XiaohuaPicItem()
                name = pic.xpath('./img/@alt').extract()[0] # 提取获取名称
                addr = pic.xpath('./img/@src').extract()[0] # 提取获取img的src
                addr = 'http://www.xiaohuar.com' + addr
                item['name'] = name
                item['addr'] = addr
                yield item # 返回爬到的信息
        # 获取所有链接地址
        urls = response.xpath("//a/@href").extract()
        for url in urls:
            # 筛选href为http://www.xiaohuar.com/list-的分页url，
            if url.startswith("http://www.xiaohuar.com/list-"):
                if url in XiaohuaSpider.url_set:
                    pass
                else:
                    XiaohuaSpider.url_set.add(url)
                    yield self.make_requests_from_url(url) # 回调parse，将新url传入
                    # 回调函数默认为parse,也可以通过from scrapy.http import Request来指定回调函数
                    # from scrapy.http import Request
                    # Request(url,callback=self.parse)
            else:
                pass