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
  	





