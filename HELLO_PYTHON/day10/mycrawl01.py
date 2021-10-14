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
    tds = soup.select('tr')
    # for td in tds :

    for i in range (1,3) :
        print(tds[i].text)
    
    tables = soup.select('table')
    tables[0].select()

# with open("http://127.0.0.1:8000/sawon_list") as fp:
#     soup = BeautifulSoup(fp)
# soup = BeautifulSoup("<html>data</html>")

