from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^news/(?P<pk>[0-9]+)/$', views.show_news),
    url(r'news/create_news/$', views.create_news, name='create_news'),
    url(r'^news/(?P<pk>[0-9]+)/edit/$', views.edit_news, name='edit_news')
]