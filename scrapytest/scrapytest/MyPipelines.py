# -*- coding: utf-8 -*-
#引入文件
from scrapy import signals
from scrapy.exceptions import DropItem
import json
import codecs

class MyPipeline(object):

    # global num
    # num=1

    def __init__(self):
        pass
        # #打开文件

        # 小区详细信息
        # self.file = codecs.open('xiaoquDetial.json', 'w',encoding='utf-8')

        # 小区列表
        # self.file = codecs.open('xiaoquList.json', 'w',encoding='utf-8')

        # 小区成交记录
        self.file = codecs.open('xiaoquchengjiao.json', 'w',encoding='utf-8')

        # 小区成交列表
        # self.file = codecs.open('xiaoquchengjiaoList.json', 'w',encoding='utf-8')

     
    def _setFileName(self,filename):
        newfilename = filename
        self.file = codecs.open(newfilename, 'w',encoding='utf-8')

    #该方法用于处理数据
    def process_item(self, item, spider):

        # global num
        # dealNum = int(item["xiaoquzongchengjiaoshu"])

        # # 创建file
        # if(num==1):
        #     num+=1
        #     filename = item["fangchanmincheng"]+'.json'  
        #     self._setFileName(filename)

        #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #     #写入文件
        #     self.file.write(line)
        #     #返回item
        #     return item

        
        # #插入数据
        # if(num>1 and num<=dealNum):
        #     num+=1
        #     if(num==(dealNum+1)):
        #         num=1
        #     #读取item中的数据
        #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #     #写入文件
        #     self.file.write(line)
        #     #返回item
        #     return item

        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #写入文件
        self.file.write(line)
        #返回item
        return item


        
    #该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass
    #该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        pass