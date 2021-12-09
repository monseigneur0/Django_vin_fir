from django.urls import path, re_path
from . import views


app_name = 'user'
urlpatterns = [
      path( "ok", views.start ),
      path( "index", views.index ),
      path( "news", views.news ),

      ]