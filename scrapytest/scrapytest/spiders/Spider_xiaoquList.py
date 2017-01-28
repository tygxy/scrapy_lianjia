# -*- coding: utf-8 -*-
import scrapy
import time
#引入容器
from scrapytest.items import xiaoquListItem

class Spider_xiaoquList(scrapy.Spider):
    #设置name
    name = "Spider_xiaoquList"
    #设定域名
    allowed_domains = ["bj.lianjia.com"]
    #填写爬取地址
    start_urls = []
    basic_url = 'http://bj.lianjia.com/xiaoqu/dongcheng/pg'
    for i in range(1,100):
        start_urls.append(basic_url+str(i))
    
    #编写爬取方法
    def parse(self, response):
        item = xiaoquListItem()
        #小区list
        for box in response.xpath('//li[@class="clear xiaoquListItem"]//div[@class="title"]'):
            item['xiaoquURL'] = box.xpath('.//a[@target="_blank"]/@href').extract()[0].strip()
            yield item

        time.sleep(5)