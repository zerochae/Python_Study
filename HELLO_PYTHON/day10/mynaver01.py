import os
import sys
import urllib.request
client_id = "W4LJlZTZkGM_1JS71Hme"
client_secret = "oKr_H0EQrB"
encText = urllib.parse.quote("인디아나존스")
# url = "https://openapi.naver.com/v1/search/movie.json" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/movie.json?query="+encText+"&display=10&start=1"  #json
url = "https://openapi.naver.com/v1/search/movie.xml?query="+encText+"&display=10&start=1"  #xml
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)