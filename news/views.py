from django.shortcuts import render, get_object_or_404, redirect
from django import http
from news.models import News
from django.utils import timezone 
from .forms import NewsForm



# Create your views here.


def create_news(request):

    if request.method == "POST":
        news_form = NewsForm(request.POST) 
        

        if news_form.is_valid():
            news_form = news_form.save(commit=False)
            news_form.author = request.user
            news_form.published_date = timezone.now()
            news_form.save()

            return redirect('news.views.show_news', pk=news_form.pk)
    else:
        news_form = NewsForm() 
        
        

        # information = {
        #     'news_form' : news_form,
        #     'page_name' : page_name
        # }
    page_name = "Criando uma nova Notícia!"

    information = {
            'news_form' : news_form,
            'page_name' : page_name
        }

    return render(request, 'news/create_news.html', information)

def edit_news(request, pk):
    news = get_object_or_404(News, pk=pk)

    if request.method == "POST":
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news = news_form.save(commit=False)
            news.author = request.user
            news.published_date = timezone.now()
            news.save()
            return redirect('news.views.show_news', pk=news.pk)

    else:
        news_form = NewsForm(instance=news)

    page_name = "Editando a Notícia"
    information = {
        'news_form' : news_form,
        'page_name' : page_name
    }
    return render(request, 'news/create_news.html', information)

def show_news(request, pk):
    selected_news = get_object_or_404(News, pk=pk)
    page_name = "Página de Notícia"

    information = {
        'selected_news' : selected_news,
        'page_name' : page_name
    }
    return render(request, 'news/show_news.html', information)

def home(request):
    recent_news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    page_name = "Página Inicial"

    information = {
        'news' : recent_news,
        'page_name' : page_name
    }

    return render(request, 'news/home.html', information)

