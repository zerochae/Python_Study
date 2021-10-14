import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import requests

from moviedao import MovieDao

class SearchMovie :

    def __init__(self) :

        pass;

    def searchMoive(self,movieName) :

        client_id = "W4LJlZTZkGM_1JS71Hme"
        client_secret = "oKr_H0EQrB"
        encText = urllib.parse.quote(movieName)
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
            # list = response_body.decode('utf-8')
            html = response_body.decode('utf-8')
            soup = BeautifulSoup(html,"html.parser")

            items = soup.select('item')

            result = []
            md = MovieDao()
            for i in items :
                
                title =  i.title.text
                link =   i.link.text
                image =  i.image.text
                subtitle = i.subtitle.text
                pubData = i.pubdate.text
                director = i.director.text
                actor = i.actor.text
                userRating = i.userrating.text
                # print(title, link, image, subtitle,pubData, director, actor,userRating)
                cnt = md.myInsert(title, link, image, subtitle, pubData, director, actor, userRating)
                print("cnt",cnt)

        else:
            print("Error Code:" + rescode)

        return result

if __name__ == '__main__':
    searchResult = SearchMovie().searchMoive("어벤져스")