from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'), 
    path('news_detail/', views.news_detail, name='news_detail') 
]