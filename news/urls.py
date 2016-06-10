from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^news/(?P<pk>[0-9]+)/$', views.show_news),
]