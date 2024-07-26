from django.urls import path, include
from .views import NewsList, NewsDetail, UserDetail, UserList

app_name = 'api'

urlpatterns = [
    path("", NewsList.as_view(), name='news_list'),
    path("<slug:slug>", NewsDetail.as_view(), name='news_detail'),
    path("users/", UserList.as_view(), name='user_list'),
    path("users/<int:pk>", UserDetail.as_view(), name='user_detail')
]
