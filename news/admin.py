from django.contrib import admin
from .models import News, Comment, Notification

# Register your models here.
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Notification)