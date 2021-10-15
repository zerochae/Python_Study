from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
from datetime import datetime
import time
from daoStock import StockDao


# with urllib.request.urlopen(web_url) as response :
#     html = response.read()
#     soup = BeautifulSoup(html, "html.parser")


url = 'https://vip.mk.co.kr/newSt/rate/item_all.php?koskok=KOSPI&orderBy=upjong'



response = requests.get(url)
# response.encoding("utf-8");
s_time = datetime.today().strftime('%Y%m%d.%H%M%S')

if response.status_code == 200 :
    html = urllib.request.urlopen(url).read().decode('cp949', 'ignore')
    soup = BeautifulSoup(html,"html.parser")

    select_tr = soup.select('.st2')
    se = StockDao()

    for index,i in enumerate(select_tr) : 
        s_name = i.text # 종목 이름
        s_code = i.a['title'] #종목 코드
        s_price = i.parent.select('td')[1].text.replace(",","")
        se.insert(s_code,s_name,s_price,s_time)

        # se.insert(s_name,s_code,s_price,s_time)

    se.mycommit()



    # print("---------------------------------------")
    # print("방법 1")
    # tds = soup.select('tr')
    # for i in range (1,3) :
    #     print(tds[i].text)

    # print("---------------------------------------")
    # print("방법 2")
    
    # tables = soup.select('table')

    # trs= tables[0].select('tr')

    # for index,tr in enumerate(trs):
    #     if index > 0 :
    #         tds = tr.select('td')
    #         print(tds[1].text, tds[2].text, tds[3].text)
    # print("---------------------------------------")