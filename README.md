# scrapy_lianjia
## 0.引言
使用Scrapy爬链家网的部分数据

## 1.任务需求

### 1.1 北京六城区小区数据

- 小区页面URL

![](raw/figure1.png?raw=true)

- 字段需求

![](raw/figure2.png?raw=true)

- 字段在页面中的样例(需从详细页面抓取)

![](raw/figure3.png?raw=true)

### 1.2 北京六城区成交数据

- 成交页面URL

![](raw/figure4.png?raw=true)

- 字段需求

![](raw/figure5.png?raw=true)

- 字段在页面中的样例(在列表页面抓取)

![](raw/figure6.png?raw=true)

## 2.爬取小区数据

### 2.1 任务分析

- 第一步：由于链家在小区列表最多能呈现100个页面，所以不能直接从list爬到所有小区URL，需要细分到六个城区分别爬取小区的详细页面URL

- 第二步：在小区详细页面中爬取所需字段

### 2.2 执行命令

- 第一步的程序在scrapytest/spiders/Spider_xiaoquList.py中，在爬取不同城区时需要手动修改start_urls

```python
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
```

- 执行 scrapy crawl Spider_xiaoquList,数据保存在xiaoquList.json中

```python
> scrapy crawl Spider_xiaoquList
```

- 第二步的程序在scrapytest/spiders/Spider_xiaoquDetial.py,读取xiaoquList.json中的小区详细页面的URL

- 执行 scrapy crawl Spider_xiaoquDetial,数据保存在xiaoquDetial.json中

```python
> scrapy crawl Spider_xiaoquDetial
```

- 第三步，将json格式的数据写入excel中，执行python JsonToExcel.py,生成六个Excel表格

```python

#!/usr/bin/env python
# coding=utf-8

import xlsxwriter
import json   

book = xlsxwriter.Workbook('西城小区.xlsx')
tmp = book.add_worksheet()

dataFile = open("西城小区.txt")
data_json_list = []
for line in dataFile:
    data_json_list.append(line)

i=0

for data_json in data_json_list:
    data = json.loads(data_json)
    i+=1
    tmp.write(i,0,data["xiaoqumincheng"])
    tmp.write(i,1,data["junjia"])
    tmp.write(i,2,data["xingzhengqu"])
    tmp.write(i,3,data["daqu"])
    tmp.write(i,4,data["xiangxiweizhi"])    
    tmp.write(i,5,data["jianzhuniandai"])
    tmp.write(i,6,data["jianzhuleixing"])
    tmp.write(i,7,data["wuyefeiyong"])
    tmp.write(i,8,data["wuyegongsi"])
    tmp.write(i,9,data["kaifashang"])
    tmp.write(i,10,data["loudongzongshu"])
    tmp.write(i,11,data["fangwuzongshu"])

book.close()

```

### 2.3 结果展示

![](raw/figure7.png?raw=true)

## 3.爬取链家成交数据

### 3.1 任务分析

- 第一步：六区共50W条数据，通过上一个任务爬到7k个小区URL，做适当的字符串修改构造出新的URL，可以爬到小区成交数据list的第一页和小区总成交量

- 第二步：由小区成交量/30可以得到小区list的数量，构造出URL

- 第三步：通过第二步得出的URL，爬到相关字段

### 3.2 执行命名

- 第一步的程序在scrapytest/spiders/Spider_xiaoquchengjiaoList.py中

- 执行 scrapy crawl Spider_xiaoquchengjiaoList,数据保存在xiaoquchengjiaoList.json中
```python
scrapy crawl Spider_xiaoquchengjiaoList
```

- 第二步的程序在scrapytest/spiders/Spider_xiaoquchengjiao.py

- 执行 scrapy crawl Spider_xiaoquchengjiao,数据保存在xiaoquchengjiao.json中

```python
scrapy crawl Spider_xiaoquchengjiao
```

- 第三步，将json格式的数据写入excel中，执行python makefile.py,生成7K个Excel

```python
#!/usr/bin/env python
# coding=utf-8

import xlsxwriter
import json   

# 获取所有数据
dataFile = open("xiaoquchengjiao.txt")
data_list = []
for line in dataFile:
    data_list.append(line)

# 获取小区名称列表
xiaoquNameList=[]
for data_json in data_list:
	data = json.loads(data_json)
	xiaoquName =data['fangchanmincheng'].encode("utf-8")
	ifHasName = False
	for name in xiaoquNameList:
		if name == xiaoquName:
			ifHasName = True
	if ifHasName == False:
		xiaoquNameList.append(xiaoquName)

# 新建excel并录入数据
for i in range(0,len(xiaoquNameList)):
	# 创建excel和写入表头
	fileName=xiaoquNameList[i]+'.xlsx'
	book = xlsxwriter.Workbook(fileName)
	tmp = book.add_worksheet()
	j=0
	tmp.write(j,0,unicode("房产名称",'utf-8'))
	tmp.write(j,1,unicode("成交日期",'utf-8'))
	tmp.write(j,2,unicode("成交总价",'utf-8'))
	tmp.write(j,3,unicode("成交单价",'utf-8'))
	tmp.write(j,4,unicode("面积",'utf-8'))
	tmp.write(j,5,unicode("朝向",'utf-8'))
	tmp.write(j,6,unicode("装修",'utf-8'))
	tmp.write(j,7,unicode("有无电梯",'utf-8'))
	tmp.write(j,8,unicode("楼层",'utf-8'))
	tmp.write(j,9,unicode("年代",'utf-8'))
	tmp.write(j,10,unicode("建筑类型",'utf-8'))
	j+=1
	# 获取指定小区所有数据
	for data_json in data_list:
	    data = json.loads(data_json)
	    xiaoquName =data['fangchanmincheng'].encode("utf-8")
	    if xiaoquName == xiaoquNameList[i]:
			# 写入excel
	   		tmp.write(j,0,data["fangchanmincheng"])
	   		tmp.write(j,1,data["chengjiaoriqi"])
	   		tmp.write(j,2,data["chengjiaozongjia"])
	   		tmp.write(j,3,data["chengjiaodanjia"])
	   		tmp.write(j,4,data["mianji"])
	   		tmp.write(j,5,data["chaoxiang"])
	   		tmp.write(j,6,data["zhuangxiu"])
	   		tmp.write(j,7,data["youwudianti"])
	   		tmp.write(j,8,data["louceng"])
	   		tmp.write(j,9,data["niandai"])
	   		tmp.write(j,10,data["jianzhuleixing"])
	   		j+=1  
	book.close()
```

### 3.3 结果展示

![](raw/figure8.png?raw=true)



