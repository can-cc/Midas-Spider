# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from collections import OrderedDict
from scrapy import signals
from pymongo import MongoClient


class BaiduencyclopediaPipeline(object):
    def __init__(self):
        self.file = codecs.open('BaiduEncy.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class BaiduEncyMongoPipeline(object):
    def __init__(self):
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        self.db = client['KnowledgeBase']
        self.collection = self.db['BaiduEncy']
        self.BaiduEncys = self.db.BaiduEncys

    def process_item(self, item, spider):
        BaiduEncyId = self.db.BaiduEncys.insert(OrderedDict(item))
        print 'hi'
        print self.db.BaiduEncys.count()
        print BaiduEncyId

    def spider_closed(self, spider):
        pass
