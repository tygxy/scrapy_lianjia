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
