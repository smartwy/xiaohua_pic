# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import os
import pymysql.cursors
class XiaohuaPicPipeline(object):
    # 图片保存到文件目录下
    # def process_item(self, item, spider):
    #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    #     req = urllib.request.Request(url=item['addr'], headers=headers, method='GET')
    #     # Python3.3之后urllib与urllib2合并，只能使用urllib.request/response代替urllib2
    #     res = urllib.request.urlopen(req)
    #     print(req)
    #     dir_path = 'E:\\python_project_dir\\xiaohua_pic\\pic_dir'
    #     # if not os.path.exists(dir_path):
    #     #     os.mkdir(dir_path)
    #     file_name = os.path.join(dir_path, item['name'] + '.jpg')
    #     with open(file_name, 'wb') as fp:
    #         fp.write(res.read())

    # 保存到mysql数据库里，name和addr
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(
            host='192.168.10.241',  # 数据库地址
            port=3306,                # 数据库端口
            db='scrapyMysql',       # 数据库名
            user='root',             # 数据库用户名
            passwd='12345678',       # 数据库密码
            charset='utf8',          # 编码方式
            use_unicode=True)
        # 游标，通过游标执行增删查改
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        self.cursor.execute('''insert into pic_link(name, addr) value (%s, %s)''',(item['name'],item['addr'],))
        # print(item['name'],item['addr'])
        self.connect.commit() # 提交
        return item  # 必须实现返回
'''
import pymongo
class InputmongodbPipeline(object):

    def __init__(self):
        # 建立MongoDB数据库连接
        client = pymongo.MongoClient('127.0.0.1', 27017) # MongoClient('mongodb://localhost:27017/')
        
        # # since MongoDB 3.0， SCRAM-SHA-1
        # from pymongo import MongoClient
        # # keyword argument
        # client = MongoClient('example.com',
        #                       username='user',
        #                       password='password',
        #                       authSource='the_database',
        #                       authMechanism='SCRAM-SHA-1') # SCRAM-SHA-1加密
        # # MongoDB URI
        # uri = "mongodb://user:password@example.com/the_database?authMechanism=SCRAM-SHA-1"
        #  client = MongoClient(uri)
        
        # 连接所需数据库,Database_name为数据库名
        db = client['Database_name']
        # 连接所用集合，也就是我们通常所说的表，table_name为表名
        self.post = db['table_name']

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.post.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写
'''
