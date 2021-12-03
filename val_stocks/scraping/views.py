from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json

# naver finance 인기 검색 종목
urls = 'https://finance.naver.com/'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
res = requests.get(urls,headers=headers)
soups = BeautifulSoup(res.text,'html.parser')

top = soups.select("#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr > th")

toplist = list()
top2 = list()

for tops in top:
    toplist.append(tops.text.strip())

for i in range(len(toplist)):
    comp = top[i].text.strip()

    item_objs={
        'comp':comp,
    }
    top2.append(item_objs)

comps = top2
print(comps)
# Create your views here.
def start(req) :
      return render(req, 'a.html')

