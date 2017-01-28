# -*- coding: utf-8 -*-
import scrapy
import fileinput
import time 
import json  
#引入容器
from scrapytest.items import xiaoquChengjiaoItem


class Spider_xiaoquchengjiao(scrapy.Spider):
    #设置name
    name = "Spider_xiaoquchengjiao"
    #设定域名
    allowed_domains = ["bj.lianjia.com"]

    # 读取xiaoquchengjiaoList中的数据
    dataFile = open("xiaoquchengjiaoList.json")
    data_json_list = []
    for line in dataFile:
        data_json_list.append(line)

    # 构造出start_urls
    start_urls=[]
    numList = len(data_json_list)
    for i in range(0,numList):
        data = json.loads(data_json_list[i])
        # url = data["xiaoquURL"].encode("utf-8")
        # start_urls.append(url)
        numPage = int(data["xiaoquzongchengjiaoshu"].encode("utf-8"))/30+1
        base_url = data["xiaoquURL"].encode("utf-8")
        for j in range(1,numPage+1):
            url = base_url[:32]+"pg"+str(j)+base_url[32:]
            start_urls.append(url)

    # start_urls = ["http://bj.lianjia.com/chengjiao/pg1c1111044977784/"]

    #编写爬取方法
    def parse(self, response):

        #实例一个容器保存爬取的信息
        item = xiaoquChengjiaoItem()
        
        # 小区成交总数
        xiaoquzongchengjiaoshu = response.xpath('//span[@class="cnt"]/text()').extract()
        if xiaoquzongchengjiaoshu:
            xiaoquzongchengjiaoshu = xiaoquzongchengjiaoshu[0]
            item['xiaoquzongchengjiaoshu'] = xiaoquzongchengjiaoshu[1:-1]
        else:
            item['xiaoquzongchengjiaoshu'] = unicode('0', "utf-8")


        for box in response.xpath('//ul[@class="listContent"]/li/div[@class="info"]'):

            # 房产名称和面积
            tmp1 = box.xpath('.//div[@class="title"]/a/text()').extract()
            if tmp1:
                tmp1 = tmp1[0].encode("utf-8").split()
                item['fangchanmincheng'] = unicode(tmp1[0],"utf-8")
                tmp1 = tmp1[1]+" "+tmp1[2]
                item['mianji'] = unicode(tmp1,"utf-8")
            else:
                tmp12 = box.xpath('.//div[@class="title"]/text()').extract()              
                if tmp12: 
                    tmp12 = tmp12[0].encode("utf-8").split()           
                    item['fangchanmincheng'] = unicode(tmp12[0],"utf-8")
                    tmp12 = tmp12[1]+" "+tmp12[2]
                    item['mianji'] = unicode(tmp12,"utf-8")
                else:
                    item['fangchanmincheng'] = unicode('暂无信息', "utf-8")
                    item['mianji'] = unicode('暂无信息', "utf-8")
             
            # 朝向/装修/电梯
            tmp2 = box.xpath('.//div[@class="address"]/div/text()').extract()
            if tmp2:
                tmp2 = tmp2[0].encode("utf-8").split("|")
                item['chaoxiang'] = unicode(tmp2[0],"utf-8")
                item['zhuangxiu'] = unicode(tmp2[1],"utf-8")
                if (len(tmp2)==2):
                    item['youwudianti'] = unicode('无电梯', "utf-8")
                if (len(tmp2)==3):
                    item['youwudianti'] = unicode(tmp2[2], "utf-8")
            else:
                item['chaoxiang'] = ('暂无信息', "utf-8")
                item['zhuangxiu'] = ('暂无信息', "utf-8")   
                item['youwudianti'] = ('暂无信息', "utf-8")      
            
            # 成交总价
            chengjiaozongjia = box.xpath('.//div[@class="address"]/div[@class="totalPrice"]/span/text()').extract()
            if chengjiaozongjia:
                item['chengjiaozongjia'] = chengjiaozongjia[0]+unicode('万', "utf-8")
            else:
                item['chengjiaozongjia'] = unicode('暂无', "utf-8")

            # 成交日期
            chengjiaoriqi = box.xpath('.//div[@class="address"]/div[@class="dealDate"]/text()').extract()
            if chengjiaoriqi:
                item['chengjiaoriqi'] = chengjiaoriqi[0]
            else:
                item['chengjiaoriqi'] = unicode('暂无信息', "utf-8")

            # 楼层/年代/建筑类型/成交单价
            divFlood = box.xpath('.//div[@class="flood"]')
            tmp3= divFlood.xpath('.//div[@class="positionInfo"]/text()').extract()
            if tmp3:
                tmp3 = tmp3[0].encode("utf-8").split()
                item['louceng'] = unicode(tmp3[0],"utf-8")
                if (len(tmp3)==1):
                    item['niandai'] = unicode('暂无信息', "utf-8")   
                    item['jianzhuleixing'] = unicode('暂无信息', "utf-8")   
                else:
                    tmp31 = tmp3[1]
                    item['niandai'] = unicode(tmp31[0:10],"utf-8")
                    item['jianzhuleixing'] = unicode(tmp31[10:],"utf-8")
            else:
                item['louceng'] = unicode('暂无信息', "utf-8")
                item['niandai'] = unicode('暂无信息', "utf-8")   
                item['jianzhuleixing'] = unicode('暂无信息', "utf-8")             

            chengjiaodanjia = divFlood.xpath('.//div[@class="unitPrice"]/span/text()').extract()
            if chengjiaodanjia:
                item['chengjiaodanjia'] = chengjiaodanjia[0]+unicode('元/平', "utf-8")
            else:
                item['chengjiaodanjia'] = unicode('暂无均价', "utf-8")

            yield item    



        time.sleep(5)


