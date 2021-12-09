from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json
from .models import Company

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


def news(req):

    #네이버 경제 메인
    url = f'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101'

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')

    my_news = soup.select('#main_content > div > div._persist > div:nth-child(1) > div.cluster_group._cluster_content > div.cluster_body > ul > li:nth-child(1) > div.cluster_text > a')
    my_news_content = soup.select('#main_content > div > div._persist > div:nth-child(1) > div.cluster_group._cluster_content > div.cluster_body > ul > li:nth-child(1) > div.cluster_text > div.cluster_text_lede')
    my_news_writing = soup.select('#main_content > div > div._persist > div:nth-child(1) > div.cluster_group._cluster_content > div.cluster_body > ul > li:nth-child(1) > div.cluster_text > div.cluster_text_info > div')
    my_news_image = soup.select('#main_content > div > div._persist > div:nth-child(1) > div.cluster_group._cluster_content > div.cluster_body > ul > li:nth-child(1) > div.cluster_thumb > div.cluster_thumb_inner > a > img')

    newslist = list()
    nnews = list()

    for news in my_news: # 뉴스 제목을 리스트에 append
        nnews.append(news.text.strip())

    for i in range(len(nnews)):
        title = my_news[i].text.strip()
        link = my_news[i].get('href')
        content = my_news_content[i].text.strip()
        writing = my_news_writing[i].text.strip()

        try: #list index out of range 방지를 위한 예외처리
            image_s = my_news_image[i].get('src')
            image = my_news_image[i].get('src').replace('nf132_90','w647') # 크기 조정을 위한 replace
        except:
            image_s="NO IMAGE"
            image = "NO IMAGE"

        item_obj = {
            'title': title,
            'link': link,
            'content': content,
            'writing': writing,
            'image': image,
            'image_s': image_s,
        }
        newslist.append(item_obj)

    print(newslist)
    context = {'newsall' : newslist }
    return render(req, 'news.html', context )
