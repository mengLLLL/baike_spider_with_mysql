#coding:utf8
#!/usr/bin/env 

from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
		# print (links)
		for link in links:
			# print ('link',link)
			new_url = link['href']
			# print (new_url)
			new_full_url = urllib.parse.urljoin(page_url,new_url)
			# print ('new_full_url',new_full_url)
			new_urls.add(new_full_url)

		return new_urls

	def _get_new_data(self,page_url,soup):
		res_data = {}
		res_data['url']=page_url
		title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find("h1")
		res_data['title'] = title_node.get_text()
		summary_node = soup.find('div',class_='lemma-summary')
		res_data['summary'] = summary_node.get_text()
		return res_data


	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		# print (soup)
		# print ('parser')
		new_urls = self._get_new_urls(page_url,soup)
		# print ('new_urls',new_urls)
		new_data = self._get_new_data(page_url,soup)
		# print(links)
		# print ('new_data',new_data)
		return new_data,new_urls
