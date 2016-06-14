from django.shortcuts import render, get_object_or_404
from django import http
from news.models import News
from django.utils import timezone 



# Create your views here.


def create_news(request):
    pass

def show_news(request, pk):
    selected_news = get_object_or_404(News, pk=pk)
    page_name = "Página de Notícia"
    information = {
        'selected_news' : selected_news,
        'page_name' : page_name
    }
    return render(request, 'news/show_news.html', information)

def home(request):
    recent_news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    page_name = "Página Inicial"
    information = {
        'news' : recent_news,
        'page_name' : page_name
    }

    return render(request, 'news/home.html', information)

