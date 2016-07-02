from django.db import models
from django.utils import timezone


# Create your models here.


class News(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 100)
    caption = models.CharField(max_length = 200)
    news_text = models.TextField(null = False, default = "Preencha aqui sua notícia!");
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    news_type = models.CharField(max_length = 50, default = 'Gerais')
    #notifications = BooleanField(default = False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey('news.News', related_name = 'comments')
    author = models.CharField(max_length = 150, default = "Anônimo")
    comment_text = models.TextField(null = False, default = "Escreva seu comentário aqui!")
    created_date = models.DateTimeField(default = timezone.now)

    def approve_comment(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_text

class Notification(models.Model):
    news = models.ForeignKey('news.News', related_name = 'notifications')
    comment = models.ForeignKey('news.Comment', related_name = 'notifications')
    user = models.ForeignKey('auth.User', related_name = 'notifications')
    #was_seen = models.BooleanField(default = False)

    #def notify(self):
        #self.was_seen = True
        #self.delete()
