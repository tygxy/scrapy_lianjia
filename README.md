# scrapy_lianjia
## 0.引言
使用Scrapy爬链家网的部分数据

## 1.任务需求

- 爬虫的内容在我这边主要是两个，一个是北京六城区所有小区的基本信息，数据量在7K条左右。第二个是北京六城区所有成交记录，数据量在50W条左右。

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

- 分两步，第一步需要在http://bj.lianjia.com/xiaoqu/ 列表中爬到所有小区详细页面的URL，第二步是到具体的小区URL爬到相关信息。

- 但是链家网的网页有两个特征需要注意，第一是任何一个列表页面，一页最多能展示30条数据，而且最多只有100页。也就是说，在/xiaoqu/这个URL中，最多只能爬到3000个小区。解决办法就是细分到城区这个级别，比如/xiaoqu/dongcheng/，东城1142个小区，小于3000条，可行。

- 第二个特征是每个页面的页脚是js动态生成的，页脚包含着页数等信息。处理翻页时就不能直接获取到下一页的URL，只能通过观察找到其中的规律，人工构造出下一页的URL并判断起止。


### 2.2 爬小区详细页面的URL

- Scrapy的程序比较简单，只需要几步简单的设置，在start_urls()中放入目标URL，item容器保存数据，xpath()语法规则爬取页面的元素。简单学习下就可以使用了，这里就不多做介绍

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

![](raw/num4.png?raw=true)

### 2.3 爬取小区相关字段

- 第二步的程序在scrapytest/spiders/Spider_xiaoquDetial.py,读取xiaoquList.json中的小区详细页面的URL

- 执行 scrapy crawl Spider_xiaoquDetial,数据保存在xiaoquDetial.json中

```python
> scrapy crawl Spider_xiaoquDetial
```

![](raw/num5.png?raw=true)

### 2.4 JSon格式转换成Excel

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

### 2.5 结果展示

![](raw/num7.png?raw=true)


![](raw/figure7.png?raw=true)


## 3.爬取链家成交数据

### 3.1 任务分析

- 这个任务的数据量就比之前的大了一两个数量级，而且不能够从城区这个角度爬，因为每个城区的成交记录也都在万这个级别，显然大于3000的限制。所以需要细分到每个小区，分别爬取每个小区的成交记录。

- 还有一个问题，就是由于不能爬到页数，导致需要我们专门写个程序判断页数。我的处理方法是：第一步先爬取小区成交的起始URL和小区成交总数。第二步通过小区成交总数/30+1，可以计算出这个小区成交总页数。第三步就是构造出相应的URL。


### 3.2 爬小区URL+成交总数

- 第一步的程序在scrapytest/spiders/Spider_xiaoquchengjiaoList.py中

- 执行 scrapy crawl Spider_xiaoquchengjiaoList,数据保存在xiaoquchengjiaoList.json中
```python
scrapy crawl Spider_xiaoquchengjiaoList
```
![](raw/num3.png?raw=true)

### 3.3 爬小区成交记录

- 第二步的程序在scrapytest/spiders/Spider_xiaoquchengjiao.py

- 执行 scrapy crawl Spider_xiaoquchengjiao,数据保存在xiaoquchengjiao.json中

```python
scrapy crawl Spider_xiaoquchengjiao
```

![](raw/num11.png?raw=true)

### 3.4 JSon格式转换成Excel

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

![](raw/num12.png?raw=true)



