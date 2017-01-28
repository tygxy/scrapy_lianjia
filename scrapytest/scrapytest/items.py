# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class xiaoquDetialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    xiaoqumincheng = scrapy.Field()
    junjia = scrapy.Field()
    xingzhengqu = scrapy.Field()
    daqu = scrapy.Field()
    xiangxiweizhi = scrapy.Field()
    jianzhuniandai = scrapy.Field()
    jianzhuleixing = scrapy.Field()
    wuyefeiyong = scrapy.Field()
    wuyegongsi = scrapy.Field()
    kaifashang = scrapy.Field()
    loudongzongshu = scrapy.Field()
    fangwuzongshu = scrapy.Field()


class xiaoquListItem(scrapy.Item):
	xiaoquURL = scrapy.Field()
	

class xiaoquChengjiaoListItem(scrapy.Item):
    xiaoquURL = scrapy.Field()
    xiaoquzongchengjiaoshu = scrapy.Field()



class xiaoquChengjiaoItem(scrapy.Item):
    xiaoquzongchengjiaoshu = scrapy.Field()
    fangchanmincheng = scrapy.Field()
    chengjiaoriqi = scrapy.Field()
    chengjiaozongjia = scrapy.Field()
    chengjiaodanjia = scrapy.Field()
    mianji = scrapy.Field()
    chaoxiang = scrapy.Field()
    zhuangxiu = scrapy.Field()
    youwudianti = scrapy.Field()
    louceng = scrapy.Field()
    niandai = scrapy.Field()
    jianzhuleixing = scrapy.Field()

