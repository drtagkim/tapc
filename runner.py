import os
# === INPUT PARAMETERS ==============
#starting from 0 to 24
hotel_ranking=0
#start page, default = 1
page_no=1
#end page, default= -1 (all pages)
end=5
# ====================================
# Input URL:
test_urls=[ "https://www.tripadvisor.com/Hotel_Review-g297884-d3813531-Reviews-Park_Hyatt_Busan-Busan.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d5113510-Reviews-JW_Marriott_Dongdaemun_Square_Seoul-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g297892-d6662809-Reviews-Kensington_Jeju_Hotel-Seogwipo_Jeju_Island.html", "https://www.tripadvisor.com/Hotel_Review-g297889-d6845530-Reviews-Oakwood_Premier_Incheon-Incheon.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d301605-Reviews-Oakwood_Premier_Coex_Center-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d8587847-Reviews-Four_Seasons_Hotel_Seoul-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d301253-Reviews-The_Shilla_Seoul-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d306105-Reviews-Imperial_Palace_Seoul-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d6663003-Reviews-Lotte_City_Hotel_Guro-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d3477158-Reviews-Conrad_Seoul-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d8522933-Reviews-L7_Myeongdong-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d659341-Reviews-Yeouido_Park_Centre_Seoul_Marriott_Executive_Apartments-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g297885-d7679225-Reviews-Shilla_Stay_Jeju-Jeju_Jeju_Island.html", "https://www.tripadvisor.com/Hotel_Review-g297892-d301723-Reviews-The_Shilla_Jeju-Seogwipo_Jeju_Island.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d302237-Reviews-Le_Meridien_Seoul-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g297884-d306067-Reviews-Lotte_Hotel_Busan-Busan.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d1640728-Reviews-The_Classic_500_Executive_Residence_Pentaz-Seoul.html", "https://www.tripadvisor.com/Hotel_Review-g297884-d8492549-Reviews-Citadines_Haeundae_Busan-Busan.html", "https://www.tripadvisor.com/Hotel_Review-g297893-d306073-Reviews-Lotte_Hotel_Ulsan-Ulsan.html", "https://www.tripadvisor.com/Hotel_Review-g294197-d306128-Reviews-Lotte_Hotel_World-Seoul.html"]
test_names=[ "ranking01", "ranking02", "ranking03", "ranking04", "ranking05", "ranking06", "ranking07", "ranking08", "ranking09", "ranking10", "ranking11", "ranking12", "ranking13", "ranking14", "ranking15", "ranking16", "ranking17", "ranking18", "ranking19", "ranking20", "ranking21", "ranking22", "ranking23", "ranking24", "ranking25" ]
#If you need to create a new folder, uncomment the following:
import os.path as oph
if oph.exists(test_names[hotel_ranking]):
    pass
else:
    os.mkdir(test_names[hotel_ranking])
# ===================================
# MAIN #
from tapc.restaurent import *
from tapc.my_phantom import MyPhantomJS
phantom=MyPhantomJS()
phantom.get(test_urls[hotel_ranking])
main_review(phantom,test_names[hotel_ranking],page_no=page_no,end=end)
phantom.close()
# ===== END PROGRAM ======== #