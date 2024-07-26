from django.urls import path, include
from .views import NewsList, NewsDetail


app_name = 'news'

urlpatterns = [
    path("", NewsList.as_view(), name='news_list'),
    path("<int:pk>", NewsDetail.as_view(), name='detail_news') 
]
