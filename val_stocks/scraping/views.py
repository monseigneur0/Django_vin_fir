from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json
from .models import Company, Category, Quarter, Daily
from pykrx import stock
from .models import Company, Quarter #data
import pandas as pd
import time
from datetime import datetime
from django.utils.dateformat import DateFormat
from IPython.display import display


def popular(req) :
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
    return render(req, 'b.html')
def start(req) :
    df = stock.get_market_ohlcv("20150720", "20150810", "005930")
    print(df.head(3))
    df1 = stock.get_market_fundamental("20210104", "20210108", "005930")
    print(df1.head(2))
    context = { 'lists_com' : df1 }
    samsung = stock.get_market_ticker_name("005930")
    print(samsung)
    print(type(samsung))
    df2 = stock.get_market_cap("20211208", "20211208", "005930")
    df3 = pd.DataFrame(df2)
    df4 = df3["시가총액"].tolist()
    print(df4)
    print(df4[0])
    print(type(df4))
    print(type(df4[0]))
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

def kospi_list(req):
#     tickers = stock.get_market_ticker_list()
#     ['095570', '006840', '027410', '282330', '138930', ...]
#
#     tickers = stock.get_market_ticker_list("20190225", market="KOSDAQ")
#     ['095570', '006840', '027410', '282330', '138930', ...]
#     aa1= stock.get_market_ticker_list("20211208", market="KOSDAQ")
#     print(len(aa1),aa1)
#     time.sleep(1)
# 코스닥
#     print("되냐")
#     tickers1 = stock.get_market_ticker_list("20211208", market="KOSDAQ")
#     print(tickers1)
#     for ticker in tickers1:
#         time.sleep(0.3)
#         df2 = stock.get_market_cap("20211208", "20211208", ticker)
#         time.sleep(0.3)
#         df3 = pd.DataFrame(df2)
#         df4 = df3["시가총액"].tolist()
#         name2 = stock.get_market_ticker_name(ticker)
#         time.sleep(0.3)
#         new_company = Company( ticker = ticker, company_name = name2, market = "d", stock_price = df4[0]  )
#         print(new_company)
#         new_company.save()

#     company1 = Company.objects.all()
#     company1.delete()
#     company2 = Category.objects.all()
#     company2.delete()

# 코스피
#     a3a1 = stock.get_market_ticker_list("20211208", market="KOSPI")
#     for ticker in a3a1:
#         time.sleep(0.05)
#         df2 = stock.get_market_cap("20211208", "20211208", ticker)
#         time.sleep(0.05)
#         df3 = pd.DataFrame(df2)
#         df4 = df3["시가총액"].tolist()
#         new_company = Company( ticker = ticker, company_name = stock.get_market_ticker_name(ticker), market = "p", stock_price = df4[0]  )
#         print(new_company)
#         time.sleep(0.05)
#         new_company.save()

# 키ㅏ테고리
#     for ef1 in range(4):
#         ak = 1024 + ef1

#     for ef1 in range(23):
#         ak = 1005 + ef1
#         print(ak)
#         pdf = stock.get_index_portfolio_deposit_file(str(ak))
#         time.sleep(2)
#         print(pdf)
#         fje1 = stock.get_index_ticker_name(str(ak))
#         time.sleep(2)
#         print(fje1)
#         new_company3 = Category( ticker2 = pdf, category_name = fje1, category_ticker =str(ak))
#         time.sleep(2)
#
#         print(new_company3)
#         new_company3.save()

    today = DateFormat(datetime.now()).format('Ymd')
    yesterday = str(int(today) - 2)
    print(today)
# 회사별 하루 거래 시가 종가 data
#     df = stock.get_market_ohlcv(yesterday, today, "005930")
#     print(df.head(3))
#
#     time.sleep(2)
#     new_company4 = Daily( ticker3 = "005930", result = df)
#     time.sleep(2)
#
#     print(new_company4)
#     new_company4.save()
#     comp_price = Daily.objects.all()
#     print(comp_price)
#     print(comp_price.values())

# 각각 시가총액 데이터 저장
#     cap = stock.get_market_cap(yesterday, today, "005930")
#     print(cap.head())
#     c_namea = Company.objects.all()
#     print("모든회사")
#     for i in c_namea :
#         print(i)
#         print(i.ticker)
#         its = str(i.ticker)
#         print(its)
#         i.stock_cap = stock.get_market_cap(yesterday, today, its )
#         print(i.stock_cap)
#         i.save()
#         time.sleep(0.1)
    c_name = Company.objects.get(ticker =  "005930")
    print(c_name)
    print(c_name.ticker)
    print(c_name.stock_cap)
    print(c_name)
    df = pd.DataFrame({"A":[1,4,7], "B":[2,5,8], "C":[3,6,9]})

    # Use `iloc[]` to select a row
    display(df)
    display(df.iloc[0])
    display(df.loc[0])

    # Use `loc[]` to select a column
    display(df.loc[:,'A'])
    display(df['A'])

    # 특정 row, column을 선택하기
    display(df.loc[0]['B'])





#     c_name.stock_cap = stock.get_market_cap(yesterday, today,  "005930")
#     c_name.save()
    expy1 = stock.get_market_cap(yesterday, today,  "005930")
    print(type(expy1))
#     print(expy1)
#     print(expy1["시가총액"])
#     print(expy1.shape)
#     c_name = Company.objects.get(ticker =  "005930")
#     print(c_name)


    return render(req, 'news.html' )

def tribeofstocks(req):

    return render(req, 'b.html')

def tribe(req):
    alotofcateg= Category.objects.all()
    context = {'comps1' : alotofcateg }
    # Django 템플릿에 사용할 파라미터 값을 변수로 선언 > 사용해야할 인자값이 많아질 때 편리하다.
    # board = get_object_or_404(Board, id=pk)
    # Board는 필자가 Model에서 설정한 DB 이름

    return render(req, 'tribe.html',context)

def com(req):
    comp = Company.objects.all()
    page = req.GET.get('page', '1')  # 페이지
    kw = req.GET.get('kw','') # 검색어
    #조회
    company_list = comp.order_by('code')
    if kw:
        company_list = company_list.filter(
            Q(code__icontains=kw) |
            Q(company__icontains=kw)
        ).distinct()

    #페이징처리
    paginator = Paginator(company_list, 20)
    page_obj = paginator.get_page(page)
    context = {'comp':page_obj, 'page':page, 'kw' : kw}
    return render(req, 'company.html', context)

