from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json
from .models import Company
from pykrx import stock

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
# print(comps)
# Create your views here.
def start(req) :
    df = stock.get_market_ohlcv("20150720", "20150810", "005930")
    print(df.head(3))
    df1 = stock.get_market_fundamental("20210104", "20210108", "005930")
    print(df1.head(2))
    context = { 'lists_com' : df1 }
    samsung = stock.get_market_ticker_name(ticker)
    print(samsung)

    return render(req, 'a.html', context)

def index(request):
    #edit
    company_list = Company.objects.all()		# Company 모델에 있는 정보를 전부 가져온다.
    context = {'company_list': company_list}	# company_list의 정보를 context에 담는다.

    return render(request, 'index.html', context)