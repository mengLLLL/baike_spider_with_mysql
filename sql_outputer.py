#coding:utf8
#!/usr/bin/env 
import pymysql


class SqlOutputer(object):
	def __init__(self):
		self.datas = []


	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_sql(self):
		print (self.datas)
		conn = pymysql.connect(
			host = '127.0.0.1',
			port = 3306,
			user = 'root',
			passwd = 'root',
			db = 'for_python',
			charset = 'utf8')

		for data in self.datas:
			try:
				print (data)
				cursor = conn.cursor()
				s = data['summary'][0:10]
				cursor.execute("insert into spider_baike (url,title,summary) values(%s,%s,%s)",(data['url'],data['title'],s.lstrip()))
				conn.commit()
			except Exception as e:
				print (e)
				conn.rollback()

		cursor.close()
		conn.close()