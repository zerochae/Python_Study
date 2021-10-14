from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests

# with urllib.request.urlopen(web_url) as response :
#     html = response.read()
#     soup = BeautifulSoup(html, "html.parser")


url = 'http://127.0.0.1:8000/sawon_list'

response = requests.get(url)

if response.status_code == 200 :
    html = response.text
    soup = BeautifulSoup(html,"html.parser")


    print("---------------------------------------")
    print("방법 1")
    tds = soup.select('tr')
    for i in range (1,3) :
        print(tds[i].text)

    print("---------------------------------------")
    print("방법 2")
    
    tables = soup.select('table')
    trs= tables[0].select('tr')

    for index,tr in enumerate(trs):
        if index > 0 :
            tds = tr.select('td')
            print(tds[1].text, tds[2].text, tds[3].text)
    print("---------------------------------------")