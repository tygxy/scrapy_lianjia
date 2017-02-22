#encoding=utf-8
import json
import MySQLdb

file = open('东城小区.txt')
datalist  =[]

for line in file:
	datalist.append(line)

# 连接数据库
conn = MySQLdb.connect(host='localhost',user='root',passwd='302313',db='lianjia',charset='utf8')
cursor = conn.cursor()

# 创建表
# sql_createTable = """create table if not exists dongcheng(
# 					id int not null auto_increment, 
# 					xiaoqumincheng varchar(100) not null,
# 					junjia varchar(100),
# 					xingzhengqu varchar(100),
# 					daqu varchar(100),
# 					xiangxiweizhi varchar(100),
# 					jianzhuniandai varchar(100),
# 					jianzhuleixing varchar(100),
# 					wuyefeiyong varchar(100),
# 					wuyegongsi varchar(100),
# 					kaifashang varchar(100),
# 					loudongzongshu varchar(100),
# 					fangwuzongshu varchar(100),
# 					primary key(id)
# 					)"""
# cursor.execute(sql_createTable)

# 插入数据
# for data in datalist:
# 	# 获取数据
# 	data = json.loads(data)
# 	xiaoqumincheng = data["xiaoqumincheng"]
# 	junjia = data["junjia"]
# 	xingzhengqu = data["xingzhengqu"]
# 	daqu = data["daqu"]
# 	xiangxiweizhi = data['xiangxiweizhi']
# 	jianzhuniandai = data['jianzhuniandai']
# 	jianzhuleixing = data['jianzhuleixing']
# 	wuyefeiyong = data['wuyefeiyong']
# 	wuyegongsi = data['wuyegongsi']
# 	kaifashang = data['kaifashang']
# 	loudongzongshu= data['loudongzongshu']
# 	fangwuzongshu = data['fangwuzongshu']

# 	# sql_insert = "insert into dongcheng(xiaoqumincheng,junjia,xingzhengqu,daqu \
# 	# 			,xiangxiweizhi,jianzhuniandai,jianzhuleixing,wuyefeiyong,wuyegongsi \
# 	# 			kaifashang,loudongzongshu,fangwuzongshu,) \
# 	# 			values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
# 	# 			(xiaoqumincheng,junjia,xingzhengqu,daqu,xiangxiweizhi,jianzhuniandai,\
# 	# 			jianzhuleixing,wuyefeiyong,wuyegongsi,kaifashang,loudongzongshu,fangwuzongshu)

# 	sql_insert = "insert into dongcheng(xiaoqumincheng,junjia,xingzhengqu,daqu,xiangxiweizhi,\
# 					jianzhuniandai,jianzhuleixing,wuyefeiyong,wuyegongsi,kaifashang,loudongzongshu,fangwuzongshu) \
# 				values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
# 				% (xiaoqumincheng,junjia,xingzhengqu,daqu,xiangxiweizhi,jianzhuniandai,jianzhuleixing,\
# 					wuyefeiyong,wuyegongsi,kaifashang,loudongzongshu,fangwuzongshu)

# 	try:
# 		cursor.execute(sql_insert)
# 		conn.commit()
# 	except Exception as e:
# 		conn.rollback()

# 查询数据
# sql_select = "select * from dongcheng"
# resultList=[]
# try:
# 	cursor.execute(sql_select)
# 	result = cursor.fetchall()
# 	for row in result:
# 		xiaoqumincheng = row[1]
# 		print xiaoqumincheng
# except Exception as e:
# 	raise e

# 更新数据
# sql_update = "update dongcheng set junjia='100001' where id='1'"
# cursor.execute(sql_update)
# conn.commit()
# sql_select = "select junjia from dongcheng where id='1'"
# result = cursor.fetchone()[0]
# print result

# 删除数据
# sql_delete = "delete dongcheng where id='1'"
# cursor.execute(sql_delete)
# conn.commit()

conn.close()