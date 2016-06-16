from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^news/(?P<pk>[0-9]+)/$', views.show_news),
    url(r'news/create_news/$', views.create_news, name='create_news'),
    url(r'^news/(?P<pk>[0-9]+)/edit/$', views.edit_news, name='edit_news'),
    url(r'^news_drafts/$', views.news_draft_list, name ='news_draft_list'),
    url(r'^news/(?P<pk>\d+)/publish_news/$', views.publish_news, name='publish_news'),
    url(r'^news/(?P<pk>\d+)/remove_news/$', views.remove_news, name='remove_news'),
    url(r'^user/create_user/$', views.create_user, name='create_user'),
    # url(r'^login/$', views.user_login, name='user_login'),
]