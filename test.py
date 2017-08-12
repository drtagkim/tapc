import os
test_dir="test3"
test_url="https://www.tripadvisor.co.kr/Hotel_Review-g274887-d7306673-Reviews-Aria_Hotel_Budapest-Budapest_Central_Hungary.html"
#os.mkdir(test_dir)
from restaurent import *
from my_phantom import MyPhantomJS
phantom=MyPhantomJS()
phantom.get(test_url)
main_review(phantom,test_dir,page_no=6,end=7)
phantom.close()