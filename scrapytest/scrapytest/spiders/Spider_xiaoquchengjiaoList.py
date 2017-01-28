# -*- coding: utf-8 -*-
import scrapy
import time
import fileinput
#引入容器
from scrapytest.items import xiaoquChengjiaoListItem

class Spider_xiaoquchengjiaoList(scrapy.Spider):
    #设置name
    name = "Spider_xiaoquchengjiaoList"
    #设定域名
    allowed_domains = ["bj.lianjia.com"]
    #填写爬取地址
    start_urls = []
    for line in fileinput.input("xiaoquchengjiaoList.txt"):
        line = line.strip()[15:-2]
        start_urls.append(line)


    #编写爬取方法
    def parse(self, response):
        item = xiaoquChengjiaoListItem()

        xiaoquURL = response.xpath('//div[@class="list-more"]//button[@class="btn-range hide"]/@data-url').extract()
        if xiaoquURL:
            xiaoquURL=xiaoquURL[0].split('/')[-2]
            item['xiaoquURL'] = unicode('http://bj.lianjia.com/chengjiao/', "utf-8")+xiaoquURL[14:]
        else:
            item['xiaoquURL'] = unicode('无成交记录', "utf-8")           
   
        # 小区成交总数
        xiaoquzongchengjiaoshu = response.xpath('//span[@class="cnt"]/text()').extract()
        if xiaoquzongchengjiaoshu:
            xiaoquzongchengjiaoshu = xiaoquzongchengjiaoshu[0]
            item['xiaoquzongchengjiaoshu'] = xiaoquzongchengjiaoshu[1:-1]
        else:
            item['xiaoquzongchengjiaoshu'] = unicode('0', "utf-8")

        yield item

        time.sleep(10)