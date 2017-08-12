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
class RestaurantReview:
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
            items=wd.find_elements_by_css_selector("div[id^=review_]")
        except:
            items=[]
        return items
    def click_more(self,wait=1):
        wd=self.wd
        css="span.taLnk.ulBlueLinks"
        more_links=wd.find_elements_by_css_selector(css)
        if len(more_links) > 0:
            more_links[0].click()
            sleep(wait)
    def get_review_id(self):
        wd=self.wd
        css="data-reviewid"
        items=self.get_items()
        ids=[item.get_attribute(css) for item in items]
        return ids
    def get_title(self):
        wd=self.wd
        css="div.quote"
        items=self.get_items()
        title=[item.find_element_by_css_selector(css).text for item in items]
        return title
    def get_date(self):
        wd=self.wd
        css=".ratingDate"
        items=self.get_items()
        date=[i.find_element_by_css_selector(css).get_attribute("title") for i in items]
        return date
    def get_content(self):
        wd=self.wd
        css="div.entry p"
        items=self.get_items()
        content=[]
        for item in items:
            p=item.find_elements_by_css_selector(css)
            text=[i.text for i in p]
            content.append("\n".join(text))
        return content
    def get_review_score(self):
        wd=self.wd
        items=self.get_items()
        css=".rating.reviewItemInline > span"
        c1=re.compile(r'[0-9]+$')
        result=[]
        for item in items:
            try:
                a1=item.find_element_by_css_selector(css)
                a2=a1.get_attribute('class')
                b1=c1.findall(a2)
                result.append(b1[0])
            except:
                result.append("")
        return result
    def get_helpful_cnt(self):
        wd=self.wd
        css=".numHelp"
        items=self.get_items()
        result=[]
        for item in items:
            try:
                a1=item.find_element_by_css_selector(css)
                a2=a1.text.strip()
                result.append(a2)
            except:
                result.append("")
        return result
    def get_eval_info(self):
        wd=self.wd
        xpath="//span[@class='stayed']/.."
        items=self.get_items()
        eval=[]
        for i in items:
            try:
                a=i.find_element_by_xpath(xpath).text
                b=a.replace("Stayed: ","")
                eval.append(b)
            except:
                eval.append("")
        return eval
    def get_recommend(self):
        wd=self.wd
        items=self.get_items()
        css="li.recommend-answer"
        result=[]
        rating_c=re.compile(r"[0-9]+")
        for item in items:
            try:
                recommend=item.find_elements_by_css_selector(css)
                rrr=[]
                for r in recommend:
                    rr=r.find_elements_by_css_selector("div")
                    if len(rr) == 2:
                        rating0=rr[0].get_attribute("class")
                        try:
                            rating1=rating_c.findall(rating0)
                            rating=rating1[0]
                        except:
                            rating=""
                        category=rr[1].text
                        rrr.append(category+","+rating)
                result.append(";".join(rrr))
            except:
                result.append("")
        return result
    def get_photo_cnt(self):
        wd=self.wd
        css=".photoContainer"
        items=self.get_items()
        result=[]
        for item in items:
            photos=item.find_elements_by_css_selector(css)
            result.append(len(photos))
        return result
    def get_photo_url(self):
        wd=self.wd
        css=".photoContainer img"
        items=self.get_items()
        result=[]
        for item in items:
            photos=item.find_elements_by_css_selector(css)
            photo_urls=[p.get_attribute("src") for p in photos]
            result.append(",".join(photo_urls))
        return result
    def get_region_exp(self):
        wd=self.wd
        css=".userLink a"
        c1=re.compile(r"See all ([0-9,]+)")
        c2=re.compile(r"for (.+)$")
        items=self.get_items()
        result=[]
        for item in items:
            try:
                a=item.find_element_by_css_selector(css)
                a1=a.text
                b1=c1.findall(a1)[0]
                b2=c2.findall(a1)[0]
                result.append(b2+","+b1)
            except:
                result.append("")
        return result
    def get_user_name(self):
        wd=self.wd
        css="div.username"
        items=self.get_items()
        result=[]
        for item in items:
            try:
                a=item.find_element_by_css_selector(css)
                result.append(a.text)
            except:
                result.append("None")
        return result
    def get_user_region(self):
        wd=self.wd
        css="div.location"
        items=self.get_items()
        result=[]
        for item in items:
            try:
                a=item.find_element_by_css_selector(css)
                result.append(a.text)
            except:
                result.append("None")
        return result
    def get_user_badging(self):
        wd=self.wd
        css="div.memberBadgingNoText span"
        items=self.get_items()
        result=[]
        for item in items:
            try:
                a=item.find_elements_by_css_selector(css)
                b=[i.text for i in a]
                if len(b) == 4:
                    result.append("write:"+b[1]+","+"liked:"+b[3])
                else:
                    result.append("write:"+b[1]+","+"liked:0")
            except:
                result.append("")
        return result
    def scroll_down(self):
        wd=self.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    def go_next(self,sleep_time=10):
        wd=self.wd
        css='div#REVIEWS span.nav.next.taLnk'
        try:
            btn=wd.find_element_by_css_selector(css)
            ActionChains(wd).click(btn).perform()
            sleep(sleep_time)
            #self.scroll_down()
            output=False
        except:
            output=True
        return output
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
def main_review(chrome,name,page_no=1,end=-1,wait=5):
    res=RestaurantReview(chrome)
    jump=page_no-1
    temp_page_no=1
    while jump > 0:
        if res.go_next(wait):
            break
        print("Page jump!, current=%d"%(temp_page_no,))
        temp_page_no+=1
        jump-=1
    while True:
        sleep(1)
        res.click_more()
        sleep(1)
        data=pd.DataFrame()
        data['review_id']=res.get_review_id()
        data['review_date']=res.get_date()
        data['user_name']=res.get_user_name()
        data['user_region']=res.get_user_region()
        data['user_badging']=res.get_user_badging()
        data['title']=res.get_title()
        data['review_score']=res.get_review_score()
        data['eval']=res.get_eval_info()
        data['recommend']=res.get_recommend()
        data['photo_cnt']=res.get_photo_cnt()
        data['photo_urls']=res.get_photo_url()
        data['region_exp']=res.get_region_exp()
        data['helpful_cnt']=res.get_helpful_cnt()
        data['content']=res.get_content()
        if res.go_next(wait):
            break
        data.to_excel("%s/%05d.xls"%(name,page_no,))
        print("Page %s/%05d.xls saved"%(name,page_no))
        if end > 0:
            if page_no >= end:
                break
        page_no+=1
    print("Thank you")
def main_directory(chrome,region,page_no=1,wait=5):
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