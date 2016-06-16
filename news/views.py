from django.shortcuts import render, get_object_or_404, redirect
from django import http
from django.http import HttpResponseRedirect, HttpResponse
from news.models import News
from django.utils import timezone 
from .forms import NewsForm
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

@login_required
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
    button_name = "Editar Notícia"
    information = {
        'news_form' : news_form,
        'page_name' : page_name,
        'button_name' : button_name
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
@login_required
def news_draft_list(request):
    news_list = News.objects.filter(published_date__isnull=True).order_by('-created_date')
    page_name = "Lista de notícias não publicadas"

    information = {
    'news_list' : news_list,
    'page_name' : page_name
    }

    return render(request, 'news/news_draft_list.html', information)
@login_required
def publish_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.publish()

    return redirect('news.views.show_news', pk=pk)
@login_required
def remove_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()

    return redirect('news.views.home')
@login_required
def create_news(request):

    if request.method == "POST":
        news_form = NewsForm(request.POST) 
        
        if news_form.is_valid():
            news_form = news_form.save(commit=False)
            news_form.author = request.user
            news_form.save()

            return redirect('news.views.show_news', pk=news_form.pk)
    else:
        news_form = NewsForm() 

    page_name = "Criando uma nova Notícia!"
    button_name = "Criar Notícia"
    
    information = {
            'news_form' : news_form,
            'page_name' : page_name,
            'button_name' : button_name
        }

    return render(request, 'news/create_news.html', information)

def create_user(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            #login(request, new_user)

            return redirect('news.views.home')

    else:
        user_form = UserForm()

    page_name = "Página de criação de usuário"
    button_name = "Criar Usuário"
    information = {
        'user_form' : user_form,
        'button_name' : button_name,
        'page_name' : page_name
    }

    return render(request, 'news/create_user.html', information)

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('news.views,home')

            else:
                return HttpResponse("Conta desativada")

        else:
            return HttpResponse("Nome de usuário ou senha inválidos!.")
    else:
        return render(request, 'login.html')

