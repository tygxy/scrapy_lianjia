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

- 执行 scrapy crawl Spider_xiaoquList,数据保存在xiaoquList.json中

- 第二步的程序在scrapytest/spiders/Spider_xiaoquDetial.py,读取xiaoquList.json中的小区详细页面的URL

- 执行 scrapy crawl Spider_xiaoquDetial,数据保存在xiaoquDetial.json中

- 第三步，将json格式的数据写入excel中，执行python JsonToExcel.py,生成六个Excel表格

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

- 第二步的程序在scrapytest/spiders/Spider_xiaoquchengjiao.py

- 执行 scrapy crawl Spider_xiaoquchengjiao,数据保存在xiaoquchengjiao.json中

- 第三步，将json格式的数据写入excel中，执行python makefile.py,生成7K个Excel

### 3.3 结果展示

![](raw/figure8.png?raw=true)

![](raw/figure8_1.png?raw=true)


