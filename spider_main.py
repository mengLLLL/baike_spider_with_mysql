#coding:utf8
#!/usr/bin/env 

import url_manager,html_downloader,sql_outputer,html_parser


class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = sql_outputer.SqlOutputer()
	def craw(self,root_url):
		count = 1
		#加到new_urls里面
		#入口
		self.urls.add_new_url(root_url) 
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print ('craw %d : %s' % (count,new_url))
				html_cont = self.downloader.download(new_url)
				# print (html_cont)
				new_data,new_urls = self.parser.parse(new_url,html_cont)
				# print (new_data)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)
				if count ==50:
					break
				count = count + 1
			except:
				print ('craw failed')
		self.outputer.output_sql()

if __name__=="__main__":
	root_url = 'http://baike.baidu.com/view/21087.htm'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)