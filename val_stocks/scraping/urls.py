from django.urls import path, re_path
from . import views


app_name = 'user'
urlpatterns = [
      path( "ok", views.start ),
      path( "index", views.index ),
      path( "news", views.news ),
      path( "pop", views.popular ),
      path( "update", views.kospi_list ),
      path( "trib", views.tribeofstocks ),
      path( "com", views.com ),
      path( "tribe", views.tribe ),

      ]