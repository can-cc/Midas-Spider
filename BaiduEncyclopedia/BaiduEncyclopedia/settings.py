# -*- coding: utf-8 -*-

# Scrapy settings for BaiduEncyclopedia project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import os
from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)
BOT_NAME = 'BaiduEncyclopedia'

SPIDER_MODULES = ['BaiduEncyclopedia.spiders']
NEWSPIDER_MODULE = 'BaiduEncyclopedia.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BaiduEncyclopedia (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    #'misc.middleware.CustomHttpProxyMiddleware': 400,
    'misc.middleware.CustomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = {
    #'doubanbook.pipelines.JsonWithEncodingPipeline': 300,
    #'BaiduEncyclopedia.pipelines.BaiduencyclopediaPipeline': 301,
    'BaiduEncyclopedia.pipelines.BaiduEncyMongoPipeline': 301,
}

DUPEFILTER_CLASS = "BaiduEncyclopedia.MyBloomFilter.BLOOMDupeFilter"

LOG_LEVEL = 'INFO'
