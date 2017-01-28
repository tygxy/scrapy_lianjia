# -*- coding: utf-8 -*-
import scrapy
import fileinput
import time 
#引入容器
from scrapytest.items import xiaoquDetialItem

class Spider_xiaoquDetial(scrapy.Spider):
    #设置name
    name = "Spider_xiaoquDetial"
    #设定域名
    allowed_domains = ["bj.lianjia.com"]
    #填写爬取地址
    start_urls = []
    for line in fileinput.input("XiaoquList.txt"):
        line = line.strip()[15:-2]
        start_urls.append(line.strip())



    #编写爬取方法
    def parse(self, response):

        #实例一个容器保存爬取的信息
        item = xiaoquDetialItem()
        # 详细位置
        box1 = response.xpath('//div[@class="detailHeader fl"]')
        xiangxiweizhi = box1.xpath('.//div[@class="detailDesc"]/text()').extract()
        if xiangxiweizhi:
            item['xiangxiweizhi'] = xiangxiweizhi[0].strip()
        else:
            item['xiangxiweizhi'] = unicode('暂无信息', "utf-8")

        # 行政区,大区,小区名称
        box2 = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]')
        xingzhengqu = box2.xpath('.//a[3]/text()').extract()
        if xingzhengqu:
            item['xingzhengqu'] = xingzhengqu[0].strip()
        else:
            item['xingzhengqu'] = unicode('暂无信息', "utf-8")

        daqu = box2.xpath('.//a[4]/text()').extract()
        if daqu:
            item['daqu'] = daqu[0].strip()
        else:
            item['daqu'] = unicode('暂无信息', "utf-8")

        xiaoqumincheng = box2.xpath('.//a[5]/text()').extract()
        if xiaoqumincheng:
            item['xiaoqumincheng'] = xiaoqumincheng[0].strip()
        else:
            item['xiaoqumincheng'] = unicode('暂无信息', "utf-8")

        # 均价
        box3 = response.xpath('//div[@class="xiaoquDescribe fr"]')
        junjia = box3.xpath('.//span[@class="xiaoquUnitPrice"]/text()').extract()
        if junjia:
            item['junjia'] = junjia[0]
        else:
            item['junjia'] = unicode('暂无均价信息', "utf-8")

        # 建筑年代,建筑类型,物业费用,物业公司,开发商,楼栋总数,房屋总数
        box4 = response.xpath('//div[@class="xiaoquInfo"]')

        jianzhuniandai = box4.xpath('.//div[1]//span[2]/text()').extract()
        if jianzhuniandai:
            item['jianzhuniandai'] = jianzhuniandai[0]
        else:
            item['jianzhuniandai'] = unicode('暂无信息', "utf-8") 


        jianzhuleixing =  box4.xpath('.//div[2]//span[2]/text()').extract()
        if jianzhuleixing:
            item['jianzhuleixing'] = jianzhuleixing[0]
        else:
            item['jianzhuleixing'] = unicode('暂无信息', "utf-8") 
        
        wuyefeiyong = box4.xpath('.//div[3]//span[2]/text()').extract()
        if wuyefeiyong:
            item['wuyefeiyong'] = wuyefeiyong[0]
        else:
            item['wuyefeiyong'] = unicode('暂无信息', "utf-8")

        wuyegongsi =  box4.xpath('.//div[4]//span[2]/text()').extract()
        if wuyegongsi:
            item['wuyegongsi'] = wuyegongsi[0]
        else:
            item['wuyegongsi'] = unicode('暂无信息', "utf-8")
 
        kaifashang = box4.xpath('.//div[5]//span[2]/text()').extract()
        if kaifashang:
            item['kaifashang'] = kaifashang[0] 
        else:
            item['kaifashang'] = unicode('暂无信息', "utf-8") 

        loudongzongshu =  box4.xpath('.//div[6]//span[2]/text()').extract()
        if loudongzongshu :
            item['loudongzongshu'] = loudongzongshu[0]
        else:
            item['loudongzongshu'] = unicode('暂无信息', "utf-8")

        fangwuzongshu = box4.xpath('.//div[7]//span[2]/text()').extract()
        if fangwuzongshu:
           item['fangwuzongshu'] = fangwuzongshu[0]
        else:
           item['fangwuzongshu'] = unicode('暂无信息', "utf-8")                 

        yield item

        time.sleep(3)


