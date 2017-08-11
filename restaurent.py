#restaurent.py
import pandas as pd
import re
from selenium.common.exceptions import *
from selenium import webdriver as wd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class ListUpRestarent:
	def __init__(self,webdriver):
		self.wd=webdriver
		self.change_us()
	def change_us(self):
		wd=self.wd
		css="div.unified-picker"
		wd.find_elements_by_css_selector(css)[1].click()
		css="a.pos_link.flag_us.ui_link"
		us=WebDriverWait(wd,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,css)))
		#us=webdriver.find_element_by_css_selector(css)
		us.click()
	def get_items(self):
		wd=self.wd
		try:
			items=wd.find_elements_by_css_selector("div[id^=eatery]")
		except:
			items=[]
		return items
	def get_anchors(self):
		wd=self.wd
		css_code='h3.title a'
		items=self.get_items()
		if len(items) > 0:
			try:
				anchors=list(map(lambda item:item.find_element_by_css_selector(css_code).get_attribute("href"),items))
			except:
				anchors=[]
		else:
			anchors=[]
		return anchors
	def get_titles(self):
		wd=self.wd
		css_code='h3.title'
		items=self.get_items()
		if len(items) > 0:
			try:
				titles=list(map(lambda item:item.find_element_by_css_selector(css_code).text,items))
			except:
				titles=[]
		else:
			titles=[]
		return titles
	def get_review_cnt(self):
		wd=self.wd
		items=self.get_items()
		if len(items) <=0:
			return []
		text_data=list(map(lambda item:item.text,items))
		re_c=re.compile(r'\n([0-9,]+) reviews')
		reviews=[]
		for txt in text_data:
			r=re_c.findall(txt)
			if len(r)>0:
				reviews.append(r[0])
			else:
				reviews.append('-1')
		return reviews
	def get_review_star(self):
		wd=self.wd
		items=self.get_items()
		if len(items) <= 0:
			return []
		css='span.ui_bubble_rating'
		re_c=re.compile(r'([0-9\.]+) of')
		stars=[]
		for item in items:
			try:
				item1=item.find_element_by_css_selector(css)
				item2=item1.get_attribute('alt')
				item3=re_c.findall(item2)
				if len(item3)>0:
					stars.append(item3[0])
				else:
					stars.append('-1')
			except:
				stars.append('-1')
		return stars
	def get_price_level(self):
		wd=self.wd
		items=self.get_items()
		if len(items) <=0:
			return []
		text_data=list(map(lambda item:item.text,items))
		re_c=re.compile(r'\$[\$\- ]+')
		price=[]
		for txt in text_data:
			r=re_c.findall(txt)
			if len(r)>0:
				price.append(r[0].strip())
			else:
				price.append('NA')
		return price
	def get_ranking(self):
		wd=self.wd
		items=self.get_items()
		if len(items) <=0:
			return ([],[],)
		text_data=list(map(lambda item:item.text,items))
		re_c=re.compile(r'\n#([0-9,]+) of')
		re_c2=re.compile(r' of ([0-9,]+) Restaurants')
		ranking=[]
		total=[]
		for txt in text_data:
			r=re_c.findall(txt)
			if len(r)>0:
				ranking.append(r[0])
			else:
				ranking.append('-1')
		for txt in text_data:
			r=re_c2.findall(txt)
			if len(r)>0:
				total.append(r[0])
			else:
				total.append('-1')
		return (ranking,total)
	def scroll_down(self):
		wd=self.wd
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	def go_next(self,sleep_time=10):
		wd=self.wd
		css='a.nav.next.rndBtn.ui_button.primary.taLnk'
		try:
			btn=wd.find_element_by_css_selector(css)
			ActionChains(wd).click(btn).perform()
			sleep(sleep_time)
			self.scroll_down()
			output=False
		except:
			output=True
		return output
def main(chrome,region,page_no=1,wait=5):
	lst=ListUpRestarent(chrome)
	while True:
		data=pd.DataFrame()
		data['title']=lst.get_titles()
		data['link']=lst.get_anchors()
		data['review_cnt']=lst.get_review_cnt()
		data['review_star']=lst.get_review_star()
		data['price_level']=lst.get_price_level()
		data['ranking'],data['ranking_base']=lst.get_ranking()
		if lst.go_next(wait):
			break
		data.to_excel('%s/%05d.xls'%(region,page_no))
		print("Page %s/%05d.xls saved"%(region,page_no))
		page_no += 1
	print("Thank you")	