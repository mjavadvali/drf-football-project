from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):
    def get_queryset(self) :
        return News.objects.filter(status=True)
    

class NewsDetail(DetailView):
    template_name = 'news/news_detail.html'
    model = 'News'
    def get_object(self):
        return get_list_or_404(News.objects.filter(status=True), 
                               pk=self.kwargs.get("pk")
                               )