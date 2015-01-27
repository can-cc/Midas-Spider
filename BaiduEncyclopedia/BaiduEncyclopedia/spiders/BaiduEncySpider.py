import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
import re
import json
from BaiduEncyclopedia.items import BaiduencyclopediaItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

class BaiduEncySpider(CrawlSpider):
    name = 'baiduEncy'
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'http://baike.baidu.com/wenhua',
        'http://baike.baidu.com/dili',
        'http://baike.baidu.com/shenghuo',
    ]
    rules = [
        Rule(sle(allow=("/view/\d+.htm$")), callback='parse1'),
        Rule(sle(allow=("/view/\d+$/\d+.htm$")), callback='parse1'),
        Rule(sle(allow=("/\w+$", )), follow=True),
    ]

    def parse1(self, response):
        item = BaiduencyclopediaItem()
        item['id'] = response.url.split('/')[-1].split('.')[0]
        item['name'] = response.xpath('//span[@class="lemmaTitleH1"]/text()').extract()
        summary = response.xpath('//div[@class="card-summary-content"]').extract()
        item['summaryText'] = re.compile('<[^>]*>').sub('', summary[0])
        rawAttrs = response.css('.biItemInner')
        attr = {}
        for rAttr in rawAttrs:
            attrName = ''.join(rAttr.css('.biTitle ::text').extract())
            attrValue = ''.join(rAttr.css('.biContent ::text').extract())
            attr[attrName] = attrValue
        item['attr'] = attr
        rawLables = response.xpath('//sapn[@class="taglist"]/text()')
        lable = []
        for rLable in rawLables:
            lab = rLable.extract()
            lable.append(lab)
        item['lable'] = lable
        return [item, ]
        
    def _process_request(self, request):
        info('process ' + str(request))
        return request
        
