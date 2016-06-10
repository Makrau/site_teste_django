from django.shortcuts import render
from django import http
from news.models import News
# Create your views here.


def create_news(request):
    pass

def show_news(request):
    return render(request, 'news/show_news.html', {})