from django.shortcuts import render
from django import http
from news.models import News
from django.utils import timezone 


# Create your views here.


def create_news(request):
    pass

def show_news(request):
    return render(request, 'news/show_news.html', {})

def home(request):
    recent_news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    information = {
    'news' : recent_news
    }

    return render(request, 'news/home.html', information)

