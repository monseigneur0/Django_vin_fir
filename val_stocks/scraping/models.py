from django.db import models

# Create your models here.
class Company(models.Model):
    ticker = models.CharField(max_length=20)
    company_name = models.CharField(max_length=40)
    stock_price = models.IntegerField(verbose_name='주식 가격')
    MARKETS = (('p','Kospi'), ('d', 'Kosdaq'), ('n', 'Nasdaq'))
    market = models.CharField(max_length=1, verbose_name='마켓', choices=MARKETS)
    category_name = models.CharField(max_length=40, verbose_name='카테고리명')
    def __str__(self):
        return self.company_name

class Quarter(models.Model):
    ticker4 = models.ForeignKey("Company", related_name="company", on_delete=models.CASCADE, db_column="ticker", verbose_name='티커')
    quarters = models.CharField(max_length=40, verbose_name='분기')
    years = models.CharField(max_length=40, verbose_name='년')
    sales = models.IntegerField( verbose_name='총 매출')
    net_profit = models.CharField(max_length=40, verbose_name='순이익')
    def __str__(self):
        return self.ticker4
